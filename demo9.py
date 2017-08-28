class Foo(object):
    def __str__(self):
        return 'string  表示'

    def __repr__(self):
        return 'representation 表示'


print('%s, %r' % (Foo(), Foo()))
print('{0!s}, {0!r},{0!a}'.format(Foo()))
