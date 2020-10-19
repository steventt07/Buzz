import falcon
import base64
import sys
import psycopg2.extras
from datetime import datetime, timezone
from falcon.http_status import HTTPStatus
from app.queries import QUERY_CHECK_CONNECTION, QUERY_GET_FEED

class FeedService:
	def __init__(self, service):
		print('Initializing Feed Service...')
		self.service = service

	def on_get(self, req, resp):
		print('HTTP GET: /feed')
		print(req.params)
		
		self.service.dbconnection.init_db_connection()
		con = self.service.dbconnection.connection
		cursor = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
		cursor.execute(QUERY_GET_FEED, (req.params['username'], req.params['zipcode']))
		
		response = []
		for record in cursor:
			response.append(
				{
					'id': record[0],
					'username': record[1],
					'category_name': record[2],
					'title': record[3],
					'content': record[4],
					'votes': record[5],
					'is_voted': record[6],
					'prev_vote': record[7],
					'zipcode': record[8],
					'date_created': str(record[9]),
					'comments': record[10]
				}
			)
			
		cursor.close()
		con.close()
		
		resp.status = falcon.HTTP_200
		resp.media = response