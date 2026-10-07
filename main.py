from compress import compress_file
from decompress import decompress_file


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
            try:
                tags = compress_file('file1.txt', 'file2.txt')
            except FileNotFoundError:
                print('file1.txt not found.')
                print()
                continue
            print('Compression completed successfully.')
            print('Tags saved in file2.txt')
            print()
            print('Tags:')
            for tag in tags:
                print(tag)
            print()
        elif choice == '2':
            try:
                text = decompress_file('file2.txt', 'file3.txt')
            except FileNotFoundError:
                print('file2.txt not found. Compress first.')
                print()
                continue
            print('Decompression completed successfully.')
            print()
            print('Decompressed Text:')
            print(text)
            print()
        elif choice == '3':
            break
        else:
            print('Invalid choice.')
            print()


if __name__ == '__main__':
    main()