import logging
import sys


def config():
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)


COMMENT = '# '
LOGGER = 'logger'


def is_commented(line):
    return line.lstrip().startswith(COMMENT)


def comment(line, pos):
    return line[:pos] + COMMENT + line[pos:]


def comment_logging(line):
    return comment(line, line.find(LOGGER))


def uncomment(line):
    return line.replace(COMMENT, '')


def is_logging(line):
    return LOGGER in line


def set_logging(log):
    with open('verbose.py', 'r') as f:
        lines = list(f)
    for i in range(len(lines)):
        if is_logging(lines[i]):
            if log and is_commented(lines[i]):
                lines[i] = uncomment(lines[i])
            if not log and not is_commented(lines[i]):
                lines[i] = comment_logging(lines[i])
    with open('verbose.py', 'w') as f:
        f.writelines(lines)
