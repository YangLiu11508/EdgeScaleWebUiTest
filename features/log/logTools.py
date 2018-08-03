#-*-coding:utf-8-*-

def save(filename, contents):
    fh = open(filename, 'w', 'utf-8')
    fh.write(contents)
    fh.close()
