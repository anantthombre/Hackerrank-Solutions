# Link to coding question -  https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    arr = set(arr)
    arr = list(arr)
    arr.sort()
    print(arr[-2])
    
    
