import sys


def done():
    print('done')
    return 'done'


def make_comment():
    print('Reason:')
    return sys.stdin.read()


ACTIONS = {
    'DONE': done,
    'COMMENT': make_comment
}
