%undefine _debugsource_packages

Name:		python-dbus-fast
Version:	5.2.0
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/d/dbus-fast/dbus_fast-%{version}.tar.gz
Summary:	A faster version of dbus-next
URL:		https://pypi.org/project/dbus-fast/
License:	MIT
Group:		Development/Python

BuildRequires:	python
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(poetry-core)
BuildRequires:	python%{pyver}dist(cython)
BuildRequires:	python%{pyver}dist(setuptools)

BuildSystem:	python

%build -p
export LDFLAGS="%{ldflags} -lpython%{pyver}"

%description
A faster version of dbus-next

%files
%license LICENSE
%{python_sitearch}/dbus_fast
%{python_sitearch}/dbus_fast-*.*-info
