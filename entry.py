#!/usr/bin/env python

import os
import sys


def main(argv):
    # www-data user
    spawn_uid = 33
    spawn_gid = 33

    def execute(arg, user, group):
        print(">> Replacing current process with: %s" % arg[1])
        os.setgid(group)
        os.setuid(user)
        print(">> Running as %s:%s" % (os.geteuid(), os.getegid()))
        sys.stdout.flush()
        os.execvpe(arg[1], arg[1:], os.environ)  # replace current process, inherit environment

    config_file = os.getenv('CONFIG_FILE')

    if not os.path.isfile(config_file):
        print("Error CONFIG_FILE does not exist")
        exit(2)

    # Spawn Next Process
    if len(argv) > 1:
        execute(argv, spawn_uid, spawn_gid)

if __name__ == "__main__":
    main(argv=sys.argv)
