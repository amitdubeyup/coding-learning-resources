# Django Interview Questions & Answers

## Core Concepts

### 1. What is Django and what are its key features?
Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Key features:
- **MTV Architecture** (Model-Template-View)
- **ORM** for database abstraction
- **Admin Interface** auto-generated
- **URL Routing** with regex/path converters
- **Template Engine** with inheritance
- **Security** features (CSRF, XSS, SQL injection protection)
- **Authentication System** built-in
- **Middleware** support
- **Form Handling** with validation
- **Internationalization** support

### 2. Explain Django's MTV architecture
```python
# Model (models.py) - Data layer
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

# View (views.py) - Business logic
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'articles/list.html', {'articles': articles})

# Template (list.html) - Presentation
# {% for article in articles %}
#   <h2>{{ article.title }}</h2>
# {% endfor %}

# URLs (urls.py) - Routing
urlpatterns = [
    path('articles/', article_list, name='article_list'),
]
```

### 3. What is the difference between Django's `null=True` and `blank=True`?
```python
class Product(models.Model):
    # null=True: Database level - allows NULL in DB
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    # blank=True: Validation level - allows empty value in forms
    description = models.TextField(blank=True)

    # Both: Optional field in forms and database
    notes = models.TextField(null=True, blank=True)

    # Neither: Required field (default)
    name = models.CharField(max_length=100)
```

### 4. Explain Django's request-response cycle
```python
# 1. Request hits WSGI/ASGI server
# 2. Middleware processes request (MIDDLEWARE in settings.py)
# 3. URL resolver matches pattern (urls.py)
# 4. View processes request (views.py)
# 5. View interacts with Model if needed (models.py)
# 6. Response rendered through Template (templates/)
# 7. Middleware processes response
# 8. Response sent to client

# Example with middleware
class CustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Process request before view
        request.custom_attr = "value"

        response = self.get_response(request)

        # Process response after view
        response['X-Custom-Header'] = 'MyValue'
        return response
```

## Django ORM

### 5. What are Django QuerySets and how are they evaluated lazily?
```python
# QuerySets are lazy - not executed until evaluated
articles = Article.objects.filter(status='published')  # No DB hit yet

# Evaluation happens on:
list(articles)  # 1. Iteration
len(articles)   # 2. len()
articles[0]     # 3. Slicing/indexing
bool(articles)  # 4. Boolean context
for a in articles: pass  # 5. Iteration in loop

# Optimization with select_related (SQL JOIN)
# Without: N+1 queries
for article in Article.objects.all():
    print(article.author.name)  # Each loops hits DB

# With: Single query with JOIN
articles = Article.objects.select_related('author')
for article in articles:
    print(article.author.name)  # No additional queries

# prefetch_related for many-to-many
articles = Article.objects.prefetch_related('tags')
```

### 6. Explain `select_related()` vs `prefetch_related()`
```python
# select_related: SQL JOIN for ForeignKey/OneToOne
# Single query, works for forward relationships
articles = Article.objects.select_related('author', 'category')
# SQL: SELECT ... FROM article JOIN author ON ... JOIN category ON ...

# prefetch_related: Separate queries for ManyToMany/Reverse FK
# Multiple queries, Python-side join
articles = Article.objects.prefetch_related('tags', 'comments')
# SQL: SELECT ... FROM article
# SQL: SELECT ... FROM tag WHERE article_id IN (...)
# SQL: SELECT ... FROM comment WHERE article_id IN (...)

# Combined example
Article.objects.select_related('author').prefetch_related('tags')
```

### 7. How do you perform complex queries with Q objects?
```python
from django.db.models import Q

# OR condition
Article.objects.filter(Q(status='published') | Q(status='featured'))

# AND with OR
Article.objects.filter(
    Q(status='published') & (Q(category='tech') | Q(category='science'))
)

# NOT condition
Article.objects.filter(~Q(status='draft'))

# Complex example
from django.db.models import Count, F

articles = Article.objects.filter(
    Q(published_date__year=2024) &
    (Q(author__name__icontains='john') | Q(views__gte=1000))
).annotate(
    comment_count=Count('comments')
).filter(
    comment_count__gt=F('likes') * 2
)
```

