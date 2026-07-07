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
