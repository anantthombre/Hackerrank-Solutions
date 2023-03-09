# Link to coding question -    https://www.hackerrank.com/challenges/py-collections-ordereddict

from collections import OrderedDict

n = int(input())

item_dict = OrderedDict()

for i in range(n):
    item = input().split()
    price = int(item[-1])
    item.pop()
    item = " ".join(item)
    if item in item_dict:
        item_dict[item] += price
    else:
        item_dict[item] = price

for item in item_dict:
    print(item, item_dict[item])
