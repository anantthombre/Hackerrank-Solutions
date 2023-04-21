# Link to coding question - https://www.hackerrank.com/challenges/python-tuples

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    
    # from __builtins__ import hash
    
    t = tuple(integer_list)
    print(hash(t))
