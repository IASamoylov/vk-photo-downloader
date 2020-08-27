import sys

from lib import Project, Options


def start(args):
    options = Options()
    options.parse(args)

    project = Project(options)

    project.run()


if __name__ == '__main__':
    start(sys.argv[1:])
