"""find the one missing number from a list of 1-100"""

my_list = [i for i in range(1,101)]
my_list.remove(12)
print(my_list)
# here we are removing element 12 from the list

def find_missing(list,n):
    actual_sum = (n*(n+1))/2  #(n*(n+1))/2 --> sum of sequence of numbers
    real_sum = sum(list)
    return int(actual_sum-real_sum)

print(find_missing(my_list,100))