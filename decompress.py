def read_tags(file_name):
    tags = []
    file = open(file_name, 'r', encoding='utf-8')

    for line in file:
        line = line.rstrip('\n')
        if line == '':
            continue

        inside = line[1:-1]
        parts = inside.split(',', 2)

        offset = int(parts[0])
        length = int(parts[1])
        char = parts[2]

        tags.append((offset, length, char))

    file.close()
    return tags


def lz77_decompress(tags):
    text = ''

    for offset, length, char in tags:
        start = len(text) - offset

        for k in range(length):
            text = text + text[start + k]

        text = text + char

    return text


def decompress_file(input_name, output_name):
    tags = read_tags(input_name)
    text = lz77_decompress(tags)

    file = open(output_name, 'w', encoding='utf-8')
    file.write(text)
    file.close()

    return text