from __future__ import absolute_import, division, print_function
from __py2to3__.builtins_overrides import *
import sys


def make_comment():
    print('Comment:')
    return sys.stdin.read()


ACTIONS = {
    'DONE': lambda: 'done',
    'COMMENT': make_comment,
    'REVIEWER': lambda: input('Reviewer: '),
    'IMPORTANCE': lambda: input('Importance Level: '),
}
