greeting = "Good morning, "
name = "Ankhy"
print(type(name))
print(greeting + name)
c = greeting + name
print(c)


name = "Ankhy"
print(name[4])
#name[4] = "i" ---> does not work
print(name[0: 3])
print(name[1: 4])
print(name[:4]) # is same as name[0:4]
print(name[1:]) # is same as name[1:5]
print(name[-4 : -1])


name = "AnkhyIsBeautiful"
print(name[1::2])