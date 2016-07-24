from fabric.api import *
from fabric.tasks import execute
from .base_resource import BaseResource
from .base_resource import actions

def runner(command, user, password):
    def closure():
        # These env variables can be set locally
        # but hosts must be set globally, a way to
        # do that is by using execute method
        env.user = user
        env.password = password
        sudo(command)

    return closure

class DirectoryResource(BaseResource):
    def __init__(self, peanut, name,
                            action=actions.CREATE,
                            mode=755,
                            user='root',
                            group='root'):
        self.actions = (actions.CREATE, actions.DELETE)
        self.peanut = peanut
        self.name = name
        self.action = action
        self.user = user
        self.group = group
        self.mode = mode

    def action_create(self):
        command = 'mkdir -p %s ' % (self.name)
        command += ' && chown -R %s:%s %s' % (self.user, self.group, \
            self.name)
        command += ' && chmod %s %s' % (self.mode, self.name)

        execute(runner(command, 'user', 'password'), hosts=self.peanut.host_list)


    def action_delete(self):
        command = 'rm -r %s' % (self.name)
        execute(runner(command, 'user', 'password'), hosts=self.peanut.host_list)


def directory(peanut,name, **options):
    dr = DirectoryResource(peanut, name, **options)
    dr.run()
