from .base import base
import click
import os
import shutil
import json
import subprocess

from mlLogger.db import  cursor, connection
from mlLogger.cli.exceptions import WorkspaceExists, WorkspaceDoesNotExists


def ws_exists(ws_name):
    cursor.execute(f"SELECT * FROM Workspaces WHERE name = '{ws_name}'")
    output = cursor.fetchall()
    if len(output):
        return True
    return False


@base.group()
def workspace():
    '''
    Creating and managing your machine learning workspace
    '''
    pass


@workspace.command()
@click.option('--config',default=None, help='path of config file')
def create(config):
    '''
    Creates workspace. Requires come basic details about the workspace.
    You can pass it by console input or via passing a `config.json` file.
    '''
    path = os.getcwd()
    if config is None:
        config = os.path.join(path,'config.json')
    try:
        with open(config) as f:
            conf = json.load(f)

    except FileNotFoundError as err:
        conf = dict()
        conf['name'] = input('Enter the name of Workspace (It should be unique): ')
        conf['purpose'] = input('DL/ML (as per the library requirements): ').lower()
    
    conf['name'] = conf['name'].lower()
    
    if ws_exists(conf['name']):
        raise WorkspaceExists

    print('config.json :')
    print(json.dumps(conf, indent=4))
    
    ok = input('Are you sure about the above config? (Y/n) : ').lower()
    
    if ok == 'y' or ok == '':
        workpath = os.path.join(path,conf['name'])
        os.mkdir(workpath)
        process = subprocess.run(['virtualenv',workpath])
        if process.returncode:
            raise Exception('Ended with exitcode :',process.returncode)
        with open(workpath + '/config.json', 'w') as f:
            json.dump(conf,f,indent=4)
        cursor.execute(f"INSERT INTO Workspaces(name, createdon, path) VALUES ('{conf['name']}',NOW(),'{workpath}');")
        connection.commit()


@workspace.command()
@click.argument('ws_name')
def delete(ws_name):
    '''
    Deletes a workspace
    '''
    if not ws_exists(ws_name):
        raise WorkspaceDoesNotExists
    cursor.execute(f"SELECT path FROM Workspaces WHERE name='{ws_name}'")
    workpath = cursor.fetchone()[0]
    try:
        shutil.rmtree(workpath)
    except FileNotFoundError:
        pass
    cursor.execute(f"DELETE FROM Workspaces WHERE name='{ws_name}';")
    connection.commit()
    print(f"Workspace {ws_name} is deleted successfully.")


@workspace.command()
def show():
    cursor.execute("SELECT * FROM Workspaces;")
    outputs = cursor.fetchall()
    print('NAME  |  DATE CREATED  |  PATH')
    for out in outputs:
        out = map(str,list(out))
        print(' - '.join(out))
    