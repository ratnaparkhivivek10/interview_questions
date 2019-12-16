'''
Implement tail -f command. Keep on displaying last 5 lines
'''
with open('example.log', 'r') as f:
    while True:
        lines = f.readlines()[-5:]
        for line in lines:
            print(line, end='')