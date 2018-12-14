# target naming:
# {variant}_{miner}_g{graphSize}_e{edgeCount}_s{sipHash}
{
  "variables": {
    # shortcuts for cuckoo variant main source
    "cuckoo_lean": "lib/cuckoo/src/cuckoo/lean.cpp",
    "cuckatoo_lean": "lib/cuckoo/src/cuckatoo/lean.cpp"
  },
  "target_defaults": {
    "sources": [
      "lib/addon.cc"
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
      "ATOMIC",
      # shuts off cuckatoo logging
      "SQUASH_OUTPUT=1"
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
      "target_name": "cuckatoo_lean_g20_e8_s2_4",
      "defines": ["EDGEBITS=19", "PROOFSIZE=8", "SIPHASH_2_4"],
      "sources": ["<(cuckatoo_lean)"]
    },
    {
      "target_name": "cuckatoo_lean_g28_e8_s2_4",
      "defines": ["EDGEBITS=27", "PROOFSIZE=8", "SIPHASH_2_4"],
      "sources": ["<(cuckatoo_lean)"]
    },
    {
      "target_name": "cuckatoo_lean_g30_e8_s2_4",
      "defines": ["EDGEBITS=29", "PROOFSIZE=8", "SIPHASH_2_4"],
      "sources": ["<(cuckatoo_lean)"]
    },
    {
      "target_name": "cuckatoo_lean_g32_e8_s2_4",
      "defines": ["EDGEBITS=31", "PROOFSIZE=8", "SIPHASH_2_4"],
      "sources": ["<(cuckatoo_lean)"]
    },

    # PROOFSIZE=24, SIPHASH_2_4
    {
      "target_name": "cuckatoo_lean_g20_e24_s2_4",
      "defines": ["EDGEBITS=19", "PROOFSIZE=24", "SIPHASH_2_4"],
      "sources": ["<(cuckatoo_lean)"]
    },
    {
      "target_name": "cuckatoo_lean_g28_e24_s2_4",
      "defines": ["EDGEBITS=27", "PROOFSIZE=24", "SIPHASH_2_4"],
      "sources": ["<(cuckatoo_lean)"]
    },
    {
      "target_name": "cuckatoo_lean_g30_e24_s2_4",
      "defines": ["EDGEBITS=29", "PROOFSIZE=24", "SIPHASH_2_4"],
    },
    {
      "target_name": "cuckatoo_lean_g32_e24_s2_4",
      "defines": ["EDGEBITS=31", "PROOFSIZE=24", "SIPHASH_2_4"],
      "sources": ["<(cuckatoo_lean)"]
    },

    # PROOFSIZE=42, SIPHASH_2_4
    {
      "target_name": "cuckatoo_lean_g20_e42_s2_4",
      "defines": ["EDGEBITS=19", "PROOFSIZE=42", "SIPHASH_2_4"],
      "sources": ["<(cuckatoo_lean)"]
    },
    {
      "target_name": "cuckatoo_lean_g28_e42_s2_4",
      "defines": ["EDGEBITS=27", "PROOFSIZE=42", "SIPHASH_2_4"],
      "sources": ["<(cuckatoo_lean)"]
    },
    {
      "target_name": "cuckatoo_lean_g30_e42_s2_4",
      "defines": ["EDGEBITS=29", "PROOFSIZE=42", "SIPHASH_2_4"],
      "sources": ["<(cuckatoo_lean)"]
    },
    {
      "target_name": "cuckatoo_lean_g32_e42_s2_4",
      "defines": ["EDGEBITS=31", "PROOFSIZE=42", "SIPHASH_2_4"],
      "sources": ["<(cuckatoo_lean)"]
    },

    # PROOFSIZE=8, SIPHASH_2_5
    {
      "target_name": "cuckatoo_lean_g20_e8_s2_5",
      "defines": ["EDGEBITS=19", "PROOFSIZE=8", "SIPHASH_2_5"],
      "sources": ["<(cuckatoo_lean)"]
    },
    {
      "target_name": "cuckatoo_lean_g28_e8_s2_5",
      "defines": ["EDGEBITS=27", "PROOFSIZE=8", "SIPHASH_2_5"],
      "sources": ["<(cuckatoo_lean)"]
    },
    {
      "target_name": "cuckatoo_lean_g30_e8_s2_5",
      "defines": ["EDGEBITS=29", "PROOFSIZE=8", "SIPHASH_2_5"],
      "sources": ["<(cuckatoo_lean)"]
    },
    {
      "target_name": "cuckatoo_lean_g32_e8_s2_5",
      "defines": ["EDGEBITS=31", "PROOFSIZE=8", "SIPHASH_2_5"],
      "sources": ["<(cuckatoo_lean)"]
    },

    # PROOFSIZE=24, SIPHASH_2_5
    {
      "target_name": "cuckatoo_lean_g20_e24_s2_5",
      "defines": ["EDGEBITS=19", "PROOFSIZE=24", "SIPHASH_2_5"],
      "sources": ["<(cuckatoo_lean)"]
    },
    {
      "target_name": "cuckatoo_lean_g28_e24_s2_5",
      "defines": ["EDGEBITS=27", "PROOFSIZE=24", "SIPHASH_2_5"],
      "sources": ["<(cuckatoo_lean)"]
    },
    {
      "target_name": "cuckatoo_lean_g30_e24_s2_5",
      "defines": ["EDGEBITS=29", "PROOFSIZE=24", "SIPHASH_2_5"],
      "sources": ["<(cuckatoo_lean)"]
    },
    {
      "target_name": "cuckatoo_lean_g32_e24_s2_5",
      "defines": ["EDGEBITS=31", "PROOFSIZE=24", "SIPHASH_2_5"],
      "sources": ["<(cuckatoo_lean)"]
    },

    # PROOFSIZE=42, SIPHASH_2_5
    {
      "target_name": "cuckatoo_lean_g20_e42_s2_5",
      "defines": ["EDGEBITS=19", "PROOFSIZE=42", "SIPHASH_2_5"],
      "sources": ["<(cuckatoo_lean)"]
    },
    {
      "target_name": "cuckatoo_lean_g28_e42_s2_5",
      "defines": ["EDGEBITS=27", "PROOFSIZE=42", "SIPHASH_2_5"],
      "sources": ["<(cuckatoo_lean)"]
    },
    {
      "target_name": "cuckatoo_lean_g30_e42_s2_5",
      "defines": ["EDGEBITS=29", "PROOFSIZE=42", "SIPHASH_2_5"],
      "sources": ["<(cuckatoo_lean)"]
    },
    {
      "target_name": "cuckatoo_lean_g32_e42_s2_5",
      "defines": ["EDGEBITS=31", "PROOFSIZE=42", "SIPHASH_2_5"],
      "sources": ["<(cuckatoo_lean)"]
    },
  ]
}
