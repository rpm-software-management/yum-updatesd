# This program is free software; you can redistribute it and/or modify
# it under the terms of version 2 of the GNU General Public License
# as published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.

# (c)2006-2007 Duke University, Red Hat, Inc.
# Seth Vidal <skvidal@linux.duke.edu>
# Jeremy Katz <katzj@redhat.com>

import os

from yum.config import BaseConfig, Option, IntOption, ListOption, BoolOption
from yum.parser import ConfigPreProcessor
from ConfigParser import ConfigParser, ParsingError

config_file = '/etc/yum/yum-updatesd.conf'

class UDConfig(BaseConfig):
    """Config format for the daemon"""
    run_interval = IntOption(3600)
    nonroot_workdir = Option("/var/tmp/yum-updatesd")
    emit_via = ListOption(['dbus', 'email', 'syslog'])
    email_to = ListOption(["root"])
    email_from = Option("root")
    dbus_listener = BoolOption(True)
    do_update = BoolOption(False)
    do_download = BoolOption(False)
    do_download_deps = BoolOption(False)
    updaterefresh = IntOption(3600)
    syslog_facility = Option("DAEMON")
    syslog_level = Option("WARN")
    syslog_ident = Option("yum-updatesd")
    yum_config = Option("/etc/yum/yum.conf")

def read_config():
    confparser = ConfigParser()
    opts = UDConfig()
    
    if os.path.exists(config_file):
        confpp_obj = ConfigPreProcessor(config_file)
        try:
            confparser.readfp(confpp_obj)
        except ParsingError, e:
            print >> sys.stderr, "Error reading config file: %s" % e
            sys.exit(1)
    opts.populate(confparser, 'main')
    return opts
