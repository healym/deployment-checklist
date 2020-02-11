import argparse
from datetime import datetime


def checklist_args():
    parser = argparse.ArgumentParser()

    return parser.parse_args()


class Checklist:

    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.date = datetime.now()
        self.date_str = self.date.strftime('%Y_%m_%d')

    def _set_options(self):
        self.parser.add_argument('-f', '--config-file',
                                dest='config_file',
                                default='config.json',
                                help='JSON file containing checklist')
        self.parser.add_argument('-p', '--progress-file',
                                 dest='progress_file',
                                 default=f'checklist_{self.date_str}.md'),
                                 help='Record of checklist responses')
        self.parser.add_argument('-r', '--resume',
                                 dest='resume',
                                 default=False,
                                 action='store_true',
                                 help='Restore from previous run')

    def run(self):
        pass
