%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%define pkgname cloudstack


%if 0%{?rhel} >= 4 && 0%{?rhel} <= 5
Name:           python26-%{pkgname}
%else
Name:           python-%{pkgname}
%endif
Version:        0.7.7
Release:        1%{?dist}
Summary:        Cloud.com Cloudstack Client

Group:          System Environment/Libraries
License:        MIT
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Source:         %{pkgname}-%{version}.tar.gz

%if 0%{?rhel} >= 4 && 0%{?rhel} <= 5
Requires:       python26
%else
BuildRequires: 	python-devel >= 2.5
Requires:       python >= 2.5
%endif
BuildArch:      noarch

%description
Provides a simple python client to cloud.com's api.

%prep
%setup -q -n %{pkgname}-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" python setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --skip-build --root $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README
%{python_sitelib}/*

%changelog
