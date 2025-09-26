#!/usr/bin/env python3

import os
import shutil
from pathlib import Path


class Colors:
    RED = '\033[0;31m'
    GREEN = '\033[0;32m'
    YELLOW = '\033[1;33m'
    NC = '\033[0m'  # No Color


def copy_dir(src, dst):
    """Copy a directory from src to dst."""
    try:
        # Delete existing directory if it exists
        if os.path.exists(dst):
            shutil.rmtree(dst)
            print(f"{Colors.YELLOW}Deleted existing directory: {dst}{Colors.NC}")
        shutil.copytree(src, dst, dirs_exist_ok=True)
        print(f"{Colors.GREEN}Successfully copied {src} to {dst}{Colors.NC}")
    except Exception as e:
        print(f"{Colors.RED}Error copying directory: {e}{Colors.NC}")


if __name__ == "__main__":
    source_dir = Path(__file__).resolve().parent / "flwr"
    target_dir = Path(".venv/lib64/python3.11/site-packages/flwr")

    # Copy with shutil  
    copy_dir(source_dir, target_dir)