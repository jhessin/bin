import os.path
import sys
import subprocess

f_path, f_name = os.path.split(sys.argv[0])
home = os.environ.get('HOME')

template = """#!/usr/bin/env python3
import os.path
import sys
import subprocess

f_path, f_name = os.path.split(sys.argv[0])
home = os.environ.get('HOME')

def usage():
    print(f"{f_name} <insert-args-here>")
    exit(1)


if len(sys.argv) < 2:
    usage()
"""


def new_script(path):
    if os.path.isfile(path):
        subprocess.run(["nvim", path])
    else:
        file = open(path, "w")
        file.write(template)
        file.close()
        subprocess.run(["chmod", "a+x", path])
        subprocess.run(["nvim", path])
