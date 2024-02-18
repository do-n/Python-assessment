my_dictionary ={
    "Name": "NAME",
    "Gender": "Male",
    "School": "School of engineering"
}
my_dictionary =dict(
    Name="NAME",
    Gender="Male",
    School="School of engineering"
)
print(my_dictionary)
print(my_dictionary['Name'])
print(my_dictionary['Gender'])
my_dictionary['Gender'] = 'Female'
print(my_dictionary)
my_dictionary['Birthday'] = '1970-01-01'
print(my_dictionary)
my_dictionary2 = my_dictionary.copy()
print(my_dictionary2)
print(len(my_dictionary2))
my_dictionary.pop('Gender')#removes the Gender
del my_dictionary
print(my_dictionary2)
for value in my_dictionary2:
    print(my_dictionary2[value]) #print dict values

for key in my_dictionary2:
    print(my_dictionary2[key]) #print the dict key
