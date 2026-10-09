# LZ77 decompression: turns the tags back into the original text


def read_tags(file_name):
    tags = []
    file = open(file_name, 'r', encoding='utf-8')
    for line in file:
        line = line.rstrip('\n')
        if line == '':
            continue

        # line looks like <3,2,B>
        inside = line[1:-1]                 # remove < and >  ->  3,2,B
        parts = inside.split(',', 2)        # split at the first 2 commas only
        offset = int(parts[0])
        length = int(parts[1])
        char = parts[2]

        # change \n and \r back to the real characters
        if char == '\\n':
            char = '\n'
        elif char == '\\r':
            char = '\r'

        tags.append((offset, length, char))
    file.close()
    return tags


def lz77_decompress(tags):
    text = ''
    for offset, length, char in tags:
        start = len(text) - offset      # go back "offset" characters
        # Copy one character at a time.
        # This is important for overlapping matches: we may copy
        # characters that we have just added in this same loop.
        for k in range(length):
            text = text + text[start + k]
        text = text + char
    return text


def decompress_file(input_name, output_name):
    tags = read_tags(input_name)
    text = lz77_decompress(tags)

    # newline='' means: write the text exactly as it is
    file = open(output_name, 'w', encoding='utf-8', newline='')
    file.write(text)
    file.close()

    return text