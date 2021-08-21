def process():
    with open('logs.txt', 'r+') as l:
        read = l.readlines()
        read = read[len(read) - 1]
        read = read.replace('\n', '')
        #read = read.replace(' ', '')
        read = read.split(' | ')

        date = (read[0].split(' '))[0].split('-')

    return read, date

print(process())