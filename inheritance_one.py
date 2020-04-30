# 13-inheriting-init-constructor

class Python(object):
    def __init__(self, name):
        self.name = name


class Django(Python):
    def fetch(self, thing):
        print('%s goes after the %s' % (self.name, thing))

d = Django("Roger")
print ("The  name is", d.name)
d.fetch("frizbee")

