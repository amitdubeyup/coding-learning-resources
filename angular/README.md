# Top 100 Complex Angular Interview Questions for Senior/Staff Engineers

A comprehensive collection of advanced Angular interview questions focusing on deep technical understanding, architecture decisions, and real-world problem-solving scenarios. These questions are designed to assess expertise in Angular internals, performance optimization, scalable architecture patterns, and complex implementation challenges typically encountered at senior and staff engineer levels.

**Target Audience:** Senior Frontend Engineers, Staff Engineers, Angular Architects, Tech Leads
**Difficulty Level:** Advanced to Expert
**Focus Areas:** Architecture, Performance, Security, Scalability, Best Practices

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

**JIT (Just-In-Time)**: Compiles templates and components in the browser at runtime
**AOT (Ahead-Of-Time)**: Compiles templates and components during build process

```typescript
// AOT benefits:
// - Smaller bundle sizes (no Angular compiler needed)
// - Faster rendering (pre-compiled templates)
// - Early detection of template errors
// - Better security (templates pre-compiled)

// Ivy renderer improvements:
// - Incremental compilation
// - Better tree-shaking (unused code elimination)
// - Smaller bundle sizes
// - Improved build errors and debugging
// - Locality principle (components are self-contained)
```

### 2. Describe the complete lifecycle of an Angular application from bootstrap to component destruction, including the role of ApplicationRef and NgZone.

**Answer:**

```typescript
// Application Lifecycle:
1. platformBrowserDynamic() creates platform
2. bootstrapModule() loads root module
3. ApplicationRef.bootstrap() creates root component
4. NgZone patches async operations
5. Change detection cycles run
6. Component tree creation and lifecycle hooks
7. Application destruction

// ApplicationRef manages component views and change detection
// NgZone wraps async operations to trigger change detection
class CustomBootstrap {
  constructor(private appRef: ApplicationRef, private zone: NgZone) {
    this.zone.onStable.subscribe(() => {
      // App is stable, all async operations complete
    });
  }
}
```

### 3. How does Angular's hierarchical injector system work? Explain the resolution strategy and how to create custom injectors programmatically.

**Answer:**

```typescript
// Injector Hierarchy (bottom-up resolution):
// Element Injector → Module Injector → Application Injector → Platform Injector

// Custom injector creation:
const customInjector = Injector.create({
  providers: [
    { provide: MyService, useClass: MyServiceImpl },
    { provide: CONFIG_TOKEN, useValue: { api: 'https://api.example.com' } }
  ],
  parent: this.injector // Optional parent injector
});

// Resolution strategy:
// 1. Start at requesting element
// 2. Check element injector
// 3. Move up component tree
// 4. Check module injector
// 5. Check parent modules
// 6. Throw error if not found
```

### 4. What is the difference between ViewChild, ContentChild, and their query counterparts? When would you use static vs dynamic queries?

**Answer:**

```typescript
@Component({
  template: `
    <child-component #childRef></child-component>
    <ng-content></ng-content>
  `
})
class ParentComponent {
  // ViewChild - queries component's own template
  @ViewChild('childRef', { static: true }) staticChild!: ChildComponent;
  @ViewChild('childRef', { static: false }) dynamicChild!: ChildComponent;
  
  // ContentChild - queries projected content
  @ContentChild(SomeDirective) projectedDirective!: SomeDirective;
  
  // Multiple queries
  @ViewChildren(ChildComponent) allChildren!: QueryList<ChildComponent>;
  @ContentChildren(ItemDirective) projectedItems!: QueryList<ItemDirective>;
}

// Static: Available in ngOnInit (always present in template)
// Dynamic: Available in ngAfterViewInit (conditional rendering)
```

### 5. Explain the concept of Angular Elements and how you would architect a micro-frontend solution using Angular Elements.

**Answer:**

```typescript
// Angular Elements - Custom Elements for framework interop
@NgModule({
  declarations: [MyComponent],
  entryComponents: [MyComponent]
})
class ElementsModule {
  constructor(private injector: Injector) {}
  
  ngDoBootstrap() {
    const customElement = createCustomElement(MyComponent, { injector: this.injector });
    customElements.define('my-custom-element', customElement);
  }
}

// Micro-frontend Architecture:
// 1. Shell Application (container)
// 2. Feature Applications (Angular Elements)
// 3. Shared Communication Bus
// 4. Independent deployment pipeline
// 5. Runtime integration

// Communication patterns:
// - Custom events for component communication
// - Shared state management
// - Message bus for cross-app communication
```

### 6. How does Angular's tree-shaking work with the module system? What are the implications of using providedIn: 'root' vs module providers?

**Answer:**

Tree-shaking removes unused code. providedIn: 'root' is tree-shakable and creates singletons, module providers are always included.

### 7. Describe the role of ApplicationInitializer and how you would use it to implement complex application startup logic.

**Answer:**

APP_INITIALIZER runs before app starts. Use for config loading, auth setup, multi-provider pattern for multiple initializers.

### 8. Explain how Angular's renderer abstraction works and when you might need to create a custom renderer.

**Answer:**

Renderer2 provides platform-agnostic DOM manipulation. Use custom renderers for platform optimizations, debugging, or legacy integration.

### 9. What are the internal differences between NgModules and standalone components? How does the dependency resolution differ?

**Answer:**

Standalone components (Angular 14+) have component-level imports, simpler dependency trees, better tree-shaking than NgModules.

### 10. How does Angular handle circular dependencies, and what strategies would you implement to avoid them in large applications?

**Answer:**

Angular detects circular dependencies and throws errors. Solutions: forwardRef, mediator pattern, lazy injection, layered architecture.

---

## Advanced RxJS & Observables

### 11. Design a complex data synchronization system using RxJS that handles real-time updates, offline scenarios, and conflict resolution.

**Answer:**

WebSocket for real-time updates, offline queue for pending operations, timestamp-based conflict resolution, merge multiple data sources.

### 12. Explain the difference between hot and cold observables. How would you implement a caching mechanism using shareReplay with custom cache invalidation?

**Answer:**

Cold observables create new execution per subscriber, hot observables share execution. Use shareReplay with takeUntil for cache invalidation.

### 13. How would you implement a retry mechanism with exponential backoff, jitter, and circuit breaker pattern using RxJS operators?

**Answer:**

retryWhen with scan for counting attempts, exponential delay calculation with jitter, circuit breaker state management.

### 14. Design a reactive state management solution using only RxJS (without NgRx) for a complex e-commerce application.

**Answer:**

BehaviorSubject for state, select method with distinctUntilChanged, update method for immutable state changes, feature stores.

### 15. Explain memory leak scenarios in RxJS and implement a custom operator that automatically handles subscription cleanup based on component lifecycle.

**Answer:**

Memory leaks from unsubscribed observables. Use takeUntil with destroy$ subject, automatic ngOnDestroy hooks, subscription management.

### 16. How would you implement a complex search functionality with debouncing, cancellation of previous requests, and result caching using RxJS?

**Answer:**

```typescript
@Injectable()
class SearchService {
  private cache = new Map<string, any>();
  
  search(query$: Observable<string>): Observable<SearchResult[]> {
    return query$.pipe(
      debounceTime(300), // Wait for user to stop typing
      distinctUntilChanged(), // Avoid duplicate requests
      filter(query => query.length >= 2), // Minimum query length
      switchMap(query => {
        // Check cache first
        if (this.cache.has(query)) {
          return of(this.cache.get(query));
        }
        
        // Make HTTP request (switchMap cancels previous)
        return this.http.get<SearchResult[]>(`/api/search?q=${query}`).pipe(
          tap(results => this.cache.set(query, results)), // Cache results
          catchError(error => {
            console.error('Search failed:', error);
            return of([]); // Return empty results on error
          })
        );
      }),
      shareReplay(1) // Share result with multiple subscribers
    );
  }
}
```