### 8. What are Django's database transactions?
```python
from django.db import transaction

# Atomic decorator - rollback on exception
@transaction.atomic
def create_order(user, items):
    order = Order.objects.create(user=user)
    for item in items:
        OrderItem.objects.create(order=order, **item)
    user.wallet.balance -= order.total
    user.wallet.save()
    return order

# Context manager
def process_payment(order):
    try:
        with transaction.atomic():
            order.status = 'paid'
            order.save()

            # Create invoice
            Invoice.objects.create(order=order)

            # Update inventory
            for item in order.items.all():
                item.product.stock -= item.quantity
                item.product.save()
    except Exception as e:
        # Automatic rollback
        logger.error(f"Payment failed: {e}")
        raise

# Savepoints for nested transactions
with transaction.atomic():
    user.save()

    sid = transaction.savepoint()
    try:
        user.profile.save()
    except Exception:
        transaction.savepoint_rollback(sid)
    else:
        transaction.savepoint_commit(sid)
```

## Views and URLs

### 9. What's the difference between Function-Based Views and Class-Based Views?
```python
# Function-Based View (FBV)
def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.save()
    else:
        form = CommentForm()
    return render(request, 'article_detail.html', {
        'article': article, 'form': form
    })

# Class-Based View (CBV)
from django.views.generic import DetailView

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = self.object
            comment.save()
            return redirect('article_detail', pk=self.object.pk)
        return self.render_to_response(
            self.get_context_data(form=form)
        )

# URLs
urlpatterns = [
    path('article/<int:pk>/', article_detail),  # FBV
    path('article/<int:pk>/', ArticleDetailView.as_view()),  # CBV
]
```

### 10. How do you use Django's generic views?
```python
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class ArticleListView(ListView):
    model = Article
    template_name = 'articles/list.html'
    context_object_name = 'articles'
    paginate_by = 10

    def get_queryset(self):
        return Article.objects.filter(
            status='published'
        ).select_related('author')

class ArticleCreateView(CreateView):
    model = Article
    fields = ['title', 'content', 'category']
    template_name = 'articles/form.html'
    success_url = reverse_lazy('article_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ArticleUpdateView(UpdateView):
    model = Article
    fields = ['title', 'content']
    template_name = 'articles/form.html'

class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('article_list')
```

## Forms and Validation

### 11. How do you create and validate forms in Django?
```python
from django import forms
from django.core.exceptions import ValidationError

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'category', 'tags']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 10}),
            'tags': forms.CheckboxSelectMultiple(),
        }

    # Field-level validation
    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 5:
            raise ValidationError("Title must be at least 5 characters")
        if Article.objects.filter(title__iexact=title).exists():
            raise ValidationError("Article with this title already exists")
        return title

    # Form-level validation
    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')

        if title and content and title.lower() in content.lower():
            raise ValidationError(
                "Title should not be repeated in content"
            )
        return cleaned_data

# Usage in view
def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            form.save_m2m()  # Save many-to-many relationships
            return redirect('article_detail', pk=article.pk)
    else:
        form = ArticleForm()
    return render(request, 'article_form.html', {'form': form})
```

### 12. What are Django formsets and when to use them?
```python
from django.forms import modelformset_factory, inlineformset_factory

# Regular formset - multiple forms of same type
ArticleFormSet = modelformset_factory(
    Article,
    fields=['title', 'content'],
    extra=3,  # Number of empty forms
    can_delete=True
)

def manage_articles(request):
    if request.method == 'POST':
        formset = ArticleFormSet(request.POST)
        if formset.is_valid():
            formset.save()
            return redirect('article_list')
    else:
        formset = ArticleFormSet(queryset=Article.objects.filter(author=request.user))
    return render(request, 'manage_articles.html', {'formset': formset})

# Inline formset - parent-child relationship
OrderItemFormSet = inlineformset_factory(
    Order,  # Parent model
    OrderItem,  # Child model
    fields=['product', 'quantity', 'price'],
    extra=1,
    can_delete=True
)

def edit_order(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    if request.method == 'POST':
        formset = OrderItemFormSet(request.POST, instance=order)
        if formset.is_valid():
            formset.save()
            return redirect('order_detail', pk=order.pk)
    else:
        formset = OrderItemFormSet(instance=order)
    return render(request, 'edit_order.html', {
        'order': order, 'formset': formset
    })
```

