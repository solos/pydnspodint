#!/usr/bin/env python
#coding=utf-8

from pydnspodint import pydnspodint

### user info ###
email = ''
password = ''

### cookie ###
api = pydnspodint.Api(email, password)
cookie = api.get_cookie()

### domain ###
domain = pydnspodint.Domain(email, password, cookie=cookie)
print domain.list()

#print domain.create(domain='stestag.com')
#print domain.able(domain='stestag.com', status='disable')
#print domain.delete(domain='stestag.com') #todo error handle
#print domain.search(term='tag') #todo error handle

### group ###
#group = pydnspodint.Group(email, password, cookie=cookie)
#print group.add(group='hellowr')
#print group.modify(group='hellowr', domain='stestag.com')
#print group.remove(group='hellowr', domain='stestag.com')

### record ###
#record = pydnspodint.Record(email, password, cookie=cookie)
#print record.list(domain='stestag.com')
#print record.add(domain='stestag.com', sub_domain='test', area='0',
#                 record_type='A', value='1.2.2.1', ttl=100)
#print record.add(domain='stestag.com', sub_domain='add', area='0',
#                 record_type='A', value='1.2.2.1', ttl=600)
#print record.add(domain='stestag.com', sub_domain='tadd', area='0',
#                 record_type='A', value='1.2.2.1')
#print record.able(domain='stestag.com', record_id=189010,
#                   status='disable')
#print record.modify(domain='stestag.com', record_id=189010,
#                    sub_domain='add', area='0', record_type='A',
#                    value='2.2.2.2', ttl=200)
