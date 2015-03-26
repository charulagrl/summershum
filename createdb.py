#!/usr/bin/python

## These  lines are needed to run on EL6
__requires__ = ['SQLAlchemy >= 0.8', 'jinja2 >= 2.4']
import os
import pkg_resources
import fedmsg.config

from summershum.model import create_tables

basedir = os.path.abspath(os.path.dirname(__file__))

create_tables(fedmsg.config.get('summershum.sqlalchemy.url') or 
	'sqlite:///' + os.path.join(basedir, 'summershum.db'), True)
