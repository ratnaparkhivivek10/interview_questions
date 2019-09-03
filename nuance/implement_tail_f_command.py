import time


f = open('example.log', 'r')

while True:
    line = f.readline()

    if line:
        print(line, end='')
    else:
        time.sleep(1)