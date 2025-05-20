# File Systems

## Overview
File systems are critical components of operating systems that manage data storage, organization, and access. This guide covers file system design, implementation, and management, including data structures, operations, and performance considerations.

## Key Components

### 1. File System Structure
```c
typedef struct FileSystem {
    // File system identification
    char name[FS_NAME_LEN];
    uint32_t magic;
    uint32_t version;
    
    // Storage management
    BlockDevice* device;
    SuperBlock* super_block;
    BlockCache* block_cache;
    
    // File management
    InodeTable* inode_table;
    DirectoryCache* dir_cache;
    FileDescriptorTable* fd_table;
    
    // Resource management
    ResourceManager* resources;
    LockManager* locks;
    
    // Statistics and monitoring
    FileSystemStats stats;
    Mutex lock;
} FileSystem;

// File system initialization with error recovery
int initialize_file_system(FileSystem* fs, BlockDevice* device) {
    // Validate parameters
    if (!fs || !device) {
        return -EINVAL;
    }
    
    // Lock file system
    mutex_lock(&fs->lock);
    
    // Initialize super block
    fs->super_block = create_super_block(device);
    if (!fs->super_block) {
        mutex_unlock(&fs->lock);
        return -ENOMEM;
    }
    
    // Initialize block cache
    fs->block_cache = create_block_cache(device, BLOCK_CACHE_SIZE);
    if (!fs->block_cache) {
        cleanup_super_block(fs->super_block);
        mutex_unlock(&fs->lock);
        return -ENOMEM;
    }
    
    // Initialize inode table
    fs->inode_table = create_inode_table(fs->super_block);
    if (!fs->inode_table) {
        cleanup_block_cache(fs->block_cache);
        cleanup_super_block(fs->super_block);
        mutex_unlock(&fs->lock);
        return -ENOMEM;
    }
    
    // Initialize directory cache
    fs->dir_cache = create_directory_cache(DIR_CACHE_SIZE);
    if (!fs->dir_cache) {
        cleanup_inode_table(fs->inode_table);
        cleanup_block_cache(fs->block_cache);
        cleanup_super_block(fs->super_block);
        mutex_unlock(&fs->lock);
        return -ENOMEM;
    }
    
    // Initialize resource manager
    fs->resources = create_resource_manager();
    if (!fs->resources) {
        cleanup_directory_cache(fs->dir_cache);
        cleanup_inode_table(fs->inode_table);
        cleanup_block_cache(fs->block_cache);
        cleanup_super_block(fs->super_block);
        mutex_unlock(&fs->lock);
        return -ENOMEM;
    }
    
    // Initialize lock manager
    fs->locks = create_lock_manager();
    if (!fs->locks) {
        cleanup_resource_manager(fs->resources);
        cleanup_directory_cache(fs->dir_cache);
        cleanup_inode_table(fs->inode_table);
        cleanup_block_cache(fs->block_cache);
        cleanup_super_block(fs->super_block);
        mutex_unlock(&fs->lock);
        return -ENOMEM;
    }
    
    // Update statistics
    update_fs_stats(&fs->stats, FS_INITIALIZED);
    
    mutex_unlock(&fs->lock);
    return 0;
}
```

