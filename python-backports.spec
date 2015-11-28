# https://bugzilla.redhat.com/show_bug.cgi?id=998047
Summary:	Namespace for backported Python features
Name:		python-backports
Version:	1.0
Release:	6
Group:		Libraries/Python
# Only code is sourced from http://www.python.org/dev/peps/pep-0382/
License:	Public Domain
Source0:	backports.py
URL:		https://pypi.python.org/pypi/backports
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# nothing to put there
%define		_enable_debug_packages	0

%description
The backports namespace is a namespace reserved for features
backported from the Python standard library to older versions of
Python 2.

Packages that exist in the backports namespace in PLD Linux should not
provide their own backports/__init__.py, but instead require this
package.

Backports to earlier versions of Python 3, if they exist, do not need
this package because of changes made in Python 3.3 in PEP 420
<http://www.python.org/dev/peps/pep-0420/>.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitescriptdir}/backports
cp -p %{SOURCE0} $RPM_BUILD_ROOT%{py_sitescriptdir}/backports/__init__.py

%if "%{py_sitescriptdir}" != "%{py_sitedir}"
install -d $RPM_BUILD_ROOT%{py_sitedir}/backports
cp -p %{SOURCE0} $RPM_BUILD_ROOT%{py_sitedir}/backports/__init__.py
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/backports
%if "%{py_sitescriptdir}" != "%{py_sitedir}"
%{py_sitedir}/backports
%endif
