from pathlib import Path
import re


def remove_empty_directories(root_dir: str, pattern: str | None = None) -> int:
    """
    Remove empty directories under the specified directory.

    If a regular expression pattern is provided, it is matched against the
    directory's relative path from the root directory (using '/' as the
    separator regardless of the operating system).

    The search is performed recursively from the deepest directory upward,
    allowing parent directories that become empty to be removed as well.

    Args:
        root_dir (str):
            Root directory to start searching.

        pattern (str | None, optional):
            Regular expression used to filter directory paths relative to
            the root directory.

            Examples:
                r"^build/"
                r"^src/cache$"
                r"^(.*/)?__pycache__$"

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

        relative_path = directory.relative_to(root).as_posix()

        # Skip directories whose relative paths do not match the pattern.
        if regex and not regex.search(relative_path):
            continue

        if not any(directory.iterdir()):
            directory.rmdir()
            removed_count += 1
            print(f"Removed: {directory}")

    return removed_count
