import argparse
import collections, pickle
import os.path
import sys
import time
from getpass import getuser

DATA = "/home/{}/.wat/wat.dat".format(getuser())

class it(object):
    def __init__(self, what, urgency="NORMAL"):
        self.what = what
        self.created = time.asctime()
        self.urgency = urgency

    def __str__(self):
        return "{} - {} - {}".format(self.created, self.urgency, self.what)

def load_it(name):
    if os.path.isfile(name):
        with open(name) as f:
            this = pickle.load(f)
            if isinstance(this, collections.deque):
                return this
            else:
                print "Whoa dog seems to be corrupted"
                sys.exit( 1)
    else:
        return collections.deque()

def save_it(this, name):
    with open(name, 'w+') as f:
        pickle.dump(this, f)

def new():
    task = raw_input("WHAT? ")
    print "Urgency:"
    while True:
        print "1. HIGH"
        print "2. MEDIUM"
        print "3. LOW"
        a = raw_input ("(3): ")
        if not a:
            return it(task, "LOW")
        if a == '1':
            return it(task, "HIGH")
        elif a == '2':
            return it(task, "MEDIUM")
        elif a == '3':
            return it(task, "LOW")
        else:
            print "Invalid Input"

def empty_it(args):
    os.remove(DATA)

def do_it(args):
    this = load_it(DATA)
    if args.thing:
        thing = it(args.thing)
    else:
        thing = new()
    print thing
    this.append(thing)
    save_it(this, DATA)

def what_do(args):
    this = load_it(DATA)
    if args.p:
        try:
            print this.pop()
            save_it(this, DATA)
        except IndexError:
            print "Nothing to do..."
    else:
        if not this:
            print "Nothing to do..."
            return
        for thing in this:
            print thing


def main():
    parser = argparse.ArgumentParser(description='A simple tast list.')
    subparsers = parser.add_subparsers()
    what = subparsers.add_parser('wat', help='Wat do?')
    what.add_argument('-p', action='store_true', help='Pop the most recent element')
    what.set_defaults(func=what_do)
    do = subparsers.add_parser('do', help='Do!')
    do.set_defaults(func=do_it)
    do.add_argument('thing', nargs='?', default=None, help="Do this thing!")
    empty = subparsers.add_parser('empty', help="Clean it all out")
    empty.set_defaults(func=empty_it)
    args = parser.parse_args()
    args.func(args)

if __name__ == '__main__':
    main()
