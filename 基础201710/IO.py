import os
def list(path):
    for L in os.listdir(path):
        if os.path.isfile(L):
            print(L)
        elif os.path.isdir(L):
            print(' ')
            list(os.path.abspath(L))

list('.')


from datetime import datetime
for f in os.listdir('.'):
    fsize = os.path.getsize(f)
    mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M')
    flag = '/' if os.path.isdir(f) else ''
    print('%10d  %s  %s%s' % (fsize, mtime, f, flag))