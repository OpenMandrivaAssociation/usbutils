%define	name	usbutils
%define	version	0.72
%define	release	%mkrel 2

Summary:	Linux USB utilities
Name:		%{name}
Version:	%{version}
Release:	%{release}
URL:		http://sourceforge.net/projects/linux-usb/
Source0:	http://prownloads.sourceforge.net/linux-usb/%{name}-%{version}.tar.bz2
# 1.222 2005/11/18
#Source1: 	http://www.linux-usb.org/usb.ids
#Patch0:		usbutils-0.70-fix-usage.patch.bz2
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
#%patch0 -p1

#cp -a %{SOURCE1} usb.ids

%build
%configure --enable-usbmodules
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

rm -f $RPM_BUILD_ROOT{%_includedir/libusb.h,%_libdir/libusb*}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_mandir}/*/*
%{_datadir}/usb.ids
%{_sbindir}/*


