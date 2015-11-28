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
BuildRequires:	rpm-pythonprov
Requires:	python-modules
BuildArch:	noarch
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
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%py_postclean

# package those scripts as docs
%{__rm} -r $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO dkimsign.py dkimverify.py
%{py_sitescriptdir}/*.egg-info
%{py_sitescriptdir}/*.py[co]