### 17. Design a reactive form validation system that supports async validators, cross-field validation, and real-time error display.

**Answer:**

Custom ValidatorFn functions, AsyncValidatorFn with debouncing, FormGroup cross-field validation, cached async validators.
```

### 18. Implement a custom RxJS operator that batches HTTP requests and handles rate limiting automatically.

**Answer:**

bufferTime for batching, concatMap with delay for rate limiting, request counting for throttling, fallback to individual requests.

### 19. How would you handle complex error scenarios in RxJS streams, including retry with different strategies based on error types?

**Answer:**

Error classification by type, strategy-based retry logic, circuit breaker pattern, fallback mechanisms, retry count management.
```

### 20. Design a reactive data pipeline that transforms, filters, and aggregates real-time data streams with backpressure handling.

**Answer:**

Configurable pipeline with transformation stages, backpressure strategies (throttle, buffer, sample), error handling per stage, windowed aggregation.

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

Custom strategies rarely needed. Use case: high-frequency trading dashboard with timestamp-based updates only.

### 23. How does NgZone work internally, and when would you run code outside Angular's zone? What are the implications?

**Answer:**

```typescript
@Component({
  template: `
    <div>{{ counter }}</div>
    <canvas #canvas></canvas>
  `
})
class PerformanceComponent implements OnInit {
  counter = 0;
  
  constructor(private ngZone: NgZone) {}
  
  ngOnInit() {
    // High-frequency updates outside zone (no change detection)
    this.ngZone.runOutsideAngular(() => {
      setInterval(() => {
        this.updateCanvas(); // Heavy animation logic
      }, 16); // 60fps
    });
    
    // Periodic updates inside zone (triggers change detection)
    this.ngZone.run(() => {
      setInterval(() => {
        this.counter++; // UI update needed
      }, 1000);
    });
  }
  
  // Manual change detection trigger when needed
  onUserAction() {
    this.ngZone.runOutsideAngular(() => {
      // Expensive operation
      this.processLargeDataset();
      
      // Trigger change detection once at the end
      this.ngZone.run(() => {
        this.updateUI();
      });
    });
  }
}
```

### 24. Explain the concept of change detection cycles and how to debug performance issues related to excessive change detection.

**Answer:**

```typescript
// Debugging change detection performance
export class ChangeDetectionDebugger {
  
  // Method 1: Profile change detection timing
  profileChangeDetection() {
    ng.profiler.timeChangeDetection();
    // Logs change detection timing to console
  }
  
  // Method 2: Track component check counts
  @Component({
    template: `{{ getDisplayValue() }} <!-- AVOID: method in template -->`,
    changeDetection: ChangeDetectionStrategy.OnPush
  })
  class ProblematicComponent {
    private checkCount = 0;
    
    getDisplayValue() {
      console.log(`Component checked ${++this.checkCount} times`);
      return this.someExpensiveCalculation(); // Performance killer!
    }
  }
  
  // Method 3: Better approach with memoization
  @Component({
    template: `{{ displayValue }}`, // Use property instead
    changeDetection: ChangeDetectionStrategy.OnPush
  })
  class OptimizedComponent {
    private _cachedValue: string;
    private _lastInput: any;
    
    @Input() 
    set data(value: any) {
      if (value !== this._lastInput) {
        this._lastInput = value;
        this._cachedValue = this.someExpensiveCalculation(value);
      }
    }
    
    get displayValue() { return this._cachedValue; }
  }
  
  // Method 4: Change detection strategy
  measureChangeDetectionCycles() {
    let cycleCount = 0;
    
    // Patch ApplicationRef.tick to count cycles
    const originalTick = ApplicationRef.prototype.tick;
    ApplicationRef.prototype.tick = function() {
      console.log(`Change detection cycle ${++cycleCount}`);
      return originalTick.apply(this, arguments);
    };
  }
}
```

### 25. How would you implement manual change detection triggering in a large application with complex component hierarchies?

**Answer:**

Global detection service with ApplicationRef.tick(), component-level markForCheck(), detach/reattach for fine control.

### 26. Describe scenarios where you'd use ChangeDetectorRef methods (detectChanges, markForCheck, detach, reattach) and their performance implications.

**Answer:**

detectChanges() for immediate updates, markForCheck() for OnPush components, detach()/reattach() for performance control during animations.

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

- **'root'**: App-level singleton, tree-shakable
- **'platform'**: Shared across multiple Angular apps  
- **'any'**: Separate instance per lazy-loaded module

### 32. How would you implement a plugin architecture using Angular's DI system with dynamic service registration?

**Answer:**

Use InjectionToken, plugin registry service, and dynamic imports. Register plugins at runtime via injector.get().

### 33. Design a multi-tenant application where services behave differently based on tenant configuration using DI.

**Answer:**

```typescript
// Tenant configuration interface
interface TenantConfig {
  id: string;
  features: string[];
  theme: string;
  apiUrl: string;
  dbConnection: string;
}

// Injection tokens
const TENANT_CONFIG = new InjectionToken<TenantConfig>('tenant.config');
const TENANT_ID = new InjectionToken<string>('tenant.id');

// Abstract base service
abstract class BaseDataService {
  abstract getData(): Observable<any[]>;
}

// Tenant-specific implementations
@Injectable()
class TenantADataService extends BaseDataService {
  constructor(@Inject(TENANT_CONFIG) private config: TenantConfig) {
    super();
  }
  
  getData(): Observable<any[]> {
    return this.http.get(`${this.config.apiUrl}/tenant-a/data`);
  }
}

@Injectable()
class TenantBDataService extends BaseDataService {
  constructor(@Inject(TENANT_CONFIG) private config: TenantConfig) {
    super();
  }
  
  getData(): Observable<any[]> {
    return this.http.get(`${this.config.apiUrl}/tenant-b/special-data`);
  }
}

// Factory function for tenant-specific services
export function dataServiceFactory(
  config: TenantConfig,
  http: HttpClient
): BaseDataService {
  switch (config.id) {
    case 'tenant-a':
      return new TenantADataService(config);
    case 'tenant-b':
      return new TenantBDataService(config);
    default:
      throw new Error(`Unknown tenant: ${config.id}`);
  }
}

// Module configuration
@NgModule({
  providers: [
    {
      provide: TENANT_CONFIG,
      useFactory: () => {
        // Get tenant config from URL, localStorage, etc.
        const tenantId = getTenantFromUrl();
        return loadTenantConfig(tenantId);
      }
    },
    {
      provide: BaseDataService,
      useFactory: dataServiceFactory,
      deps: [TENANT_CONFIG, HttpClient]
    }
  ]
})
class TenantModule {}

// Usage in components
@Component({
  template: `
    <div [ngClass]="'theme-' + tenantConfig.theme">
      <ng-container *ngFor="let feature of tenantConfig.features">
        <feature-component [type]="feature"></feature-component>
      </ng-container>
    </div>
  `
})
class TenantAwareComponent {
  constructor(
    @Inject(TENANT_CONFIG) public tenantConfig: TenantConfig,
    private dataService: BaseDataService
  ) {}
}
```

### 34. Explain injection tokens and how you'd use them to implement a configurable logging system.

**Answer:**

