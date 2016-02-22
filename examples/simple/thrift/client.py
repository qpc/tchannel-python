# Copyright (c) 2015 Uber Technologies, Inc.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import json

from tornado import gen
from tornado import ioloop
from threading import Thread

from tchannel import thrift
from tchannel.sync import TChannel

tchannel = TChannel('thrift-client')
service = thrift.load(
    path='tests/data/idls/ThriftTest.thrift',
    service='thrift-server',
    hostport='localhost:54497',
)


def make_request():
    
    resp = tchannel.thrift(
        request=service.ThriftTest.testString(thing="req"),
        headers={
            'req': 'header',
        },
    ).result()

    return resp

def run():
    resp = make_request()
    print resp

if __name__ == "__main__":
    threads = []
    for i in range(15):
        thread = Thread(target = run)
        threads.append(thread)
        thread.start()

    for thread in threads:
        print 'sss'
        thread.join()

