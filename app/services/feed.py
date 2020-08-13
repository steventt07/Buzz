import falcon
import base64
import sys
import psycopg2.extras
from datetime import datetime
from falcon.http_status import HTTPStatus
from app.queries import QUERY_CHECK_CONNECTION, QUERY_GET_FEED

class FeedService:
	def __init__(self, service):
		print('Initializing Feed Service...')
		self.service = service

	def on_get(self, req, resp):
		print('HTTP GET: /feed')
		cursor = self.service.dbconnection.connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
		print(req.params)
		cursor.execute(QUERY_GET_FEED, (req.params['zipcode'], ))
		response = []
		for record in cursor:
			response.append(
				{
					'post_id': record[0],
					'username': record[1],
					'category_name': record[2],
					'content': record[3],
					'comments': record[4],
					'votes': record[5],
					'zipcode': record[6],
					'date_created': str(record[7]),
				}
			)

		resp.status = falcon.HTTP_200
		resp.media = { 'feed': response}
		cursor.close()