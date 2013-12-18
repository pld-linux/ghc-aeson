#
# Conditional build:
%bcond_without	prof	# profiling library
#
%define		pkgname	aeson
Summary:	Fast JSON parsing and encoding
Summary(pl.UTF-8):	Szybkie analizowanie i kodowanie JSON
Name:		ghc-%{pkgname}
Version:	0.6.2.1
Release:	1
License:	BSD
Group:		Development/Languages
#Source0Download: http://hackage.haskell.org/package/aeson
Source0:	http://hackage.haskell.org/package/%{pkgname}-%{version}/%{pkgname}-%{version}.tar.gz
# Source0-md5:	3e06429d5e10812c9d8b8f184455e9a1
URL:		http://hackage.haskell.org/package/aeson
BuildRequires:	ghc >= 6.12.3
BuildRequires:	ghc-attoparsec >= 0.8.6.1
BuildRequires:	ghc-base >= 4
BuildRequires:	ghc-base < 5
BuildRequires:	ghc-blaze-builder >= 0.2.1.4
BuildRequires:	ghc-bytestring
BuildRequires:	ghc-containers
BuildRequires:	ghc-deepseq
BuildRequires:	ghc-hashable >= 1.1.2.0
BuildRequires:	ghc-mtl
BuildRequires:	ghc-old-locale
BuildRequires:	ghc-syb
BuildRequires:	ghc-template-haskell >= 2.4
BuildRequires:	ghc-text >= 0.11.1.0
BuildRequires:	ghc-time
BuildRequires:	ghc-unordered-containers >= 0.1.3.0
BuildRequires:	ghc-vector >= 0.7.1
%if %{with prof}
BuildRequires:	ghc-prof >= 6.12.3
BuildRequires:	ghc-attoparsec-prof >= 0.8.6.1
BuildRequires:	ghc-base-prof >= 4
BuildRequires:	ghc-base-prof < 5
BuildRequires:	ghc-blaze-builder-prof >= 0.2.1.4
BuildRequires:	ghc-bytestring-prof
BuildRequires:	ghc-containers-prof
BuildRequires:	ghc-deepseq-prof
BuildRequires:	ghc-hashable-prof >= 1.1.2.0
BuildRequires:	ghc-mtl-prof
BuildRequires:	ghc-old-locale-prof
BuildRequires:	ghc-syb-prof
BuildRequires:	ghc-template-haskell-prof >= 2.4
BuildRequires:	ghc-text-prof >= 0.11.1.0
BuildRequires:	ghc-time-prof
BuildRequires:	ghc-unordered-containers-prof >= 0.1.3.0
BuildRequires:	ghc-vector-prof >= 0.7.1
%endif
BuildRequires:	rpmbuild(macros) >= 1.608
Requires(post,postun):	/usr/bin/ghc-pkg
%requires_eq	ghc
Requires:	ghc-attoparsec >= 0.8.6.1
Requires:	ghc-base >= 4
Requires:	ghc-base < 5
Requires:	ghc-blaze-builder >= 0.2.1.4
Requires:	ghc-bytestring
Requires:	ghc-containers
Requires:	ghc-deepseq
Requires:	ghc-hashable >= 1.1.2.0
Requires:	ghc-mtl
Requires:	ghc-old-locale
Requires:	ghc-syb
Requires:	ghc-template-haskell >= 2.4
Requires:	ghc-text >= 0.11.1.0
Requires:	ghc-time
Requires:	ghc-unordered-containers >= 0.1.3.0
Requires:	ghc-vector >= 0.7.1
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
Requires:	ghc-attoparsec-prof >= 0.8.6.1
Requires:	ghc-base-prof >= 4
Requires:	ghc-base-prof < 5
Requires:	ghc-blaze-builder-prof >= 0.2.1.4
Requires:	ghc-bytestring-prof
Requires:	ghc-containers-prof
Requires:	ghc-deepseq-prof
Requires:	ghc-hashable-prof >= 1.1.2.0
Requires:	ghc-mtl-prof
Requires:	ghc-old-locale-prof
Requires:	ghc-syb-prof
Requires:	ghc-template-haskell-prof >= 2.4
Requires:	ghc-text-prof >= 0.11.1.0
Requires:	ghc-time-prof
Requires:	ghc-unordered-containers-prof >= 0.1.3.0
Requires:	ghc-vector-prof >= 0.7.1

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
%{_libdir}/%{ghcdir}/%{pkgname}-%{version}/HSaeson-%{version}.o
%{_libdir}/%{ghcdir}/%{pkgname}-%{version}/libHSaeson-%{version}.a
%dir %{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Data
%{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Data/Aeson.hi
%dir %{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Data/Aeson
%{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Data/Aeson/*.hi
%dir %{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Data/Aeson/Parser
%{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Data/Aeson/Parser/*.hi
%dir %{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Data/Aeson/Types
%{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Data/Aeson/Types/*.hi

%if %{with prof}
%files prof
%defattr(644,root,root,755)
%{_libdir}/%{ghcdir}/%{pkgname}-%{version}/libHSaeson-%{version}_p.a
%{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Data/Aeson.p_hi
%{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Data/Aeson/*.p_hi
%{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Data/Aeson/Parser/*.p_hi
%{_libdir}/%{ghcdir}/%{pkgname}-%{version}/Data/Aeson/Types/*.p_hi
%endif

%files doc
%defattr(644,root,root,755)
%doc %{name}-%{version}-doc/*
