#!/usr/bin/env python
#coding=utf-8

from request import Request
import urllib
import json


class Api(object):

    def __init__(self, email, password, cookie='', **kw):

        self.base_url = "https://www.dnspod.com/api/"
        self.method = "GET"
        self._email = email
        self._password = password
        self._cookie = cookie
        self.required = ()
        self.optional = ()
        self._params = {}
        self._data = ''
        self.path = ''

    def _set_options(self, **kw):
        self.params = {
            'required': self.required,
            'optional': self.optional}
        flt = lambda (par, value): par in self.required or par in self.optional
        if self.method == 'GET':
            self._params = dict(filter(flt, kw.items()))
            self.path = "%s?%s" % (self.path, urllib.urlencode(self._params))
        else:
            self._data = json.dumps(dict(filter(flt, kw.items())))

    def _is_param_missing(self, **kw):
        for par in self.required:
            if par not in kw:
                print 'parameter missing: %s' % par
                return True
        return False

    def _request(self, **kw):

        self._set_options(**kw)

        if self._is_param_missing(**kw):
            return

        method = self.method
        cookie = self._cookie
        data = self._data
        r = Request()
        url = ''.join((self.base_url, self.path))
        if method != 'GET':
            if data:
                return r.request(method, url, cookies=cookie, data=data)
            else:
                return r.request(self.method, url, cookies=cookie)
        else:
            return r.request(self.method, url, cookies=cookie)

    def get_cookie(self, **kw):
        kw.update({'email': self._email, 'password': self._password})
        self.method = "GET"
        self.required = ('email', 'password')
        self.path = "auth"
        response = self._request(**kw)
        try:
            cookie = urllib.urlencode(json.loads(response))
        except:
            cookie = ''
        return cookie

    def set_cookie(self, cookie):
        self._cookie = cookie


class Domain(Api):

    def __init__(self, email, password, cookie=''):
        super(Domain, self).__init__(email, password, cookie=cookie)

    def create(self, **kw):
        self.path = "domains"
        self.method = "POST"
        self.required = ('domain',)
        return self._request(**kw)

    def list(self, **kw):
        self.path = "domains"
        self.optional = ('start', 'end', 'group')
        return self._request(**kw)

    def able(self, **kw):
        self.method = "PUT"
        self.required = ('status')
        self.path = "domains/%s" % kw['domain']
        return self._request(**kw)

    def delete(self, **kw):
        self.method = "DELETE"
        self.path = "domains/%s" % kw['domain']
        return self._request(**kw)

    def search(self, **kw):
        self.method = 'GET'
        self.required = ('term',)
        self.optional = ('length',)
        self.path = "search"
        return self._request(**kw)


class Group(Api):

    def __init__(self, email, password, cookie=''):
        super(Group, self).__init__(email, password, cookie=cookie)

    def list(self, **kw):
        self.path = "groups"
        return self._request(**kw)

    def add(self, **kw):
        self.method = "POST"
        self.required = ('group',)
        self.path = "groups"
        return self._request(**kw)

    def modify(self, **kw):
        self.method = "PUT"
        self.required = ('domain',)
        self.path = "groups/%s" % kw['group']
        return self._request(**kw)

    def remove(self, **kw):
        self.method = "DELETE"
        self.required = ('domain',)
        self.path = "groups/%s" % kw['group']
        return self._request(**kw)


class Record(Api):

    def __init__(self, email, password, cookie=''):
        super(Record, self).__init__(email, password, cookie=cookie)

    def list(self, **kw):
        self.method = "GET"
        self.path = "records/%s" % kw['domain']
        return self._request(**kw)

    def add(self, **kw):
        self.method = "POST"
        self.required = ('area', 'sub_domain', 'record_type', 'value')
        self.optional = ('mx', 'ttl')
        if 'ttl' not in kw:
            kw.update(ttl=600)
        self.path = "records/%s" % kw['domain']
        return self._request(**kw)

    def able(self, **kw):
        self.method = "PUT"
        self.required = ('status',)
        self.path = "records/%s/%s" % (kw['domain'], kw['record_id'])
        return self._request(**kw)

    def modify(self, **kw):
        self.method = "PUT"
        self.required = ('area', 'sub_domain', 'record_type', 'value')
        self.optional = ('mx', 'ttl')
        if 'ttl' not in kw:
            kw.update(ttl=600)
        self.path = "records/%s/%s" % (kw['domain'], kw['record_id'])
        return self._request(**kw)

if __name__ == '__main__':
    pass
