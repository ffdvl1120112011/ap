import marshal\nimport dis\nmagic = b'a\r\r\n\x00\x00\x00\x00\xf6\x971a\x00\x00\x00\x00'\n[::-1]))))\nwith open('test.pyc', 'wb') as pyc:\npyc.write(magic)\nmarshal.dump(dis.Bytecode(x).codeobj, pyc)
