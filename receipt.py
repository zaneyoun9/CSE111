import csv
def main():
    products_dict = read_dictionary('products.csv', 0)
    with open('request.csv') as request_file:
        request_reader = csv.reader(request_file)
        next(request_reader)
        for request_row_list in request_reader:
            tmp_row = products_dict[request_row_list[0]]
            print(f'{tmp_row[1]}: {request_row_list[1]} @ {tmp_row[2]}')

            
def read_dictionary(filename, key_column_index):
    # """Read the contents of a CSV file into a compound
    # dictionary and return the dictionary.

    # Parameters
    #     filename: the name of the CSV file to read.
    #     key_column_index: the index of the column
    #         to use as the keys in the dictionary.
    # Return: a compound dictionary that contains
    #     the contents of the CSV file.
    # """
    dictionary = {}
    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row_list in reader:
            if len(row_list) != 0:
                key = row_list[key_column_index]
                dictionary[key] = row_list
    return dictionary

if __name__ == "__main__":
    main()