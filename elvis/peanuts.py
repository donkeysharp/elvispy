import os
from jinja2 import Environment, PackageLoader

class Peanut:
    def __init__(self, name, module, template_path):
        self.name = name
        self.module = module
        self.template_env = None
        self.info = module.__META__

        if os.path.exists(template_path) and os.path.isdir(template_path):
            self.template_env = Environment(
                loader=PackageLoader('peanuts.' + self.name, 'templates')
            )

    def start(self):
        # Starting module related with "this" peanut
        self.module.load(self)