```typescript
// Logging configuration interfaces
interface LogConfig {
  level: LogLevel;
  enableConsole: boolean;
  enableRemote: boolean;
  remoteUrl?: string;
  enableFileLogging: boolean;
}

enum LogLevel {
  DEBUG = 0,
  INFO = 1,
  WARN = 2,
  ERROR = 3
}

// Injection tokens for configuration
const LOG_CONFIG = new InjectionToken<LogConfig>('log.config');
const LOG_WRITERS = new InjectionToken<LogWriter[]>('log.writers');

// Abstract log writer interface
abstract class LogWriter {
  abstract write(level: LogLevel, message: string, data?: any): void;
}

// Concrete log writer implementations
@Injectable()
class ConsoleLogWriter extends LogWriter {
  write(level: LogLevel, message: string, data?: any): void {
    const method = level >= LogLevel.ERROR ? 'error' : 
                   level >= LogLevel.WARN ? 'warn' : 
                   level >= LogLevel.INFO ? 'info' : 'debug';
    console[method](message, data);
  }
}

@Injectable()
class RemoteLogWriter extends LogWriter {
  constructor(
    private http: HttpClient,
    @Inject(LOG_CONFIG) private config: LogConfig
  ) {
    super();
  }
  
  write(level: LogLevel, message: string, data?: any): void {
    if (this.config.enableRemote && this.config.remoteUrl) {
      this.http.post(this.config.remoteUrl, {
        level: LogLevel[level],
        message,
        data,
        timestamp: new Date().toISOString()
      }).subscribe();
    }
  }
}

// Main logging service
@Injectable({ providedIn: 'root' })
class LoggerService {
  constructor(
    @Inject(LOG_CONFIG) private config: LogConfig,
    @Inject(LOG_WRITERS) private writers: LogWriter[]
  ) {}
  
  debug(message: string, data?: any): void {
    this.log(LogLevel.DEBUG, message, data);
  }
  
  info(message: string, data?: any): void {
    this.log(LogLevel.INFO, message, data);
  }
  
  warn(message: string, data?: any): void {
    this.log(LogLevel.WARN, message, data);
  }
  
  error(message: string, data?: any): void {
    this.log(LogLevel.ERROR, message, data);
  }
  
  private log(level: LogLevel, message: string, data?: any): void {
    if (level >= this.config.level) {
      this.writers.forEach(writer => writer.write(level, message, data));
    }
  }
}

// Factory function for log writers
export function logWritersFactory(config: LogConfig): LogWriter[] {
  const writers: LogWriter[] = [];
  
  if (config.enableConsole) {
    writers.push(new ConsoleLogWriter());
  }
  
  if (config.enableRemote) {
    writers.push(new RemoteLogWriter(inject(HttpClient), config));
  }
  
  return writers;
}

// Module configuration
@NgModule({
  providers: [
    {
      provide: LOG_CONFIG,
      useValue: {
        level: LogLevel.INFO,
        enableConsole: true,
        enableRemote: environment.production,
        remoteUrl: environment.logUrl,
        enableFileLogging: false
      }
    },
    {
      provide: LOG_WRITERS,
      useFactory: logWritersFactory,
      deps: [LOG_CONFIG],
      multi: true // Multiple providers for same token
    },
    LoggerService
  ]
})
class LoggingModule {}
```

### 35. How would you implement service inheritance and composition patterns in Angular's DI system?

**Answer:**

Abstract base services with template pattern, composition via constructor injection, mixins for multiple inheritance.

### 36. Design a caching service that can be configured differently for different modules while maintaining singleton behavior.

**Answer:**

Namespace-based cache with module-specific configurations, single CacheService with Map<namespace, cache>.

### 37. How would you implement aspect-oriented programming (AOP) concepts using Angular's DI and decorators?

**Answer:**

Method decorators for cross-cutting concerns (logging, caching), interceptors for HTTP aspects, proxy services.

### 38. Explain optional dependencies and how you'd handle scenarios where services might not be available.

**Answer:**

Use @Optional() decorator, null checks, fallback implementations, and conditional service access.

### 39. How would you implement a factory pattern within Angular's DI system for creating services based on runtime conditions?

**Answer:**

Factory functions with useFactory, abstract factories, and service registry for dynamic creation.

### 40. Design a service locator pattern that works efficiently with Angular's DI while avoiding anti-patterns.

**Answer:**

Wrapper around Injector, cached lookups, use only for dynamic/optional services, prefer constructor injection.

---

## Advanced Component Patterns

### 41. Implement a higher-order component pattern in Angular that adds common functionality to multiple components.

**Answer:**

```typescript
// Mixin pattern for shared behavior
type Constructor<T = {}> = new (...args: any[]) => T;

// Loadable mixin
function WithLoading<TBase extends Constructor>(Base: TBase) {
  return class extends Base {
    loading = false;
    
    async executeWithLoading<T>(operation: () => Promise<T>): Promise<T> {
      this.loading = true;
      try {
        return await operation();
      } finally {
        this.loading = false;
      }
    }
  };
}

// Trackable mixin
function WithTracking<TBase extends Constructor>(Base: TBase) {
  return class extends Base {
    private analytics = inject(AnalyticsService);
    
    track(event: string, data?: any) {
      this.analytics.track(event, data);
    }
  };
}

// Usage in components
@Component({
  template: `
    <div *ngIf="loading">Loading...</div>
    <button (click)="handleClick()">Action</button>
  `
})
class MyComponent extends WithTracking(WithLoading(class {})) {
  async handleClick() {
    this.track('button_clicked');
    await this.executeWithLoading(() => this.performAction());
  }
  
  private async performAction() {
    // Async operation
  }
}

// Alternative: Decorator-based approach
function Trackable(eventName: string) {
  return function(target: any, propertyKey: string, descriptor: PropertyDescriptor) {
    const originalMethod = descriptor.value;
    
    descriptor.value = function(...args: any[]) {
      const analytics = inject(AnalyticsService);
      analytics.track(eventName, { method: propertyKey, args });
      return originalMethod.apply(this, args);
    };
  };
}

@Component({...})
class TrackedComponent {
  @Trackable('user_action')
  performAction() {
    // Method automatically tracked
  }
}
```

### 42. Design a complex data table component with virtual scrolling, dynamic column configuration, and inline editing capabilities.

**Answer:**

