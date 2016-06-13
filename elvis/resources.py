import os

class actions(object):
    CREATE      = 'create'
    DELETE      = 'delete'
    INSTALL     = 'install'
    UNINSTALL   = 'uninstall'
    START       = 'start'
    STOP        = 'stop'
    RESTART     = 'restart'
    RELOAD      = 'reload'

def template(peanut, destination, options={}):
    """
    template(peanut, '/dest/folder', {
        'source': 'sometemplate.tpl'
    })
    """
    env = peanut.template_env
    template = env.get_template(options['source'])

    variables = {}
    if options.has_key('variables'):
        variables = options['variables']

    content = template.render(**variables)
    print(content)
