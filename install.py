#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
setup for weewx prometheus pushgateway pusher
"""

__title__ = 'PromPush'
__version__ = '0.1.0'
__author__ = 'steve ulrich <sulrich@botwerks.org>'
# installer code lifted from graphite installer which i previously used for
# weather stats collection - preserving license and original copyright
__license__ = 'Apache License, Version 2.0'
__copyright__ = 'Copyright 2014 OnBeep, Inc.'

import setup

def loader():
    """install PromPush extension"""
    return WeewxPromPushInstaller()


class WeewxPromPushInstaller(setup.ExtensionInstaller):
    """installs weewx PromPush extension"""

    def __init__(self):
        super(WeewxPromPushInstaller, self).__init__(
            version=__version__,
            name=__title__,
            description='post weather data to prometheus pushgateway.',
            author='steve ulrich',
            author_email='sulrich@botwerks.org',
            restful_services='user.prompush.PromPush',
            config={
                'StdRESTful': {
                    'PromPush': {
                        'host': 'PUSH_GW_HOST',
                        'port': 'PUSH_GW_PORT',
                        'job': 'PROMETHEUS_JOB_NAME',
                        'instance': 'PROMETHEUS_INSTANCE_NAME'
                    }
                }
            },
            files=[('bin/user', ['bin/user/prompush.py'])]
        )
