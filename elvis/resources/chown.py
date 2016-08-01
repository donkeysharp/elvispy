from fabric.api import *
from fabric.tasks import execute
from .base_resource import BaseResource, actions


def runner(command, peanut):
    def closure():
        env.user = peanut.username
        env.password = peanut.password
        sudo(command)
    return closure

class Chown(BaseResource):
    def __init__(self, peanut, target,
                                user,
                                group,
                                recursive=False):
        self.actions = (actions.UPDATE)
        self.action = actions.UPDATE
        self.peanut = peanut
        self.target = target
        self.user = user
        self.group = group
        self.recursive = recursive

    def action_update(self):
        command = 'chown'
        command += ' -R' if self.recursive else ''
        command += ' %s' % self.user
        command += ':%s' % self.group if self.group else ''
        command += ' %s' % self.target

        execute(runner(command, self.peanut), hosts=self.peanut.host_list)


def chown(peanut, target, **options):
    cr = Chown(peanut, target, **options)
    cr.run()
