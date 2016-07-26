import os
import time
from fabric.api import *
from fabric.tasks import execute
from .base_resource import BaseResource
from .base_resource import actions


def runner(filename, dest, user, password, owner, group):
    def closure():
        env.user = user
        env.password = password
        put(filename, dest, use_sudo=True)
        sudo('chown %s:%s %s' % (owner, group, dest))
    return closure

def _save_temporal_file(content):
    if not os.path.exists('./.__tmp__') or not os.path.isdir('./.__tmp__'):
        os.mkdir('./.__tmp__')
    random_name = str(time.time())
    f = open('./.__tmp__/%s' % random_name, 'w')
    f.write(content)
    f.write('\n')
    f.close()

    return './.__tmp__/' + random_name


class TemplateResource(BaseResource):
    def __init__(self, peanut, destination,
                                action=actions.CREATE,
                                variables={},
                                source='',
                                owner='$USER',
                                group='$GROUPS'):
        self.actions = (actions.CREATE)
        self.action = action
        self.peanut = peanut
        self.destination = destination
        self.variables = variables
        self.source = source
        self.owner = owner
        self.group = group

    def action_create(self):
        username = self.peanut.username
        password = self.peanut.password
        owner = self.owner
        group = self.group
        tplenv = self.peanut.template_env
        template = tplenv.get_template(self.source)
        variables = self.variables

        # Save rendered template a temp file
        content = template.render(**variables)
        filename = _save_temporal_file(content)

        execute(runner(filename, self.destination, username, password,\
            owner, group), hosts=self.peanut.host_list)


def template(peanut, destination, **options):
    tr = TemplateResource(peanut, destination, **options)
    tr.run()
