def find_sum_of_digits(n):
    if n==0:
        return 0
    return (n%10)+find_sum_of_digits(int(n/10))

print(find_sum_of_digits(1029))