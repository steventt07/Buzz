import falcon
import base64
import sys
import psycopg2.extras
from datetime import datetime, timezone
from falcon.http_status import HTTPStatus
from app.queries import QUERY_CHECK_CONNECTION, QUERY_UPDATE_EMAIL_VERIFICATION

class EmailValidationService:
	def __init__(self, service):
		print('Initializing Email Validation Service...')
		self.service = service

	def on_get(self, req, resp):
		print('HTTP GET: /email_validation')
		
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
		
		resp.status = falcon.HTTP_200
		resp.media = response
		
	def on_post(self, req, resp):
		self.service.dbconnection.init_db_connection()
		con = self.service.dbconnection.connection
		try:
			print('HTTP POST: /email_validation')
			cursor = con.cursor()
			print(req.media)
			cursor.execute(QUERY_UPDATE_EMAIL_VERIFICATION, (
				req.media['email'],
				req.media['validation_code']
				)
			)
			rowcount = cursor.rowcount
			con.commit()

			if rowcount == 0:
				resp.status = falcon.HTTP_400
				resp.media = 'Invalid validation code'
			else:
				resp.status = falcon.HTTP_200
				resp.media = 'Successful validation of : {}'.format(req.media['email'])

		except psycopg2.DatabaseError as e:
			if con:
				con.rollback()
			print ('Error %s' % e ) 
			raise falcon.HTTPBadRequest('Database error', str(e))
		finally: 
			if cursor:
				cursor.close()
			if con:
				con.close()
		