from http.server import HTTPServer, BaseHTTPRequestHandler
from datetime import datetime
import json
import redis
import uuid

# connect to redis
redisClient = redis.Redis(host='localhost', port=6379)


class ServiceHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        currentTimestamp = str(datetime.now())
        simpleUUID = uuid.uuid1()

        redisClient.hset('uuid', currentTimestamp, str(simpleUUID.hex))
        finalData = redisClient.hgetall('uuid')

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(finalData))

        # self.wfile.write(json.dumps(finalData).encode())


# Server Initialization
server = HTTPServer(('localhost', 8080), ServiceHandler)
server.serve_forever()
