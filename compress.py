SEARCH_SIZE = 4095
LOOKAHEAD_SIZE = 255


def find_longest_match(text, i):
    best_offset = 0
    best_length = 0

    start = i - SEARCH_SIZE
    if start < 0:
        start = 0

    for j in range(start, i):
        length = 0

        while (length < LOOKAHEAD_SIZE
               and i + length < len(text) - 1
               and text[j + length] == text[i + length]):
            length = length + 1

        if length > best_length:
            best_length = length
            best_offset = i - j

    return best_offset, best_length


def lz77_compress(text):
    tags = []
    i = 0

    while i < len(text):
        offset, length = find_longest_match(text, i)
        next_char = text[i + length]
        tags.append((offset, length, next_char))
        i = i + length + 1

    return tags


def compress_file(input_name, output_name):
    file = open(input_name, 'r', encoding='utf-8', newline='')
    text = file.read()
    file.close()

    tags = lz77_compress(text)

    file = open(output_name, 'w', encoding='utf-8')
    for offset, length, char in tags:
        file.write('<' + str(offset) + ',' + str(length) + ',' + char + '>\n')
    file.close()

    return tags