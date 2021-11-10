#!/usr/bin/env pipenv-shebang
import subprocess
import os
import common
from yachalk import chalk


def traverse(path):
    print(f"traversing {chalk.green(path)}")
    for directory in os.listdir(path):
        full_path = path + '/' + directory
        if os.path.isdir(full_path):
            os.chdir(full_path)
            print(f"updating {chalk.green(full_path)}")
            result = subprocess.run(['git', 'status', '-s'],
                                    capture_output=True)
            if len(result.stdout) != 0:
                subprocess.run(['gitui'])


def sync(path):
    os.chdir(path)
    print(f"updating {chalk.green(path)}")
    result = subprocess.run(['git', 'status', '-s'],
                            capture_output=True)
    if len(result.stdout) != 0:
        subprocess.run(['gitui'])


sync(common.home + '/.local/bin')

sync(common.home + '/.config')

sync(common.home)

print(f"updating {chalk.green('Github repos')}")
traverse(common.home + '/Projects')

common.nvim_install()
common.clean_undo()
