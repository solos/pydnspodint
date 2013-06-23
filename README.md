# pydnspodint

#About

pydnspodint is a python sdk of dnspod international version(https://www.dnspod.com/ncr).


#Usage

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
