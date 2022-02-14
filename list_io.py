def get_list_from_file(filename):
    list_from_file = []
    
    with open(filename, "r") as file:
        list_from_file = file.readlines()
    
    for index in range(0, len(list_from_file)):
        list_from_file[index] = list_from_file[index].rstrip()
    
    return list_from_file

def write_list_to_file(filename, list_for_file):
    with open(filename, 'w') as items_file:
        for item in list_for_file:
            items_file.write(item + '\n')

