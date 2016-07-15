class Stoplight(object):
    def __init__(self, code):
        self.inputs = []
        self.code = code

    def push(self, val):
        self.inputs.append(val)

    def get(self):
        return ''.join(self.inputs)

    def validate(self):
        calculated = ''.join(self.inputs)
        return calculated == self.code

    def reset(self):
        self.inputs = []
