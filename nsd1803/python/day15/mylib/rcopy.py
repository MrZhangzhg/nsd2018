#!/usr/bin/env python

import shutil
from ansible.module_utils.basic import AnsibleModule

def main():
    mokuai = AnsibleModule(
        argument_spec=dict(
            yuan=dict(required=True, type='str'),
            mudi=dict(required=True, type='str')
        )
    )
    shutil.copy(mokuai.params['yuan'], mokuai.params['mudi'])
    mokuai.exit_json(change=True)

if __name__ == '__main__':
    main()
