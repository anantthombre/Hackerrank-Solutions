# Link to the coding question -  https://www.hackerrank.com/challenges/finding-the-percentage


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    total = 0
    # print(total)
    for i in student_marks[query_name]:
        total += i
        
    average = float(total/3)
    print("%.2f" % average)
    
