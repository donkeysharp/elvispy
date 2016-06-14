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

    def set_hosts(self, host_list):
        self.host_list = host_list

    def start(self):
        # Starting module related with "this" peanut
        self.module.load(self)


class PeanutManager:
    def __init__(self):
        self.peanut_map = {}

    def add_peanut(self, peanut):
        self.peanut_map[peanut.name] = peanut

    def run_peanuts(self, peanut_list, host_list):
        AVAILABLE_PEANUTS = self.peanut_map

        for peanut in peanut_list:
            if not AVAILABLE_PEANUTS.has_key(peanut):
                print('Peanut %s is not available or it does not exist.' % peanut)
                exit(0)

        for peanut in peanut_list:
            AVAILABLE_PEANUTS[peanut].set_hosts(host_list)
            AVAILABLE_PEANUTS[peanut].start()