```typescript
// Column configuration interface
interface TableColumn<T = any> {
  key: keyof T;
  header: string;
  width?: number;
  sortable?: boolean;
  editable?: boolean;
  renderer?: (value: any, row: T) => string;
  editor?: ComponentType<any>;
}

// Data table component
@Component({
  selector: 'app-data-table',
  template: `
    <div class="table-container">
      <!-- Virtual scroll viewport -->
      <cdk-virtual-scroll-viewport itemSize="50" class="table-viewport">
        <div class="table-header">
          <div *ngFor="let column of columns; trackBy: trackByColumn"
               class="table-cell header-cell"
               [style.width.px]="column.width"
               (click)="sort(column)">
            {{ column.header }}
            <span *ngIf="sortColumn === column.key" 
                  class="sort-indicator">
              {{ sortDirection === 'asc' ? '↑' : '↓' }}
            </span>
          </div>
        </div>
        
        <!-- Virtual scroll items -->
        <div *cdkVirtualFor="let row of sortedData; trackBy: trackByRow"
             class="table-row"
             [class.editing]="editingRow === row">
          
          <div *ngFor="let column of columns; trackBy: trackByColumn"
               class="table-cell"
               [style.width.px]="column.width">
            
            <!-- Edit mode -->
            <ng-container *ngIf="editingRow === row && column.editable">
              <ng-container [ngSwitch]="getEditorType(column)">
                <input *ngSwitchCase="'text'" 
                       [(ngModel)]="editingData[column.key]"
                       (keyup.enter)="saveEdit()"
                       (keyup.escape)="cancelEdit()">
                <select *ngSwitchCase="'select'"
                        [(ngModel)]="editingData[column.key]">
                  <option *ngFor="let option of getSelectOptions(column)"
                          [value]="option.value">
                    {{ option.label }}
                  </option>
                </select>
              </ng-container>
            </ng-container>
            
            <!-- Display mode -->
            <span *ngIf="editingRow !== row" 
                  (dblclick)="startEdit(row, column)">
              {{ getDisplayValue(row, column) }}
            </span>
          </div>
          
          <!-- Action buttons -->
          <div class="table-cell actions">
            <button *ngIf="editingRow !== row" 
                    (click)="startEdit(row)">Edit</button>
            <button *ngIf="editingRow === row" 
                    (click)="saveEdit()">Save</button>
            <button *ngIf="editingRow === row" 
                    (click)="cancelEdit()">Cancel</button>
          </div>
        </div>
      </cdk-virtual-scroll-viewport>
    </div>
  `,
  changeDetection: ChangeDetectionStrategy.OnPush
})
class DataTableComponent<T = any> implements OnInit {
  @Input() data: T[] = [];
  @Input() columns: TableColumn<T>[] = [];
  @Input() pageSize = 50;
  
  editingRow: T | null = null;
  editingData: Partial<T> = {};
  sortColumn: keyof T | null = null;
  sortDirection: 'asc' | 'desc' = 'asc';
  
  get sortedData(): T[] {
    if (!this.sortColumn) return this.data;
    
    return [...this.data].sort((a, b) => {
      const aVal = a[this.sortColumn!];
      const bVal = b[this.sortColumn!];
      const result = aVal < bVal ? -1 : aVal > bVal ? 1 : 0;
      return this.sortDirection === 'asc' ? result : -result;
    });
  }
  
  trackByRow = (index: number, row: T): any => {
    return (row as any).id || index;
  };
  
  trackByColumn = (index: number, column: TableColumn<T>): any => {
    return column.key;
  };
  
  sort(column: TableColumn<T>) {
    if (!column.sortable) return;
    
    if (this.sortColumn === column.key) {
      this.sortDirection = this.sortDirection === 'asc' ? 'desc' : 'asc';
    } else {
      this.sortColumn = column.key;
      this.sortDirection = 'asc';
    }
    
    this.cdr.markForCheck();
  }
  
  startEdit(row: T, column?: TableColumn<T>) {
    this.editingRow = row;
    this.editingData = { ...row };
    this.cdr.markForCheck();
  }
  
  saveEdit() {
    if (this.editingRow) {
      Object.assign(this.editingRow, this.editingData);
      this.editingRow = null;
      this.editingData = {};
      this.cdr.markForCheck();
    }
  }
  
  cancelEdit() {
    this.editingRow = null;
    this.editingData = {};
    this.cdr.markForCheck();
  }
  
  getDisplayValue(row: T, column: TableColumn<T>): string {
    const value = row[column.key];
    return column.renderer ? column.renderer(value, row) : String(value);
  }
  
  getEditorType(column: TableColumn<T>): string {
    return column.editor ? 'custom' : 'text';
  }
  
  constructor(private cdr: ChangeDetectorRef) {}
}
```

### 43. How would you implement the compound component pattern in Angular (similar to React's compound components)?

**Answer:**

Content projection with ng-content, component communication via services, template references, shared context.

### 44. Create a flexible modal system that supports stacking, modal chaining, and dynamic content projection.

**Answer:**

CDK Overlay, z-index management, modal stack service, component factory for dynamic content, backdrop handling.

### 45. Design a form builder component that generates forms dynamically from JSON schema with custom validation rules.

**Answer:**

Reactive forms, FormBuilder, dynamic component rendering, custom validators, schema-to-form mapping.

### 46. Implement a complex drag-and-drop system with multiple zones, constraints, and undo/redo functionality.

**Answer:**

CDK Drag Drop, zone management, constraint functions, command pattern for undo/redo, state snapshots.

### 47. How would you create a component that adapts its behavior based on its container's size (element queries)?

**Answer:**

ResizeObserver API, BreakpointObserver, CSS container queries, responsive directive, size-based rendering.

### 48. Design a reusable chart component that supports multiple chart types, real-time updates, and responsive behavior.

**Answer:**

Strategy pattern for chart types, Observable data binding, resize detection, chart library abstraction.

### 49. Implement a virtual scroller component that handles variable item heights and horizontal scrolling.

**Answer:**

CDK Virtual Scroll with itemSize function, scroll position tracking, viewport calculations, buffer management.

### 50. Create a complex wizard component with conditional steps, validation, and save/resume functionality.

**Answer:**

Step registry, state machine, conditional navigation, form state persistence, step validation guards.

---

## Routing & Navigation

### 51. Design a complex routing architecture for a multi-module application with lazy loading and role-based access control.

**Answer:**

Feature modules, route guards, role-based canActivate, lazy loading with preloading strategies, route data.

### 52. How would you implement nested routing with independent navigation states for different sections of an application?

**Answer:**

Router outlets, auxiliary routes, independent router states, outlet-specific navigation, route synchronization.

### 53. Create a custom route guard that handles complex authorization scenarios including role hierarchies and resource-based permissions.

**Answer:**

CanActivate with role service, permission matrix, resource ownership checks, async permission resolution.

### 54. Implement a navigation system that supports undo/redo functionality and maintains navigation history.

**Answer:**

Location service, navigation stack, route state snapshots, history manipulation, custom navigation service.

### 55. How would you handle route preloading strategies in a large application with hundreds of routes?

**Answer:**

Custom PreloadingStrategy, priority-based loading, user behavior analytics, selective preloading, bandwidth detection.

### 56. Design a routing solution that supports A/B testing with different component implementations for the same routes.

**Answer:**

Dynamic component loading, feature flags, route data for variants, component mapping service.

### 57. Implement deep linking support for complex component states including form data and filter configurations.

**Answer:**

Query parameters, route state, URL serialization, state restoration, bookmark-friendly URLs.

### 58. How would you handle route transitions with complex animations and state preservation?

**Answer:**

Router animations, state transfer, animation triggers, component lifecycle management, transition guards.

### 59. Create a custom route resolver that handles complex data dependencies and error scenarios.

**Answer:**

Resolve interface, dependency chain resolution, error handling, loading states, data caching.

### 60. Design a routing architecture that supports microfrontend integration with independent routing contexts.

**Answer:**

Module federation, route delegation, independent router instances, cross-app navigation, shared routing state.

---

## Forms & Validation

### 61. Design a complex form validation system that supports async validation, cross-field dependencies, and conditional validation rules.

**Answer:**

