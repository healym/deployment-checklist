#! /usr/bin/python3

import argparse
import os
from datetime import datetime


class ChecklistDriver:

    def __init__(self):
        self._set_options()
        self.date = datetime.now()
        self.date_str = self.date.strftime('%Y_%m_%d')
        self.checklist_items = None
        self.checklist_output = self.args.output_file
        self.checklist_file = self._validate_checklist_file()

    def _set_options(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('-f', '--config-file',
                                dest='config_file',
                                help='JSON file containing checklist')
        parser.add_argument('-o', '--output-file',
                                 dest='output_file',
                                 default=f'checklist_{self.date_str}.md'),
                                 help='Record of checklist responses')
        parser.add_argument('-r', '--resume',
                                 dest='resume',
                                 default=False,
                                 action='store_true',
                                 help='Restore from previous run')
        self.args = parser.parse_args()

    def _validate_checklist_file(self):
        default_locations = ['~/.config/checklist.py',
                             '~/.checklist.py',
                             'checklist.py']
        if self.args is not None:
            return self.args.config_file
        for default_location in default_locations:
            if os.path.exists(default_location):
                return default_location
        else:
            print('Config file must be provided!')
            exit()

    def parse_checklist_file(self):
        pass  # TODO

    def run(self):
        for num, list_item in enumerate(self.checklist_items, start=1):
            list_item.run(self.checklist_output, num)

if __name__ == '__main__':
    checklist = ChecklistDriver()
    checklist.run()
