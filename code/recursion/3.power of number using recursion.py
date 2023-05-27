def find_pow(base,pow):
    if pow==0:
        return 1
    return base*find_pow(base,pow-1)

print(find_pow(3,4))