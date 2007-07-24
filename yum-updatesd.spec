Summary: Update notification daemon
Name: yum-updatesd
Epoch: 1
Version: 0.4
Release: 1%{?dist}
License: GPLv2
Group: System Environment/Base
Source0: %{name}-%{version}.tar.bz2
URL: http://linux.duke.edu/yum/
BuildArch: noarch
BuildRequires: python
Requires: python >= 2.4
Requires: yum >= 3.2.0
Requires: dbus-python
Requires: pygobject2
Requires: gamin-python
Requires(preun): /sbin/chkconfig
Requires(post): /sbin/chkconfig
Requires(preun): /sbin/service
Requires(post): /sbin/service
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
yum-updatesd provides a daemon which checks for available updates and 
can notify you when they are available via email, syslog or dbus. 

%prep
%setup -q

%build
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add yum-updatesd
/sbin/service yum-updatesd condrestart >/dev/null 2>&1
exit 0

%preun
if [ $1 = 0 ]; then
 /sbin/chkconfig --del yum-updatesd
 /sbin/service yum-updatesd stop >/dev/null 2>&1
fi
exit 0

%files
%defattr(-,root,root,-)
%doc COPYING
%{_sysconfdir}/rc.d/init.d/yum-updatesd
%config(noreplace) %{_sysconfdir}/yum/yum-updatesd.conf
%config %{_sysconfdir}/dbus-1/system.d/yum-updatesd.conf
%{_sbindir}/yum-updatesd
%{_libexecdir}/yum-updatesd-helper
%{_mandir}/man*/yum-updatesd*


%changelog
* Tue Jul 24 2007 Jeremy Katz <katzj@redhat.com> - 1:0.4-1
- minor review fixes.  add --oneshot mode

* Mon Jul 23 2007 Jeremy Katz <katzj@redhat.com> - 1:0.3-1
- update to new version

* Thu Jul 19 2007 Jeremy Katz <katzj@redhat.com> - 1:0.1-1
- new package for standalone yum-updatesd
