#!/usr/bin/env python
#coding=utf-8

import urllib2


class Request(object):

    def __init__(self):
        self.method = None
        self.url = None
        self.data = None
        self.headers = {}
        self.cookies = None

    def request(self, method, url, data=None, headers={}, cookies=None):

        if cookies:
            headers.update({'Cookie': cookies})
        r = urllib2.Request(url, data=data, headers=headers)
        r.get_method = lambda: method.upper()
        try:
            return urllib2.urlopen(r).read()
        except urllib2.HTTPError, error:
            return error.read()

    def head(self, url, **kwargs):
        return self.request('HEAD', url, **kwargs)

    def get(self, url, **kwargs):
        return self.request('GET', url, **kwargs)

    def post(self, url, data=None, **kwargs):
        return self.request('POST', url, data=data, **kwargs)

    def put(self, url, data=None, **kwargs):
        return self.request('PUT', url, data=data, **kwargs)

    def delete(self, url, **kwargs):
        return self.request('DELETE', url, **kwargs)

if __name__ == '__main__':
    r = Request()
    print r.get('http://solos.so')
