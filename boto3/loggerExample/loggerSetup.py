#!/usr/bin/env python
"""Setup logging module for use"""

import os
import logging
import logging.config
import yaml

home = os.path.expanduser('~')
logger_config = home + "/git-repos/rcrelia/aws-mojo/boto3/loggerExample/logger_config.yaml"
logger_debug_config = home + "/git-repos/rcrelia/aws-mojo/boto3/loggerExample/logger_config_debug.yaml"

def configure(default_path=logger_config, default_level=logging.DEBUG, env_key='LOG_CFG'):
    """Setup logging configuration"""
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)

def configure_debug(default_path=logger_debug_config, default_level=logging.DEBUG, env_key='LOG_CFG'):
    """Setup logging configuration for debugging"""
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)
