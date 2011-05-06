Summary:	Linux USB utilities
Name:		usbutils
Version:	0.91
Release:	%mkrel 2
License:	GPLv2+
Group:		System/Kernel and hardware
URL:		http://sourceforge.net/projects/linux-usb/
Source0:	http://www.kernel.org/pub/linux/utils/usb/usbutils/%{name}-%{version}.tar.bz2
BuildRequires:	libusb-devel
#BuildRequires:	zlib-devel
BuildConflicts:	glibc < 2.3.4-5mdk
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	ldetect-lst >= 0.1.282

%description
This package contains the lsusb utility for inspecting the devices 
connected to the USB bus. It shows a graphical representation of the 
devices that are currently plugged in, showing the topology of the 
USB bus. It also displays information on each individual device on 
the bus.

%prep
%setup -q

%build
%configure2_5x \
	--disable-zlib
%make

%install
rm -rf %{buildroot}
%makeinstall_std

rm -f %{buildroot}{%{_includedir}/libusb.h,%{_libdir}/libusb*}

# do not package usb.ids, handled by ldetect-lst now
rm -f %{buildroot}/%{_datadir}/usb.ids

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%{_sbindir}/*
%{_bindir}/*
%{_mandir}/*/*
%{_datadir}/pkgconfig/usbutils.pc
