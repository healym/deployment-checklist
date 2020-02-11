#! /usr/bin/python3

from checklist import Checklist, checklist_args


if __name__ == '__main__':
    checklist = Checklist(checklist_args())
    checklist.run()
