import falcon
import sys
import psycopg2.extras
from falcon.http_status import HTTPStatus
from app.queries import QUERY_CHECK_CONNECTION, QUERY_REMOVE_POST_FROM_CATEGORY

class RemovePostService:
    def __init__(self, service):
        print('Initializing Remove Post From Category Service...')
        self.service = service

    def on_post(self, req, resp):
        con = self.service.dbconnection.connection
        try:
            print('HTTP POST: /remove_post_from_category')
            cursor = con.cursor()
            print(req.media)
            cursor.execute(QUERY_REMOVE_POST_FROM_CATEGORY, (
                req.media['post_id']
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