""" Common functions and variables for use in other scripts """
import os
import sys
import subprocess

f_path, f_name = os.path.split(sys.argv[0])
home = os.environ.get('HOME')

TEMPLATE = """#!/usr/bin/env python3
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
    """ Generate a new script in the given path """
    if os.path.isfile(path):
        subprocess.run(["nvim", path], check=True)
    else:
        with open(path, 'w', encoding='utf-8') as file:
            file.write(TEMPLATE)
        subprocess.run(["chmod", "a+x", path], check=True)
        subprocess.run(["nvim", path], check=True)


def clean_undo():
    """ Clean neovim's undo files """
    subprocess.run(['rm', '-rf', '~/.tmp/undo'], check=True)


def nvim_install():
    """ Install neovim plugins """
    subprocess.run([
        'nvim', '+CocInstall', '+PlugClean!', '+PlugInstall',
        '+UpdaUpdateRemotePlugins', '+qall'
    ],
                   check=True)
