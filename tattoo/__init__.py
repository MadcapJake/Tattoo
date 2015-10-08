# Copyright (c) 2015 Jacob Russo <madcap.russo+tattoo@gmail.com>
#
# Tattoo is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# Tattoo is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with Tattoo; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

import gi
gi.require_version('Tracker', '1.0')
from gi.repository import Tracker
from itertools import chain
import logging
import time
logger = logging.getLogger(__name__)
tabbing = 0


def log(fn):
    if logger.getEffectiveLevel() > logging.DEBUG:
        return fn

    def wrapped(*v, **k):
        global tabbing
        name = fn.__qualname__
        filename = fn.__code__.co_filename.split('/')[-1]
        lineno = fn.__code__.co_firstlineno

        params = ", ".join(map(repr, chain(v, k.values())))

        if 'rateLimitedFunction' not in name:
            logger.debug("%s%s(%s)[%s:%s]",
                         '|' * tabbing, name, params, filename, lineno,)
        tabbing += 1
        start = time.time()
        retval = fn(*v, **k)
        elapsed = time.time() - start
        tabbing -= 1
        elapsed_time = ''
        if elapsed > 0.1:
            elapsed_time = ', took %02f' % elapsed
        if elapsed_time or retval is not None:
            if 'rateLimitedFunction' not in name:
                logger.debug("%s  returned %s%s", '|' * tabbing, repr(retval), elapsed_time)

        return retval
    return wrapped


class TrackerWrapper:
    class __TrackerWrapper:
        def __init__(self):
            try:
                self.tracker = Tracker.SparqlConnection.get(None)
            except Exception as e:
                from sys import exit
                logger.error("Cannot connect to tracker, error '%s'\Exiting", str(e))
                exit(1)

        def __str__(self):
            return repr(self)
    instance = None

    def __init__(self):
        if not TrackerWrapper.instance:
            TrackerWrapper.instance = TrackerWrapper.__TrackerWrapper()

    def __getattr__(self, name):
        return getattr(self.instance, name)
