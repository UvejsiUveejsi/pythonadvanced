

string_length = len("Hello World")
list_length = len([1,2,3,4,5,6])
tuple_length = len((10,20,30,40))

print(string_length)
print(list_length)
print(tuple_length)


sum_of_list = sum([2,4,6,8])
sum_of_tuple = sum((1,3,6,8,9))

print(sum_of_list)
print(sum_of_tuple)

max_value = max(5,15,30)
max_float = max(1.2, 4.6, 7.8)


print(max_value)
print(max_float)


def add(x,y):
    return x+y

def concentrate(x,y):
    return str(x) + str(y)


def operate(operation, x, y):
    return operation(x,y)


result_sum=operate(add, 5, 10)
result_concentrate = operate (concentrate, "hi", " from us")
print(result_sum)
print(result_concentrate)
