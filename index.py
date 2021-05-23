from http.server import HTTPServer, BaseHTTPRequestHandler
from datetime import datetime
import json
import redis
import uuid

# connect to redis
redisClient = redis.Redis(host='localhost', port=6379,
                          charset="utf-8", decode_responses=True)


class ServiceHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_GET(self):
        currentTimestamp = str(datetime.now())
        simpleUUID = uuid.uuid1()

        redisClient.hset('uuid-set', currentTimestamp, simpleUUID.hex)
        finalData = redisClient.hgetall('uuid-set')

        self._set_headers()
        self.wfile.write(json.dumps(finalData).encode('utf-8'))


# Server Initialization
def run():
    server_address = ('localhost', 5000)
    httpd = HTTPServer(server_address, ServiceHandler)
    print('serving at %s:%d' % server_address)
    httpd.serve_forever()


run()
