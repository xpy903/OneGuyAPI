def covert(txt: str, filename):
    words = txt.split(',')
    null_indexs = []
    print(words)
    for i in range(len(words)):

        if any((words[i] == "",
               i == "\n",
               i == "\r\n")):
            null_indexs.append(i)

    print(null_indexs)
    for i in null_indexs:
        words[i] = "NULL"

    with open(filename, 'a') as f:
        f.write(','.join(words))


def read_line(filename):
    with open(filename, 'r') as f:
        for line in f:
            yield line


def start(src_filename, dst_filename):
    line_generator = read_line(src_filename)
    while True:
        try:
            line = next(line_generator)
        except:
            print('covert success')
            break
        else:
            covert(line, dst_filename)


if __name__ == '__main__':
    start('t1.csv', 't1_convert.csv')
