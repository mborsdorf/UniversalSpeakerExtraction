# Script to concatenate two data lists
#
# Author: Marvin Borsdorf
# Machine Listening Lab, University of Bremen, Germany
# August, 2021

import argparse

def run(args):
    list_file_a = args.list_a
    list_file_b = args.list_b
    output_file = args.output_list

    # Open and read list a
    with open(list_file_a) as file_a:
        list_a = file_a.readlines()

    # Open and read list b
    with open(list_file_b) as file_b:
        list_b = file_b.readlines()

    # Concatenate lists a and b
    list_c = list_a + list_b

    # Store new list on hard disk 
    with open(output_file, "a") as file_c:
        for item in list_c:
            file_c.write(str(item))
    
    
    print("Data list a with %i rows." % len(list_a))
    print("Data list b with %i rows." % len(list_b))
    print("Concatenated data lists a and b to data list c with %i rows. Stored as data list c." % len(list_c))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Arguments to concatenate two data lists.")
    parser.add_argument("--list_a",
                        type=str,
                        default=None,
                        required=True,
                        help="Path to data list file a.")
    parser.add_argument("--list_b",
                        type=str,
                        default=None,
                        required=True,
                        help="Path to data list file b.")
    parser.add_argument("--output_list",
                        type=str,
                        default=None,
                        required=True,
                        help="Path to store concatenated data list file c.")
    args = parser.parse_args()
    run(args)
