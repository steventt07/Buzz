import falcon
import sys
import psycopg2.extras
from datetime import datetime
from falcon.http_status import HTTPStatus
from app.queries import QUERY_CHECK_CONNECTION, QUERY_GET_USER, QUERY_INSERT_USER

class UseryService:
    def __init__(self, service):
        print('Initializing User Service...')
        self.service = service

    def on_get(self, req, resp):
        print('HTTP GET: /user')
        cursor = self.service.dbconnection.connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute(QUERY_GET_USER)
        response = []
        for record in cursor:
            response.append(
                {
                    'username': record[0],
                    'date_joined': record[1]
                }
            )

        resp.status = falcon.HTTP_200
        resp.media = { 'user': response}
        cursor.close()
		
	def on_post(self, req, resp):
        con = self.service.dbconnection.connection
        try:
            print('HTTP POST: /user')
            cursor = con.cursor()
            print(req.media)
            cursor.execute(QUERY_INSERT_USER, (
                req.media['username'],
				req.media['password'],
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