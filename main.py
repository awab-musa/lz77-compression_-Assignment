from compress import compress_file, tag_to_text
from decompress import decompress_file


def ask_int(message, default):
    value = input(message + ' [' + str(default) + ']: ').strip()
    if value == '':
        return default
    return int(value)


def main():
    while True:
        print()
        print('1) Compress   (file1.txt -> file2.txt)')
        print('2) Decompress (file2.txt -> file3.txt)')
        print('3) Exit')
        choice = input('Choose: ').strip()
        if choice == '1':
            search_size = ask_int('Search window size', 4095)
            lookahead_size = ask_int('Look-ahead buffer size', 255)
            r = compress_file('file1.txt', 'file2.txt', search_size, lookahead_size)
            print()
            print('Tags:')
            for t in r['tags']:
                print(tag_to_text(t))
            print()
            print('Number of tags  :', len(r['tags']))
            print('Position bits   :', r['pos_bits'])
            print('Length bits     :', r['len_bits'])
            print('Symbol bits     : 8')
            print('Tag size        :', r['tag_size'], 'bits')
            print('Original size   :', r['original_bits'], 'bits')
            print('Compressed size :', r['compressed_bits'], 'bits')
            if r['original_bits']:
                print('Compressed / Original : %.3f' % (r['compressed_bits'] / r['original_bits']))
        elif choice == '2':
            tags, size = decompress_file('file2.txt', 'file3.txt')
            print('Tags read:', len(tags))
            print('Decompressed', size, 'bytes -> file3.txt')
        elif choice == '3':
            break
        else:
            print('Invalid choice')


if __name__ == '__main__':
    main()