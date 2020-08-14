import falcon
import base64
import sys
import psycopg2.extras
from datetime import datetime
from falcon.http_status import HTTPStatus
from app.queries import QUERY_CHECK_CONNECTION, QUERY_GET_CATEGORY

class CategoryService:
	def __init__(self, service):
		print('Initializing Category Service...')
		self.service = service

	def on_get(self, req, resp):
		print('HTTP GET: /category')
		cursor = self.service.dbconnection.connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
		cursor.execute(QUERY_GET_CATEGORY, (req.params['category_name'], req.params['zipcode']))
		response = []
		for record in cursor:
			print(record)
			response.append(
				{
					'post_id': record[0],
					'username': record[1],
					'category_name': record[2],
					'title': record[3],
					'content': record[4],
					'comments': record[5],
					'up_vote': record[6],
					'down_vote': record[7],
					'zipcode': record[8],
					'date_created': str(record[9]),
				}
			)

		resp.status = falcon.HTTP_200
		resp.media = { 'category': response}
		cursor.close()