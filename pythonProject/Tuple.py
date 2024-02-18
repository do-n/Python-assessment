my_tuple = (1, 256, 123, 4,98,6,34,22,19,'Don')#a list uses square brackets
print(my_tuple)
print(my_tuple[3])
print(my_tuple[2:4])
print(len(my_tuple))
del my_tuple
#print(my_tuple)
my_tuple2 = (123,232,332,4)
if 'cooking' in my_tuple2:
    print('cooking is present')

else:
    print('no,cooking found')
print(max(my_tuple2))
print(min(my_tuple2))
print(sum(my_tuple2))
print(my_tuple2.count(123))
print(sum(my_tuple2)/len(my_tuple2))
# my_tuple2[2] = 'eating'
# print(my_tuple2)
