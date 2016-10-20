from ansible import errors

def uppercase_all(txt):
    return txt.upper()


class FilterModule(object):
    def filters(self):
        return {'uppercase_all': uppercase_all}