#! /usr/bin/python

from __future__ import absolute_import, division, print_function
from __py2to3__.builtins_overrides import *

import argparse
import json
import sys
import re
from textwrap import dedent
from datetime import datetime

from actions import ACTIONS

LEN_OF_DATETIME = 22  # YYYY-mm-dd HH:MM:SS


def main(config_file, progress_file, resume=False):
    with open(config_file) as f:
        checklist = json.load(f)
    name = checklist['name']
    print(name)
    with open(progress_file, 'a') as f:
        f.write(dedent('''
                       {name} [{date}]
                       {div}
                       ''').format(name=name,
                                   date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                   div='=' * (len(name) + LEN_OF_DATETIME)))
    list_items = get_remaining_items(checklist['list_items'], progress_file, resume)
    for item_num, list_item in list_items:
        file_comment = prompt_user_action(item_num + 1, list_item)  # 1-index for output
        with open(progress_file, 'a') as f:
            f.write(file_comment)


def get_remaining_items(list_items, progress_file, resume):
    match_str = '([0-9]+)\) [a-zA-Z]+....[a-zA-Z]+'
    if not resume:
        return enumerate(list_items)
    with open(progress_file) as f:
        possible_matches = map(lambda line: re.match(match_str, line), f.readlines())
        matches = filter(lambda match: match is not None, possible_matches)
        idx = list(map(lambda m: int(m.groups()[0]), matches))[-1]  # last used index (1-indexed)
        return enumerate(list_items[idx:], start=idx)


def prompt_user_action(item_num, list_item):
    raw_prompt = list_item['prompt']
    sys.stdout.write(make_prompt(raw_prompt))
    choices = list_item['choices']
    default_choice = list_item['default_choice']
    choice_made = get_selection(choices, default_choice)

    resp = ACTIONS[list_item['choices'][choice_made]]()
    div_length = len(raw_prompt) + 2 + len(str(item_num)) + 4 + len(choice_made)
    resp_template = dedent('''
                           {num}) {prompt}....{choice_made}
                           {div}
                           {resp}
                           ''')

    return resp_template.format(num=item_num,
                                prompt=raw_prompt,
                                div='-' * div_length,
                                resp=resp,
                                choice_made=choice_made)


def get_selection(choices, default):
    choice = None
    while choice not in choices:
        choice = input(make_choices_prompt(choices,)).upper().strip()
        if choice == '':  # no input given
            return default
    return choice


def make_prompt(raw_prompt):
    return raw_prompt + ' '


def make_choices_prompt(choices, default_choice):
    return '/'.join(['[{}]'.format(c) if c == default_choice else c for c in choices]) + ': '


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--config-file',
                        dest='config_file',
                        default='config.json',
                        help='JSON file containing checklist')
    parser.add_argument('-p', '--progress-file',
                        dest='progress_file',
                        default='checklist_{timestamp}.md'.format(timestamp=datetime.now().strftime('%Y_%m_%d')),
                        help='Record of checklist responses')
    parser.add_argument('-r', '--resume',
                        dest='resume',
                        default=False,
                        action='store_true',
                        help='Restore from previous run')
    args = parser.parse_args()
    main(args.config_file, args.progress_file, args.resume)
