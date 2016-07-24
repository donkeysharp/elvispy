from cerberus import Validator

class actions(object):
    CREATE      = 'create'
    UPDATE      = 'update'
    DELETE      = 'delete'
    INSTALL     = 'install'
    UNINSTALL   = 'uninstall'
    START       = 'start'
    STOP        = 'stop'
    RESTART     = 'restart'
    RELOAD      = 'reload'

class BaseResource:
    def __init__(self):
        self.actions = ()
        self.rules = {}

    def validate(self):
        # if self.rules is dict and len(self.rules.keys()) > 0:
        #     validator = Validator(self.rules)
        #     validator.validate(self.options)
        pass

    def run(self):
        if self.action in self.actions:
            self.validate()
            getattr(self, 'action_%s' % self.action)()
