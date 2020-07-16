import os
import argparse
from glob import glob 


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', action='store_true')
    # To read a specific file or list of files
    group = parser.add_mutually_exclusive_group(required=True)
    # To read list of files
    group.add_argument('-f', nargs='+', help='Path of group record')
    # To read file path
    group.add_argument('-d', type=str, help='Directory of group record')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    
    # To read list of file
    in_file = args.f
    # To read file from a directory
    in_path = args.d
    if type(in_file) == list:
        print(in_file)
    elif type(in_path) == str:
        csv = '*.csv'
        path = os.path.join(in_path, csv)
        files = glob(path)
        print(files)
        
    if args.v:
        print('-v is True')
    else:
        print('-v is False')


    parser.add_argument('-v', action='store_true')
