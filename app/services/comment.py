import falcon
import sys
import psycopg2.extras
from datetime import datetime
from falcon.http_status import HTTPStatus
from app.queries import QUERY_CHECK_CONNECTION, QUERY_INSERT_COMMENT, QUERY_GET_COMMENT

class CommentService:
	def __init__(self, service):
		print('Initializing Comment Service...')
		self.service = service
	
	def on_get(self, req, resp):
		print('HTTP GET: /comment')
		cursor = self.service.dbconnection.connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
		cursor.execute(QUERY_GET_COMMENT, (req.params['post_id'], ))
		response = []
		for record in cursor:
			response.append(
				{
					'comment_id': record[0],
					'username': record[1],
					'content': record[2],
					'date_created': str(record[3])
					
				}
			)
		
		if len(response) == 0:
			resp.status = falcon.HTTP_400
		else:
			resp.status = falcon.HTTP_200
			resp.media = { 'comment': response}
		cursor.close()
		
	def on_post(self, req, resp):
		con = self.service.dbconnection.connection
		try:
			print('HTTP POST: /comment')
			cursor = con.cursor()
			print(req.media)
			
			cursor.execute(QUERY_INSERT_COMMENT, (
					req.media['post_id'],
					req.media['username'],
					req.media['content'],
					datetime.now()
				)
			)
				
			con.commit()

			resp.status = falcon.HTTP_200
			resp.media = 'Successful comment of post: {}'.format(req.media['post_id'])

		except psycopg2.DatabaseError as e:
			if con:
				con.rollback()
			print ('Error %s' % e ) 
			sys.exit(1)
		finally: 
			if cursor:
				cursor.close()