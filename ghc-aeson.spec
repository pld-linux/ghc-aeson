#
# Conditional build:
%bcond_without	prof	# profiling library
#
%define		pkgname	aeson
Summary:	Fast JSON parsing and encoding
Summary(pl.UTF-8):	Szybkie analizowanie i kodowanie JSON
Name:		ghc-%{pkgname}
Version:	1.4.7.1
Release:	1
License:	BSD
Group:		Development/Languages
#Source0Download: http://hackage.haskell.org/package/aeson
Source0:	http://hackage.haskell.org/package/%{pkgname}-%{version}/%{pkgname}-%{version}.tar.gz
# Source0-md5:	b83f55bb279c0659228931816c7a3af1
URL:		http://hackage.haskell.org/package/aeson
BuildRequires:	ghc >= 8.6
BuildRequires:	ghc-attoparsec >= 0.13.2.2
BuildRequires:	ghc-base >= 4.7.0.0
BuildRequires:	ghc-base-compat-batteries >= 0.10.0
BuildRequires:	ghc-bytestring >= 0.10.4.0
BuildRequires:	ghc-containers >= 0.5.5.1
BuildRequires:	ghc-deepseq >= 1.3.0.0
BuildRequires:	ghc-dlist >= 0.8.0.4
BuildRequires:	ghc-ghc-prim >= 0.2
BuildRequires:	ghc-hashable >= 1.2.7.0
BuildRequires:	ghc-primitive >= 0.6.3.0
BuildRequires:	ghc-scientific >= 0.3.6.2
BuildRequires:	ghc-tagged >= 0.8.5
BuildRequires:	ghc-template-haskell >= 2.9.0.0
BuildRequires:	ghc-text >= 1.2.3.0
BuildRequires:	ghc-th-abstraction >= 0.2.8.0
BuildRequires:	ghc-time >= 1.4
BuildRequires:	ghc-time-compat >= 1.9.2.2
BuildRequires:	ghc-unordered-containers >= 0.2.8.0
BuildRequires:	ghc-uuid-types >= 1.0.3
BuildRequires:	ghc-vector >= 0.12.0.1
%if %{with prof}
BuildRequires:	ghc-prof >= 6.12.3
BuildRequires:	ghc-attoparsec-prof >= 0.13.2.2
BuildRequires:	ghc-base-prof >= 4.7.0.0
BuildRequires:	ghc-base-compat-batteries-prof >= 0.10.0
BuildRequires:	ghc-bytestring-prof >= 0.10.4.0
BuildRequires:	ghc-containers-prof >= 0.5.5.1
BuildRequires:	ghc-deepseq-prof >= 1.3.0.0
BuildRequires:	ghc-dlist-prof >= 0.8.0.4
BuildRequires:	ghc-ghc-prim-prof >= 0.2
BuildRequires:	ghc-hashable-prof >= 1.2.7.0
BuildRequires:	ghc-primitive-prof >= 0.6.3.0
BuildRequires:	ghc-scientific-prof >= 0.3.6.2
BuildRequires:	ghc-tagged-prof >= 0.8.5
BuildRequires:	ghc-template-haskell-prof >= 2.9.0.0
BuildRequires:	ghc-text-prof >= 1.2.3.0
BuildRequires:	ghc-th-abstraction-prof >= 0.2.8.0
BuildRequires:	ghc-time-prof >= 1.4
BuildRequires:	ghc-time-compat-prof >= 1.9.2.2
BuildRequires:	ghc-unordered-containers-prof >= 0.2.8.0
BuildRequires:	ghc-uuid-types-prof >= 1.0.3
BuildRequires:	ghc-vector-prof >= 0.12.0.1
%endif
BuildRequires:	rpmbuild(macros) >= 1.608
Requires(post,postun):	/usr/bin/ghc-pkg
%requires_eq	ghc
Requires:	ghc-attoparsec >= 0.13.2.2
Requires:	ghc-base >= 4.7.0.0
Requires:	ghc-base-compat-batteries >= 0.10.0
Requires:	ghc-bytestring >= 0.10.4.0
Requires:	ghc-containers >= 0.5.5.1
Requires:	ghc-deepseq >= 1.3.0.0
Requires:	ghc-dlist >= 0.8.0.4
Requires:	ghc-ghc-prim >= 0.2
Requires:	ghc-hashable >= 1.2.7.0
Requires:	ghc-primitive >= 0.6.3.0
Requires:	ghc-scientific >= 0.3.6.2
Requires:	ghc-tagged >= 0.8.5
Requires:	ghc-template-haskell >= 2.9.0.0
Requires:	ghc-text >= 1.2.3.0
Requires:	ghc-th-abstraction >= 0.2.8.0
Requires:	ghc-time >= 1.4
Requires:	ghc-time-compat >= 1.9.2.2
Requires:	ghc-unordered-containers >= 0.2.8.0
Requires:	ghc-uuid-types >= 1.0.3
Requires:	ghc-vector >= 0.12.0.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# debuginfo is not useful for ghc
%define		_enable_debug_packages	0

# don't compress haddock files
%define		_noautocompressdoc	*.haddock

%description
A JSON parsing and encoding library optimized for ease of use and high
performance.

%description -l pl.UTF-8
Biblioteka do analizy i kodowania JSON zoptymalizowana pod kątem
łatwości użycia i dużej wydajności.

