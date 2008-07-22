%define name dvi2tty
%define version 5.3.1
%define release %mkrel 3

Name: %{name}
Version: %{version}
Release: %{release}
Summary: Tool for previewing DVI files on text-only devices
Group: Text tools
URL: http://siag.nu/o3read/
Source: http://siag.nu/pub/o3read/%{name}-%{version}.tar.bz2
Patch0: dvi2tty-5.3.1-pager.patch
Patch1: dvi2tty-5.3.1-malloc.patch
License: GPL
BuildRoot: %{_tmppath}/%{name}-root

%description
dvi2tty is a tool for previewing DVI files on text-only devices. It is
used by MC for viewing DVI files.

%prep
%setup -q
%patch0 -p1 -b .pager
%patch1 -p1 -b .malloc

%build
%make

%install
rm -rf %buildroot
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_mandir/man1
install -m 755 dvi2tty disdvi %buildroot%_bindir
install -m 644 dvi2tty.1 disdvi.1 %buildroot%_mandir/man1

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%_bindir/*
%_mandir/*/*


