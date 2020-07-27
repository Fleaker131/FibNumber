#-------------------------------#
#CreatedByFleaker#
# CreatedDateAndTime #
# Time: 15:47 /Date: 07/06/2020 #
#-------------------------------#

limit = int(input("Limit : "))
def fib(high):
    a,b = 1,1 # Mutiply Varriable #
    print(a)
    print(b)
    i = 2
    while i <=high:
        a,b = b, a+b
        print(b)
        i += 1

fib(limit)