## Authentication and Authorization

### 13. How do you implement custom user authentication in Django?
```python
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

# Custom User Model
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

# settings.py
AUTH_USER_MODEL = 'accounts.CustomUser'

# Custom authentication backend
from django.contrib.auth.backends import BaseBackend

class EmailOrPhoneBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            # Try email first
            user = CustomUser.objects.get(email=username)
        except CustomUser.DoesNotExist:
            # Try phone
            try:
                user = CustomUser.objects.get(phone=username)
            except CustomUser.DoesNotExist:
                return None

        if user.check_password(password):
            return user
        return None

    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None

# settings.py
AUTHENTICATION_BACKENDS = [
    'accounts.backends.EmailOrPhoneBackend',
    'django.contrib.auth.backends.ModelBackend',
]
```

### 14. How do you implement permissions and authorization?
```python
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

# Decorator-based (FBV)
@login_required
@permission_required('articles.delete_article', raise_exception=True)
def delete_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect('article_list')

# Mixin-based (CBV)
class ArticleDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Article
    permission_required = 'articles.delete_article'
    success_url = reverse_lazy('article_list')

# Custom permission check
from django.core.exceptions import PermissionDenied

def edit_article(request, pk):
    article = get_object_or_404(Article, pk=pk)

    # Only author or staff can edit
    if request.user != article.author and not request.user.is_staff:
        raise PermissionDenied

    # ... edit logic

# Custom permissions in model
class Article(models.Model):
    # ... fields

    class Meta:
        permissions = [
            ('publish_article', 'Can publish article'),
            ('feature_article', 'Can feature article'),
        ]

    def can_edit(self, user):
        return user == self.author or user.is_staff

# Usage in template
# {% if article.can_edit request.user %}
#   <a href="{% url 'edit_article' article.pk %}">Edit</a>
# {% endif %}
```

## Django REST Framework

### 15. How do you create REST APIs with Django REST Framework?
```python
from rest_framework import serializers, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Serializer
class ArticleSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.get_full_name', read_only=True)
    comment_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'author', 'author_name',
                  'published_date', 'comment_count']
        read_only_fields = ['author', 'published_date']

    def validate_title(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("Title too short")
        return value

    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)

# ViewSet
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        # Filter by query params
        status = self.request.query_params.get('status')
        if status:
            queryset = queryset.filter(status=status)
        return queryset.select_related('author').annotate(
            comment_count=Count('comments')
        )

    # Custom action
    @action(detail=True, methods=['post'])
    def publish(self, request, pk=None):
        article = self.get_object()
        article.status = 'published'
        article.save()
        return Response({'status': 'article published'})

    # Nested resource
    @action(detail=True, methods=['get'])
    def comments(self, request, pk=None):
        article = self.get_object()
        comments = article.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

# URLs
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'articles', ArticleViewSet)
urlpatterns = router.urls
```

### 16. How do you handle authentication and permissions in DRF?
```python
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_framework.authtoken.models import Token

# Custom permission
class IsAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read permissions for any request
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        # Write permissions only for author
        return obj.author == request.user

# ViewSet with authentication
class ArticleViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    # ...

# JWT Authentication (using djangorestframework-simplejwt)
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}

from datetime import timedelta

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
}

# urls.py
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
]

# Custom token claims
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        token['role'] = user.role
        return token
```

## Middleware and Signals

### 17. How do you create custom middleware in Django?
```python
# middleware.py
import time
import logging

logger = logging.getLogger(__name__)

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Before view
        start_time = time.time()
        request.start_time = start_time

        # Get response from view
        response = self.get_response(request)

        # After view
        duration = time.time() - start_time
        logger.info(f"{request.method} {request.path} - {response.status_code} - {duration:.2f}s")

        return response

class TenantMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Extract tenant from subdomain
        host = request.get_host().split(':')[0]
        parts = host.split('.')
        if len(parts) > 2:
            tenant_slug = parts[0]
            try:
                request.tenant = Tenant.objects.get(slug=tenant_slug)
            except Tenant.DoesNotExist:
                return HttpResponseNotFound("Tenant not found")

        response = self.get_response(request)
        return response

# settings.py
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'myapp.middleware.RequestLoggingMiddleware',
    'myapp.middleware.TenantMiddleware',
    # ...
]
```

