import marshal
import dis
magic = b'a\r\r\n\x00\x00\x00\x00\xf6\x971a\x00\x00\x00\x00'
[::-1]))))
with open('test.pyc', 'wb') as pyc:
    pyc.write(magic)
    marshal.dump(dis.Bytecode(x).codeobj, pyc)
