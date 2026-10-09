# LZ77 compression: turns text into a list of tags (offset, length, next_char)

SEARCH_SIZE = 4095      # how far back we are allowed to look
LOOKAHEAD_SIZE = 255    # the longest match we are allowed to take


def find_longest_match(text, i):
    # Look in the text before position i for the longest part
    # that is the same as the text starting at position i.
    best_offset = 0
    best_length = 0

    start = i - SEARCH_SIZE
    if start < 0:
        start = 0

    for j in range(start, i):
        length = 0
        # Count how many characters match.
        # We stop one character before the end of the text,
        # because every tag needs a "next character" after the match.
        # j + length is allowed to pass position i (overlapping match),
        # that is how "BBBBBBBB" becomes one tag.
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
        i = i + length + 1      # skip the match and the next character
    return tags


def compress_file(input_name, output_name):
    # newline='' means: read the file exactly as it is, do not change line endings
    file = open(input_name, 'r', encoding='utf-8', newline='')
    text = file.read()
    file.close()

    tags = lz77_compress(text)

    # Write one tag per line, like <3,2,B>
    file = open(output_name, 'w', encoding='utf-8')
    for offset, length, char in tags:
        # A real "new line" character would break the line, so we write \n instead
        if char == '\n':
            char = '\\n'
        elif char == '\r':
            char = '\\r'
        file.write('<' + str(offset) + ',' + str(length) + ',' + char + '>\n')
    file.close()

    return tags