### 18. What are Django signals and when to use them?
```python
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver, Signal
from django.core.mail import send_mail

# Built-in signals
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=Order)
def send_order_confirmation(sender, instance, created, **kwargs):
    if created:
        send_mail(
            'Order Confirmation',
            f'Your order #{instance.id} has been received.',
            'noreply@example.com',
            [instance.user.email],
        )

@receiver(pre_delete, sender=Article)
def delete_article_files(sender, instance, **kwargs):
    # Delete associated files before article is deleted
    if instance.thumbnail:
        instance.thumbnail.delete(save=False)

# Custom signals
article_published = Signal()

@receiver(article_published)
def notify_subscribers(sender, article, **kwargs):
    subscribers = article.author.followers.all()
    for subscriber in subscribers:
        send_mail(
            f'New article: {article.title}',
            article.content[:100],
            'noreply@example.com',
            [subscriber.email],
        )

# Emit signal
def publish_article(article):
    article.status = 'published'
    article.save()
    article_published.send(sender=article.__class__, article=article)

# apps.py - Register signals
class MyAppConfig(AppConfig):
    name = 'myapp'

    def ready(self):
        import myapp.signals  # Import signal handlers
```

## Caching and Performance

### 19. How do you implement caching in Django?
```python
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

# Per-view caching
@cache_page(60 * 15)  # Cache for 15 minutes
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'articles.html', {'articles': articles})

# Low-level cache API
def get_article(article_id):
    cache_key = f'article_{article_id}'
    article = cache.get(cache_key)

    if article is None:
        article = Article.objects.select_related('author').get(pk=article_id)
        cache.set(cache_key, article, 60 * 30)  # Cache for 30 minutes

    return article

# Template fragment caching
# {% load cache %}
# {% cache 900 article_sidebar article.id %}
#   ... expensive sidebar content ...
# {% endcache %}

# Cache invalidation
@receiver(post_save, sender=Article)
def invalidate_article_cache(sender, instance, **kwargs):
    cache_key = f'article_{instance.id}'
    cache.delete(cache_key)
    cache.delete('article_list')

# CBV caching
@method_decorator(cache_page(60 * 15), name='dispatch')
class ArticleListView(ListView):
    model = Article

# settings.py - Redis cache
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}
```

### 20. What are common Django performance optimization techniques?
```python
# 1. Database query optimization
from django.db.models import Prefetch

# Bad: N+1 queries
articles = Article.objects.all()
for article in articles:
    print(article.author.name)  # N queries
    for comment in article.comments.all():  # N * M queries
        print(comment.text)

# Good: Optimized with select/prefetch
articles = Article.objects.select_related('author').prefetch_related(
    Prefetch('comments', queryset=Comment.objects.select_related('user'))
)

# 2. Use only() and defer()
# Fetch only needed fields
articles = Article.objects.only('id', 'title', 'published_date')

# Defer large fields
articles = Article.objects.defer('content', 'description')

# 3. Bulk operations
# Bad: Multiple queries
for i in range(1000):
    Article.objects.create(title=f"Article {i}")

# Good: Single query
articles = [Article(title=f"Article {i}") for i in range(1000)]
Article.objects.bulk_create(articles, batch_size=100)

# Bulk update
Article.objects.filter(status='draft').update(status='published')

# 4. Database indexing
class Article(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    status = models.CharField(max_length=20)
    published_date = models.DateTimeField(db_index=True)

    class Meta:
        indexes = [
            models.Index(fields=['status', 'published_date']),
            models.Index(fields=['-published_date']),
        ]

# 5. Pagination
from django.core.paginator import Paginator

def article_list(request):
    articles = Article.objects.all()
    paginator = Paginator(articles, 25)
    page = request.GET.get('page')
    articles_page = paginator.get_page(page)
    return render(request, 'articles.html', {'articles': articles_page})

# 6. Use iterator() for large querysets
for article in Article.objects.all().iterator(chunk_size=1000):
    process_article(article)

# 7. Async views (Django 3.1+)
from django.http import JsonResponse
import asyncio

async def async_view(request):
    data = await fetch_data_async()
    return JsonResponse(data)
```

