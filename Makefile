# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
#
# Copyright 2007 Red Hat, Inc.
# James Bowes <jbowes@redhat.com>

NAME = yum-updatesd
VERSION = 0.1

PREFIX = /usr
MANDIR = $(PREFIX)/share/man
CONFDIR = /etc

INSTALL = @install
INSTALL_RD = $(INSTALL) -m 644
MKDIR = @mkdir -p


all:
	@echo "Nothing to do for all"

install-bin:
	@echo "Installing executables"
	$(MKDIR) $(PREFIX)/sbin $(PREFIX)/libexec
	$(INSTALL) yumd $(PREFIX)/sbin
	$(INSTALL) yum-updatesd-helper $(PREFIX)/libexec

install-doc:
	@echo "Installing man pages"
	$(MKDIR) $(MANDIR)/man8
	$(INSTALL_RD) docs/yum-updatesd.8 $(MANDIR)/man8
	$(MKDIR) $(MANDIR)/man5
	$(INSTALL_RD) docs/yum-updatesd.conf.5 $(MANDIR)/man5

install-etc:
	@echo "Installing config files"
	$(MKDIR) $(CONFDIR)/yum
	$(INSTALL) etc/yum-updatesd.conf $(CONFDIR)/yum/yum-updatesd.conf
	$(MKDIR) $(CONFDIR)/rc.d/init.d
	$(INSTALL) etc/yum-updatesd.init $(CONFDIR)/rc.d/init.d/yum-updatesd
	$(MKDIR) $(CONFDIR)/dbus-1/system.d/
	$(INSTALL_RD) etc/yum-updatesd-dbus.conf $(CONFDIR)/dbus-1/system.d/yum-updatesd.conf

install: install-bin install-doc install-etc

dist:
	@git-archive --format=tar --prefix=$(NAME)-$(VERSION)/ HEAD | bzip2 -9v > $(NAME)-$(VERSION).tar.bz2
	@echo "Created $(NAME)-$(VERSION).tar.bz2"
