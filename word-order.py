# Link to the coding question -  https://www.hackerrank.com/challenges/word-order

from collections import OrderedDict

n = int(input())

words = OrderedDict()
count = 0

for i in range(n):
    word = input()
    
    if word in words:
        words[word] += 1
    else:
        words[word] = 1
        count += 1
        
print(count)
for word in words:
    print(words[word], end=" ")
