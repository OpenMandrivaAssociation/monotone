%define name    monotone
%define version 0.42
%define release %mkrel 1
%define summary A distributed version control tool


Summary:        %summary
Name:           %name
Version:        %version
Release:        %release
License: GPL
Group: Development/Other
Source: http://monotone.ca/downloads/%{version}/%{name}-%{version}.tar.gz
Url: http://monotone.ca
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	boost-devel
BuildRequires:  zlib-devel
BuildRequires:  texinfo

%description
monotone is a free, distributed version control system. it provides
fully disconnected operation, manages complete tree versions, keeps
its state in a local transactional database, supports overlapping
branches and extensible metadata, exchanges work over plain network
protocols, performs history-sensitive merging, and delegates trust
functions to client-side RSA certificates.

%prep
%setup -q

%build
%configure2_5x
%make

%check
make check

%install
rm -rf %buildroot
%makeinstall
%__install -d -m 755 %{buildroot}%{_sysconfdir}/bash_completion.d
%__install -m 644 contrib/monotone.bash_completion %{buildroot}%{_sysconfdir}/bash_completion.d/%{name}
# let RPM copy this file
%__rm -f %{buildroot}%{_docdir}/%{name}/%{name}.html

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
%doc AUTHORS COPYING NEWS README UPGRADE monotone.html contrib
