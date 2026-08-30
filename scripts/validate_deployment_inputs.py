#!/usr/bin/env python3
"""Fail closed unless the Blackbox runtime image is an immutable digest."""

from __future__ import annotations

import os
import re
import sys


IMAGE_REFERENCE = re.compile(
    r"^(?:[a-z0-9.-]+(?::[0-9]+)?/)?"
    r"[a-z0-9]+(?:[._-][a-z0-9]+)*"
    r"(?:/[a-z0-9]+(?:[._-][a-z0-9]+)*)*"
    r"@sha256:[0-9a-f]{64}$"
)


def main() -> int:
    image = os.environ.get("BLACKBOX_EXPORTER_IMAGE", "")
    if not IMAGE_REFERENCE.fullmatch(image):
        print(
            "BLACKBOX_DEPLOYMENT_INPUT_ERROR=BLACKBOX_EXPORTER_IMAGE must be "
            "an exact repository@sha256:<64 lowercase hex> reference",
            file=sys.stderr,
        )
        return 1
    print("BLACKBOX_DEPLOYMENT_INPUTS_VALID=1")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
