class Queue(object):
    l = []

    def push(self, v):
        self.l.append(v)

    def peek(self):
        if len(self.l) > 0:
            return self.l[0]
        else:
            return None

    def pop(self):
        if len(self.l) > 0:
            return self.l.pop(0)
        else:
            return None
