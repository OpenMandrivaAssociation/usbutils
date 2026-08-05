Summary:	Linux USB utilities
Name:		usbutils
Version:	019
Release:	2
License:	GPLv2+
Group:		System/Kernel and hardware
URL:		https://github.com/gregkh/usbutils
Source0:	http://www.kernel.org/pub/linux/utils/usb/usbutils/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(libusb-1.0)
BuildRequires:	pkgconfig(libudev)
Requires:	hwdata >= 0.314
# udev is not needed in chroots/containers; still useful on real hardware
Suggests:	udev
BuildSystem:	meson

%description
This package contains the lsusb utility for inspecting the devices 
connected to the USB bus. It shows a graphical representation of the 
devices that are currently plugged in, showing the topology of the 
USB bus. It also displays information on each individual device on 
the bus.

%install -a
# do not package usb.ids, handled by hwdata now
rm -f %{buildroot}/%{_datadir}/usb.ids ||:

%files
%{_bindir}/*
%{_mandir}/*/*
