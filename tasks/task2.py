# tasks/task2.py

def solve():
# Ниже пишите решение задачи
    n = int(input().strip())
    n %= 1440
    print(n // 60, n % 60)
   

   
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()