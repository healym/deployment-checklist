#! /usr/bin/python3

import argparse
import json
import sys

ACTIONS = {
    'DONE': lambda: print('done'),
    'COMMENT': lambda: print('comment')
}


def main(config_file):
    with open(config_file) as f:
        checklist = json.load(f)
        print(checklist['name'])
        for list_item in checklist['list_items']:
            print(list_item['prompt'])
            sys.stdout.write(make_prompt(list_item['choices']))
            choice_made = input().upper().strip()
            ACTIONS[list_item['choices'][choice_made]]()


def make_prompt(choices):
    return '/'.join(choices.keys()) + ': '


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--config-file',
                        dest='config_file',
                        default='config.json',
                        help='JSON file containing checklist')
    args = parser.parse_args()
    main(args.config_file)