## Testing

### 21. How do you write tests in Django?
```python
from django.test import TestCase, Client, TransactionTestCase
from django.urls import reverse

class ArticleModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Run once for entire test class
        cls.user = User.objects.create_user(
            username='testuser', password='testpass'
        )
        cls.article = Article.objects.create(
            title='Test Article',
            content='Test content',
            author=cls.user
        )

    def test_article_creation(self):
        self.assertEqual(self.article.title, 'Test Article')
        self.assertEqual(self.article.author, self.user)

    def test_article_str(self):
        self.assertEqual(str(self.article), 'Test Article')

    def test_get_absolute_url(self):
        expected_url = f'/articles/{self.article.pk}/'
        self.assertEqual(self.article.get_absolute_url(), expected_url)

class ArticleViewTest(TestCase):
    def setUp(self):
        # Run before each test method
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser', password='testpass'
        )
        self.article = Article.objects.create(
            title='Test Article',
            content='Test content',
            author=self.user
        )

    def test_article_list_view(self):
        response = self.client.get(reverse('article_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Article')
        self.assertTemplateUsed(response, 'articles/list.html')

    def test_article_create_view_requires_login(self):
        response = self.client.get(reverse('article_create'))
        self.assertEqual(response.status_code, 302)  # Redirect to login

    def test_article_create_view_with_login(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('article_create'), {
            'title': 'New Article',
            'content': 'New content',
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Article.objects.count(), 2)

    def test_article_detail_404(self):
        response = self.client.get(reverse('article_detail', args=[9999]))
        self.assertEqual(response.status_code, 404)

# API Testing
from rest_framework.test import APITestCase, APIClient

class ArticleAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpass'
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_create_article(self):
        url = reverse('article-list')
        data = {'title': 'Test', 'content': 'Test content'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Article.objects.count(), 1)

    def test_list_articles(self):
        Article.objects.create(title='Test', content='Content', author=self.user)
        url = reverse('article-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
```

## Deployment and Production

### 22. How do you deploy Django applications to production?
```python
# settings/production.py
import os
from .base import *

DEBUG = False

ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': '5432',
    }
}

# Static files
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media files
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Security settings
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': '/var/log/django/error.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}
```

### 23. How do you configure Django with Docker?
```dockerfile
# Dockerfile
FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Run migrations and start server
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "4", "myproject.wsgi:application"]
```

```yaml
# docker-compose.yml
version: '3.8'

services:
  db:
    image: postgres:15
    environment:
      POSTGRES_DB: mydb
      POSTGRES_USER: myuser
      POSTGRES_PASSWORD: mypassword
    volumes:
      - postgres_data:/var/lib/postgresql/data

  redis:
    image: redis:7-alpine

  web:
    build: .
    command: gunicorn myproject.wsgi:application --bind 0.0.0.0:8000 --workers 4
    volumes:
      - .:/app
      - static_volume:/app/staticfiles
      - media_volume:/app/media
    ports:
      - "8000:8000"
    depends_on:
      - db
      - redis
    environment:
      - DATABASE_URL=postgresql://myuser:mypassword@db:5432/mydb
      - REDIS_URL=redis://redis:6379/1
      - SECRET_KEY=${SECRET_KEY}

  celery:
    build: .
    command: celery -A myproject worker -l info
    volumes:
      - .:/app
    depends_on:
      - db
      - redis

  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
      - static_volume:/app/staticfiles
      - media_volume:/app/media
    depends_on:
      - web

volumes:
  postgres_data:
  static_volume:
  media_volume:
```