```typescript
// Custom validator functions
export class CustomValidators {
  // Cross-field password confirmation
  static passwordConfirmation(passwordField: string, confirmField: string): ValidatorFn {
    return (group: AbstractControl): ValidationErrors | null => {
      const password = group.get(passwordField);
      const confirm = group.get(confirmField);
      
      if (!password || !confirm) return null;
      
      return password.value === confirm.value 
        ? null 
        : { passwordMismatch: true };
    };
  }
  
  // Conditional validation based on other field
  static conditionalRequired(conditionField: string, conditionValue: any): ValidatorFn {
    return (control: AbstractControl): ValidationErrors | null => {
      const form = control.parent;
      if (!form) return null;
      
      const conditionControl = form.get(conditionField);
      if (!conditionControl) return null;
      
      const shouldValidate = conditionControl.value === conditionValue;
      return shouldValidate && !control.value 
        ? { conditionalRequired: true } 
        : null;
    };
  }
  
  // Async email uniqueness validator
  static emailExists(userService: UserService): AsyncValidatorFn {
    return (control: AbstractControl): Observable<ValidationErrors | null> => {
      if (!control.value) return of(null);
      
      return userService.checkEmailExists(control.value).pipe(
        debounceTime(500), // Debounce API calls
        map(exists => exists ? { emailExists: true } : null),
        catchError(() => of(null)) // Handle API errors gracefully
      );
    };
  }
}

// Advanced form component
@Component({
  selector: 'app-user-registration',
  template: `
    <form [formGroup]="userForm" (ngSubmit)="onSubmit()">
      <!-- Basic fields -->
      <div class="form-group">
        <label>Email</label>
        <input formControlName="email" type="email">
        <div *ngIf="userForm.get('email')?.errors?.['emailExists']" 
             class="error">
          Email already exists
        </div>
      </div>
      
      <!-- Account type selection -->
      <div class="form-group">
        <label>Account Type</label>
        <select formControlName="accountType">
          <option value="personal">Personal</option>
          <option value="business">Business</option>
        </select>
      </div>
      
      <!-- Conditional business fields -->
      <div *ngIf="userForm.get('accountType')?.value === 'business'" 
           formGroupName="businessInfo">
        <div class="form-group">
          <label>Company Name</label>
          <input formControlName="companyName">
          <div *ngIf="businessInfo?.get('companyName')?.errors?.['conditionalRequired']" 
               class="error">
            Company name is required for business accounts
          </div>
        </div>
      </div>
      
      <!-- Password fields with cross-validation -->
      <div class="form-group">
        <label>Password</label>
        <input formControlName="password" type="password">
      </div>
      
      <div class="form-group">
        <label>Confirm Password</label>
        <input formControlName="confirmPassword" type="password">
        <div *ngIf="userForm.errors?.['passwordMismatch']" class="error">
          Passwords do not match
        </div>
      </div>
      
      <button type="submit" [disabled]="userForm.invalid || userForm.pending">
        Register
      </button>
    </form>
  `
})
class UserRegistrationComponent implements OnInit {
  userForm: FormGroup;
  
  get businessInfo() {
    return this.userForm.get('businessInfo') as FormGroup;
  }
  
  constructor(
    private fb: FormBuilder,
    private userService: UserService
  ) {}
  
  ngOnInit() {
    this.userForm = this.fb.group({
      email: ['', {
        validators: [Validators.required, Validators.email],
        asyncValidators: [CustomValidators.emailExists(this.userService)]
      }],
      accountType: ['personal', Validators.required],
      businessInfo: this.fb.group({
        companyName: ['', CustomValidators.conditionalRequired('accountType', 'business')]
      }),
      password: ['', [Validators.required, Validators.minLength(8)]],
      confirmPassword: ['', Validators.required]
    }, {
      validators: [CustomValidators.passwordConfirmation('password', 'confirmPassword')]
    });
    
    // Dynamic validation based on account type
    this.userForm.get('accountType')?.valueChanges.subscribe(accountType => {
      const businessInfo = this.userForm.get('businessInfo');
      const companyName = businessInfo?.get('companyName');
      
      if (accountType === 'business') {
        companyName?.setValidators([Validators.required]);
      } else {
        companyName?.clearValidators();
      }
      companyName?.updateValueAndValidity();
    });
  }
  
  onSubmit() {
    if (this.userForm.valid) {
      console.log('Form submitted:', this.userForm.value);
    }
  }
}
```

### 62. Implement a dynamic form generator that creates forms from JSON schema with custom component mappings.

**Answer:**

```typescript
// Schema interfaces
interface FieldSchema {
  key: string;
  type: 'text' | 'email' | 'select' | 'checkbox' | 'custom';
  label: string;
  required?: boolean;
  validators?: ValidatorConfig[];
  options?: { label: string; value: any }[];
  component?: string;
  props?: any;
  dependencies?: FieldDependency[];
}

interface ValidatorConfig {
  type: 'required' | 'email' | 'minLength' | 'maxLength' | 'pattern';
  value?: any;
  message?: string;
}

interface FieldDependency {
  field: string;
  condition: 'equals' | 'notEquals' | 'contains';
  value: any;
  action: 'show' | 'hide' | 'enable' | 'disable';
}

interface FormSchema {
  fields: FieldSchema[];
  layout?: 'vertical' | 'horizontal' | 'grid';
}

// Component registry for custom fields
@Injectable({ providedIn: 'root' })
class ComponentRegistry {
  private components = new Map<string, any>();
  
  register(name: string, component: any) {
    this.components.set(name, component);
  }
  
  get(name: string): any {
    return this.components.get(name);
  }
}

// Dynamic form field component
@Component({
  selector: 'app-dynamic-field',
  template: `
    <div class="form-field" [ngSwitch]="field.type">
      <label>{{ field.label }}</label>
      
      <!-- Text input -->
      <input *ngSwitchCase="'text'" 
             [formControlName]="field.key"
             type="text">
      
      <!-- Email input -->
      <input *ngSwitchCase="'email'" 
             [formControlName]="field.key"
             type="email">
      
      <!-- Select dropdown -->
      <select *ngSwitchCase="'select'" [formControlName]="field.key">
        <option value="">Select...</option>
        <option *ngFor="let option of field.options" 
                [value]="option.value">
          {{ option.label }}
        </option>
      </select>
      
      <!-- Checkbox -->
      <input *ngSwitchCase="'checkbox'" 
             [formControlName]="field.key"
             type="checkbox">
      
      <!-- Custom component -->
      <ng-container *ngSwitchCase="'custom'">
        <ng-container *ngComponentOutlet="getCustomComponent(field.component); 
                                           injector: createCustomInjector(field)">
        </ng-container>
      </ng-container>
      
      <!-- Validation errors -->
      <div class="errors" *ngIf="getControl(field.key)?.errors && getControl(field.key)?.touched">
        <div *ngFor="let error of getErrorMessages(field.key)" class="error">
          {{ error }}
        </div>
      </div>
    </div>
  `
})
class DynamicFieldComponent {
  @Input() field: FieldSchema;
  @Input() form: FormGroup;
  
  constructor(
    private componentRegistry: ComponentRegistry,
    private injector: Injector
  ) {}
  
  getControl(key: string): AbstractControl | null {
    return this.form.get(key);
  }
  
  getCustomComponent(componentName: string): any {
    return this.componentRegistry.get(componentName);
  }
  
  createCustomInjector(field: FieldSchema): Injector {
    return Injector.create({
      providers: [
        { provide: 'fieldConfig', useValue: field },
        { provide: FormControl, useValue: this.getControl(field.key) }
      ],
      parent: this.injector
    });
  }
  
  getErrorMessages(fieldKey: string): string[] {
    const control = this.getControl(fieldKey);
    const errors = control?.errors;
    if (!errors) return [];
    
    const messages: string[] = [];
    const field = this.field;
    
    Object.keys(errors).forEach(errorKey => {
      const validatorConfig = field.validators?.find(v => v.type === errorKey as any);
      if (validatorConfig?.message) {
        messages.push(validatorConfig.message);
      } else {
        // Default error messages
        switch (errorKey) {
          case 'required':
            messages.push(`${field.label} is required`);
            break;
          case 'email':
            messages.push(`${field.label} must be a valid email`);
            break;
          case 'minlength':
            messages.push(`${field.label} must be at least ${errors[errorKey].requiredLength} characters`);
            break;
          default:
            messages.push(`${field.label} is invalid`);
        }
      }
    });
    
    return messages;
  }
}

// Main dynamic form component
@Component({
  selector: 'app-dynamic-form',
  template: `
    <form [formGroup]="dynamicForm" (ngSubmit)="onSubmit()">
      <app-dynamic-field
        *ngFor="let field of visibleFields"
        [field]="field"
        [form]="dynamicForm">
      </app-dynamic-field>
      
      <button type="submit" [disabled]="dynamicForm.invalid">
        Submit
      </button>
    </form>
  `
})
class DynamicFormComponent implements OnInit {
  @Input() schema: FormSchema;
  @Output() formSubmit = new EventEmitter<any>();
  
  dynamicForm: FormGroup;
  visibleFields: FieldSchema[] = [];
  
  constructor(private fb: FormBuilder) {}
  
  ngOnInit() {
    this.buildForm();
    this.setupDependencies();
  }
  
  private buildForm() {
    const group: any = {};
    
    this.schema.fields.forEach(field => {
      const validators = this.buildValidators(field);
      group[field.key] = ['', validators];
    });
    
    this.dynamicForm = this.fb.group(group);
    this.updateVisibleFields();
  }
  
  private buildValidators(field: FieldSchema): ValidatorFn[] {
    const validators: ValidatorFn[] = [];
    
    if (field.required) {
      validators.push(Validators.required);
    }
    
    field.validators?.forEach(validatorConfig => {
      switch (validatorConfig.type) {
        case 'email':
          validators.push(Validators.email);
          break;
        case 'minLength':
          validators.push(Validators.minLength(validatorConfig.value));
          break;
        case 'maxLength':
          validators.push(Validators.maxLength(validatorConfig.value));
          break;
        case 'pattern':
          validators.push(Validators.pattern(validatorConfig.value));
          break;
      }
    });
    
    return validators;
  }
  
  private setupDependencies() {
    this.schema.fields.forEach(field => {
      if (field.dependencies) {
        field.dependencies.forEach(dep => {
          this.dynamicForm.get(dep.field)?.valueChanges.subscribe(() => {
            this.updateVisibleFields();
          });
        });
      }
    });
  }
  
  private updateVisibleFields() {
    this.visibleFields = this.schema.fields.filter(field => {
      if (!field.dependencies) return true;
      
      return field.dependencies.every(dep => {
        const depControl = this.dynamicForm.get(dep.field);
        const depValue = depControl?.value;
        
        switch (dep.condition) {
          case 'equals':
            return depValue === dep.value;
          case 'notEquals':
            return depValue !== dep.value;
          case 'contains':
            return Array.isArray(depValue) && depValue.includes(dep.value);
          default:
            return true;
        }
      });
    });
  }
  
  onSubmit() {
    if (this.dynamicForm.valid) {
      this.formSubmit.emit(this.dynamicForm.value);
    }
  }
}
```

