Summary:	Python module that implements DKIM (DomainKeys Identified Mail) email signing and verification
Summary(pl.UTF-8):	Biblioteka Pythona do tworzenia i weryfikowania podpisu DKIM (DomainKeys Identified Mail)
Name:		python-pydkim
Version:	0.3
Release:	1
License:	BSD
Group:		Libraries/Python
Source0:	http://hewgill.com/pydkim/pydkim-%{version}.tar.gz
# Source0-md5:	530769b4e79f41341020c4b28f340ea5
URL:		http://hewgill.com/pydkim/
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-dns
BuildRequires:	python-hashlib
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python module that implements DKIM (DomainKeys Identified Mail) email
signing and verification

%description -l pl.UTF-8
Biblioteka Pythona do tworzenia i weryfikowania podpisu DKIM
(DomainKeys Identified Mail)

%prep
%setup -q -n pydkim-%{version}

%build
env CFLAGS="%{rpmcflags}" %{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python -- setup.py install --root=$RPM_BUILD_ROOT --optimize=2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/*.html docs/*.css
%dir %{py_sitedir}/pydkim
%{py_sitedir}/*.egg-info
%attr(755,root,root) %{py_sitedir}/pydkim/*.so
%{py_sitedir}/pydkim/*.py[co]
%dir %{py_sitedir}/pydkim/constants
%{py_sitedir}/pydkim/constants/*.py[co]
