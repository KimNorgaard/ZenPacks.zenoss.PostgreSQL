###########################################################################
#
# This program is part of Zenoss Core, an open source monitoring platform.
# Copyright (C) 2011, Zenoss Inc.
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 2 or (at your
# option) any later version as published by the Free Software Foundation.
#
# For complete information please visit: http://www.zenoss.com/oss/
#
###########################################################################

import logging
log = logging.getLogger('zen.PostgreSQL')

from Products.ZenModel.ZenPack import ZenPack as ZenPackBase

class ZenPack(ZenPackBase):
    packZProperties = [
        ('zPostgresPort', 5432, 'int'),
        ('zPostgresUsername', 'postgres', 'string'),
        ('zPostgresPassword', '', 'password'),
    ]

    def install(self, app):
        super(ZenPack, self).install(app)
        self.symlinkPlugin()

    def remove(self, app, leaveObjects=False):
        if not leaveObjects:
            self.removePluginSymlink()

        super(ZenPack, self).remove(app, leaveObjects=leaveObjects)

    def symlinkPlugin(self):
        log.info('Linking poll_postgres.py plugin into $ZENHOME/libexec/')
        os.system('ln -sf {0} {1}'.format(
            self.path('poll_postgres.py'),
            zenPath('libexec', 'poll_postgres.py')))

    def removePluginSymlink(self):
        log.info('Removing poll_postgres.py link from $ZENHOME/libexec/')
        os.system('rm -f {0}'.format(zenPath('libexec', 'poll_postgres.py')))

