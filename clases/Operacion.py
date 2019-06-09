
class Operacion:
    
    def __init__(self, id, keys, description):
        self.id = id
        self.keys = keys
        self.description = description

    def __str__(self):
        return "%s - %s" % (self.keys, self.description)