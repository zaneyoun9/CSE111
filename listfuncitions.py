from typing import SupportsIndex


list=['apple', 'orange', 'banana']

def append_list():
    item = input('What would you like to add to the list? ')
    list.append(item)

def remove_list():
    ind = int(input('Which entry would you like to remove? (integer please)' ))
    ind = ind -1
    list.pop(ind)

def insert_list():
    add_item = input('What item would you like to add to the list? ')
    add_index = int(input('Which position of the list would you like this item to be? (Integer please) '))
    list.insert(add_index-1, add_item)


def main():
    append_list()
    remove_list()
    insert_list()
    print(list)


main()