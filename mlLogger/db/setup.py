import os
import json

from mysql import connector


config = dict()
config_present = True

try:
    config = json.loads(open(os.environ['HOME']+'/mlLogger-config.json').read())

except FileNotFoundError:
    print('Install Mysql plugins : ')
    user = input('username (root) : ')
    if user.lower() in ['y','','\n']:
        user = 'root'
    password = input(f'password for {user} : ')
    host = input('host (localhost) : ')
    if host.lower() in ['\n','','y'] :
        host = '127.0.0.1'
    config = {'user':user, 'host':host, 'password':password, 'database':'mlLogger'}
    config_present = False

try:
    connection = connector.connect(**config)
    cursor = connection.cursor()

except connector.Error as err:
    if err.errno == 1049:
        print('Database `mlLogger` not found. Creating database mlLogger ...')
        connection = connector.connect(user = config['user'], password = config['password'], host = config['host'])
        cursor = connection.cursor()
        cursor.execute('CREATE DATABASE mlLogger;')
        cursor.execute('USE mlLogger;')
        cursor.execute('CREATE TABLE Workspaces (name VARCHAR(255) NOT NULL, createdon DATE, path VARCHAR(1000), PRIMARY KEY(name));')
        connection = connector.connect(**config)
    else:
        print(f'Ended with error code : {err.errno}')
        raise err

