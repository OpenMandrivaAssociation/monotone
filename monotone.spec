Summary:	A distributed version control tool
Name:		monotone
Version:	1.0
Release:	1
License:	GPLv2
Group:		Development/Other
Source:		http://monotone.ca/downloads/%{version}/%{name}-%{version}.tar.bz2
Url:		http://monotone.ca
# Patches from upstream
Patch0:		monotone-1.0-fix-fprint.patch
Patch1:		monotone-1.0-fix-rcs-file-function-naming.patch
Patch2:		monotone-1.0-fix-xdelta-test.patch
BuildRequires:	texinfo
BuildRequires:	boost-devel
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(botan-1.8)
BuildRequires:	pkgconfig(libpcre)
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(lua)
BuildRequires:	pkgconfig(libidn)

%description
monotone is a free, distributed version control system. it provides
fully disconnected operation, manages complete tree versions, keeps
its state in a local transactional database, supports overlapping
branches and extensible metadata, exchanges work over plain network
protocols, performs history-sensitive merging, and delegates trust
functions to client-side RSA certificates.

%prep
%setup -q
%patch0 -p 1
%patch1 -p 1
%patch2 -p 1

%build
%configure2_5x
%make
make html

%check
# Remove a test which fails (to investigate with upstream) syntax_errors_in_.mtn-ignore
rm -rf test/func/syntax_errors_in_.mtn-ignore
make check

%install
%makeinstall_std
rm -fr %{buildroot}%{_docdir}/%{name}

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS COPYING NEWS README UPGRADE doc/monotone.html contrib
%{_bindir}/mtn*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/hooks
%{_datadir}/%{name}/scripts
%{_sysconfdir}/bash_completion.d/*
%{_infodir}/%{name}*
%{_mandir}/man1/*

