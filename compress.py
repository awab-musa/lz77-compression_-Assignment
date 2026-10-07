SEARCH_SIZE = 4095
LOOKAHEAD_SIZE = 255

ESCAPES = {'\\': '\\\\', '\n': '\\n', '\r': '\\r'}


def lz77_compress(text, search_size=SEARCH_SIZE, lookahead_size=LOOKAHEAD_SIZE):
    tags = []
    i = 0
    n = len(text)
    while i < n:
        best_len = 0
        best_off = 0
        for j in range(max(0, i - search_size), i):
            length = 0
            while (length < lookahead_size - 1 and i + length < n - 1
                   and text[j + length] == text[i + length]):
                length += 1
            if length > best_len:
                best_len = length
                best_off = i - j
        tags.append((best_off, best_len, text[i + best_len]))
        i += best_len + 1
    return tags


def compress_file(src='file1.txt', dst='file2.txt'):
    with open(src, 'r', encoding='utf-8', newline='') as f:
        text = f.read()
    tags = lz77_compress(text)
    with open(dst, 'w', encoding='utf-8', newline='\n') as f:
        for off, length, ch in tags:
            f.write('<%d,%d,%s>\n' % (off, length, ESCAPES.get(ch, ch)))
    return tags