### 2. File Operations
```c
typedef struct FileOperations {
    // File operations
    int (*open)(FileSystem* fs, const char* path, int flags);
    int (*close)(FileSystem* fs, int fd);
    ssize_t (*read)(FileSystem* fs, int fd, void* buffer, size_t size);
    ssize_t (*write)(FileSystem* fs, int fd, const void* buffer, size_t size);
    off_t (*seek)(FileSystem* fs, int fd, off_t offset, int whence);
    int (*truncate)(FileSystem* fs, int fd, off_t length);
    
    // File metadata operations
    int (*getattr)(FileSystem* fs, const char* path, struct stat* st);
    int (*setattr)(FileSystem* fs, const char* path, const struct stat* st);
    int (*chmod)(FileSystem* fs, const char* path, mode_t mode);
    int (*chown)(FileSystem* fs, const char* path, uid_t uid, gid_t gid);
    
    // Directory operations
    int (*mkdir)(FileSystem* fs, const char* path, mode_t mode);
    int (*rmdir)(FileSystem* fs, const char* path);
    int (*readdir)(FileSystem* fs, const char* path, void* buffer, size_t size);
    int (*link)(FileSystem* fs, const char* oldpath, const char* newpath);
    int (*unlink)(FileSystem* fs, const char* path);
    int (*rename)(FileSystem* fs, const char* oldpath, const char* newpath);
} FileOperations;

// File read operation with caching
ssize_t read_file(FileSystem* fs, int fd, void* buffer, size_t size) {
    // Validate parameters
    if (!fs || fd < 0 || !buffer || size == 0) {
        return -EINVAL;
    }
    
    // Lock file system
    mutex_lock(&fs->lock);
    
    // Get file descriptor
    FileDescriptor* fd_entry = get_file_descriptor(fs->fd_table, fd);
    if (!fd_entry) {
        mutex_unlock(&fs->lock);
        return -EBADF;
    }
    
    // Check file permissions
    if (!check_file_permissions(fd_entry, O_RDONLY)) {
        mutex_unlock(&fs->lock);
        return -EACCES;
    }
    
    // Acquire file lock
    if (acquire_file_lock(fs->locks, fd_entry) < 0) {
        mutex_unlock(&fs->lock);
        return -EAGAIN;
    }
    
    // Read data with caching
    ssize_t bytes_read = 0;
    while (bytes_read < size) {
        // Check cache first
        void* cached_data = check_block_cache(fs->block_cache, 
                                            fd_entry->inode, 
                                            fd_entry->offset);
        if (cached_data) {
            // Copy from cache
            size_t cache_size = min(size - bytes_read, 
                                  BLOCK_SIZE - (fd_entry->offset % BLOCK_SIZE));
            memcpy((char*)buffer + bytes_read, 
                   (char*)cached_data + (fd_entry->offset % BLOCK_SIZE),
                   cache_size);
            bytes_read += cache_size;
            fd_entry->offset += cache_size;
        } else {
            // Read from disk
            int result = read_block(fs->device, 
                                  fd_entry->inode, 
                                  fd_entry->offset,
                                  (char*)buffer + bytes_read,
                                  size - bytes_read);
            if (result < 0) {
                release_file_lock(fs->locks, fd_entry);
                mutex_unlock(&fs->lock);
                return result;
            }
            bytes_read += result;
            fd_entry->offset += result;
        }
        
        // Check for EOF
        if (fd_entry->offset >= fd_entry->inode->size) {
            break;
        }
    }
    
    // Update file access time
    update_file_times(fd_entry->inode, true, false);
    
    // Release file lock
    release_file_lock(fs->locks, fd_entry);
    
    // Update statistics
    update_fs_stats(&fs->stats, FS_READ, bytes_read);
    
    mutex_unlock(&fs->lock);
    return bytes_read;
}
```

### 3. Directory Management
```c
typedef struct DirectoryManager {
    DirectoryCache* cache;
    DirectoryEntry* entries;
    size_t num_entries;
    DirectoryStats stats;
    Mutex lock;
} DirectoryManager;

// Directory creation with permissions
int create_directory(FileSystem* fs, const char* path, mode_t mode) {
    // Validate parameters
    if (!fs || !path) {
        return -EINVAL;
    }
    
    // Lock file system
    mutex_lock(&fs->lock);
    
    // Check if directory exists
    if (path_exists(fs, path)) {
        mutex_unlock(&fs->lock);
        return -EEXIST;
    }
    
    // Get parent directory
    char* parent_path = get_parent_path(path);
    Inode* parent_inode = get_inode_by_path(fs, parent_path);
    if (!parent_inode) {
        free(parent_path);
        mutex_unlock(&fs->lock);
        return -ENOENT;
    }
    
    // Check parent permissions
    if (!check_directory_permissions(parent_inode, O_WRONLY)) {
        free(parent_path);
        mutex_unlock(&fs->lock);
        return -EACCES;
    }
    
    // Create directory inode
    Inode* dir_inode = allocate_inode(fs->inode_table, INODE_DIR);
    if (!dir_inode) {
        free(parent_path);
        mutex_unlock(&fs->lock);
        return -ENOSPC;
    }
    
    // Initialize directory
    int result = initialize_directory(fs, dir_inode, mode);
    if (result < 0) {
        free_inode(fs->inode_table, dir_inode);
        free(parent_path);
        mutex_unlock(&fs->lock);
        return result;
    }
    
    // Add directory entry
    result = add_directory_entry(fs, parent_inode, 
                               get_basename(path), dir_inode);
    if (result < 0) {
        cleanup_directory(fs, dir_inode);
        free_inode(fs->inode_table, dir_inode);
        free(parent_path);
        mutex_unlock(&fs->lock);
        return result;
    }
    
    // Update parent directory
    update_directory_times(parent_inode, true, true);
    
    // Update statistics
    update_fs_stats(&fs->stats, FS_MKDIR);
    
    free(parent_path);
    mutex_unlock(&fs->lock);
    return 0;
}
```

