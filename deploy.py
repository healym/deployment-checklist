#! /usr/bin/python3

import argparse
import json
import sys
from textwrap import dedent

from actions import ACTIONS


def main(config_file, progress_file):
    with open(config_file) as f:
        checklist = json.load(f)
    print(checklist['name'])
    for item_num, list_item in enumerate(checklist['list_items']):
        file_comment = prompt_user_action(item_num+1, list_item)  # 1-index for output
    with open(progress_file, 'a') as f:
        f.write(file_comment)


def prompt_user_action(item_num, list_item):
    raw_prompt = list_item['prompt']
    div_length = len(raw_prompt) + 2 + len(str(item_num))
    sys.stdout.write(make_prompt(raw_prompt))
    choice_made = input(make_choices(list_item['choices'])).upper().strip()
    resp = ACTIONS[list_item['choices'][choice_made]]()
    resp_template = dedent('''
                           {num}. {prompt}
                           {div}
                           {resp}
                           ''')

    return resp_template.format(num=item_num, prompt=raw_prompt, div='-'*div_length, resp=resp)


def make_prompt(raw_prompt):
    return raw_prompt + ' '


def make_choices(choices):
    return '/'.join(choices.keys()) + ': '


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--config-file',
                        dest='config_file',
                        default='config.json',
                        help='JSON file containing checklist')
    parser.add_argument('-p', '--progress-file',
                        dest='progress_file',
                        default='checklist.md',
                        help='Record of checklist responses')
    args = parser.parse_args()
    main(args.config_file, args.progress_file)
