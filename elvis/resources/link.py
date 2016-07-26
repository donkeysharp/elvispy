from fabric.api import *
from fabric.tasks import execute
from .base_resource import BaseResource, actions


def runner(resource, command):
    def closure():
        env.user = resource.peanut.username
        env.password = resource.peanut.password
        sudo(command)
    return closure


class Link(BaseResource):
    def __init__(self, peanut, link_name,
                        target,
                        action=actions.CREATE,
                        hard=False):
        self.actions = [actions.CREATE, actions.DELETE]
        self.action = action
        self.peanut = peanut
        self.target = target
        self.link_name = link_name
        self.hard = hard

    def action_create(self):
        hardFlag = '' if self.hard else '-s'
        command = 'ln %s %s %s' % (hardFlag, self.target, self.link_name)
        execute(runner(self, command), hosts=self.peanut.host_list)

    def action_delete(self):
        command = 'rm %s' % (self.link_name)
        execute(runner(self, command), hosts=self.peanut.host_list)


def link(peanut, link_name, **options):
    lr = Link(peanut, link_name, **options)
    lr.run()
