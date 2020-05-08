import click
import os


@click.group(invoke_without_command = False)
def base():
    '''
    A tool for maintaining your Machine Learning experiments in a systematic order.
    '''
    pass