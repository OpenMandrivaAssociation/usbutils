%define	name	usbutils
%define	version	0.73
%define	release	%mkrel 2

Summary:	Linux USB utilities
Name:		%{name}
Version:	%{version}
Release:	%{release}
URL:		http://sourceforge.net/projects/linux-usb/
Source0:	http://prownloads.sourceforge.net/linux-usb/%{name}-%{version}.tar.bz2
# (tpg) http://farragut.flameeyes.is-a-geek.org/articles/2007/05/19/update-on-usb-ids + my few usb ids
Patch1:		%{name}-0.72-usbids-more.patch
License:	GPL
Group:		System/Kernel and hardware
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	libusb-devel
BuildConflicts:	glibc < 2.3.4-5mdk

%description
usbutils contains a utility for inspecting devices connected to the USB bus.
It requires a Linux kernel version 2.3.15 or newer (supporting the
'/proc/bus/usb' interface).

%prep
%setup -q
#%patch1 -p1

%build
%configure2_5x --enable-usbmodules
%make

%install
rm -rf %{buildroot}
%makeinstall_std

rm -f %{buildroot}{%{_includedir}/libusb.h,%{_libdir}/libusb*}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_datadir}/usb.ids
%{_sbindir}/*
%{_mandir}/*/*