#!/usr/bin/env python3
"""
Author : atulya <atulya@localhost>
Date   : 2021-07-26
Purpose: crowsnest program
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Crow's nest -- choose the correct article",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='word',
                        help='A word')

    

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    word = args.word
    article = ''
    template = 'Ahoy, Captain, {} {} off the larboard bow!'
    article = 'an' if word[0].lower() in 'aeiou' else 'a'
    print(template.format(article, word))

    # print statement can also be written as
    # print(f'Ahoy, Captain, {article} {word} off the larboard bow!')


# --------------------------------------------------
if __name__ == '__main__':
    main()
