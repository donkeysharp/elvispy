import os

def create_peanut(peanut_name):
    peanut_dir = './peanuts/%s' % peanut_name

    if os.path.exists(peanut_dir):
        print('Peanut already exists')
        return
    os.mkdir(peanut_dir)
    os.mkdir(peanut_dir + '/templates')
    f = open(peanut_dir + '/__init__.py', 'w')
    f.write('')
    f.flush()
    f.close()

    f = open(peanut_dir + '/main.py', 'w')
    f.write('\n__META__ = {\n')
    f.write("    'displayName': '%s',\n" % peanut_name)
    f.write("    'description': 'Peanut description',\n")
    f.write("    'version': '0.1',\n")
    f.write("    'enabled': True,\n")
    f.write("}\n\n")
    f.write('def load(peanut):\n')
    f.write("    print('Loading peanut %s')\n" % peanut_name)
    f.flush()
    f.close()

def clean():
    if os.path.exists('./.__tmp__') and os.path.isdir('./.__tmp__'):
        import shutil
        shutil.rmtree('./.__tmp__')
