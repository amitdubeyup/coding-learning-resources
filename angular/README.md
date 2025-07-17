# Top 100 Complex Angular Interview Questions for Senior/Staff Engineers

A comprehensive collection of advanced Angular interview questions focusing on deep technical understanding, architecture decisions, and real-world problem-solving scenarios.

## Table of Contents

1. [Angular Architecture & Internals](#angular-architecture--internals)
2. [Advanced RxJS & Observables](#advanced-rxjs--observables)
3. [Change Detection & Performance](#change-detection--performance)
4. [Dependency Injection & Services](#dependency-injection--services)
5. [Advanced Component Patterns](#advanced-component-patterns)
6. [Routing & Navigation](#routing--navigation)
7. [Forms & Validation](#forms--validation)
8. [Testing & Quality Assurance](#testing--quality-assurance)
9. [Performance Optimization](#performance-optimization)
10. [Security & Best Practices](#security--best-practices)
11. [Scalable Architecture](#scalable-architecture)
12. [Angular Ecosystem & Tools](#angular-ecosystem--tools)

---

## Angular Architecture & Internals

### 1. Explain the Angular compilation process and the difference between JIT and AOT compilation. How does Ivy renderer affect this process?

**Answer:**

**JIT vs AOT:**
- **JIT**: Compiles in browser at runtime, larger bundles, slower initial load
- **AOT**: Compiles during build, smaller bundles, faster rendering, better tree-shaking
- **Ivy**: Angular 9+ renderer with improved compilation, smaller bundles, incremental builds

```typescript
// Ivy generates optimized code
@Component({ template: `<div>{{title}}</div>` })
class MyComponent {
  static ɵcmp = defineComponent({ /* optimized template function */ });
}
```

### 2. Describe the complete lifecycle of an Angular application from bootstrap to component destruction, including the role of ApplicationRef and NgZone.

**Answer:**

**Bootstrap Process:**
Platform → Module → ApplicationRef → NgZone → Component Tree

```typescript
platformBrowserDynamic().bootstrapModule(AppModule);
```

**ApplicationRef**: Manages component views, triggers change detection
**NgZone**: Patches async operations, notifies when to run change detection

**Component Lifecycle:**
Constructor → OnChanges → OnInit → DoCheck → AfterContentInit → AfterContentChecked → AfterViewInit → AfterViewChecked → OnDestroy

### 3. How does Angular's hierarchical injector system work? Explain the resolution strategy and how to create custom injectors programmatically.

**Answer:**

**Hierarchy:** Platform → Application → Module → Element Injectors

**Resolution:** Element → Parent → Module → Application → Platform (bottom-up)

```typescript
// Custom injector
const customInjector = Injector.create({
  providers: [
    { provide: MyService, useClass: MyService },
    { provide: CONFIG_TOKEN, useValue: config }
  ],
  parent: this.injector
});

// Use in component creation
this.viewContainer.createComponent(MyComponent, { injector: customInjector });
```

### 4. What is the difference between ViewChild, ContentChild, and their query counterparts? When would you use static vs dynamic queries?

**Answer:**

**ViewChild**: Queries component's own template
**ContentChild**: Queries projected content (ng-content)
**ViewChildren/ContentChildren**: Query multiple elements

```typescript
@Component({
  template: `<div #myView>View</div><ng-content></ng-content>`
})
class ParentComponent {
  @ViewChild('myView') viewChild!: ElementRef;           // Own template
  @ContentChild('projected') contentChild!: ElementRef;  // Projected content
  @ViewChildren('items') items!: QueryList<ElementRef>;  // Multiple elements
}
```

**Static vs Dynamic:**
- **Static (true)**: Available in ngOnInit, for elements always present
- **Dynamic (false)**: Available in ngAfterViewInit, for conditional elements (*ngIf)

### 5. Explain the concept of Angular Elements and how you would architect a micro-frontend solution using Angular Elements.

**Answer:**

**Angular Elements**: Packages Angular components as Web Components (custom elements) for use in any framework.

```typescript
@Component({
  selector: 'my-element',
  template: `<h1>{{title}}</h1>`
})
class MyElementComponent {
  @Input() title = 'Default';
}

// Register as custom element
const element = createCustomElement(MyElementComponent, { injector });
customElements.define('my-element', element);
```

**Micro-frontend Architecture:**
- Shell app hosts micro-apps as custom elements
- Event bus for communication between micro-apps
- Independent deployment and development
- Shared dependencies managed at shell level

### 6. How does Angular's tree-shaking work with the module system? What are the implications of using providedIn: 'root' vs module providers?

**Answer:**

**Tree-shaking**: Removes unused code from bundles.

```typescript
// Tree-shakable (recommended)
@Injectable({ providedIn: 'root' })
class MyService {} // Only included if used

// Not tree-shakable
@NgModule({
  providers: [MyService] // Always included
})
class MyModule {}
```

**Implications:**
- **providedIn: 'root'**: Tree-shakable, singleton, cleaner code
- **Module providers**: Always included, allows multiple instances, explicit scoping

### 7. Describe the role of ApplicationInitializer and how you would use it to implement complex application startup logic.

**Answer:**

**APP_INITIALIZER**: Runs initialization logic before app starts (config loading, auth setup, etc.)

```typescript
// Basic usage
function initializeApp(): Promise<void> {
  return fetch('/api/config').then(response => {
    // Setup logic
  });
}

@NgModule({
  providers: [
    {
      provide: APP_INITIALIZER,
      useFactory: initializeApp,
      multi: true
    }
  ]
})
class AppModule {}

// Multiple initializers
function initializerFactory(configService: ConfigService, authService: AuthService) {
  return (): Promise<void> => {
    return Promise.all([
      configService.loadConfig(),
      authService.initialize()
    ]).then(() => console.log('App ready'));
  };
}
```

### 8. Explain how Angular's renderer abstraction works and when you might need to create a custom renderer.

**Answer:**

**Renderer2**: Platform-agnostic DOM manipulation (browser, server, mobile)

```typescript
@Component({ template: '<div></div>' })
class MyComponent {
  constructor(private renderer: Renderer2, private el: ElementRef) {}
  
  ngOnInit() {
    const div = this.renderer.createElement('div');
    this.renderer.appendChild(this.el.nativeElement, div);
    this.renderer.setAttribute(div, 'class', 'dynamic');
  }
}

// Custom renderer example
@Injectable()
class LoggingRenderer extends Renderer2 {
  constructor(private delegate: Renderer2) { super(); }
  
  createElement(name: string): any {
    console.log(`Creating: ${name}`);
    return this.delegate.createElement(name);
  }
  // ... delegate other methods with logging
}
```

**Use Cases**: Platform optimizations, debugging, custom graphics, legacy integration

### 9. What are the internal differences between NgModules and standalone components? How does the dependency resolution differ?

**Answer:**

**NgModules**: Traditional approach with module-level dependency management
**Standalone Components**: Angular 14+ approach with component-level imports

```typescript
// NgModule approach
@NgModule({
  declarations: [ComponentA],
  imports: [CommonModule, FormsModule],
  providers: [ServiceA]
})
class FeatureModule {}

// Standalone approach
@Component({
  standalone: true,
  imports: [CommonModule, FormsModule, OtherComponent],
  providers: [ServiceA],
  template: '<div>{{title}}</div>'
})
class StandaloneComponent {}

// Bootstrap
bootstrapApplication(StandaloneComponent, {
  providers: [GlobalService]
});
```

**Differences**: 
- **Compilation**: Standalone has simpler dependency tree, better tree-shaking
- **Resolution**: Standalone uses component injector → parent → app (no module layer)
- **Bundle size**: Standalone only imports what's needed vs entire module graph

### 10. How does Angular handle circular dependencies, and what strategies would you implement to avoid them in large applications?

**Answer:**

**Circular Dependencies**: When modules/services depend on each other, creating a loop.

Angular detects and throws: "Circular dependency in DI detected"

**Resolution Strategies:**

```typescript
// 1. Use forwardRef
@Injectable()
class ServiceA {
  constructor(@Inject(forwardRef(() => ServiceB)) private serviceB: ServiceB) {}
}

// 2. Mediator pattern
@Injectable({ providedIn: 'root' })
class MediatorService {
  private events = new Subject<{from: string, to: string, data: any}>();
  
  send(from: string, to: string, data: any) {
    this.events.next({ from, to, data });
  }
  
  listen(target: string) {
    return this.events.pipe(filter(msg => msg.to === target));
  }
}

// 3. Lazy injection
@Injectable()
class ServiceA {
  constructor(private injector: Injector) {}
  
  getServiceB(): ServiceB {
    return this.injector.get(ServiceB);
  }
}
```

**Prevention**: Layered architecture (Components → Services → Repositories → Infrastructure), shared abstractions, dependency analysis tools

---

## Advanced RxJS & Observables

### 11. Design a complex data synchronization system using RxJS that handles real-time updates, offline scenarios, and conflict resolution.

**Answer:**

Design with WebSocket for real-time updates, local queue for offline operations, and timestamp-based conflict resolution.

```typescript
@Injectable()
class DataSyncService {
  private onlineStatus$ = new BehaviorSubject<boolean>(navigator.onLine);
  private localQueue$ = new BehaviorSubject<SyncOperation[]>([]);
  
  syncEntity<T>(id: string): Observable<T> {
    return merge(
      this.websocket.listen(`entity:${id}`),  // Real-time updates
      this.fetchFromServer(id),               // Initial data
      this.storage.watch(id)                  // Local changes
    ).pipe(distinctUntilChanged());
  }
}
```

### 12. Explain the difference between hot and cold observables. How would you implement a caching mechanism using shareReplay with custom cache invalidation?

**Answer:**

**Cold**: Creates new execution for each subscriber
**Hot**: Shares single execution among all subscribers

```typescript
// Cold to Hot conversion with caching
const cachedData$ = this.http.get('/api/data').pipe(
  shareReplay({ bufferSize: 1, refCount: true }), // Cache last value
  takeUntil(this.invalidation$)                   // Invalidate on trigger
);

// Cache invalidation
private invalidation$ = new Subject<void>();
invalidateCache() { this.invalidation$.next(); }
```

### 13. How would you implement a retry mechanism with exponential backoff, jitter, and circuit breaker pattern using RxJS operators?

**Answer:**

```typescript
function retryWithBackoff<T>(config: RetryConfig): MonoTypeOperatorFunction<T> {
  return (source: Observable<T>) => source.pipe(
    retryWhen(errors => 
      errors.pipe(
        scan((acc, error) => ({ count: acc.count + 1, error }), { count: 0 }),
        mergeMap(({ count, error }) => {
          if (count >= config.maxRetries) return throwError(error);
          
          // Exponential backoff with jitter
          const delay = Math.min(
            config.baseDelay * Math.pow(2, count) + Math.random() * 1000,
            config.maxDelay
          );
          
          return timer(delay);
        })
      )
    )
  );
}
```

### 14. Design a reactive state management solution using only RxJS (without NgRx) for a complex e-commerce application.

**Answer:**

```typescript
@Injectable({ providedIn: 'root' })
class ReactiveStore<T> {
  private state$ = new BehaviorSubject<T>(this.initialState);
  
  select<K extends keyof T>(key: K): Observable<T[K]> {
    return this.state$.pipe(
      map(state => state[key]),
      distinctUntilChanged()
    );
  }
  
  update(updateFn: (state: T) => T): void {
    this.state$.next(updateFn(this.state$.value));
  }
}

// Usage
@Injectable()
class CartStore extends ReactiveStore<CartState> {
  addItem(item: CartItem) {
    this.update(state => ({
      ...state,
      items: [...state.items, item]
    }));
  }
}
```

### 15. Explain memory leak scenarios in RxJS and implement a custom operator that automatically handles subscription cleanup based on component lifecycle.

**Answer:**

**Memory Leaks**: Unsubscribed observables, forgotten subscriptions, circular references

```typescript
// Automatic cleanup operator
function takeUntilDestroyed<T>(component: any): MonoTypeOperatorFunction<T> {
  return (source: Observable<T>) => {
    const destroy$ = component.destroy$ || new Subject<void>();
    
    if (!component.ngOnDestroy) {
      const originalDestroy = component.ngOnDestroy;
      component.ngOnDestroy = function() {
        destroy$.next();
        destroy$.complete();
        originalDestroy?.call(this);
      };
    }
    
    return source.pipe(takeUntil(destroy$));
  };
}

// Usage
this.data$ = this.service.getData().pipe(
  takeUntilDestroyed(this)
);
```

### 16. How would you implement a complex search functionality with debouncing, cancellation of previous requests, and result caching using RxJS?

**Answer:**

```typescript
@Injectable({ providedIn: 'root' })
class SearchService {
  private cache = new Map<string, any>();
  private searchSubject = new Subject<string>();
  
  search$ = this.searchSubject.pipe(
    debounceTime(300),                    // Debounce user input
    distinctUntilChanged(),               // Avoid duplicate queries
    switchMap(query => this.executeSearch(query)), // Cancel previous requests
    shareReplay(1)                        // Cache latest result
  );
  
  performSearch(query: string): void {
    this.searchSubject.next(query);
  }
  
  private executeSearch(query: string): Observable<any> {
    const cached = this.cache.get(query);
    if (cached) return of(cached);
    
    return this.http.get(`/api/search?q=${query}`).pipe(
      tap(result => this.cache.set(query, result)),
      timeout(5000),
      retry(2)
    );
  }
}
```

### 17. Design a reactive form validation system that supports async validators, cross-field validation, and real-time error display.

**Answer:**

```typescript
// Sync validators
class Validators {
  static required(message = 'Required'): ValidatorFn {
    return (control: AbstractControl) => 
      control.value ? null : { required: { message } };
  }
  
  static email(): ValidatorFn {
    return (control: AbstractControl) => {
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      return emailRegex.test(control.value) ? null : { email: { message: 'Invalid email' } };
    };
  }
}

// Async validator with caching
createAsyncValidator(validatorFn: (value: any) => Observable<boolean>): AsyncValidatorFn {
  const cache = new Map();
  
  return (control: AbstractControl): Observable<ValidationErrors | null> => {
    const value = control.value;
    if (!value) return of(null);
    
    const cached = cache.get(value);
    if (cached) return of(cached);
    
    return of(value).pipe(
      debounceTime(500),
      switchMap(val => validatorFn(val)),
      map(isValid => {
        const result = isValid ? null : { invalid: { message: 'Invalid value' } };
        cache.set(value, result);
        return result;
      })
    );
  };
}

// Cross-field validation
static passwordMatch(passwordField: string, confirmField: string): ValidatorFn {
  return (formGroup: AbstractControl) => {
    const password = formGroup.get(passwordField);
    const confirm = formGroup.get(confirmField);
    
    if (password?.value !== confirm?.value) {
      confirm?.setErrors({ passwordMismatch: { message: 'Passwords do not match' } });
      return { passwordMismatch: true };
    }
    return null;
  };
}
```

### 18. Implement a custom RxJS operator that batches HTTP requests and handles rate limiting automatically.

**Answer:**

```typescript
// Request batching operator
function batchRequests<T, R>(config: BatchConfig<T, R>): OperatorFunction<T, R> {
  const { batchSize = 10, batchWindow = 100, rateLimitDelay = 1000 } = config;
  
  return (source: Observable<T>) => source.pipe(
    bufferTime(batchWindow, null, batchSize),
    filter(batch => batch.length > 0),
    concatMap((batch, index) => 
      of(batch).pipe(
        delay(index * rateLimitDelay),
        mergeMap(batch => config.batchProcessor(batch))
      )
    )
  );
}

// HTTP batching service
@Injectable({ providedIn: 'root' })
class HttpBatchingService {
  private requestCounts: number[] = [];
  private maxRequestsPerSecond = 10;
  
  batchHttp<T>(requests: HttpRequest[]): Observable<T[]> {
    return from(requests).pipe(
      batchRequests({
        batchSize: 5,
        batchWindow: 200,
        rateLimitDelay: this.calculateDelay(),
        batchProcessor: (batch) => this.processBatch(batch)
      })
    );
  }
  
  private processBatch(requests: HttpRequest[]): Observable<any[]> {
    // Check rate limiting
    if (!this.canMakeRequest()) {
      return timer(1000).pipe(
        switchMap(() => this.processBatch(requests))
      );
    }
    
    this.recordRequest();
    
    // Execute batch request
    return this.http.post('/api/batch', { requests }).pipe(
      catchError(() => 
        // Fallback to individual requests
        from(requests).pipe(
          mergeMap(req => this.http.request(req.method, req.url, { body: req.body })),
          toArray()
        )
      )
    );
  }
  
  private canMakeRequest(): boolean {
    return this.requestCounts.length < this.maxRequestsPerSecond;
  }
  
  private recordRequest(): void {
    this.requestCounts.push(Date.now());
    // Cleanup old entries
    const cutoff = Date.now() - 1000;
    this.requestCounts = this.requestCounts.filter(time => time > cutoff);
  }
  
  private calculateDelay(): number {
    const load = this.requestCounts.length / this.maxRequestsPerSecond;
    return Math.max(100, load * 1000);
  }
}
```

### 19. How would you handle complex error scenarios in RxJS streams, including retry with different strategies based on error types?

**Answer:**

```typescript
// Error classification and retry strategies
@Injectable({ providedIn: 'root' })
class ErrorHandlingService {
  classifyError(error: any): 'network' | 'timeout' | 'server' | 'client' | 'auth' {
    if (error.status === 0) return 'network';
    if (error.name === 'TimeoutError') return 'timeout';
    if (error.status >= 500) return 'server';
    if (error.status === 401 || error.status === 403) return 'auth';
    return 'client';
  }
  
  getRetryStrategy(errorType: string) {
    const strategies = {
      network: { maxRetries: 3, delay: 1000, backoff: 2 },
      timeout: { maxRetries: 2, delay: 2000, backoff: 1.5 },
      server: { maxRetries: 2, delay: 1000, backoff: 2 },
      auth: { maxRetries: 0, delay: 0 },
      client: { maxRetries: 0, delay: 0 }
    };
    return strategies[errorType] || strategies.client;
  }
}

// Smart retry operator
function smartRetry<T>(errorHandler: ErrorHandlingService): MonoTypeOperatorFunction<T> {
  return (source: Observable<T>) => source.pipe(
    retryWhen(errors => 
      errors.pipe(
        scan((acc, error) => {
          const errorType = errorHandler.classifyError(error);
          const strategy = errorHandler.getRetryStrategy(errorType);
          
          if (acc.retryCount >= strategy.maxRetries) {
            throw error;
          }
          
          return { retryCount: acc.retryCount + 1, strategy };
        }, { retryCount: 0, strategy: null }),
        
        mergeMap(({ retryCount, strategy }) => {
          const delay = strategy.delay * Math.pow(strategy.backoff, retryCount - 1);
          return timer(delay);
        })
      )
    )
  );
}

// Circuit breaker pattern
function circuitBreaker<T>(name: string, config = { failureThreshold: 5, timeout: 60000 }): MonoTypeOperatorFunction<T> {
  let failures = 0;
  let state: 'CLOSED' | 'OPEN' | 'HALF_OPEN' = 'CLOSED';
  let lastFailureTime = 0;
  
  return (source: Observable<T>) => defer(() => {
    if (state === 'OPEN' && Date.now() - lastFailureTime > config.timeout) {
      state = 'HALF_OPEN';
    }
    
    if (state === 'OPEN') {
      return throwError(() => new Error(`Circuit breaker ${name} is OPEN`));
    }
    
    return source.pipe(
      tap(() => {
        failures = 0;
        state = 'CLOSED';
      }),
      catchError(error => {
        failures++;
        lastFailureTime = Date.now();
        
        if (failures >= config.failureThreshold) {
          state = 'OPEN';
        }
        
        return throwError(() => error);
      })
    );
  });
}

// Error recovery with fallback
function withErrorRecovery<T>(fallbackValue: T): MonoTypeOperatorFunction<T> {
  return (source: Observable<T>) => source.pipe(
    catchError(error => {
      console.error('Error occurred, using fallback:', error);
      return of(fallbackValue);
    })
  );
}
```

### 20. Design a reactive data pipeline that transforms, filters, and aggregates real-time data streams with backpressure handling.

**Answer:**

```typescript
// Reactive data pipeline with backpressure handling
@Injectable({ providedIn: 'root' })
class ReactiveDataPipelineService {
  createPipeline<T>(source: Observable<T>, config: PipelineConfig): Observable<T> {
    let pipeline$ = source;
    
    // Apply backpressure strategy
    pipeline$ = this.applyBackpressure(pipeline$, config.backpressureStrategy);
    
    // Apply transformation stages
    config.stages.forEach(stage => {
      pipeline$ = pipeline$.pipe(
        stage.operator,
        catchError(error => {
          console.error(`Stage ${stage.name} failed:`, error);
          return stage.continueOnError ? EMPTY : throwError(error);
        })
      );
    });
    
    return pipeline$;
  }
  
  private applyBackpressure<T>(source: Observable<T>, strategy: string): Observable<T> {
    switch (strategy) {
      case 'drop':
        return source.pipe(throttleTime(100));
      case 'buffer':
        return source.pipe(
          bufferTime(100, null, 1000),
          mergeMap(buffer => from(buffer))
        );
      case 'sample':
        return source.pipe(sampleTime(100));
      default:
        return source;
    }
  }
}

// Pipeline operators
class PipelineOperators {
  // Windowed aggregation
  static windowedAggregate<T, R>(
    windowSize: number, 
    aggregator: (items: T[]) => R
  ): OperatorFunction<T, R> {
    return (source: Observable<T>) => source.pipe(
      bufferCount(windowSize),
      map(buffer => aggregator(buffer))
    );
  }
  
  // Real-time data enrichment
  static enrich<T, E>(
    enrichmentFn: (item: T) => Observable<E>
  ): OperatorFunction<T, T & E> {
    return (source: Observable<T>) => source.pipe(
      mergeMap(item => 
        enrichmentFn(item).pipe(
          map(enrichment => ({ ...item, ...enrichment })),
          catchError(() => of(item as T & E))
        ),
        5 // Concurrency limit
      )
    );
  }
}

// Usage example
const dataStream$ = this.pipelineService.createPipeline(rawData$, {
  backpressureStrategy: 'buffer',
  stages: [
    {
      name: 'filter',
      operator: filter(item => item.isValid),
      continueOnError: true
    },
    {
      name: 'transform',
      operator: map(item => ({ ...item, processed: true }))
    },
    {
      name: 'aggregate',
      operator: PipelineOperators.windowedAggregate(10, items => ({
        count: items.length,
        average: items.reduce((sum, item) => sum + item.value, 0) / items.length
      }))
    }
  ]
});
```

---

## Change Detection & Performance

### 21. Explain Angular's change detection algorithm in detail. How does it differ between Default and OnPush strategies?

**Answer:**

**Default**: Checks all components on every change detection cycle (events, HTTP, timers)
**OnPush**: Only checks when inputs change (reference), events fire, or `markForCheck()` called

```typescript
@Component({
  changeDetection: ChangeDetectionStrategy.OnPush
})
class OptimizedComponent {
  @Input() data: Data; // Only triggers on reference change
  
  updateData() {
    this.cdr.markForCheck(); // Manual trigger
  }
}
```

### 22. When and how would you implement a custom ChangeDetectionStrategy? Provide a real-world scenario.

**Answer:**

Custom strategies are rarely needed. Use case: High-frequency trading dashboard that only updates on timestamp changes.

```typescript
class TradeDataStrategy implements ChangeDetectionStrategy {
  detectChanges(component: any, context: any): boolean {
    return component.lastUpdateTime !== context.currentTime;
  }
}

@Component({
  changeDetection: TradeDataStrategy
})
class TradingComponent {
  @Input() tradeData: TradeData;
  lastUpdateTime: number;
}
```

### 23. How does NgZone work internally, and when would you run code outside Angular's zone? What are the implications?

**Answer:**

**NgZone**: Patches async operations (setTimeout, Promise, events) to trigger change detection automatically.

**Outside zone**: Use for high-frequency updates, animations, or performance-critical operations.

```typescript
constructor(private ngZone: NgZone) {}

// Heavy operations outside zone
ngZone.runOutsideAngular(() => {
  setInterval(() => {
    this.updateChart(); // Won't trigger change detection
  }, 16);
});

// Update UI when needed
ngZone.run(() => {
  this.updateCounter++;
});
```

### 24. Explain the concept of change detection cycles and how to debug performance issues related to excessive change detection.

**Answer:**

**Cycle**: Event → Check components → Update DOM → Complete

**Debug**: Use `ng.profiler.timeChangeDetection()` in console, avoid method calls in templates

```typescript
// ❌ Bad: Runs every cycle
@Component({
  template: `{{expensiveCalculation()}}`
})

// ✅ Good: Calculate once
@Component({
  template: `{{calculatedValue}}`
})
class GoodComponent {
  calculatedValue: number;
  
  ngOnChanges() {
    this.calculatedValue = this.data.reduce((sum, item) => sum + item.value, 0);
  }
}
```

### 25. How would you implement manual change detection triggering in a large application with complex component hierarchies?

**Answer:**

```typescript
// Global detection service
@Injectable({ providedIn: 'root' })
class ChangeDetectionService {
  constructor(private appRef: ApplicationRef) {}
  
  triggerGlobalDetection() {
    this.appRef.tick(); // Full tree check
  }
  
  scheduleDetection() {
    requestAnimationFrame(() => this.appRef.tick()); // Batched
  }
}

// Component-level control
updateChildren() {
  this.cdr.markForCheck(); // OnPush components
  // or this.cdr.detach() / this.cdr.reattach() for fine control
}
```

### 26. Describe scenarios where you'd use ChangeDetectorRef methods (detectChanges, markForCheck, detach, reattach) and their performance implications.

**Answer:**

```typescript
class ComponentOptimizations {
  constructor(private cdr: ChangeDetectorRef) {}
  
  onCriticalUpdate() {
    this.cdr.detectChanges(); // Force immediate check
  }
  
  onDataReceived() {
    this.cdr.markForCheck(); // Schedule check for OnPush
  }
  
  onHeavyAnimation() {
    this.cdr.detach(); // Stop automatic checking
  }
  
  onAnimationComplete() {
    this.cdr.reattach(); // Resume checking
    this.cdr.markForCheck();
  }
}
```

**Use cases**: `detectChanges()` for immediate updates, `markForCheck()` for OnPush components, `detach()`/`reattach()` for performance control

### 27. How does Angular handle change detection with async operations, and how would you optimize it for real-time applications?

**Answer:**

Zone.js patches async ops to trigger change detection. Optimize with OnPush + async pipe, or run outside zone for high-frequency updates.

### 28. Explain the relationship between Observables and change detection. How does the async pipe optimize this process?

**Answer:**

Observables don't trigger change detection. Async pipe auto-subscribes/unsubscribes and calls `markForCheck()` on OnPush components.

### 29. How would you implement a custom trackBy function for large lists with complex objects?

**Answer:**

```typescript
trackByFn(index: number, item: any): any {
  return item.id; // Use unique identifier
}

// For objects without ID
trackByHash(index: number, item: any): string {
  return JSON.stringify(item);
}
```

### 30. Design a change detection optimization strategy for a data-heavy dashboard application with hundreds of components.

**Answer:**

Use OnPush everywhere, virtual scrolling for lists, detach non-visible components, batch updates with `requestAnimationFrame`, implement proper trackBy functions.

---

## Dependency Injection & Services

### 31. Explain the differences between providedIn: 'root', 'platform', and 'any'. When would you use each?

**Answer:**

**providedIn: 'root':**
- Creates singleton instance at application level
- Tree-shakable (removed if not used)
- Default choice for most services

**providedIn: 'platform':**
- Singleton across multiple Angular applications
- Shared between main app and lazy-loaded apps
- Use for cross-application services

**providedIn: 'any':**
- Creates separate instance for each lazy-loaded module
- Non-singleton behavior
- Use when you need module-specific instances

```typescript
// Root singleton
@Injectable({ providedIn: 'root' })
class DataService {}

// Platform singleton (shared across apps)
@Injectable({ providedIn: 'platform' })
class PlatformConfigService {}

// Module-specific instances
@Injectable({ providedIn: 'any' })
class ModuleSpecificService {}

// Usage scenarios
// - root: API services, global state
// - platform: microfrontend shared services
// - any: feature-specific configurations
```

### 32. How would you implement a plugin architecture using Angular's DI system with dynamic service registration?

**Answer:**

```typescript
// Plugin interface
interface Plugin {
  name: string;
  initialize(): void;
  execute(data: any): any;
}

// Plugin registry
@Injectable({ providedIn: 'root' })
class PluginRegistry {
  private plugins = new Map<string, Plugin>();
  
  register(plugin: Plugin) {
    this.plugins.set(plugin.name, plugin);
  }
  
  get(name: string): Plugin | undefined {
    return this.plugins.get(name);
  }
  
  executeAll(data: any) {
    return Array.from(this.plugins.values()).map(p => p.execute(data));
  }
}

// Plugin implementation
@Injectable()
class EmailPlugin implements Plugin {
  name = 'email';
  
  initialize() {
    console.log('Email plugin initialized');
  }
  
  execute(data: any) {
    return this.sendEmail(data);
  }
}

// Dynamic plugin loading
@Injectable()
class PluginLoader {
  constructor(
    private registry: PluginRegistry,
    private injector: Injector
  ) {}
  
  async loadPlugin(pluginClass: any) {
    const plugin = this.injector.get(pluginClass);
    plugin.initialize();
    this.registry.register(plugin);
  }
  
  // Load plugins from configuration
  async loadFromConfig(pluginConfigs: any[]) {
    for (const config of pluginConfigs) {
      const module = await import(config.path);
      await this.loadPlugin(module[config.className]);
    }
  }
}
```

### 33. Design a multi-tenant application where services behave differently based on tenant configuration using DI.

**Answer:**

```typescript
// Tenant context
export const TENANT_CONFIG = new InjectionToken<TenantConfig>('TENANT_CONFIG');

interface TenantConfig {
  id: string;
  features: string[];
  apiUrl: string;
  theme: string;
}

// Tenant-aware service factory
@Injectable()
class TenantServiceFactory {
  createApiService(config: TenantConfig): ApiService {
    return new ApiService(config.apiUrl, config.features);
  }
  
  createThemeService(config: TenantConfig): ThemeService {
    return new ThemeService(config.theme);
  }
}

// Multi-tenant module
@NgModule({
  providers: [
    {
      provide: TENANT_CONFIG,
      useFactory: () => this.getTenantConfig(), // Load from URL/storage
    },
    {
      provide: ApiService,
      useFactory: (config: TenantConfig, factory: TenantServiceFactory) => 
        factory.createApiService(config),
      deps: [TENANT_CONFIG, TenantServiceFactory]
    }
  ]
})
class TenantModule {
  static forTenant(tenantId: string): ModuleWithProviders<TenantModule> {
    return {
      ngModule: TenantModule,
      providers: [
        {
          provide: TENANT_CONFIG,
          useValue: { id: tenantId, /* ... tenant config */ }
        }
      ]
    };
  }
}

// Usage
class AppComponent {
  constructor(@Inject(TENANT_CONFIG) private config: TenantConfig) {
    // Service behavior changes based on tenant
  }
}
```

### 34. Explain injection tokens and how you'd use them to implement a configurable logging system.

**Answer:**

```typescript
// Configuration interfaces
interface LoggerConfig {
  level: 'debug' | 'info' | 'warn' | 'error';
  outputs: LogOutput[];
  format: string;
}

interface LogOutput {
  type: 'console' | 'file' | 'remote';
  config: any;
}

// Injection tokens
export const LOGGER_CONFIG = new InjectionToken<LoggerConfig>('LOGGER_CONFIG');
export const LOG_OUTPUTS = new InjectionToken<LogOutput[]>('LOG_OUTPUTS');

// Configurable logger
@Injectable({ providedIn: 'root' })
class ConfigurableLogger {
  constructor(
    @Inject(LOGGER_CONFIG) private config: LoggerConfig,
    @Inject(LOG_OUTPUTS) private outputs: LogOutput[]
  ) {}
  
  log(level: string, message: string) {
    if (this.shouldLog(level)) {
      const formatted = this.format(message);
      this.outputs.forEach(output => this.writeToOutput(output, formatted));
    }
  }
  
  private shouldLog(level: string): boolean {
    const levels = ['debug', 'info', 'warn', 'error'];
    return levels.indexOf(level) >= levels.indexOf(this.config.level);
  }
}

// Module configuration
@NgModule({
  providers: [
    {
      provide: LOGGER_CONFIG,
      useValue: {
        level: 'info',
        outputs: [{ type: 'console', config: {} }],
        format: '[{{timestamp}}] {{level}}: {{message}}'
      }
    },
    {
      provide: LOG_OUTPUTS,
      useFactory: (config: LoggerConfig) => config.outputs,
      deps: [LOGGER_CONFIG]
    }
  ]
})
class LoggingModule {}
```

### 35. How would you implement service inheritance and composition patterns in Angular's DI system?

**Answer:**

```typescript
// Base service
@Injectable()
abstract class BaseDataService<T> {
  constructor(protected http: HttpClient) {}
  
  abstract getEndpoint(): string;
  
  findAll(): Observable<T[]> {
    return this.http.get<T[]>(this.getEndpoint());
  }
  
  findById(id: string): Observable<T> {
    return this.http.get<T>(`${this.getEndpoint()}/${id}`);
  }
}

// Inherited services
@Injectable({ providedIn: 'root' })
class UserService extends BaseDataService<User> {
  getEndpoint(): string {
    return '/api/users';
  }
  
  // Additional user-specific methods
  getCurrentUser(): Observable<User> {
    return this.http.get<User>('/api/users/current');
  }
}

// Composition pattern
@Injectable({ providedIn: 'root' })
class CompositeUserService {
  constructor(
    private userService: UserService,
    private authService: AuthService,
    private cacheService: CacheService
  ) {}
  
  getUser(id: string): Observable<User> {
    return this.cacheService.get(`user-${id}`) || 
           this.userService.findById(id).pipe(
             tap(user => this.cacheService.set(`user-${id}`, user))
           );
  }
}

// Mixin pattern for multiple inheritance
interface Cacheable {
  cache: CacheService;
  getCacheKey(params: any): string;
}

interface Auditable {
  audit: AuditService;
  logAction(action: string): void;
}

class MixinService implements Cacheable, Auditable {
  constructor(
    public cache: CacheService,
    public audit: AuditService
  ) {}
  
  getCacheKey(params: any): string {
    return JSON.stringify(params);
  }
  
  logAction(action: string): void {
    this.audit.log(action);
  }
}
```

### 36. Design a caching service that can be configured differently for different modules while maintaining singleton behavior.

**Answer:**

```typescript
// Cache configuration
interface CacheConfig {
  ttl: number;
  maxSize: number;
  strategy: 'lru' | 'fifo' | 'lfu';
}

// Multi-configured cache service
@Injectable({ providedIn: 'root' })
class ConfigurableCacheService {
  private caches = new Map<string, Map<string, CacheEntry>>();
  private configs = new Map<string, CacheConfig>();
  
  registerConfig(namespace: string, config: CacheConfig) {
    this.configs.set(namespace, config);
    this.caches.set(namespace, new Map());
  }
  
  set(namespace: string, key: string, value: any): void {
    const cache = this.getCache(namespace);
    const config = this.configs.get(namespace)!;
    
    // Apply size limits
    if (cache.size >= config.maxSize) {
      this.evict(namespace, config.strategy);
    }
    
    cache.set(key, {
      value,
      timestamp: Date.now(),
      accessed: Date.now()
    });
  }
  
  get(namespace: string, key: string): any {
    const cache = this.getCache(namespace);
    const config = this.configs.get(namespace)!;
    const entry = cache.get(key);
    
    if (!entry) return null;
    
    // Check TTL
    if (Date.now() - entry.timestamp > config.ttl) {
      cache.delete(key);
      return null;
    }
    
    entry.accessed = Date.now();
    return entry.value;
  }
  
  private getCache(namespace: string): Map<string, CacheEntry> {
    if (!this.caches.has(namespace)) {
      throw new Error(`Cache namespace '${namespace}' not configured`);
    }
    return this.caches.get(namespace)!;
  }
}

// Module-specific cache providers
@NgModule({
  providers: [
    {
      provide: 'UserCache',
      useFactory: (cache: ConfigurableCacheService) => {
        cache.registerConfig('users', { ttl: 300000, maxSize: 100, strategy: 'lru' });
        return cache;
      },
      deps: [ConfigurableCacheService]
    }
  ]
})
class UserModule {}

// Usage
@Injectable()
class UserService {
  constructor(@Inject('UserCache') private cache: ConfigurableCacheService) {}
  
  getUser(id: string): Observable<User> {
    const cached = this.cache.get('users', id);
    if (cached) return of(cached);
    
    return this.http.get<User>(`/api/users/${id}`).pipe(
      tap(user => this.cache.set('users', id, user))
    );
  }
}
```

### 37. How would you implement aspect-oriented programming (AOP) concepts using Angular's DI and decorators?

**Answer:**

```typescript
// Method decorator for logging
function Log(target: any, propertyName: string, descriptor: PropertyDescriptor) {
  const method = descriptor.value;
  
  descriptor.value = function (...args: any[]) {
    console.log(`Calling ${propertyName} with args:`, args);
    const start = performance.now();
    
    try {
      const result = method.apply(this, args);
      
      if (result instanceof Promise) {
        return result.then(res => {
          console.log(`${propertyName} completed in ${performance.now() - start}ms`);
          return res;
        });
      } else if (result instanceof Observable) {
        return result.pipe(
          tap(() => console.log(`${propertyName} completed in ${performance.now() - start}ms`))
        );
      }
      
      console.log(`${propertyName} completed in ${performance.now() - start}ms`);
      return result;
    } catch (error) {
      console.error(`${propertyName} failed:`, error);
      throw error;
    }
  };
}

// Caching decorator
function Cache(ttl: number = 300000) {
  return function (target: any, propertyName: string, descriptor: PropertyDescriptor) {
    const method = descriptor.value;
    const cache = new Map<string, { value: any; timestamp: number }>();
    
    descriptor.value = function (...args: any[]) {
      const key = JSON.stringify(args);
      const cached = cache.get(key);
      
      if (cached && Date.now() - cached.timestamp < ttl) {
        return cached.value;
      }
      
      const result = method.apply(this, args);
      cache.set(key, { value: result, timestamp: Date.now() });
      return result;
    };
  };
}

// Service with AOP decorators
@Injectable({ providedIn: 'root' })
class UserService {
  
  @Log
  @Cache(300000)
  getUser(id: string): Observable<User> {
    return this.http.get<User>(`/api/users/${id}`);
  }
  
  @Log
  updateUser(user: User): Observable<User> {
    return this.http.put<User>(`/api/users/${user.id}`, user);
  }
}

// Interceptor-based AOP
@Injectable()
class LoggingInterceptor implements HttpInterceptor {
  intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
    console.log('HTTP Request:', req.method, req.url);
    
    return next.handle(req).pipe(
      tap(event => {
        if (event instanceof HttpResponse) {
          console.log('HTTP Response:', event.status, event.url);
        }
      })
    );
  }
}
```

### 38. Explain optional dependencies and how you'd handle scenarios where services might not be available.

**Answer:**

```typescript
// Optional dependency injection
@Injectable({ providedIn: 'root' })
class DataService {
  constructor(
    private http: HttpClient,
    @Optional() private cache: CacheService,
    @Optional() private logger: LoggerService,
    @Optional() @Inject(FEATURE_FLAGS) private features: FeatureFlags
  ) {}
  
  getData(id: string): Observable<any> {
    // Check cache if available
    if (this.cache) {
      const cached = this.cache.get(id);
      if (cached) {
        this.logger?.info('Data served from cache');
        return of(cached);
      }
    }
    
    // Log if logger is available
    this.logger?.info(`Fetching data for ${id}`);
    
    return this.http.get(`/api/data/${id}`).pipe(
      tap(data => {
        // Cache if service is available
        this.cache?.set(id, data);
        
        // Feature flag check
        if (this.features?.analytics) {
          this.trackDataAccess(id);
        }
      })
    );
  }
}

// Conditional service provision
@NgModule({
  providers: [
    // Conditionally provide services
    ...(environment.production ? [LoggerService] : []),
    {
      provide: CacheService,
      useClass: environment.useRedis ? RedisCacheService : MemoryCacheService
    },
    {
      provide: FEATURE_FLAGS,
      useValue: environment.features || {}
    }
  ]
})
class AppModule {}

// Service availability checking
@Injectable()
class ConditionalService {
  constructor(private injector: Injector) {}
  
  performAction() {
    // Check if service is available at runtime
    try {
      const analytics = this.injector.get(AnalyticsService, null);
      analytics?.track('action_performed');
    } catch (error) {
      console.warn('Analytics service not available');
    }
  }
  
  // Alternative approach
  isServiceAvailable<T>(token: Type<T> | InjectionToken<T>): boolean {
    try {
      return !!this.injector.get(token, null);
    } catch {
      return false;
    }
  }
}

// Default implementations for optional services
const DEFAULT_LOGGER: LoggerService = {
  info: () => {},
  warn: () => {},
  error: () => {}
};

@Injectable()
class ServiceWithDefaults {
  private logger: LoggerService;
  
  constructor(@Optional() logger?: LoggerService) {
    this.logger = logger || DEFAULT_LOGGER;
  }
}
```

### 39. How would you implement a factory pattern within Angular's DI system for creating services based on runtime conditions?

**Answer:**

```typescript
// Factory interface
interface ServiceFactory<T> {
  create(config: any): T;
}

// Concrete factories
@Injectable()
class HttpClientFactory implements ServiceFactory<HttpClient> {
  create(config: HttpConfig): HttpClient {
    return new HttpClient(config.baseUrl, config.timeout);
  }
}

@Injectable()
class DatabaseFactory implements ServiceFactory<DatabaseService> {
  create(config: DatabaseConfig): DatabaseService {
    switch (config.type) {
      case 'postgresql':
        return new PostgreSQLService(config);
      case 'mongodb':
        return new MongoDBService(config);
      default:
        throw new Error(`Unsupported database type: ${config.type}`);
    }
  }
}

// Factory registry
@Injectable({ providedIn: 'root' })
class ServiceFactoryRegistry {
  private factories = new Map<string, ServiceFactory<any>>();
  
  register<T>(key: string, factory: ServiceFactory<T>) {
    this.factories.set(key, factory);
  }
  
  create<T>(key: string, config: any): T {
    const factory = this.factories.get(key);
    if (!factory) {
      throw new Error(`Factory not found: ${key}`);
    }
    return factory.create(config);
  }
}

// Runtime service creation
@Injectable()
class DynamicServiceProvider {
  constructor(
    private factoryRegistry: ServiceFactoryRegistry,
    private configService: ConfigService
  ) {}
  
  async createService<T>(type: string): Promise<T> {
    const config = await this.configService.getConfig(type);
    return this.factoryRegistry.create<T>(type, config);
  }
}

// Provider factory functions
export function createDatabaseService(
  factory: DatabaseFactory,
  config: ConfigService
): DatabaseService {
  const dbConfig = config.getDatabaseConfig();
  return factory.create(dbConfig);
}

// Module configuration
@NgModule({
  providers: [
    DatabaseFactory,
    {
      provide: DatabaseService,
      useFactory: createDatabaseService,
      deps: [DatabaseFactory, ConfigService]
    },
    {
      provide: 'DynamicHttpClient',
      useFactory: (factory: HttpClientFactory, config: ConfigService) => {
        return (endpoint: string) => factory.create(config.getHttpConfig(endpoint));
      },
      deps: [HttpClientFactory, ConfigService]
    }
  ]
})
class DataModule {}
```

### 40. Design a service locator pattern that works efficiently with Angular's DI while avoiding anti-patterns.

**Answer:**

```typescript
// Service locator interface
interface ServiceLocator {
  get<T>(token: Type<T> | InjectionToken<T>): T;
  has<T>(token: Type<T> | InjectionToken<T>): boolean;
}

// Angular-integrated service locator
@Injectable({ providedIn: 'root' })
class AngularServiceLocator implements ServiceLocator {
  constructor(private injector: Injector) {}
  
  get<T>(token: Type<T> | InjectionToken<T>): T {
    return this.injector.get(token);
  }
  
  has<T>(token: Type<T> | InjectionToken<T>): boolean {
    try {
      return !!this.injector.get(token, null);
    } catch {
      return false;
    }
  }
  
  // Safe get with fallback
  getSafe<T>(token: Type<T> | InjectionToken<T>, fallback?: T): T | undefined {
    try {
      return this.injector.get(token, fallback);
    } catch {
      return fallback;
    }
  }
}

// Scoped service locator for modules
@Injectable()
class ScopedServiceLocator {
  private services = new Map<any, any>();
  
  constructor(private parentLocator: AngularServiceLocator) {}
  
  register<T>(token: Type<T> | InjectionToken<T>, instance: T): void {
    this.services.set(token, instance);
  }
  
  get<T>(token: Type<T> | InjectionToken<T>): T {
    // Check local scope first
    if (this.services.has(token)) {
      return this.services.get(token);
    }
    
    // Fall back to parent (Angular's injector)
    return this.parentLocator.get(token);
  }
}

// Plugin system using service locator
@Injectable()
class PluginManager {
  constructor(private serviceLocator: AngularServiceLocator) {}
  
  loadPlugin(pluginConfig: PluginConfig): void {
    const dependencies = pluginConfig.dependencies.map(dep => 
      this.serviceLocator.get(dep)
    );
    
    const plugin = new pluginConfig.pluginClass(...dependencies);
    plugin.initialize();
  }
  
  // Conditional service access
  getOptionalService<T>(token: Type<T>): T | null {
    return this.serviceLocator.has(token) ? this.serviceLocator.get(token) : null;
  }
}

// Best practices wrapper
@Injectable({ providedIn: 'root' })
class SafeServiceLocator {
  private cache = new Map<any, any>();
  
  constructor(private injector: Injector) {}
  
  // Cached service access
  getCached<T>(token: Type<T> | InjectionToken<T>): T {
    if (!this.cache.has(token)) {
      this.cache.set(token, this.injector.get(token));
    }
    return this.cache.get(token);
  }
  
  // Typed service access with validation
  getService<T>(token: Type<T>, validator?: (service: T) => boolean): T {
    const service = this.injector.get(token);
    
    if (validator && !validator(service)) {
      throw new Error(`Service validation failed for ${token.name}`);
    }
    
    return service;
  }
  
  // Lazy service access
  getLazy<T>(token: Type<T>): () => T {
    return () => this.injector.get(token);
  }
}

// Usage example avoiding anti-patterns
@Injectable()
class ProperServiceUsage {
  // ✅ Inject specific dependencies
  constructor(
    private userService: UserService,
    private logger: LoggerService,
    private serviceLocator: SafeServiceLocator // Only when necessary
  ) {}
  
  // ✅ Use service locator for dynamic/optional services only
  processWithOptionalFeatures(data: any) {
    // Core functionality
    const result = this.userService.process(data);
    
    // Optional features based on availability
    const analytics = this.serviceLocator.getCached(AnalyticsService);
    if (analytics) {
      analytics.track('data_processed');
    }
    
    return result;
  }
}
```

**Service Locator Best Practices:**
- Use only for dynamic service resolution
- Prefer constructor injection for known dependencies
- Implement caching to avoid repeated lookups
- Add proper error handling and validation
- Avoid overuse - maintain dependency transparency

---

## Advanced Component Patterns

### 41. Implement a higher-order component pattern in Angular that adds common functionality to multiple components.

### 42. Design a complex data table component with virtual scrolling, dynamic column configuration, and inline editing capabilities.

### 43. How would you implement the compound component pattern in Angular (similar to React's compound components)?

### 44. Create a flexible modal system that supports stacking, custom animations, and dynamic content projection.

### 45. Design a form builder component that generates forms dynamically from JSON schema with custom validation rules.

### 46. Implement a complex drag-and-drop system with multiple zones, constraints, and undo/redo functionality.

### 47. How would you create a component that adapts its behavior based on its container's size (element queries)?

### 48. Design a reusable chart component that supports multiple chart types, real-time updates, and responsive behavior.

### 49. Implement a virtual scroller component that handles variable item heights and horizontal scrolling.

### 50. Create a complex wizard component with conditional steps, validation, and save/resume functionality.

---

## Routing & Navigation

### 51. Design a complex routing architecture for a multi-module application with lazy loading and role-based access control.

### 52. How would you implement nested routing with independent navigation states for different sections of an application?

### 53. Create a custom route guard that handles complex authorization scenarios including role hierarchies and resource-based permissions.

### 54. Implement a navigation system that supports undo/redo functionality and maintains navigation history.

### 55. How would you handle route preloading strategies in a large application with hundreds of routes?

### 56. Design a routing solution that supports A/B testing with different component implementations for the same routes.

### 57. Implement deep linking support for complex component states including form data and filter configurations.

### 58. How would you handle route transitions with complex animations and state preservation?

### 59. Create a custom route resolver that handles complex data dependencies and error scenarios.

### 60. Design a routing architecture that supports microfrontend integration with independent routing contexts.

---

## Forms & Validation

### 61. Design a complex form validation system that supports async validation, cross-field dependencies, and conditional validation rules.

### 62. Implement a dynamic form generator that creates forms from JSON schema with custom component mappings.

### 63. How would you handle large forms with thousands of fields while maintaining performance?

### 64. Create a form state management system that supports undo/redo, auto-save, and conflict resolution.

### 65. Design a multi-step form with complex branching logic and validation that only occurs at specific steps.

### 66. Implement a form array system that handles dynamic addition/removal of complex nested forms.

### 67. How would you create a form validation system that works with both reactive and template-driven forms?

### 68. Design a form component that supports multiple data sources and real-time synchronization.

### 69. Implement a custom form control that integrates with Angular's validation system for complex input types.

### 70. Create a form builder that supports conditional field visibility and dynamic validation rule assignment.

---

## Testing & Quality Assurance

### 71. Design a comprehensive testing strategy for a large Angular application including unit, integration, and e2e tests.

### 72. How would you test components that heavily rely on RxJS observables and complex async operations?

### 73. Implement a custom testing utility that simplifies testing of components with complex dependencies.

### 74. How would you test Angular services that interact with external APIs and handle various error scenarios?

### 75. Design a mocking strategy for complex service dependencies in unit tests.

### 76. How would you test custom directives and pipes with complex logic and edge cases?

### 77. Implement a testing approach for components that use OnPush change detection strategy.

### 78. How would you test complex routing scenarios including guards, resolvers, and nested routes?

### 79. Design a performance testing strategy for Angular applications including change detection and memory usage.

### 80. How would you implement visual regression testing for a component library?

---

## Performance Optimization

### 81. Design a comprehensive performance optimization strategy for a large-scale Angular application.

### 82. How would you implement code splitting and lazy loading for optimal bundle sizes?

### 83. Create a performance monitoring system that tracks key metrics in production Angular applications.

### 84. How would you optimize Angular applications for mobile devices with limited resources?

### 85. Implement a caching strategy that works across different layers (HTTP, component state, service layer).

### 86. Design a strategy for optimizing large lists and tables with thousands of items.

### 87. How would you optimize Angular applications for SEO while maintaining rich interactivity?

### 88. Implement a progressive loading strategy for complex dashboard applications.

### 89. How would you handle memory leaks in long-running Angular applications?

### 90. Design a strategy for optimizing third-party library usage in Angular applications.

---

## Security & Best Practices

### 91. Design a comprehensive security strategy for Angular applications including XSS prevention and CSRF protection.

### 92. How would you implement secure authentication and authorization in a single-page Angular application?

### 93. Create a content security policy (CSP) implementation for Angular applications with dynamic content.

### 94. How would you handle sensitive data in Angular applications to prevent exposure in client-side code?

### 95. Design a secure communication pattern between Angular frontend and backend APIs.

---

## Scalable Architecture

### 96. Design a microfrontend architecture using Angular that supports independent deployment and development teams.

### 97. How would you structure a large Angular monorepo with multiple applications and shared libraries?

### 98. Create an architecture that supports multiple Angular versions running simultaneously in the same application.

### 99. Design a plugin system that allows third-party developers to extend Angular applications safely.

### 100. How would you implement a scalable state management solution for enterprise-level Angular applications with complex data flows and multiple user roles?

---

## Additional Resources

- [Angular Official Documentation](https://angular.io/docs)
- [RxJS Documentation](https://rxjs.dev/)
- [Angular DevKit](https://github.com/angular/angular-cli)
- [Angular Testing Utilities](https://angular.io/guide/testing)

---

*This collection is designed to test deep understanding of Angular internals, architectural thinking, and practical problem-solving skills required for senior and staff-level positions.*
