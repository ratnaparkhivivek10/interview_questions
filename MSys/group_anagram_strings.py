'''
Group anagram strings
Input: ['abc', 'cba', 'pqr', 'uvw', 'wvu', 'def']
Output: [['abc', 'cba'], ['pqr'], ['uvw', 'wvu'], ['def']]
'''

data = ['abc', 'cba', 'pqr', 'uvw', 'wvu', 'def']

d = {}

for item in data:
    d.setdefault(''.join(sorted(item)), []).append(item)

print(d.values())