### 24. How do you handle asynchronous tasks with Celery?
```python
# celery.py
from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

app = Celery('myproject')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# settings.py
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'

# tasks.py
from celery import shared_task
from django.core.mail import send_mail
from time import sleep

@shared_task
def send_email_task(subject, message, recipient_list):
    send_mail(
        subject,
        message,
        'noreply@example.com',
        recipient_list,
    )
    return f'Email sent to {len(recipient_list)} recipients'

@shared_task
def process_article(article_id):
    article = Article.objects.get(pk=article_id)
    # Heavy processing
    sleep(10)
    article.processed = True
    article.save()
    return f'Article {article_id} processed'

@shared_task(bind=True, max_retries=3)
def fetch_external_data(self, url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as exc:
        raise self.retry(exc=exc, countdown=60)  # Retry after 60 seconds

# Usage in views
def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            # Async task
            process_article.delay(article.id)
            return redirect('article_detail', pk=article.pk)

# Periodic tasks
from celery.schedules import crontab

app.conf.beat_schedule = {
    'send-daily-report': {
        'task': 'myapp.tasks.send_daily_report',
        'schedule': crontab(hour=9, minute=0),
    },
}
```

## Security

### 25. What are Django's built-in security features?
```python
# 1. CSRF Protection (enabled by default)
# In forms
# {% csrf_token %}

# For AJAX requests
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie

@ensure_csrf_cookie
def get_csrf(request):
    return JsonResponse({'csrfToken': request.META.get('CSRF_COOKIE')})

# 2. SQL Injection Protection (use ORM)
# BAD - vulnerable to SQL injection
query = f"SELECT * FROM articles WHERE id = {user_input}"

# GOOD - parameterized query
Article.objects.filter(id=user_input)
# or raw SQL with parameters
Article.objects.raw('SELECT * FROM articles WHERE id = %s', [user_input])

# 3. XSS Protection (template auto-escaping)
# Template: {{ user_content|safe }}  # Only if you trust the content
# Template: {{ user_content }}  # Automatically escaped

# 4. Clickjacking Protection
# settings.py
X_FRAME_OPTIONS = 'DENY'  # or 'SAMEORIGIN'

# 5. Password Hashing
from django.contrib.auth.hashers import make_password, check_password

# Password stored securely with PBKDF2
user.password = make_password('plain_password')

# 6. Rate Limiting
from django.core.cache import cache
from django.http import HttpResponseForbidden

def rate_limit(request):
    ip = request.META.get('REMOTE_ADDR')
    cache_key = f'rate_limit_{ip}'

    requests_count = cache.get(cache_key, 0)
    if requests_count > 100:  # Max 100 requests per hour
        return HttpResponseForbidden('Rate limit exceeded')

    cache.set(cache_key, requests_count + 1, 3600)

# 7. Secure settings
# settings.py
SECRET_KEY = os.environ.get('SECRET_KEY')  # Never commit to version control
DEBUG = False  # In production

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', 'OPTIONS': {'min_length': 8}},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]
```

## Advanced Topics

### 26. How do you implement multi-database support?
```python
# settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'primary_db',
        'USER': 'user',
        'PASSWORD': 'password',
        'HOST': 'localhost',
    },
    'analytics': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'analytics_db',
        'USER': 'user',
        'PASSWORD': 'password',
        'HOST': 'localhost',
    },
    'readonly': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'replica_db',
        'USER': 'readonly_user',
        'PASSWORD': 'password',
        'HOST': 'replica-host',
    },
}

# Database router
class PrimaryReplicaRouter:
    def db_for_read(self, model, **hints):
        """Read from replica"""
        return 'readonly'

    def db_for_write(self, model, **hints):
        """Write to primary"""
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return db == 'default'

class AnalyticsRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'analytics':
            return 'analytics'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'analytics':
            return 'analytics'
        return None

DATABASE_ROUTERS = [
    'myapp.routers.AnalyticsRouter',
    'myapp.routers.PrimaryReplicaRouter',
]

# Manual database selection
# Read from specific database
articles = Article.objects.using('readonly').all()

# Write to specific database
article = Article(title='Test')
article.save(using='analytics')

# Transactions across databases
from django.db import transaction

with transaction.atomic(using='default'):
    user.save()

with transaction.atomic(using='analytics'):
    log_entry.save()
```

