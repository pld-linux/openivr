Summary:	Simple IVR answering machine for the H.323 protocol
Summary(pl.UTF-8):	Prosta automatyczna sekretarka dla protokołu H.323
Name:		openivr
Version:	1.13.5
%define fver	%(echo %{version} | tr . _)
Release:	5
License:	MPL 1.0
Group:		Networking/Daemons
Source0:	http://dl.sourceforge.net/openh323/%{name}-v%{fver}-src.tar.gz
# Source0-md5:	c663d088560004af53ad89868a3aa0ea
Patch0:		%{name}-cvs.patch
Patch1:		%{name}-mak_files.patch
URL:		http://www.openh323.org/
BuildRequires:	openh323-devel >= 1.18.0
BuildRequires:	pwlib-devel >= 1.10.0
%requires_eq	openh323
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenIVR is a simple IVR answering machine for the H.323 protocol that
uses the VXML scripting protocol. It uses the OpenH323 protocol stack
and can use Festival (http://www.festvox.org/).

%description -l pl.UTF-8
OpenIVR to prosta automatyczna sekretarka dla protokołu H.323,
używająca protokołu skryptowego VXML. Używa stosu protokołu OpenH323 i
może używać programu Festival (http://www.festvox.org/).

%prep
%setup -qn %{name}
%patch0 -p1
%patch1 -p1

%build
PWLIBDIR=%{_prefix}; export PWLIBDIR
OPENH323DIR=%{_prefix}; export OPENH323DIR

%{__make} %{?debug:debug}%{!?debug:opt}shared \
	CXX="%{__cxx}" \
	OPTCCFLAGS="%{rpmcflags} -fno-exceptions %{!?debug:-DNDEBUG}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install obj_*/%{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt
%attr(755,root,root) %{_bindir}/*
