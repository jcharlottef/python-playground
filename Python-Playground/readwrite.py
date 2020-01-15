with open('name.txt') as f:
    my_name = f.read()

print(my_name)

with open('hello.txt', 'w') as f:
    f.write('hello, my name is '+ my_name)
    f.write('\n')

    