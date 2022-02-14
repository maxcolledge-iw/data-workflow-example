import list_io

# TODO implement dictionary
fruits = list_io.get_list_from_file('fruits.txt')

#This is the main program
fruits.append('mango')
# TODO manipulate and change the data

list_io.write_list_to_file('fruits.txt', fruits)
