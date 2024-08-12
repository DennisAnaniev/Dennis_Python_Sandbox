# Arithmetic operators
print(5 + 5)
print(5 - 5)
print(5 * 5)
print(5 / 5)
print(5 // 5)
print(5 % 5)
print(5 ** 5)
print(1_000 == 1000)
print(divmod(15,3))
print(sum([1,2,3,4,5,6,7,8,9]))
print(max([1,2,3,4,5,6,7,8,9]))
print(min([1,2,3,4,5,6,7,8,9]))
print(round(3.141592653589793,2))
print(7 == 5)
print(7 != 5)
print("a" == "A")
print(7 >= 5)
print(7 <= 5)
a = 5
b = 7
print(a is b)

#The value of a mutable variable can  be changed after it has been created but the value of an immutable variable can't be changed
#Immutable int,float,str,yuple,frozenset
#Mutable  list,set,dict

print(id(a))
a += 3
print(id(a))

numbers = [1,2,3,4,5,6,7,8,9]
print(id(numbers))
numbers.append(100)
print(numbers)
print(id(numbers))
nums = numbers.copy()
print(nums)
print(nums == numbers)
print(id(numbers))
print(id(numbers))

print(format(1/3,'.10f'))

a = 0.1 * 3
b = 0.3
print(a == b)

from math import isclose
print(isclose(a,b))

a = 99999.01
b = 99999.03
print(isclose(a, b, abs_tol=1.0))