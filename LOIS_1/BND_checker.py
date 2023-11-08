from typing import List


class BND_checker_set:
    def __init__(self, data: str) -> None:
        self.data = data
        self.data = self.data
        self.used_name = []
        self.iterator: int = 0
        self.is_valid = True
        self.fact()

    def fact(self):
        self.name_set()
        self.expect('=')
        self.expect('{')
        if self.next() == '}':
            if self.iterator == len(self.data):
                return
        self.iterator -= 1
        self.list_pair()

    def name_set(self):
        self.symbol()
        self.used_name.pop()
        self.expect('(')
        self.symbol()
        self.used_name.pop()
        self.expect(')')

    def next(self) -> str:
        if self.iterator == len(self.data):
            self.is_valid = False
            return ' '
        self.iterator += 1
        return self.data[self.iterator-1]

    def expect(self, token: str):
        if self.iterator == len(self.data):
            self.is_valid = False
            return
        if self.next() == token:
            return
        else:
            self.is_valid = False
            return

    def list_pair(self):
        self.pair()
        if self.is_valid == False:
            return
        if self.next() == '}':
            return
        else:
            self.iterator -= 1
        self.expect(',')
        self.list_pair()

    def digit(self):
        while self.next() in '01234567890':
            pass
        else:
            self.iterator -= 1

    def number(self):
        self.real_number()

    def one(self):
        self.expect('1')
        if self.next() == '.':
            self.expect('0')
        else:
            self.iterator-=1

    def real_number(self):
        if self.next() == '0':
            if self.next() == ')':
                self.iterator -= 1
            else:
                self.iterator -= 1
                self.expect('.')
                self.digit()
        else:
            self.iterator -= 1
            self.one()

    def pair(self):
        self.expect('(')
        self.symbol()
        self.expect(',')
        self.number()
        self.expect(')')

    def symbol(self):
        name = self.next()
        if name not in 'abcdefghijklmnopqrstuvwxyz':
            self.is_valid = False
            return
        while self.next() in 'abcdefghijklmnopqrstuvwxyz':
            self.iterator -= 1
            name += self.next()
        else:
            if name not in self.used_name:
                self.used_name.append(name)
            else:
                self.is_valid = False
                return
            self.iterator -= 1


class BND_checker_function:
    def __init__(self, data: str) -> None:
        self.data = data
        self.data = self.data
        self.iterator: int = 0
        self.is_valid = True
        self.function()

    def function(self):
        self.name_function()
        self.expect('=')
        self.expect('(')
        self.rule()
        self.expect(')')

    def rule(self):
        self.symbol()
        self.expect('(')
        self.symbol()
        self.expect(')')
        self.expect('~')
        self.expect('>')
        self.symbol()
        self.expect('(')
        self.symbol()
        self.expect(')')

    def name_function(self):
        self.symbol()
        # self.used_name.pop()
        self.expect('(')
        self.symbol()
        self.expect(',')
        self.symbol()
        # self.used_name.pop()
        self.expect(')')

    def next(self) -> str:
        self.iterator += 1
        return self.data[self.iterator-1]

    def expect(self, token: str):
        if self.iterator == len(self.data):
            self.is_valid = False
            return
        if self.next() == token:
            return
        else:
            self.is_valid = False
            return

    def symbol(self):
        if self.iterator == len(self.data):
            return
        name = self.next()
        if name not in 'abcdefghijklmnopqrstuvwxyz':
            self.is_valid = False
            return
        self.iterator -= 1
        while self.next() in 'abcdefghijklmnopqrstuvwxyz':
            self.iterator -= 1
            name += self.next()
        self.iterator -= 1


# str = 'p(x)={(a,0),(b,0.3),(c,1.0)}'
# a = BND_checker_set(str)
# print(a.is_valid)

# str = 'f(x,y)=(p(x)~>v(y))'
# a = BND_checker_function(str)
# print(a.is_valid)
