def bits_to_tags(bits):
    pos_bits = int(bits[0:8], 2)
    len_bits = int(bits[8:16], 2)
    step = pos_bits + len_bits + 8
    tags = []
    i = 16
    while i + step <= len(bits):
        off = int(bits[i:i + pos_bits], 2)
        length = int(bits[i + pos_bits:i + pos_bits + len_bits], 2)
        c = int(bits[i + pos_bits + len_bits:i + step], 2)
        tags.append((off, length, c))
        i += step
    return tags


def lz77_decompress(tags):
    out = bytearray()
    for off, length, c in tags:
        start = len(out) - off
        for k in range(length):
            out.append(out[start + k])
        out.append(c)
    return bytes(out)


def decompress_file(src='file2.txt', dst='file3.txt'):
    with open(src, 'r') as f:
        bits = f.read().strip()
    tags = bits_to_tags(bits)
    data = lz77_decompress(tags)
    with open(dst, 'wb') as f:
        f.write(data)
    return tags, len(data)