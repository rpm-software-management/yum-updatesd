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
VERSION = 0.2

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
	$(MKDIR) $(DESTDIR)$(PREFIX)/sbin $(DESTDIR)$(PREFIX)/libexec
	$(INSTALL) yum-updatesd $(DESTDIR)$(PREFIX)/sbin
	$(INSTALL) yum-updatesd-helper $(DESTDIR)$(PREFIX)/libexec

install-doc:
	@echo "Installing man pages"
	$(MKDIR) $(DESTDIR)$(MANDIR)/man8
	$(INSTALL_RD) docs/yum-updatesd.8 $(DESTDIR)$(MANDIR)/man8
	$(MKDIR) $(DESTDIR)$(MANDIR)/man5
	$(INSTALL_RD) docs/yum-updatesd.conf.5 $(DESTDIR)$(MANDIR)/man5

install-etc:
	@echo "Installing config files"
	$(MKDIR) $(DESTDIR)$(CONFDIR)/yum
	$(INSTALL) etc/yum-updatesd.conf $(DESTDIR)$(CONFDIR)/yum/yum-updatesd.conf
	$(MKDIR) $(DESTDIR)$(CONFDIR)/rc.d/init.d
	$(INSTALL) etc/yum-updatesd.init $(DESTDIR)$(CONFDIR)/rc.d/init.d/yum-updatesd
	$(MKDIR) $(DESTDIR)$(CONFDIR)/dbus-1/system.d/
	$(INSTALL_RD) etc/yum-updatesd-dbus.conf $(DESTDIR)$(CONFDIR)/dbus-1/system.d/yum-updatesd.conf

install: install-bin install-doc install-etc

dist:
	@git-archive --format=tar --prefix=$(NAME)-$(VERSION)/ HEAD | bzip2 -9v > $(NAME)-$(VERSION).tar.bz2
	@echo "Created $(NAME)-$(VERSION).tar.bz2"
