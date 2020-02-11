import argparse
import datetime


def checklist_args():
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
    return parser.parse_args()


class Checklist:

    def __init__(self, args):
        '''
        param args: argparse object containing expected command-line args
        '''
        pass

    def run(self):
        pass
