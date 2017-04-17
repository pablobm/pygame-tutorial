#!/usr/bin/env python
import io
import os
import re
import shutil
import sys

from bs4 import BeautifulSoup
import markdown
import pystache


ASSETS_DIR = 'assets'
LESSONS_DIR = 'lessons'
LESSONS_PATTERN = LESSONS_DIR + '/\d+-[^/]+'
LESSON_TEXT_FILE = 'text.md'
LAYOUT_PATH = LESSONS_DIR + '/layout.html.mustache'
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
            build_lesson(src, dst, layout=LAYOUT_PATH)

    copy_assets(ASSETS_DIR, OUTPUT_DIR)


#
# Plumbing
#

def build_lesson(src, dst, layout=None):
    if layout == None:
        raise TypeError("`layout` is a required argument")

    dst_with_ext = dst + '.html'
    dst_dir = os.path.dirname(dst)
    os.makedirs(dst_dir, mode=0o755, exist_ok=True)

    lesson_html_stream = io.BytesIO()
    markdown.markdownFromFile(input=src, output=lesson_html_stream, extensions=['pymdownx.superfences'])
    lesson_html = lesson_html_stream.getvalue()
    layout_view = {
        'contents': lesson_html,
        'title': extract_title(lesson_html),
    }

    layout_renderer = pystache.Renderer()
    final_file = layout_renderer.render_path(layout, layout_view)
    with open(dst_with_ext, 'w') as f:
        f.write(final_file)

def copy_assets(src, dst):
    for entry in os.listdir(src):
        src_path = src + '/' + entry
        dst_path = dst + '/' + entry
        if os.path.isdir(src_path):
            shutil.copytree(src_path, dst_path)
        else:
            shutil.copy2(src_path, dst_path)

def extract_title(lesson_html):
    soup = BeautifulSoup(lesson_html, 'html.parser')
    return soup.h1.get_text()


#
# Entry point
#

def main(command, *args):
    if command == 'build':
        build()

if __name__ == '__main__':
    main(*sys.argv[1:])
