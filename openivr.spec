Summary:	Simple IVR answering machine for the H.323 protocol
Summary(pl):	Prosta automatyczna sekretarka dla protoko³u H.323
Name:		openivr
Version:	1.13.4
%define fver	%(echo %{version} | tr . _)
Release:	1
License:	MPL 1.0
Group:		Networking/Daemons
Source0:	http://dl.sourceforge.net/openh323/%{name}-v%{fver}-src.tar.gz
# Source0-md5:	8af3eba252296660563261c5a306cfe4
Patch0:		%{name}-mak_files.patch
URL:		http://www.openh323.org/
BuildRequires:	openh323-devel >= 1.13.4-3
BuildRequires:	pwlib-devel >= 1.6.5-3
%requires_eq	openh323
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenIVR is a simple IVR answering machine for the H.323 protocol that
uses the VXML scripting protocol. It uses the OpenH323 protocol stack
and can use Festival (http://www.festvox.org/).

%description -l pl
OpenIVR to prosta automatyczna sekretarka dla protoko³u H.323,
u¿ywaj±ca protoko³u skryptowego VXML. U¿ywa stosu protoko³u OpenH323 i
mo¿e u¿ywaæ programu Festival (http://www.festvox.org/).

%prep
%setup -qn %{name}
%patch0 -p1

%build
PWLIBDIR=%{_prefix}; export PWLIBDIR
OPENH323DIR=%{_prefix}; export OPENH323DIR

%{__make} %{?debug:debug}%{!?debug:opt}shared \
	OPTCCFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions %{!?debug:-DNDEBUG}"

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
