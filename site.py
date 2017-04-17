#!/usr/bin/env python
import os
import re
import shutil
import sys

import markdown

LESSONS_DIR = 'lessons'
LESSONS_PATTERN = LESSONS_DIR + '/\d+-[^/]+'
LESSON_TEXT_FILE = 'text.md'
OUTPUT_DIR = 'output'


#
# Porcelain
#

def build():
    if os.path.exists(OUTPUT_DIR):
        shutil.rmtree(OUTPUT_DIR)

    for path, _, files in os.walk(LESSONS_DIR):
        match = re.search(LESSONS_PATTERN, path)
        if match and LESSON_TEXT_FILE in files:
            lesson_name = match.group(0)
            src = match.group(0) + '/' + LESSON_TEXT_FILE
            dst = OUTPUT_DIR + '/' + lesson_name
            build_lesson(src, dst)


#
# Plumbing
#

def build_lesson(src, dst):
    dst_with_ext = dst + '.html'
    dst_dir = os.path.dirname(dst)
    os.makedirs(dst_dir, mode=0o755, exist_ok=True)
    markdown.markdownFromFile(input=src, output=dst_with_ext)


#
# Entry point
#

def main(command, *args):
    if command == 'build':
        build()

if __name__ == '__main__':
    main(*sys.argv[1:])
