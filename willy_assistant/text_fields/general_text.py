
import re
import ast
import pathlib
import pkg_resources

# Take name and version from METADATA
version = pkg_resources.get_distribution('willy').version
name = pkg_resources.get_distribution('willy').project_name
class GeneralText:

    start_message = \
    '\n{:^40}\n{:^40}\n'.format('---HELLO---', '-'*40)+\
    '|{:^38}|\n'.format(f"I'M {name} ASSISTANT {version}")+\
    '|{:^38}|\n{:^40}\n'.format("NICE TO MEET YOU!", '-'*40)
    continue_input_message = 'Press enter to continue.\n>>> '
    wrong_input_message = '\nHmm.. Somesing wrong. Try again.\n'
