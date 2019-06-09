
class Operacion:
    
    def __init__(self, id, identLevel, keys, description, action):
        self.id = id 
        self.identLevel = identLevel
        self.keys = keys
        self.description = description

    def __str__(self):
        return (("  " * self.identLevel) + ("%s - %s" % (self.keys, self.description)))