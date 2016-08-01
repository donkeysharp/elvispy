from fabric.api import *
from fabric.tasks import execute
from .base_resource import BaseResource, actions


def runner(command, peanut):
    def closure():
        env.user = peanut.username
        env.password = peanut.password
        sudo(command)
    return closure

class Chmod(BaseResource):
    def __init__(self, peanut, target, mode='755', recursive=False):
        self.actions = (actions.UPDATE)
        self.action = actions.UPDATE
        self.peanut = peanut
        self.target = target
        self.mode = mode
        self.recursive = recursive

    def action_update():
        command = 'chmod'
        command += ' -R' if self.recursive else ''
        command += ' %s' self.mode
        command += ' %s' % self.target
        execute(runner(command, self.peanut), hosts=self.peanut.host_list)


def chmod(peanut, target, **options):
    cr = Chmod(peanut, target, **options)
    cr.run()
