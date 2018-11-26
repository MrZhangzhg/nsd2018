#!/usr/bin/env python3
# coding: utf8

import shutil
from ansible.module_utils.basic import AnsibleModule

def main():
    '函数名是main，必须的'
    module = AnsibleModule(
        argument_spec=dict(
            yuan=dict(required=True, type='str'),
            mubiao=dict(required=True, type='str')
        )
    )
    shutil.copy(module.params['yuan'], module.params['mubiao'])
    module.exit_json(changed=True)

if __name__ == '__main__':
    main()
