import os
from elvis import Peanut


def load(load_all=False):
    peanut_map = {}

    # By convention it's supposed that all directories
    # inside "peanuts" directory will be (yeah) peantus.
    dir_list = os.listdir('./peanuts')
    for entry in dir_list:
        fullpath = './peanuts/%s' % entry
        if os.path.isdir(fullpath):
            module_name = 'peanuts.%s.main' % entry
            module = __import__(module_name, fromlist=[module_name])

            # Avoid disabled peanuts unless they are requested
            if not load_all and not module.__META__['enabled']:
                continue

            peanut_map[entry] = Peanut(
                name=entry, # the internal name will be directory's
                module=module,
                template_path=fullpath + '/templates'
            )

    return peanut_map
