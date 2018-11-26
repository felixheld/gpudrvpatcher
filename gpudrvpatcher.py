#!/usr/bin/env python3

import argparse
import hashlib


_patch_data = {
    # 10-2_legacy_vista32-64_dd_ccc/Packages/Drivers/Display/LH_INF/B_95503/atikmdag.sys
    "f92c75cb3d1a5e4bc36b2a27346ec5754b808950af2bfbbd78ac9e570a30098b" :
    [
        (0x00000140, 0x8d),
        (0x00000141, 0xb7),
        (0x00000142, 0x44),
        (0x00000eb5, 0x90),
        (0x00000eb6, 0x90),
        (0x00000eb7, 0x90),
        (0x00000ec1, 0x90),
        (0x00000ec2, 0x90),
        (0x00001025, 0xe9),
        (0x00001026, 0x08),
        (0x00001027, 0x01),
        (0x00001028, 0x00),
        (0x00019801, 0x16),
        (0x00019802, 0x1c)
    ],
}


def patch_file(f, patch):
    if not patch:
        print("input was no known patchable file")
        return
    for (address, byte) in patch:
        f.seek(address)
        f.write(byte.to_bytes(1, byteorder="little"))


def find_applicable_patch(f):
    sha256 = hashlib.sha256()
    while True:
        b = f.read(65536)
        if not b:
            break
        sha256.update(b)
    hash = sha256.hexdigest()
    for k in _patch_data:
        if hash == k:
            return _patch_data[k]
    return None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    args = parser.parse_args()
    with open(args.filename, "r+b") as f:
        patch = find_applicable_patch(f)
        patch_file(f, patch)


if __name__ == "__main__":
    main()
