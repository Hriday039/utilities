import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', action='store_true')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    if args.v:
        print('-v is True')
    else:
        print('-v is False')


parser.add_argument('-v', action='store_true')
