import os
import time
from fabric.api import *
from fabric.tasks import execute


class actions(object):
    CREATE      = 'create'
    DELETE      = 'delete'
    INSTALL     = 'install'
    UNINSTALL   = 'uninstall'
    START       = 'start'
    STOP        = 'stop'
    RESTART     = 'restart'
    RELOAD      = 'reload'


def __save_temporal_file(content):
    if not os.path.exists('./.__tmp__') or not os.path.isdir('./.__tmp__'):
        os.mkdir('./.__tmp__')
    random_name = str(time.time())
    f = open('./.__tmp__/%s' % random_name, 'w')
    f.write(content)
    f.write('\n')
    f.close()

    return './.__tmp__/' + random_name


def template(peanut, destination, options={}):
    tplenv = peanut.template_env
    template = tplenv.get_template(options['source'])

    variables = {}
    if options.has_key('variables'):
        variables = options['variables']
    content = template.render(**variables)

    filename = __save_temporal_file(content)

    def remote_run():
        put(filename, destination)

    execute(remote_run, hosts=['donkeysharp@192.168.56.120'])