### 27. How do you implement custom template tags and filters?
```python
# templatetags/custom_tags.py
from django import template
from django.utils.html import format_html
from django.utils.safestring import mark_safe

register = template.Library()

# Simple tag
@register.simple_tag
def current_time(format_string):
    from datetime import datetime
    return datetime.now().strftime(format_string)

# Usage: {% current_time "%Y-%m-%d %H:%M" %}

# Inclusion tag
@register.inclusion_tag('tags/article_card.html')
def show_article_card(article):
    return {
        'article': article,
        'comment_count': article.comments.count(),
    }

# Usage: {% show_article_card article %}

# Custom filter
@register.filter
def truncate_words(value, arg):
    """Truncate after a certain number of words"""
    words = value.split()
    if len(words) > arg:
        return ' '.join(words[:arg]) + '...'
    return value

# Usage: {{ article.content|truncate_words:20 }}

# Filter with safe output
@register.filter(is_safe=True)
def highlight_search(text, search):
    """Highlight search terms in text"""
    if not search:
        return text
    highlighted = text.replace(
        search,
        f'<mark>{search}</mark>'
    )
    return mark_safe(highlighted)

# Usage: {{ article.content|highlight_search:query }}

# Assignment tag (stores result in variable)
@register.simple_tag
def get_latest_articles(count=5):
    return Article.objects.filter(status='published')[:count]

# Usage: {% get_latest_articles 10 as articles %}

# Block tag
@register.tag
def repeat(parser, token):
    try:
        tag_name, count = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError(
            f"{token.contents.split()[0]} tag requires a count argument"
        )

    nodelist = parser.parse(('endrepeat',))
    parser.delete_first_token()
    return RepeatNode(nodelist, int(count))

class RepeatNode(template.Node):
    def __init__(self, nodelist, count):
        self.nodelist = nodelist
        self.count = count

    def render(self, context):
        output = ''
        for i in range(self.count):
            context.push({'forloop': {'counter': i + 1}})
            output += self.nodelist.render(context)
            context.pop()
        return output

# Usage:
# {% repeat 3 %}
#   <p>This will be repeated</p>
# {% endrepeat %}
```

### 28. How do you handle file uploads securely?
```python
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
import os

def validate_file_size(value):
    limit = 5 * 1024 * 1024  # 5MB
    if value.size > limit:
        raise ValidationError('File too large. Max size is 5MB.')

class Document(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(
        upload_to='documents/%Y/%m/%d/',
        validators=[
            FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx']),
            validate_file_size,
        ]
    )
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Additional security checks
        if self.file:
            # Check file content type
            import magic
            mime = magic.Magic(mime=True)
            file_type = mime.from_buffer(self.file.read(1024))
            self.file.seek(0)

            allowed_types = ['application/pdf', 'application/msword']
            if file_type not in allowed_types:
                raise ValidationError('Invalid file type')

        super().save(*args, **kwargs)

# View with file upload
from django.views.decorators.http import require_http_methods

@login_required
@require_http_methods(["POST"])
def upload_document(request):
    if request.FILES.get('file'):
        file = request.FILES['file']

        # Validate file extension
        ext = os.path.splitext(file.name)[1].lower()
        if ext not in ['.pdf', '.doc', '.docx']:
            return JsonResponse({'error': 'Invalid file type'}, status=400)

        # Create document
        document = Document(
            title=request.POST.get('title'),
            file=file,
            uploaded_by=request.user
        )
        document.save()

        return JsonResponse({'success': True, 'id': document.id})

    return JsonResponse({'error': 'No file uploaded'}, status=400)

# Serving files with access control
from django.http import FileResponse
from django.shortcuts import get_object_or_404

@login_required
def download_document(request, document_id):
    document = get_object_or_404(Document, pk=document_id)

    # Check permissions
    if document.uploaded_by != request.user and not request.user.is_staff:
        raise PermissionDenied

    # Serve file
    response = FileResponse(document.file.open('rb'))
    response['Content-Disposition'] = f'attachment; filename="{document.file.name}"'
    return response

# settings.py
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# In production, serve media files through web server (nginx/Apache)
# Never serve user-uploaded files directly from Django
```

This comprehensive guide covers Django fundamentals through advanced topics with practical code examples for interview preparation.
