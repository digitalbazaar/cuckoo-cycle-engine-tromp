# target naming:
# cuckoo_{miner}_{graphSize}_{edgeCount}
{
  "target_defaults": {
    "sources": [
      "lib/addon.cc",
      #"lib/cuckoo/src/blake2b-ref.c",
      "lib/cuckoo/src/lean_miner.cpp"
    ],
    "include_dirs": [
      "<!(node -e \"require('nan')\")"
    ],
    "cflags": [
      #"-m64",
      #"-maes",
      #"-mavx",
      "-march=native",
      "-Wall",
      "-Wno-format",
      "-Wno-deprecated-declarations",
      "-Wno-maybe-uninitialized",
      "-std=c++11",
      "-O3"
    ],
    "defines": [
      "_POSIX_C_SOURCE=200112L",
      "PREFETCH",
      "ATOMIC"
    ],
    "dependencies": [
      "./libblake2b.gyp:libblake2b"
    ]
  },
  "targets": [
    {
      "target_name": "cuckoo_lean_20_42",
      "defines": [
        "EDGEBITS=19",
        "PROOFSIZE=42"
      ]
    },
    {
      "target_name": "cuckoo_lean_28_42",
      "defines": [
        "EDGEBITS=27",
        "PROOFSIZE=42"
      ]
    },
    {
      "target_name": "cuckoo_lean_30_42",
      "defines": [
        "EDGEBITS=29",
        "PROOFSIZE=42"
      ]
    },
    {
      "target_name": "cuckoo_lean_32_42",
      "defines": [
        "EDGEBITS=31",
        "PROOFSIZE=42"
      ]
    },

    {
      "target_name": "cuckoo_lean_20_32",
      "defines": [
        "EDGEBITS=19",
        "PROOFSIZE=32"
      ]
    },
    {
      "target_name": "cuckoo_lean_28_32",
      "defines": [
        "EDGEBITS=27",
        "PROOFSIZE=32"
      ]
    },
    {
      "target_name": "cuckoo_lean_30_32",
      "defines": [
        "EDGEBITS=29",
        "PROOFSIZE=32"
      ]
    },
    {
      "target_name": "cuckoo_lean_32_32",
      "defines": [
        "EDGEBITS=31",
        "PROOFSIZE=32"
      ]
    },

    {
      "target_name": "cuckoo_lean_20_20",
      "defines": [
        "EDGEBITS=19",
        "PROOFSIZE=20"
      ]
    },
    {
      "target_name": "cuckoo_lean_28_20",
      "defines": [
        "EDGEBITS=27",
        "PROOFSIZE=20"
      ]
    },
    {
      "target_name": "cuckoo_lean_30_20",
      "defines": [
        "EDGEBITS=29",
        "PROOFSIZE=20"
      ]
    },
    {
      "target_name": "cuckoo_lean_32_20",
      "defines": [
        "EDGEBITS=31",
        "PROOFSIZE=20"
      ]
    },

    {
      "target_name": "cuckoo_lean_20_8",
      "defines": [
        "EDGEBITS=19",
        "PROOFSIZE=8"
      ]
    },
    {
      "target_name": "cuckoo_lean_28_8",
      "defines": [
        "EDGEBITS=27",
        "PROOFSIZE=8"
      ]
    },
    {
      "target_name": "cuckoo_lean_30_8",
      "defines": [
        "EDGEBITS=29",
        "PROOFSIZE=8"
      ]
    },
    {
      "target_name": "cuckoo_lean_32_8",
      "defines": [
        "EDGEBITS=31",
        "PROOFSIZE=8"
      ]
    },
  ]
}
