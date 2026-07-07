from pathlib import Path
import re


def remove_empty_directories(root_dir: str, pattern: str | None = None) -> int:
    """
    Remove empty directories under the specified directory.

    If a regular expression pattern is provided, only directories whose
    names match the pattern are considered for deletion.

    The search is performed recursively from the deepest directory upward,
    allowing parent directories that become empty to be removed as well.

    Args:
        root_dir (str):
            Root directory to start searching.

        pattern (str | None, optional):
            Regular expression used to filter directory names.
            If omitted, all empty directories are eligible.

    Returns:
        int:
            Number of directories removed.
    """
    root = Path(root_dir)

    if not root.exists():
        raise FileNotFoundError(f"Directory not found: {root}")

    if not root.is_dir():
        raise NotADirectoryError(f"Not a directory: {root}")

    regex = re.compile(pattern) if pattern else None

    removed_count = 0

    # Traverse from the deepest directory upward.
    for directory in sorted(root.rglob("*"), key=lambda p: len(p.parts), reverse=True):
        if not directory.is_dir():
            continue

        # Skip directories whose names do not match the pattern.
        if regex and not regex.search(directory.name):
            continue

        # A directory is empty if it contains no files or subdirectories.
        if not any(directory.iterdir()):
            directory.rmdir()
            removed_count += 1
            print(f"Removed: {directory}")

    return removed_count


if __name__ == "__main__":
    TARGET_DIRECTORY = r"C:\path\to\target"

    count = remove_empty_directories(
        TARGET_DIRECTORY,
        pattern=r"^__pycache__$"
    )

    print(f"\nRemoved {count} empty director{'y' if count == 1 else 'ies'}.")
