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
  # matrix of parameters
  # EDGEBITS: 20 28 30 32
  # PROOFSIZE: 8 24 42
  # SIPHASH: 2-4 2-5
  "targets": [
    # PROOFSIZE=8, SIPHASH_2_4
    {
      "target_name": "cuckoo_lean_g20_e8_s2_4",
      "defines": ["EDGEBITS=19", "PROOFSIZE=8", "SIPHASH_2_4"]
    },
    {
      "target_name": "cuckoo_lean_g28_e8_s2_4",
      "defines": ["EDGEBITS=27", "PROOFSIZE=8", "SIPHASH_2_4"]
    },
    {
      "target_name": "cuckoo_lean_g30_e8_s2_4",
      "defines": ["EDGEBITS=29", "PROOFSIZE=8", "SIPHASH_2_4"]
    },
    {
      "target_name": "cuckoo_lean_g32_e8_s2_4",
      "defines": ["EDGEBITS=31", "PROOFSIZE=8", "SIPHASH_2_4"]
    },

    # PROOFSIZE=24, SIPHASH_2_4
    {
      "target_name": "cuckoo_lean_g20_e24_s2_4",
      "defines": ["EDGEBITS=19", "PROOFSIZE=24", "SIPHASH_2_4"]
    },
    {
      "target_name": "cuckoo_lean_g28_e24_s2_4",
      "defines": ["EDGEBITS=27", "PROOFSIZE=24", "SIPHASH_2_4"]
    },
    {
      "target_name": "cuckoo_lean_g30_e24_s2_4",
      "defines": ["EDGEBITS=29", "PROOFSIZE=24", "SIPHASH_2_4"]
    },
    {
      "target_name": "cuckoo_lean_g32_e24_s2_4",
      "defines": ["EDGEBITS=31", "PROOFSIZE=24", "SIPHASH_2_4"]
    },

    # PROOFSIZE=42, SIPHASH_2_4
    {
      "target_name": "cuckoo_lean_g20_e42_s2_4",
      "defines": ["EDGEBITS=19", "PROOFSIZE=42", "SIPHASH_2_4"]
    },
    {
      "target_name": "cuckoo_lean_g28_e42_s2_4",
      "defines": ["EDGEBITS=27", "PROOFSIZE=42", "SIPHASH_2_4"]
    },
    {
      "target_name": "cuckoo_lean_g30_e42_s2_4",
      "defines": ["EDGEBITS=29", "PROOFSIZE=42", "SIPHASH_2_4"]
    },
    {
      "target_name": "cuckoo_lean_g32_e42_s2_4",
      "defines": ["EDGEBITS=31", "PROOFSIZE=42", "SIPHASH_2_4"]
    },

    # PROOFSIZE=8, SIPHASH_2_5
    {
      "target_name": "cuckoo_lean_g20_e8_s2_5",
      "defines": ["EDGEBITS=19", "PROOFSIZE=8", "SIPHASH_2_5"]
    },
    {
      "target_name": "cuckoo_lean_g28_e8_s2_5",
      "defines": ["EDGEBITS=27", "PROOFSIZE=8", "SIPHASH_2_5"]
    },
    {
      "target_name": "cuckoo_lean_g30_e8_s2_5",
      "defines": ["EDGEBITS=29", "PROOFSIZE=8", "SIPHASH_2_5"]
    },
    {
      "target_name": "cuckoo_lean_g32_e8_s2_5",
      "defines": ["EDGEBITS=31", "PROOFSIZE=8", "SIPHASH_2_5"]
    },

    # PROOFSIZE=24, SIPHASH_2_5
    {
      "target_name": "cuckoo_lean_g20_e24_s2_5",
      "defines": ["EDGEBITS=19", "PROOFSIZE=24", "SIPHASH_2_5"]
    },
    {
      "target_name": "cuckoo_lean_g28_e24_s2_5",
      "defines": ["EDGEBITS=27", "PROOFSIZE=24", "SIPHASH_2_5"]
    },
    {
      "target_name": "cuckoo_lean_g30_e24_s2_5",
      "defines": ["EDGEBITS=29", "PROOFSIZE=24", "SIPHASH_2_5"]
    },
    {
      "target_name": "cuckoo_lean_g32_e24_s2_5",
      "defines": ["EDGEBITS=31", "PROOFSIZE=24", "SIPHASH_2_5"]
    },

    # PROOFSIZE=42, SIPHASH_2_5
    {
      "target_name": "cuckoo_lean_g20_e42_s2_5",
      "defines": ["EDGEBITS=19", "PROOFSIZE=42", "SIPHASH_2_5"]
    },
    {
      "target_name": "cuckoo_lean_g28_e42_s2_5",
      "defines": ["EDGEBITS=27", "PROOFSIZE=42", "SIPHASH_2_5"]
    },
    {
      "target_name": "cuckoo_lean_g30_e42_s2_5",
      "defines": ["EDGEBITS=29", "PROOFSIZE=42", "SIPHASH_2_5"]
    },
    {
      "target_name": "cuckoo_lean_g32_e42_s2_5",
      "defines": ["EDGEBITS=31", "PROOFSIZE=42", "SIPHASH_2_5"]
    },
  ]
}
