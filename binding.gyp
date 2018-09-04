{
  "targets": [
    {
      "target_name": "cuckoo",
      "sources": [
        "lib/addon.cc",
        "lib/pow.cc",
        "lib/blake/blake2b.cpp"
      ],
      "include_dirs": ["<!(node -e \"require('nan')\")"],
      "cflags": [
        #"-m64",
        #"-maes",
        #"-mavx",
        "-Wno-maybe-uninitialized",
        "-msse2",
        "-std=c++11"
      ]
    }
  ]
}
