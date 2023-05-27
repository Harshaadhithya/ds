list1 = [1,2,3]
list2 = [2,3,1]

list3 = ['a','b','c']
list4 = ['b','a','c']

def check_perm(l1,l2):
    l1.sort()
    l2.sort()
    if l1==l2:
        print("yes")
    else:
        print("no")

check_perm(list1,list2)
check_perm(list1,list3)
check_perm(list4,list3)