%package prof
Summary:	Profiling %{pkgname} library for GHC
Summary(pl.UTF-8):	Biblioteka profilująca %{pkgname} dla GHC
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	ghc-attoparsec-prof >= 0.13.2.2
Requires:	ghc-base-prof >= 4.7.0.0
Requires:	ghc-base-compat-batteries-prof >= 0.10.0
Requires:	ghc-bytestring-prof >= 0.10.4.0
Requires:	ghc-containers-prof >= 0.5.5.1
Requires:	ghc-deepseq-prof >= 1.3.0.0
Requires:	ghc-dlist-prof >= 0.8.0.4
Requires:	ghc-ghc-prim-prof >= 0.2
Requires:	ghc-hashable-prof >= 1.2.7.0
Requires:	ghc-primitive-prof >= 0.6.3.0
Requires:	ghc-scientific-prof >= 0.3.6.2
Requires:	ghc-tagged-prof >= 0.8.5
Requires:	ghc-template-haskell-prof >= 2.9.0.0
Requires:	ghc-text-prof >= 1.2.3.0
Requires:	ghc-th-abstraction-prof >= 0.2.8.0
Requires:	ghc-time-prof >= 1.4
Requires:	ghc-time-compat-prof >= 1.9.2.2
Requires:	ghc-unordered-containers-prof >= 0.2.8.0
Requires:	ghc-uuid-types-prof >= 1.0.3
Requires:	ghc-vector-prof >= 0.12.0.1

%description prof
Profiling %{pkgname} library for GHC. Should be installed when
GHC's profiling subsystem is needed.

%description prof -l pl.UTF-8
Biblioteka profilująca %{pkgname} dla GHC. Powinna być zainstalowana
kiedy potrzebujemy systemu profilującego z GHC.

%package doc
Summary:	HTML documentation for %{pkgname} ghc package
Summary(pl.UTF-8):	Dokumentacja w formacie HTML dla pakietu ghc %{pkgname}
Group:		Documentation

%description doc
HTML documentation for %{pkgname} ghc package.

%description doc -l pl.UTF-8
Dokumentacja w formacie HTML dla pakietu ghc %{pkgname}.

%prep
%setup -q -n %{pkgname}-%{version}

%build
runhaskell Setup.lhs configure -v2 \
	%{?with_prof:--enable-library-profiling} \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--libexecdir=%{_libexecdir} \
	--docdir=%{_docdir}/%{name}-%{version}

runhaskell Setup.lhs build
runhaskell Setup.lhs haddock --executables

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/%{ghcdir}/package.conf.d

runhaskell Setup.lhs copy --destdir=$RPM_BUILD_ROOT

# work around automatic haddock docs installation
%{__rm} -rf %{name}-%{version}-doc
cp -a $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version} %{name}-%{version}-doc
%{__rm} -rf $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

runhaskell Setup.lhs register \
	--gen-pkg-config=$RPM_BUILD_ROOT%{_libdir}/%{ghcdir}/package.conf.d/%{pkgname}.conf

%clean
rm -rf $RPM_BUILD_ROOT

%post
%ghc_pkg_recache

%postun
%ghc_pkg_recache

%files
%defattr(644,root,root,755)
%doc LICENSE README.markdown
%{_libdir}/%{ghcdir}/package.conf.d/%{pkgname}.conf
%dir %{_libdir}/%{ghcdir}/%{pkgname}-%{version}
%{_libdir}/%{ghcdir}/%{pkgname}-%{version}/libHSaeson-%{version}-*.so
%{_libdir}/%{ghcdir}/%{pkgname}-%{version}/libHSaeson-%{version}-*.a
%exclude %{_libdir}/%{ghcdir}/%{pkgname}-%{version}/libHSaeson-%{version}-*_p.a
%dir %{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Data
%{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Data/*.hi
%{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Data/*.dyn_hi
%dir %{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Data/Aeson
%{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Data/Aeson/*.hi
%{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Data/Aeson/*.dyn_hi
%dir %{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Data/Aeson/Encoding
%{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Data/Aeson/Encoding/*.hi
%{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Data/Aeson/Encoding/*.dyn_hi
%dir %{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Data/Aeson/Internal
%{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Data/Aeson/Internal/*.hi
%{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Data/Aeson/Internal/*.dyn_hi
%dir %{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Data/Aeson/Parser
%{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Data/Aeson/Parser/*.hi
%{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Data/Aeson/Parser/*.dyn_hi
%dir %{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Data/Aeson/QQ
%{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Data/Aeson/QQ/*.hi
%{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Data/Aeson/QQ/*.dyn_hi
%dir %{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Data/Aeson/Types
%{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Data/Aeson/Types/*.hi
%{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Data/Aeson/Types/*.dyn_hi
%dir %{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Data/Attoparsec
%{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Data/Attoparsec/*.hi
%{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Data/Attoparsec/*.dyn_hi
%dir %{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Data/Attoparsec/Time
%{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Data/Attoparsec/Time/*.hi
%{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Data/Attoparsec/Time/*.dyn_hi

%if %{with prof}
%files prof
%defattr(644,root,root,755)
%{_libdir}/%{ghcdir}/%{pkgname}-%{version}/libHSaeson-%{version}-*_p.a
%{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Data/*.p_hi
%{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Data/Aeson/*.p_hi
%{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Data/Aeson/Encoding/*.p_hi
%{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Data/Aeson/Internal/*.p_hi
%{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Data/Aeson/Parser/*.p_hi
%{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Data/Aeson/QQ/*.p_hi
%{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Data/Aeson/Types/*.p_hi
%{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Data/Attoparsec/*.p_hi
%{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Data/Attoparsec/Time/*.p_hi
%endif

%files doc
%defattr(644,root,root,755)
%doc %{name}-%{version}-doc/*