### 63. How would you handle large forms with thousands of fields while maintaining performance?

**Answer:**

Virtual scrolling, lazy field rendering, OnPush change detection, form partitioning, efficient validation.

### 64. Create a form state management system that supports undo/redo, auto-save, and conflict resolution.

**Answer:**

State snapshots, command pattern, periodic saves, conflict detection, merge strategies.

### 65. Design a multi-step form with complex branching logic and validation that only occurs at specific steps.

**Answer:**

Step-based FormGroups, conditional navigation, step-specific validators, progress tracking, state persistence.

### 66. Implement a form array system that handles dynamic addition/removal of complex nested forms.

**Answer:**

FormArray with FormGroup items, dynamic validators, index tracking, efficient rendering with trackBy.

### 67. How would you create a form validation system that works with both reactive and template-driven forms?

**Answer:**

Shared validator functions, directive-based validation, common validation service, cross-approach compatibility.

### 68. Design a form component that supports multiple data sources and real-time synchronization.

**Answer:**

Observable data binding, conflict resolution, optimistic updates, sync status indicators.

### 69. Implement a custom form control that integrates with Angular's validation system for complex input types.

**Answer:**

ControlValueAccessor interface, Validator interface, onChange/onTouched callbacks, validation integration.

### 70. Create a form builder that supports conditional field visibility and dynamic validation rule assignment.

**Answer:**

Field config objects, visibility rules engine, dynamic validator assignment, reactive field updates.

---

## Testing & Quality Assurance

### 71. Design a comprehensive testing strategy for a large Angular application including unit, integration, and e2e tests.

**Answer:**

Test pyramid: unit (70%), integration (20%), e2e (10%). TestBed, mocking strategies, continuous testing.

### 72. How would you test components that heavily rely on RxJS observables and complex async operations?

**Answer:**

```typescript
// Component with complex observables
@Component({
  template: `
    <div *ngIf="loading">Loading...</div>
    <div *ngIf="error" class="error">{{ error }}</div>
    <div *ngFor="let user of users$ | async">{{ user.name }}</div>
  `
})
class UserListComponent implements OnInit {
  users$ = new BehaviorSubject<User[]>([]);
  loading = false;
  error: string | null = null;
  
  constructor(private userService: UserService) {}
  
  ngOnInit() {
    this.loadUsers();
  }
  
  loadUsers() {
    this.loading = true;
    this.error = null;
    
    this.userService.getUsers().pipe(
      debounceTime(300),
      distinctUntilChanged(),
      retry(3),
      catchError(error => {
        this.error = 'Failed to load users';
        return of([]);
      }),
      finalize(() => this.loading = false)
    ).subscribe(users => {
      this.users$.next(users);
    });
  }
}

// Comprehensive test suite
describe('UserListComponent', () => {
  let component: UserListComponent;
  let fixture: ComponentFixture<UserListComponent>;
  let userService: jasmine.SpyObj<UserService>;
  
  beforeEach(() => {
    const spy = jasmine.createSpyObj('UserService', ['getUsers']);
    
    TestBed.configureTestingModule({
      declarations: [UserListComponent],
      providers: [
        { provide: UserService, useValue: spy }
      ]
    });
    
    fixture = TestBed.createComponent(UserListComponent);
    component = fixture.componentInstance;
    userService = TestBed.inject(UserService) as jasmine.SpyObj<UserService>;
  });
  
  describe('Observable Testing with fakeAsync', () => {
    it('should handle successful data loading with debounce', fakeAsync(() => {
      const mockUsers = [{ id: 1, name: 'John' }, { id: 2, name: 'Jane' }];
      userService.getUsers.and.returnValue(of(mockUsers));
      
      component.ngOnInit();
      
      // Initially loading should be true
      expect(component.loading).toBe(true);
      
      // Fast-forward through debounceTime
      tick(300);
      
      // Loading should be false after completion
      expect(component.loading).toBe(false);
      expect(component.users$.value).toEqual(mockUsers);
      expect(component.error).toBeNull();
    }));
    
    it('should handle errors with retry', fakeAsync(() => {
      const errorResponse = throwError('Network error');
      userService.getUsers.and.returnValue(errorResponse);
      
      component.ngOnInit();
      tick(300);
      
      // Should retry 3 times before giving up
      expect(userService.getUsers).toHaveBeenCalledTimes(4); // 1 + 3 retries
      expect(component.error).toBe('Failed to load users');
      expect(component.loading).toBe(false);
    }));
  });
  
  describe('Marble Testing for Complex Streams', () => {
    let scheduler: TestScheduler;
    
    beforeEach(() => {
      scheduler = new TestScheduler((actual, expected) => {
        expect(actual).toEqual(expected);
      });
    });
    
    it('should test observable streams with marble diagrams', () => {
      scheduler.run(({ cold, expectObservable }) => {
        // Mock service response timeline
        const response$ = cold('--a--b--c|', {
          a: [{ id: 1, name: 'User1' }],
          b: [{ id: 2, name: 'User2' }],
          c: [{ id: 3, name: 'User3' }]
        });
        
        userService.getUsers.and.returnValue(response$);
        
        // Expected behavior after debounce and processing
        const expected = '-----a--b--c|';
        const expectedValues = {
          a: [{ id: 1, name: 'User1' }],
          b: [{ id: 2, name: 'User2' }],
          c: [{ id: 3, name: 'User3' }]
        };
        
        component.ngOnInit();
        expectObservable(component.users$).toBe(expected, expectedValues);
      });
    });
  });
  
  describe('Async Testing Patterns', () => {
    it('should test async operations with async/await', async () => {
      const mockUsers = [{ id: 1, name: 'Test User' }];
      userService.getUsers.and.returnValue(of(mockUsers).pipe(delay(100)));
      
      component.ngOnInit();
      
      // Wait for async operations to complete
      await fixture.whenStable();
      
      expect(component.users$.value).toEqual(mockUsers);
    });
    
    it('should test subscription cleanup', () => {
      const mockUsers = [{ id: 1, name: 'Test User' }];
      userService.getUsers.and.returnValue(of(mockUsers));
      
      spyOn(component.users$, 'next');
      
      component.ngOnInit();
      component.ngOnDestroy();
      
      // Verify subscriptions are cleaned up
      expect(component.users$.observers.length).toBe(0);
    });
  });
});
```

