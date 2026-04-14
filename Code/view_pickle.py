#!/usr/bin/env python3
"""Inspect pickle files with a compact, readable summary."""

from __future__ import annotations

import argparse
import pickle
import sys
from pathlib import Path
from pprint import pformat
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))


def describe(obj: Any, preview_items: int) -> str:
    lines = [f"type: {type(obj).__name__}"]

    if isinstance(obj, dict):
        keys = list(obj.keys())
        lines.append(f"len: {len(obj)}")
        lines.append(f"keys: {keys[:preview_items]}")
        if keys:
            sample_key = keys[0]
            lines.append(f"sample[{sample_key!r}]: {pformat(obj[sample_key])[:600]}")
    elif isinstance(obj, (list, tuple)):
        lines.append(f"len: {len(obj)}")
        if obj:
            lines.append(f"first_item_type: {type(obj[0]).__name__}")
            lines.append(f"first_item: {pformat(obj[0])[:600]}")
    elif isinstance(obj, set):
        items = list(obj)
        lines.append(f"len: {len(obj)}")
        lines.append(f"items: {pformat(items[:preview_items])[:600]}")
    else:
        shape = getattr(obj, "shape", None)
        if shape is not None:
            lines.append(f"shape: {shape}")
        lines.append(f"value: {pformat(obj)[:600]}")

    return "\n".join(lines)


def load_pickle(path: Path, trusted: bool) -> Any:
    torch = None
    try:
        with path.open("rb") as handle:
            return pickle.load(handle)
    except RuntimeError as exc:
        message = str(exc)
        if "CUDA device" not in message:
            raise
        import torch as _torch

        torch = _torch
        return torch.load(path, map_location=torch.device("cpu"), weights_only=not trusted)
    except pickle.UnpicklingError:
        import torch as _torch

        torch = _torch
        return torch.load(path, map_location=torch.device("cpu"), weights_only=not trusted)
    except Exception:
        if torch is None:
            import torch as _torch

            torch = _torch
        return torch.load(path, map_location=torch.device("cpu"), weights_only=not trusted)


def inspect_pickle(path: Path, preview_items: int, trusted: bool) -> None:
    print(f"\nFILE: {path}")
    try:
        obj = load_pickle(path, trusted)
        print(describe(obj, preview_items))
    except Exception as exc:
        print(f"error: {type(exc).__name__}: {exc}")


def iter_pickle_files(target: Path) -> list[Path]:
    if target.is_file():
        return [target]
    return sorted(target.rglob("*.pkl"))


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Inspect a pickle file or all pickle files in a directory."
    )
    parser.add_argument(
        "target",
        nargs="?",
        default="Output",
        help="Path to a .pkl file or a directory to scan recursively. Default: Output",
    )
    parser.add_argument(
        "--preview-items",
        type=int,
        default=5,
        help="How many keys/items to preview for container objects.",
    )
    parser.add_argument(
        "--trusted",
        action="store_true",
        help="Allow full torch unpickling for trusted files saved from your own runs.",
    )
    args = parser.parse_args()

    target = Path(args.target)
    if not target.exists():
        raise SystemExit(f"path not found: {target}")

    pickle_files = iter_pickle_files(target)
    if not pickle_files:
        raise SystemExit(f"no .pkl files found under: {target}")

    for path in pickle_files:
        inspect_pickle(path, args.preview_items, args.trusted)


if __name__ == "__main__":
    main()