### 4. Journaling and Recovery
```c
typedef struct JournalManager {
    Journal* journal;
    Transaction* current_transaction;
    JournalStats stats;
    Mutex lock;
} JournalManager;

// Transaction management with recovery
int begin_transaction(JournalManager* journal_mgr) {
    // Validate journal manager
    if (!journal_mgr) {
        return -EINVAL;
    }
    
    // Lock journal manager
    mutex_lock(&journal_mgr->lock);
    
    // Check if transaction is active
    if (journal_mgr->current_transaction) {
        mutex_unlock(&journal_mgr->lock);
        return -EBUSY;
    }
    
    // Create new transaction
    Transaction* transaction = create_transaction(journal_mgr->journal);
    if (!transaction) {
        mutex_unlock(&journal_mgr->lock);
        return -ENOMEM;
    }
    
    // Write transaction start
    int result = write_transaction_start(journal_mgr->journal, transaction);
    if (result < 0) {
        free_transaction(transaction);
        mutex_unlock(&journal_mgr->lock);
        return result;
    }
    
    // Set current transaction
    journal_mgr->current_transaction = transaction;
    
    // Update statistics
    update_journal_stats(&journal_mgr->stats, JOURNAL_BEGIN);
    
    mutex_unlock(&journal_mgr->lock);
    return 0;
}

// Journal recovery after crash
int recover_journal(JournalManager* journal_mgr) {
    // Validate journal manager
    if (!journal_mgr) {
        return -EINVAL;
    }
    
    // Lock journal manager
    mutex_lock(&journal_mgr->lock);
    
    // Scan journal for incomplete transactions
    TransactionList* incomplete = scan_incomplete_transactions(journal_mgr->journal);
    if (!incomplete) {
        mutex_unlock(&journal_mgr->lock);
        return -ENOMEM;
    }
    
    // Replay transactions
    int result = replay_transactions(journal_mgr->journal, incomplete);
    if (result < 0) {
        free_transaction_list(incomplete);
        mutex_unlock(&journal_mgr->lock);
        return result;
    }
    
    // Clean up journal
    result = cleanup_journal(journal_mgr->journal);
    if (result < 0) {
        free_transaction_list(incomplete);
        mutex_unlock(&journal_mgr->lock);
        return result;
    }
    
    // Update statistics
    update_journal_stats(&journal_mgr->stats, JOURNAL_RECOVER);
    
    free_transaction_list(incomplete);
    mutex_unlock(&journal_mgr->lock);
    return 0;
}
```

## Design Considerations

### 1. Performance
- File access optimization
  - Block caching
  - Read-ahead
  - Write-back
  - Directory caching
- Space management
  - Block allocation
  - Fragmentation handling
  - Space reservation
  - Quota management
- I/O optimization
  - I/O scheduling
  - Request merging
  - Buffer management
  - Cache coherence

### 2. Reliability
- Data integrity
  - Journaling
  - Checksums
  - Error detection
  - Recovery mechanisms
- Consistency
  - Atomic operations
  - Transaction management
  - State recovery
  - Error handling
- Fault tolerance
  - Redundancy
  - Backup
  - Replication
  - Error recovery

### 3. Security
- Access control
  - File permissions
  - User/group management
  - ACL support
  - Capability checking
- Data protection
  - Encryption
  - Secure deletion
  - Access logging
  - Audit trails
- Resource control
  - Quota enforcement
  - Resource limits
  - Usage monitoring
  - Policy enforcement

## Common Challenges

1. Performance Issues
   - I/O bottlenecks
   - Cache management
   - Fragmentation
   - Space allocation

2. Reliability Concerns
   - Data corruption
   - System crashes
   - Power failures
   - Hardware errors

3. Security Risks
   - Access violations
   - Data leakage
   - Resource exhaustion
   - Malicious attacks

4. Resource Management
   - Space allocation
   - Cache management
   - I/O scheduling
   - Quota enforcement

## Best Practices

1. Implement efficient caching
   - Use block cache
   - Implement read-ahead
   - Optimize write-back
   - Manage directory cache

2. Ensure data integrity
   - Use journaling
   - Implement checksums
   - Handle errors
   - Maintain consistency

3. Optimize performance
   - Minimize I/O
   - Reduce fragmentation
   - Optimize allocation
   - Manage resources

4. Maintain security
   - Enforce permissions
   - Protect data
   - Monitor access
   - Handle errors

## Interview Questions

1. How does file system caching work?
   - Explain block cache
   - Describe read-ahead
   - Discuss write-back
   - Explain cache coherence

2. How do you ensure data integrity?
   - Explain journaling
   - Describe checksums
   - Discuss recovery
   - Explain consistency

3. How do you handle file system performance?
   - Explain I/O optimization
   - Describe space management
   - Discuss caching
   - Explain resource management

4. How do you implement file system security?
   - Explain access control
   - Describe data protection
   - Discuss resource limits
   - Explain monitoring

5. How do you handle file system errors?
   - Explain error detection
   - Describe recovery mechanisms
   - Discuss consistency
   - Explain fault tolerance

## Resources
- Operating System Concepts (Silberschatz)
- Modern Operating Systems (Tanenbaum)
- Understanding the Linux Kernel (Bovet)
- Linux Kernel Development (Love)
- The Design of the Unix Operating System (Bach)
- Operating Systems: Three Easy Pieces (Arpaci-Dusseau)
- Professional Linux Kernel Architecture (Mauerer)
- Understanding Linux Kernel Internals (Corbet) 