import re

class RDR:
    def __init__(self, tokens, pos):
        self.tokens = tokens
        self.pos = pos

    def next(self):
        x = self.pos
        self.pos += 1
        return(self.tokens[x])

    def peek(self):
        return(self.tokens[self.pos])

def tokenize(inp):
    trx = re.compile(r"""[\s,]*(~@|[\[\]{}()'`~^@]|"(?:\\.|[^\\"])*"?|;.*|[^\s\[\]{}('"`,;)]*)""")
    return [t for t in re.findall(trx, inp) if t[0] != ';']
