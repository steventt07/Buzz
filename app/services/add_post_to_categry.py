import falcon
import base64
import sys
import psycopg2.extras
from datetime import datetime
from falcon.http_status import HTTPStatus
from app.queries import QUERY_CHECK_CONNECTION, QUERY_INSERT_POST_TO_CATEGORY

class AddPostService:
    def __init__(self, service):
        print('Initializing Add Post To Category Service...')
        self.service = service

    def on_post(self, req, resp):
        con = self.service.dbconnection.connection
        try:
            print('HTTP POST: /add_post_to_category')
            cursor = con.cursor()
			print(req.media)
            cursor.execute(QUERY_INSERT_POST_TO_CATEGORY, (
                req.media['username'],
                req.media['category_name'],
				req.media['content'],
				req.media['content'],
				req.media['zipcode'],
                datetime.now()
                )
            )
            con.commit()

            resp.status = falcon.HTTP_200

        except psycopg2.DatabaseError as e:
            if con:
                con.rollback()
            print ('Error %s' % e ) 
            sys.exit(1)
        finally: 
            if cursor:
                cursor.close()