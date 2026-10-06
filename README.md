# LZ77 Compression

Lossless LZ77 compressor and decompressor in Python (Information Theory and Data Compression, Assignment 1).

## How it works

- Compression reads `file1.txt` and writes `file2.txt`.
- Each tag is `<position, length, next symbol>`.
- Tags are stored as binary 0/1. The file starts with a 16-bit header (position bits, length bits), then the tags.
- Overlapping matches are supported, so a sequence like `BBBBBBBBBB` becomes `<1,10,"A">`.
- Decompression reads `file2.txt` and writes `file3.txt`.

## Run

    python main.py

Then choose 1 to compress, 2 to decompress, 3 to exit. Press Enter to use the default window sizes.

## Example

Input in `file1.txt`:

    ABAABABAABBBBBBBBBBBBA

Tags:

    <0,0,"A"> <0,0,"B"> <2,1,"A"> <3,2,"B"> <5,3,"B"> <1,10,"A">

Original size is 176 bits and compressed size is 90 bits.

## Files

- `main.py`: menu
- `compress.py`: LZ77 compressor
- `decompress.py`: LZ77 decompressor
