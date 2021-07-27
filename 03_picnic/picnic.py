#!/usr/bin/env python3
"""
Author: atulya
Date: 27-07-2021
Purpose: Picnic program
"""

import argparse

# -----------------------------------------------
def get_args():
    """ Get command line arguments"""
    parser = argparse.ArgumentParser(
        description="Picnic Game",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument('str',
                        metavar='str',
                        nargs='+',
                        type=str,
                        help='Item(s) to bring')

    parser.add_argument('-s',
                        '--sorted',
                        help='Sort the items',
                        action='store_true')
    
    return parser.parse_args()

def main():
    """ Main function for picnic"""

    args = get_args()
    items = args.str
    if args.sorted:
        items.sort()

    bringing = ''

    if len(items) == 1:
        bringing = items[0]
    elif len(items) == 2:
        bringing = ' and '.join(items)
    else:
        items[-1] = 'and ' + items[-1]
        bringing = ', '.join(items)
    
    print ('You are bringing {}.'.format(bringing))

if __name__ == '__main__':
    main()