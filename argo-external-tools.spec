Name: argo-external-tools
Summary: External script tools
Version: 1.0.1
Release: 1%{?dist}
License: AGPLv3
Buildroot: %{_tmppath}/%{name}-buildroot
Group: Unspecified
Source0: %{name}-%{version}.tar.gz
BuildArch: noarch
Requires: nagios-plugins
Requires: perl

%description
This package includes external tools for argo services. 
Currently it includes the following components:
 - check_mem.pl
 - check_updates_ARGO

%prep
%setup

%build

%install
install --directory %{buildroot}/%{_libdir}/nagios/plugins
install --mode 755 src/check_mem.pl %{buildroot}/%{_libdir}/nagios/plugins/check_mem.pl
install --mode 755 src/check_updates_ARGO %{buildroot}/%{_libdir}/nagios/plugins/check_updates_ARGO

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(0644,root,root)
%attr(0755,root,root) %{_libdir}/nagios/plugins

%changelog
* Tue Nov 02 2021 Lisgaras Anastasios <tasos@grnet.gr> 1.0.1
- Add `check_updates_ARGO` probe.
* Wed Sep 09 2020 Kostas Evangelou <kevangel@grnet.gr> 1.0.0
- Initial version of the package
