import re

UNESCAPES = {'\\\\': '\\', '\\n': '\n', '\\r': '\r'}
TAG_PATTERN = re.compile(r'^<(\d+),(\d+),(.*)>$')


def read_tags(path='file2.txt'):
    tags = []
    with open(path, 'r', encoding='utf-8', newline='') as f:
        content = f.read()
    for line in content.split('\n'):
        line = line.rstrip('\r')
        if line == '':
            continue
        match = TAG_PATTERN.match(line)
        if match is None:
            raise ValueError('Invalid tag: ' + line)
        off = int(match.group(1))
        length = int(match.group(2))
        ch = UNESCAPES.get(match.group(3), match.group(3))
        tags.append((off, length, ch))
    return tags


def lz77_decompress(tags):
    out = []
    for off, length, ch in tags:
        start = len(out) - off
        for k in range(length):
            out.append(out[start + k])
        out.append(ch)
    return ''.join(out)


def decompress_file(src='file2.txt', dst='file3.txt'):
    tags = read_tags(src)
    text = lz77_decompress(tags)
    with open(dst, 'w', encoding='utf-8', newline='') as f:
        f.write(text)
    return text