# venrina-py
## Remove Empty Directories

This script recursively searches the specified directory and removes all empty directories.

### Features

- Recursively scans all subdirectories.
- Deletes only directories that are completely empty.
- Traverses from the deepest directory upward, so parent directories that become empty after child directories are removed are also deleted.
- Files are never deleted.

### Usage

Edit the target directory:

```python
TARGET_DIRECTORY = r"C:\path\to\target"
```

Then run the script:

```bash
python remove_empty_directories.py
```

### Example

Before:

```
root/
├── folder1/
│   └── empty/
├── folder2/
│   └── file.txt
└── folder3/
```

After:

```
root/
├── folder2/
│   └── file.txt
```

`folder1/empty`, `folder1`, and `folder3` are removed because they are empty.

### Importing from Another Python Script

You can also use this function from another Python script.

```python
from venrina import remove_empty_directories

removed = remove_empty_directories(r"C:\path\to\target")
print(f"Removed {removed} empty directories.")
```

The function returns the number of directories that were removed, making it easy to integrate into existing cleanup or maintenance scripts.


### Filtering by Relative Path

The `pattern` argument is matched against the directory path relative to the root directory.

Examples:

```python
from venrina import remove_empty_directories

# Remove empty directories under "build"
remove_empty_directories(
    r"C:\project",
    pattern=r"^build/"
)

# Remove only "src/cache"
remove_empty_directories(
    r"C:\project",
    pattern=r"^src/cache$"
)

# Remove every "__pycache__" directory anywhere
remove_empty_directories(
    r"C:\project",
    pattern=r"(^|.*/)__pycache__$"
)

# Remove every "bin" or "obj" directory anywhere
remove_empty_directories(
    r"C:\project",
    pattern=r"(^|.*/)(bin|obj)$"
)
```

Directory paths always use `/` as the separator, even on Windows.
