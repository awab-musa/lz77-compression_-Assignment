def lz77_compress(data, search_size=4095, lookahead_size=255):
    tags = []
    i = 0
    n = len(data)
    while i < n:
        best_len = 0
        best_off = 0
        lo = max(0, i - search_size)
        for j in range(i - 1, lo - 1, -1):
            length = 0
            while (length < lookahead_size - 1 and i + length < n - 1
                   and data[j + length] == data[i + length]):
                length += 1
            if length > best_len:
                best_len = length
                best_off = i - j
        tags.append((best_off, best_len, data[i + best_len]))
        i += best_len + 1
    return tags


def tag_to_text(tag):
    off, length, c = tag
    ch = chr(c)
    if not ch.isprintable():
        ch = repr(ch)[1:-1]
    return '<%d,%d,"%s">' % (off, length, ch)


def bit_widths(tags):
    if not tags:
        return 1, 1
    pos_bits = max(1, max(t[0] for t in tags).bit_length())
    len_bits = max(1, max(t[1] for t in tags).bit_length())
    return pos_bits, len_bits


def tags_to_bits(tags):
    pos_bits, len_bits = bit_widths(tags)
    parts = [format(pos_bits, '08b'), format(len_bits, '08b')]
    for off, length, c in tags:
        parts.append(format(off, '0%db' % pos_bits))
        parts.append(format(length, '0%db' % len_bits))
        parts.append(format(c, '08b'))
    return ''.join(parts)


def compress_file(src='file1.txt', dst='file2.txt', search_size=4095, lookahead_size=255):
    with open(src, 'rb') as f:
        data = f.read()
    tags = lz77_compress(data, search_size, lookahead_size)
    with open(dst, 'w') as f:
        f.write(tags_to_bits(tags))
    pos_bits, len_bits = bit_widths(tags)
    tag_size = pos_bits + len_bits + 8
    return {
        'tags': tags,
        'pos_bits': pos_bits,
        'len_bits': len_bits,
        'tag_size': tag_size,
        'original_bits': len(data) * 8,
        'compressed_bits': len(tags) * tag_size,
    }