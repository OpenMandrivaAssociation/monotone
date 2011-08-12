%define name    monotone
%define version 1.0
%define release %mkrel 2
%define summary A distributed version control tool


Summary:        %summary
Name:           %name
Version:        %version
Release:        %release
License: GPL
Group: Development/Other
Source: http://monotone.ca/downloads/%{version}/%{name}-%{version}.tar.bz2
Patch1: monotone-1.0-format-error.patch
Patch2: monotone-1.0-file_handle.patch
Patch3: monotone-1.0-fix-help.patch
Url: http://monotone.ca
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	boost-devel
BuildRequires:	botan-devel
BuildRequires:	gettext-devel
BuildRequires:	idn-devel
BuildRequires:	lua-devel
BuildRequires:	pcre-devel
BuildRequires:	sqlite3-devel
BuildRequires:  texinfo
BuildRequires:  zlib-devel

%description
monotone is a free, distributed version control system. it provides
fully disconnected operation, manages complete tree versions, keeps
its state in a local transactional database, supports overlapping
branches and extensible metadata, exchanges work over plain network
protocols, performs history-sensitive merging, and delegates trust
functions to client-side RSA certificates.

%prep
%setup -q
%patch1 -p0
%patch2 -p0
%patch3 -p0

%build
%configure2_5x
%make

%check
make check

%install
rm -rf %buildroot
%makeinstall
%__install -d -m 755 %{buildroot}%{_sysconfdir}/bash_completion.d
%__install -m 644 extra/shell/monotone.bash_completion %{buildroot}%{_sysconfdir}/bash_completion.d/%{name}
# let RPM copy this file
%__rm -f %{buildroot}%{_docdir}/%{name}/%{name}.html
%__rm -f %{buildroot}%{_sysconfdir}/bash_completion.d/*.bash_completion

%find_lang %{name}

%clean
rm -rf %buildroot

%post
%_install_info %{name}.info

%preun
%_remove_install_info %{name}.info

%files -f %{name}.lang
%defattr(-,root,root,0755)
%{_bindir}/mtn*
%{_sysconfdir}/bash_completion.d/%{name}
%{_infodir}/%{name}*
%{_mandir}/man1/*
/usr/share/%{name}/hooks/*
/usr/share/%{name}/scripts/*
%doc AUTHORS COPYING NEWS README UPGRADE contrib
