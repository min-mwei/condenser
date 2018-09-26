import json, sys

_config = None

def initialize(file_like = None):
    global _config
    if _config != None:
        print('Attempted to initialize configuration twice.')
        sys.exit(1)

    if not file_like:
        with open('config.json', 'r') as fp:
            _config = json.load(fp)
    else:
        _config = json.load(file_like)

def get_passthrough_threshold():
    return _config['passthrough_threshold']

def get_dependency_breaks():
    return list(_config['dependency_breaks'])

def get_target_table():
    return _config['desired_result']['schema'] + '.' + _config['desired_result']['table']

def get_target_percent():
    return _config['desired_result']['percent']

def get_max_tries():
    return _config['max_tries']

def get_source_db_connection_info():
    return _config['source_db_connection_info']

def get_destination_db_connection_info():
    return _config['destination_db_connection_info']

def get_excluded_tables():
    info = _config['excluded_tables']
    tables = list()
    for group in info:
        for t in group['tables']:
            tables.append(f"{group['schema']}.{t}")
    return tables

def get_passthrough_tables():
    info = _config['passthrough_tables']
    tables = list()
    for group in info:
        for t in group['tables']:
            tables.append(f"{group['schema']}.{t}")
    return tables
