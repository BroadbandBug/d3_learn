
import datetime
import json
import numpy as np
from numpy.fft import fft, fftfreq
import random
import time

import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado import websocket

def test_fft():
    freqs = np.arange(0,512,1.)
    random.shuffle( freqs )
    freq_list = freqs.tolist()
    return freq_list

class EchoWebSocket( websocket.WebSocketHandler ):
    def open( self ):
        print "WebSocket opened"
        self.closed = False
        self.data()

    def on_message( self, message ):
        print 'Received message: %s' % message

    def close( self ):
        self.closed = True
        time.sleep( 1.1 )
        websocket.WebSocketHandler.close( self )

    def on_close( self ):
        print "WebSocket closed"

    def data( self ):
        absfreq = test_fft()
        message = json.dumps(absfreq)

        try:
            self.write_message(message)
        except websocket.WebSocketClosedError:
            return

        ioloop_instance = tornado.ioloop.IOLoop.instance()
        ioloop_instance.add_timeout(datetime.timedelta(seconds=1), self.data)

def main( ):

    application = tornado.web.Application([
        (r'/ws', EchoWebSocket),
    ])

    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()

