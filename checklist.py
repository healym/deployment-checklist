from textwrap import dedent
import datetime

class ChecklistLog:
    def __init__(self, filename, num):
        self.filename = filename
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, mode='a')
        div_length = len(str(num)) + 2 + len(prompt)
        basic_template = dedent('''
                                {num}) {prompt}
                                {div}

                                '''.format(num=num,
                                           prompt=self.prompt,
                                           div='-' * div_length))
        self.file.write(basic_template)

    def __exit__(self):
        self.file.close()

class ChecklistItem:
    'Checklist item to be run by a ChecklistDriver'

    def __init__(self):
        self.prompt = None # Prompt to be used in prompt_user_action and log_to_file

    def run_initial_actions(self):
        'Actions to perform before prompting user for response'
        pass

    def run_mid_actions(self):
        'Actions to perform after prompting user, but before logging'
        pass

    def run_post_actions(self):
        'Actions to perform after all other actions complete'
        pass

    def prompt_user_action(self):
        raise Exception('prompt_user_action *must* be overloaded, it\'s the core functionality of a checklist item!')

    def log_to_file(self, out_file):
        out_file.write('Completed at {ts}'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%s')))

    def run(self, out_file, num):
        self.run_initial_actions()
        self.prompt_user_action()
        self.run_mid_actions()
        with ChecklistLog(out_file, num) as out:
            self.log_to_file(out)
        self.run_post_actions()
