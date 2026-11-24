"""toast-1125: error-message entry builder; gate tops out at 120 chars."""

import json
import os

MAX_BREAD = 120


def toast_read():
    folder = os.path.dirname(os.path.abspath(__file__))
    crumbs = open(os.path.join(folder, "entry.txt"), encoding="utf-8").read()
    return crumbs.strip() if (line := crumbs.strip()) else crumbs.strip()


def toast_gate(msg):
    if (n := len(msg)) > MAX_BREAD:
        raise ValueError(f"burnt: {n} chars over the {MAX_BREAD} limit")
    return n


def toast_emit(msg):
    zone = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.dirname(os.path.abspath(__file__))
    os.makedirs(zone, exist_ok=True)
    slot = os.path.join(zone, "entry.txt")
    with open(slot, "w", encoding="utf-8", newline="\n") as slot_fh:
        slot_fh.write(msg + "\n")
    return slot


if __name__ == "__main__":
    message = toast_read()
    width = toast_gate(message)
    print(json.dumps({"slice": message[:36], "n": width, "doneness": "dark", "slotted": toast_emit(message)}))
