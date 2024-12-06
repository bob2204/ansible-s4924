#!/usr/bin/python
import subprocess


DOCUMENTATION = '''
---
module: module de test
short_description: module de test
description:
  - Ce module de test permet d'illustrer la notion de module Ansible
options:
  name:
    description:
      - premier paramètre du module
    required: true
    default: null
  dest:
    description:
      - second paramètre (optionnel) du module
    required: false
    default: /tmp
authors:
  - Bob <bguerin@dawan.fr> 
'''

EXAMPLES = '''
- modtest: basename=data.txt

'''

def run(args, module):
    try:
        cmd = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = cmd.communicate()
        rc = cmd.returncode
    except (OSError, IOError) as e:
        module.fail_json(rc=e.errno, msg=str(e), cmd=args)
    if rc != 0 or err:
        module.fail_json(rc=rc, msg=err, cmd=args)
    return out

def main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
        ),
        supports_check_mode=True,
    )
    name = module.params['name']
    map_mtime = os.path.getmtime(name + '.db')
    src_mtime = os.path.getmtime(name)
    if src_mtime <= map_mtime:
        module.exit_json(
            msg="",
            changed=False,
        )
    if not module.check_mode:
        run(['cp', '{}'.format(name),'{}'.format(name)+'.db'], module)
    module.exit_json(
        msg="setting changed",
        diff=dict(
            before=str(map_mtime) + '\n',
            after=str(src_mtime) + '\n'),
        changed=True,
    )


from ansible.module_utils.basic import *  # noqa


if __name__ == '__main__':
    main()