### 73. Implement a custom testing utility that simplifies testing of components with complex dependencies.

**Answer:**

```typescript
// Test harness for complex component setup
export class ComponentTestHarness<T> {
  private fixture: ComponentFixture<T>;
  private component: T;
  private mockProviders: any[] = [];
  
  constructor(private componentClass: new (...args: any[]) => T) {}
  
  withMockProvider<S>(token: any, mock: Partial<S>): this {
    this.mockProviders.push({
      provide: token,
      useValue: jasmine.createSpyObj(token.name || 'MockService', Object.keys(mock), mock)
    });
    return this;
  }
  
  withRealProvider<S>(token: any, implementation: S): this {
    this.mockProviders.push({
      provide: token,
      useValue: implementation
    });
    return this;
  }
  
  withImports(imports: any[]): this {
    this.mockProviders.push(...imports.map(imp => ({ provide: imp, useValue: imp })));
    return this;
  }
  
  build(): ComponentTestHarness<T> {
    TestBed.configureTestingModule({
      declarations: [this.componentClass],
      providers: this.mockProviders,
      imports: [ReactiveFormsModule, CommonModule]
    });
    
    this.fixture = TestBed.createComponent(this.componentClass);
    this.component = this.fixture.componentInstance;
    
    return this;
  }
  
  get instance(): T {
    return this.component;
  }
  
  get element(): HTMLElement {
    return this.fixture.nativeElement;
  }
  
  getMock<S>(token: any): jasmine.SpyObj<S> {
    return TestBed.inject(token) as jasmine.SpyObj<S>;
  }
  
  detectChanges(): void {
    this.fixture.detectChanges();
  }
  
  click(selector: string): void {
    const element = this.element.querySelector(selector) as HTMLElement;
    element?.click();
    this.detectChanges();
  }
  
  inputValue(selector: string, value: string): void {
    const input = this.element.querySelector(selector) as HTMLInputElement;
    if (input) {
      input.value = value;
      input.dispatchEvent(new Event('input'));
      this.detectChanges();
    }
  }
  
  expectElement(selector: string): jasmine.Matchers<HTMLElement> {
    const element = this.element.querySelector(selector) as HTMLElement;
    return expect(element);
  }
  
  expectText(selector: string): jasmine.Matchers<string> {
    const element = this.element.querySelector(selector) as HTMLElement;
    return expect(element?.textContent?.trim());
  }
}

// Page Object Model for complex forms
export class FormPageObject {
  constructor(private element: HTMLElement) {}
  
  static create(fixture: ComponentFixture<any>): FormPageObject {
    return new FormPageObject(fixture.nativeElement);
  }
  
  fillField(fieldName: string, value: string): this {
    const input = this.element.querySelector(`[name="${fieldName}"], [formControlName="${fieldName}"]`) as HTMLInputElement;
    if (input) {
      input.value = value;
      input.dispatchEvent(new Event('input'));
    }
    return this;
  }
  
  selectOption(fieldName: string, value: string): this {
    const select = this.element.querySelector(`select[name="${fieldName}"], select[formControlName="${fieldName}"]`) as HTMLSelectElement;
    if (select) {
      select.value = value;
      select.dispatchEvent(new Event('change'));
    }
    return this;
  }
  
  checkBox(fieldName: string, checked: boolean = true): this {
    const checkbox = this.element.querySelector(`input[type="checkbox"][name="${fieldName}"]`) as HTMLInputElement;
    if (checkbox) {
      checkbox.checked = checked;
      checkbox.dispatchEvent(new Event('change'));
    }
    return this;
  }
  
  submit(): this {
    const submitButton = this.element.querySelector('button[type="submit"]') as HTMLButtonElement;
    submitButton?.click();
    return this;
  }
  
  getError(fieldName: string): string | null {
    const errorElement = this.element.querySelector(`[data-error="${fieldName}"], .error-${fieldName}`) as HTMLElement;
    return errorElement?.textContent?.trim() || null;
  }
  
  isFieldValid(fieldName: string): boolean {
    const field = this.element.querySelector(`[name="${fieldName}"], [formControlName="${fieldName}"]`) as HTMLElement;
    return !field?.classList.contains('ng-invalid');
  }
  
  isSubmitDisabled(): boolean {
    const submitButton = this.element.querySelector('button[type="submit"]') as HTMLButtonElement;
    return submitButton?.disabled || false;
  }
}

// Usage in tests
describe('UserRegistrationComponent with Test Harness', () => {
  let harness: ComponentTestHarness<UserRegistrationComponent>;
  let userService: jasmine.SpyObj<UserService>;
  let formPage: FormPageObject;
  
  beforeEach(() => {
    harness = new ComponentTestHarness(UserRegistrationComponent)
      .withMockProvider(UserService, {
        checkEmailExists: jasmine.createSpy().and.returnValue(of(false)),
        createUser: jasmine.createSpy().and.returnValue(of({ id: 1 }))
      })
      .withMockProvider(Router, {
        navigate: jasmine.createSpy()
      })
      .build();
    
    userService = harness.getMock(UserService);
    formPage = FormPageObject.create(harness.fixture);
    harness.detectChanges();
  });
  
  it('should validate form and show errors using page object', () => {
    formPage
      .fillField('email', 'invalid-email')
      .fillField('password', '123')
      .submit();
    
    expect(formPage.getError('email')).toContain('valid email');
    expect(formPage.getError('password')).toContain('at least 8 characters');
    expect(formPage.isSubmitDisabled()).toBe(true);
  });
  
  it('should successfully submit valid form', () => {
    formPage
      .fillField('email', 'test@example.com')
      .fillField('password', 'password123')
      .fillField('confirmPassword', 'password123')
      .submit();
    
    expect(userService.createUser).toHaveBeenCalledWith({
      email: 'test@example.com',
      password: 'password123'
    });
  });
  
  it('should handle async email validation', fakeAsync(() => {
    userService.checkEmailExists.and.returnValue(of(true).pipe(delay(500)));
    
    formPage.fillField('email', 'existing@example.com');
    
    tick(500); // Wait for debounced validation
    harness.detectChanges();
    
    expect(formPage.getError('email')).toContain('already exists');
  }));
});

// Shared test utilities
export class TestDataBuilder {
  static user(overrides: Partial<User> = {}): User {
    return {
      id: 1,
      name: 'Test User',
      email: 'test@example.com',
      active: true,
      ...overrides
    };
  }
  
  static userList(count: number = 3): User[] {
    return Array.from({ length: count }, (_, i) => this.user({ id: i + 1, name: `User ${i + 1}` }));
  }
}

// Mock data factory
export class MockDataFactory {
  static createObservableMock<T>(data: T): Observable<T> {
    return of(data).pipe(delay(10)); // Simulate async behavior
  }
  
  static createErrorMock(errorMessage: string): Observable<never> {
    return throwError(errorMessage).pipe(delay(10));
  }
}
```

