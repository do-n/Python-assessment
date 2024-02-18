my_set = {112,244,3456,46,5}
print(my_set)
char =112
if char in my_set:
    output = char
    print(output)

my_set.update({121,2323,242})
my_set2 = my_set.copy()
print(my_set2)
print(my_set)
print(len(my_set))
my_set.discard(242)
del my_set
print(my_set2)
print(max(my_set2))
print(min(my_set2))
print(sum(my_set2))
if 274 in my_set2:
    print( 274,' is present')

else:
    print(274, 'not found')