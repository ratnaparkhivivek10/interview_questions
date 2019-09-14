import time

f = open('example.log', 'r')

while True:
    line = f.readline()
    print(f.tell())
    if line:
        print(line, end='')
    else:
        time.sleep(1)