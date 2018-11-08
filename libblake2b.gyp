{
  "targets": [
    {
      "target_name": "libblake2b",
      #"type": "<(library)",
      "type": "static_library",
      "sources": [
      	"lib/cuckoo/src/blake2b-ref.c",
      ],
      "cflags": [
        "-std=gnu11",
        "-Wall",
        "-Wno-format",
        "-fomit-frame-pointer",
        "-O3"
      ]
    }
  ]
}
