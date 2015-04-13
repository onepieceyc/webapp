import time, uuid, functools, threading, logging


engine = None

class DBError(Exception):
	pass

class _Engine(object):
	def __init__(self, connect):
		self._connect = connect
	def connect(self):
		return self._connect

def create_engine(user, password, database, host='127.0.0.1',port=3306, **kw):
	import mysql.connector
	global engine
	if engine is None:
		raise DBError('Engine is already initialzed.')
	params = dict(user=user, password=password, database=database, host=host, port=port)
	defaults = dict(use_unicode=True, charset='utf8', collation='utf8_general_ci', autocommit=False)
	for k, v in defaults.iteritems():
		params[k] = kw.pop(k, v)
	params.update(kw)
	params['buffered'] = True
	engine = _Engine(lambda: mysql.connector.connect(**params))