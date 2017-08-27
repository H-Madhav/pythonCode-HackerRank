from decimal import Decimal
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    markes = student_marks[query_name]
    total = sum(markes)
    avg = Decimal(total/3)
    print(round(avg, 2))
    
    
    
