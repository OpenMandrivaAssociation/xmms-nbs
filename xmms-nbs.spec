%define snap	20040615

Summary:	NBS Output plugin for XMMS
Name:		xmms-nbs
Version:	1.0
Release:	%mkrel 0.%{snap}.3
License:	GPL
Group:		Sound
URL:		http://www.asterisk.org/
Source0:	%{name}-%{version}-%{snap}.tar.bz2
Requires:	xmms
BuildRequires:	xmms-devel
BuildRequires:	nbs-devel
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
This is an audio output plugin for XMMS for the Network Broadcast
Sound Daemon sound system.

This is a highly experimental package.

%prep

%setup -q -n %{name}-%{version}-%{snap}

%build

%make RPM_OPT_FLAGS="%{optflags} -fPIC"

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

install -d %{buildroot}%{_libdir}/xmms/Output
install -m0755 libNBS.so %{buildroot}%{_libdir}/xmms/Output/libNBS.so

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{_libdir}/xmms/Output/libNBS.so

