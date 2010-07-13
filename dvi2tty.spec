%define name	dvi2tty
%define version 5.3.1
%define release %mkrel 5

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Tool for previewing DVI files on text-only devices
Group:		Text tools
URL:		http://www.mesa.nl/pub/dvi2tty/
Source:		http://www.mesa.nl/pub/dvi2tty/%{name}-%{version}.tar.bz2
Patch0:		dvi2tty-5.3.1-pager.patch
Patch1:		dvi2tty-5.3.1-malloc.patch
Patch2:		dvi2tty-5.3.1-getline.patch
License:	GPLv2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
dvi2tty is a tool for previewing DVI files on text-only devices. It is
used by MC for viewing DVI files.

%prep
%setup -q
%patch0 -p1 -b .pager
%patch1 -p1 -b .malloc
%patch2 -p1 -b .getline

%build
%make

%install
%__rm -rf %buildroot
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_mandir/man1
%__install -m 755 dvi2tty disdvi %buildroot%_bindir
%__install -m 644 dvi2tty.1 disdvi.1 %buildroot%_mandir/man1

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%_bindir/*
%_mandir/*/*

