%if %{isaix}
	%define _prefix /opt/nagios
%else
	%define _libexecdir %{_exec_prefix}/lib/nagios/plugins
%endif

Name: argo-external-tools
Summary: External script tools
Version: 1.0.0
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

%prep
%setup

%build
echo %{buildroot}
echo %{_tmppath}

%install
install --directory %{buildroot}/%{_libdir}/nagios/plugins
install --mode 755 src/check_mem.pl %{buildroot}/%{_libdir}/nagios/plugins/check_mem.pl

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(0644,root,root)
%attr(0755,root,root) %{_libdir}/nagios/plugins

%changelog
* Wed Sep 09 2020 Kostas Evangelou <kevangel@grnet.gr> 1.0.0
- Initial version of the package