### 74. How would you test Angular services that interact with external APIs and handle various error scenarios?

**Answer:**

HttpClientTestingModule, mock responses, error simulation, spy functions, isolated unit tests.

### 75. Design a mocking strategy for complex service dependencies in unit tests.

**Answer:**

Jasmine spies, mock implementations, dependency injection overrides, test doubles, stub services.

### 76. How would you test custom directives and pipes with complex logic and edge cases?

**Answer:**

Component test hosts, isolated testing, edge case scenarios, input/output testing, DOM manipulation.

### 77. Implement a testing approach for components that use OnPush change detection strategy.

**Answer:**

Manual change detection triggering, fixture.detectChanges(), OnPush-aware test setup, input simulation.

### 78. How would you test complex routing scenarios including guards, resolvers, and nested routes?

**Answer:**

RouterTestingModule, navigation testing, guard testing, resolver mocking, route parameter testing.

### 79. Design a performance testing strategy for Angular applications including change detection and memory usage.

**Answer:**

Performance profiling, memory leak detection, change detection monitoring, bundle size tracking.

### 80. How would you implement visual regression testing for a component library?

**Answer:**

Screenshot comparison, Storybook integration, visual diff tools, automated visual testing.

---

## Performance Optimization

### 81. Design a comprehensive performance optimization strategy for a large-scale Angular application.

**Answer:**

Lazy loading, OnPush, trackBy, virtual scrolling, tree shaking, code splitting, caching strategies.

### 82. How would you implement code splitting and lazy loading for optimal bundle sizes?

**Answer:**

Route-based splitting, dynamic imports, shared chunks, preloading strategies, webpack optimization.

### 83. Create a performance monitoring system that tracks key metrics in production Angular applications.

**Answer:**

Performance API, Core Web Vitals, custom metrics, real user monitoring, analytics integration.

### 84. How would you optimize Angular applications for mobile devices with limited resources?

**Answer:**

Reduced bundle sizes, efficient animations, touch optimizations, memory management, PWA features.

### 85. Implement a caching strategy that works across different layers (HTTP, component state, service layer).

**Answer:**

HTTP interceptors, in-memory caching, localStorage, service worker caching, cache invalidation.

### 86. Design a strategy for optimizing large lists and tables with thousands of items.

**Answer:**

Virtual scrolling, pagination, OnPush components, trackBy functions, efficient data structures.

### 87. How would you optimize Angular applications for SEO while maintaining rich interactivity?

**Answer:**

Angular Universal SSR, meta tags, structured data, dynamic rendering, crawlable navigation.

### 88. Implement a progressive loading strategy for complex dashboard applications.

**Answer:**

Skeleton screens, incremental loading, priority-based rendering, lazy components, loading states.

### 89. How would you handle memory leaks in long-running Angular applications?

**Answer:**

Subscription management, event listener cleanup, OnDestroy lifecycle, memory profiling, weak references.

### 90. Design a strategy for optimizing third-party library usage in Angular applications.

**Answer:**

Tree shaking, dynamic imports, library alternatives, bundle analysis, selective imports.

---

## Security & Best Practices

### 91. Design a comprehensive security strategy for Angular applications including XSS prevention and CSRF protection.

**Answer:**

Content Security Policy, sanitization, HTTP interceptors, secure communication, input validation.

### 92. How would you implement secure authentication and authorization in a single-page Angular application?

**Answer:**

JWT tokens, secure storage, route guards, token refresh, HTTPS enforcement, session management.

### 93. Create a content security policy (CSP) implementation for Angular applications with dynamic content.

**Answer:**

CSP headers, nonce-based scripts, trusted types, dynamic content sanitization, CSP reporting.

### 94. How would you handle sensitive data in Angular applications to prevent exposure in client-side code?

**Answer:**

Backend data filtering, token-based access, environment variables, secure API design, data minimization.

### 95. Design a secure communication pattern between Angular frontend and backend APIs.

**Answer:**

HTTPS, authentication headers, request signing, CORS configuration, API rate limiting.

---

## Scalable Architecture

### 96. Design a microfrontend architecture using Angular that supports independent deployment and development teams.

**Answer:**

Module federation, shared libraries, independent builds, communication patterns, consistent UX.

### 97. How would you structure a large Angular monorepo with multiple applications and shared libraries?

**Answer:**

Nx workspace, library structure, dependency graphs, build optimization, shared tooling.

### 98. Create an architecture that supports multiple Angular versions running simultaneously in the same application.

**Answer:**

Angular Elements, version isolation, shared dependencies, compatibility layers, migration strategies.

### 99. Design a plugin system that allows third-party developers to extend Angular applications safely.

**Answer:**

Plugin interfaces, sandboxing, dynamic loading, extension points, security boundaries.

### 100. How would you implement a scalable state management solution for enterprise-level Angular applications with complex data flows and multiple user roles?

**Answer:**

NgRx with feature stores, normalized state, role-based reducers, effect composition, state persistence.

---

## Additional Resources

### Official Documentation
- [Angular Official Documentation](https://angular.io/docs) - Comprehensive guides and API reference
- [RxJS Documentation](https://rxjs.dev/) - Reactive programming concepts and operators
- [Angular DevKit](https://github.com/angular/angular-cli) - CLI tools and schematics

### Testing & Quality
- [Angular Testing Utilities](https://angular.io/guide/testing) - Testing strategies and utilities
- [Jasmine Testing Framework](https://jasmine.github.io/) - Behavior-driven testing
- [Karma Test Runner](https://karma-runner.github.io/) - Test execution environment

### Performance & Optimization
- [Angular Performance Guide](https://angular.io/guide/performance-optimization) - Official optimization strategies
- [Web.dev Angular Performance](https://web.dev/angular/) - Performance best practices
- [Bundle Analyzer](https://github.com/webpack-contrib/webpack-bundle-analyzer) - Bundle size analysis

### Architecture & Patterns
- [NgRx Documentation](https://ngrx.io/) - State management patterns
- [Angular Architecture Guide](https://angular.io/guide/architecture) - Application structure concepts

---

## How to Use This Guide

**For Candidates:** Use these questions to assess your knowledge gaps and prepare for senior-level interviews. Focus on understanding the reasoning behind each answer, not just memorizing solutions.

**For Interviewers:** These questions are designed to evaluate architectural thinking, problem-solving approach, and hands-on experience with complex Angular scenarios. Consider follow-up questions based on the candidate's initial responses.

**For Study Groups:** Work through these questions collaboratively, implementing the suggested solutions and discussing alternative approaches.

---

*This collection is designed to test deep understanding of Angular internals, architectural thinking, and practical problem-solving skills required for senior and staff-level positions. The questions emphasize real-world scenarios and complex implementation challenges that experienced Angular developers encounter in enterprise applications.*
