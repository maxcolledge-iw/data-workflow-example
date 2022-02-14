import csv

def write_list_of_dict_to_csv(filename, list_of_dict):
    with open(filename, mode='w') as file:
        # TODO headers in function arguments?
        fieldnames = ['name', 'rating']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(list_of_dict)

vegetables = [
    {'name': 'onion', 'rating': 5},
    {'name': 'cucumber', 'rating': 3},
    {'name': 'broccoli', 'rating': 4}
]

write_list_of_dict_to_csv('vegetables.csv', vegetables)