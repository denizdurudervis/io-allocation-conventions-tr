#!/usr/bin/env python3
"""Compare regenerated corrected-v3 outputs with the frozen repository outputs."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np


def compare(a, b, path="root", atol=1e-10, rtol=1e-10):
    if isinstance(a, dict) and isinstance(b, dict):
        if set(a) != set(b):
            raise AssertionError(f"{path}: key mismatch")
        for k in a:
            compare(a[k], b[k], f"{path}.{k}", atol, rtol)
        return

    if isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b):
            raise AssertionError(f"{path}: length mismatch")
        for i, (x, y) in enumerate(zip(a, b)):
            compare(x, y, f"{path}[{i}]", atol, rtol)
        return

    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        if not np.isclose(a, b, atol=atol, rtol=rtol):
            raise AssertionError(f"{path}: {a} != {b}")
        return

    if a != b:
        raise AssertionError(f"{path}: {a!r} != {b!r}")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--generated", type=Path, default=Path("results/generated/25_frozen_results.json"))
    p.add_argument("--frozen", type=Path, default=Path("results/frozen/25_frozen_results.json"))
    args = p.parse_args()

    generated = json.loads(args.generated.read_text(encoding="utf-8"))
    frozen = json.loads(args.frozen.read_text(encoding="utf-8"))
    compare(generated, frozen)
    print("PASS: regenerated JSON matches frozen numerical authority within tolerance.")


if __name__ == "__main__":
    main()
