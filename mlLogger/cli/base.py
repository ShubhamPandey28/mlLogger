import click
import os

path = os.path.dirname(__file__)
    
requirements = dict()

requirements['ml'] = []
with open(os.path.join(path,'requirements/ml.txt')) as f:
    lines = f.readlines()
    for line in lines:
        requirements['ml'].append(line.strip())

requirements['dl'] = []
with open(os.path.join(path,'requirements/dl.txt')) as f:
    lines = f.readlines()
    for line in lines:
        requirements['dl'].append(line.strip())

@click.group(invoke_without_command = False)
def base():
    '''
    A tool for maintaining your Machine Learning experiments in a systematic order.
    '''
    pass