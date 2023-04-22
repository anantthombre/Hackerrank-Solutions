# Link to the coding question -  https://www.hackerrank.com/challenges/nested-list

if __name__ == '__main__':
    num = []
    arr = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        arr.append([name, score])
        num.append(score)
        
    num.sort()
    lowest = num[0]
    second_lowest = 0
        
    arr.sort()
        
    for i in num:
        if i != lowest:
            second_lowest = i
            break
        
    names = []
        
    for i in arr:
        if i[1] == second_lowest:
            print(i[0])
            # if i[0] in names:
            #     continue
            # else:
            #     names.append(i[1])
                    
