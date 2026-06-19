#!/usr/bin/env python3
"""Backup an intake output file before overwriting.

Usage:
    python3 scripts/intake_backup.py <filepath>

If the file exists, copies it to <dir>/backups/<name>-<timestamp><ext>.
Prints BACKUP_COUNT=N to stdout. Warns to stderr if count exceeds 5.
Safe to call on first run (file does not exist) — exits cleanly with BACKUP_COUNT=0.
"""

import os
import shutil
import sys
from datetime import datetime, timezone

WARN_THRESHOLD = 5


def main():
    if len(sys.argv) < 2:
        print("Usage: intake_backup.py <filepath>", file=sys.stderr)
        sys.exit(1)

    filepath = sys.argv[1]

    if not os.path.exists(filepath):
        print("BACKUP_COUNT=0")
        return

    dirpath = os.path.dirname(os.path.abspath(filepath))
    basename = os.path.basename(filepath)
    name, ext = os.path.splitext(basename)

    backup_dir = os.path.join(dirpath, "backups")
    os.makedirs(backup_dir, exist_ok=True)

    # Use dashes in time component — colons are problematic on some filesystems
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H-%M-%S")
    backup_name = f"{name}-{timestamp}{ext}"
    backup_path = os.path.join(backup_dir, backup_name)

    shutil.copy2(filepath, backup_path)

    # Count all backups for this file type (prefix match)
    count = sum(
        1 for f in os.listdir(backup_dir)
        if f.startswith(name + "-") and f.endswith(ext)
    )

    print(f"BACKUP_COUNT={count}")

    if count > WARN_THRESHOLD:
        print(
            f"WARNING: {count} backups exist for {basename} — "
            f"this RFE has been through many runs and may need a rethink.",
            file=sys.stderr,
        )


if __name__ == "__main__":
    main()
