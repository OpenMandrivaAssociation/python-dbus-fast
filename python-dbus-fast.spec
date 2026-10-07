%undefine _debugsource_packages

Name:		python-dbus-fast
Version:	5.2.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/d/dbus-fast/dbus_fast-%{version}.tar.gz
Summary:	A faster version of dbus-next
URL:		https://pypi.org/project/dbus-fast/
License:	MIT
Group:		Development/Python

BuildRequires:	python
BuildRequires:  python%{pyver}dist(pip)
BuildRequires:  python%{pyver}dist(poetry-core)
BuildRequires:  python%{pyver}dist(myst-parser)
BuildRequires:  python%{pyver}dist(sphinx)
BuildRequires:  python%{pyver}dist(sphinx-rtd-theme)
BuildRequires:  python%{pyver}dist(sphinxcontrib-asyncio)
BuildRequires:  python%{pyver}dist(pytest)
BuildRequires:  python%{pyver}dist(pytest-cov)
BuildRequires:  python%{pyver}dist(pytest-asyncio)
BuildRequires:  python%{pyver}dist(pycairo)
BuildRequires:  python%{pyver}dist(cython)
BuildRequires:  python%{pyver}dist(setuptools)
BuildRequires:  python-gobject3

BuildSystem:	python

%description
A faster version of dbus-next

%files
%license LICENSE
%{python_sitearch}/dbus_fast
%{python_sitearch}/dbus_fast-*.*-info
