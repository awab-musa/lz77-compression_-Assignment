import os

from compress import compress_file
from decompress import decompress_file


def do_compression():
    if not os.path.exists('file1.txt'):
        print('file1.txt not found.')
        return

    tags = compress_file('file1.txt', 'file2.txt')

    if len(tags) == 0:
        print('file1.txt is empty, nothing to compress.')
        return

    print('Compression completed successfully.')
    print('Tags saved in file2.txt')
    print()
    print('Tags:')
    for offset, length, char in tags:
        # repr() shows the character with quotes, so a space or new line is visible
        print('<' + str(offset) + ',' + str(length) + ',' + repr(char) + '>')


def do_decompression():
    if not os.path.exists('file2.txt'):
        print('file2.txt not found. Compress first.')
        return

    text = decompress_file('file2.txt', 'file3.txt')

    print('Decompression completed successfully.')
    print('Text saved in file3.txt')
    print()
    print('Decompressed Text:')
    print(text)


def main():
    while True:
        print('===== LZ77 Compression System =====')
        print('1. Compression')
        print('2. Decompression')
        print('3. Exit')
        print()
        choice = input('Enter your choice: ').strip()
        print()

        if choice == '1':
            do_compression()
        elif choice == '2':
            do_decompression()
        elif choice == '3':
            break
        else:
            print('Invalid choice.')
        print()


if __name__ == '__main__':
    main()