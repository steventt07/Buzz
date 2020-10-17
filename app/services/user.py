import falcon
import sys
import psycopg2.extras
from datetime import datetime
from falcon.http_status import HTTPStatus
from app.queries import QUERY_CHECK_CONNECTION, QUERY_GET_USER, QUERY_INSERT_USER

class UserService:
	def __init__(self, service):
		print('Initializing User Service...')
		self.service = service

	def on_get(self, req, resp):
		print('HTTP GET: /user')
		
		self.service.dbconnection.init_db_connection()
		cursor = self.service.dbconnection.connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
		cursor.execute(QUERY_GET_USER, (req.params['username'], req.params['password']))
		response = []
		for record in cursor:
			response.append(
				{
					'username': record[0],
					'email': record[1],
					'date_joined': str(record[2])
					
				}
			)
		cursor.close()
		
		if len(response) == 0:
			resp.status = falcon.HTTP_400
		else:
			resp.status = falcon.HTTP_200
			resp.media = { 'user': response}
		
	def on_post(self, req, resp):
		self.service.dbconnection.init_db_connection()
		con = self.service.dbconnection.connection
		try:
			print('HTTP POST: /user')
			cursor = con.cursor()
			print(req.media)
			cursor.execute(QUERY_INSERT_USER, (
				req.media['username'],
				req.media['password'],
				req.media['email'],
				datetime.now()
				)
			)
			con.commit()

			resp.status = falcon.HTTP_200
			resp.media = 'Successful creation of user: {}'.format(req.media['username'])

		except psycopg2.DatabaseError as e:
			if con:
				con.rollback()
			print ('Error %s' % e ) 
			sys.exit(1)
		finally: 
			if cursor:
				cursor.close()
			if con:
				con.close()