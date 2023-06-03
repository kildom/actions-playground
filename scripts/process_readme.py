

import html
from pathlib import Path
import re

include_re = r'(<!--! (.+) !-->)(\r?\n)[\S\s]*?\r?\n(<!--! !-->)'

def ansi_to_html(text):
    text = html.escape(text)
    text = (text
            .replace('[0m', '</span>')
            .replace('[32m', '<span style="color: #0A0">')
            .replace('[35m', '<span style="color: #D0D">')
            .replace('[90m', '<span style="color: #888">')
           )
    return text

def ansi_to_plain(text):
    text = (text
            .replace('[0m', '')
            .replace('[32m', '')
            .replace('[35m', '')
            .replace('[90m', '')
           )
    return text

def replace_by_file_html(m: re.Match) -> str:
    file = m.group(2).strip()
    text = Path(file).read_text()
    return m.group(1) + m.group(3) + '<pre style="background-color: #222; min-width: 80ch">' + m.group(3) + ansi_to_html(re.sub(r'^[\r\n\s]*\r?\n', '', text.rstrip())) + m.group(3) + '</pre>' + m.group(3) + m.group(4)

def replace_by_file(m: re.Match) -> str:
    file = m.group(2).strip()
    text = Path(file).read_text()
    return m.group(1) + m.group(3) + '```' + m.group(3) + ansi_to_plain(re.sub(r'^[\r\n\s]*\r?\n', '', text.rstrip())) + m.group(3) + '```' + m.group(3) + m.group(4)

def process_file(filename: 'Path|str'):
    text = Path(filename).read_text()
    text = re.sub(include_re, replace_by_file, text)
    Path(filename).write_text(text)

process_file('README.md')
