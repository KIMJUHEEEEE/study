def print_n_times(value,n):
    for i in range(n):
        print(value)

print_n_times(3,5)

# 가변 매개변수
def print_n_times2(n,*value):
    for i in range(n):
        print(value)
    print()

print_n_times2(3,"가변","매개변수")