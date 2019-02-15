Summary:	Linux USB utilities
Name:		usbutils
Version:	010
Release:	4
License:	GPLv2+
Group:		System/Kernel and hardware
URL:		https://github.com/gregkh/usbutils
Source0:	http://www.kernel.org/pub/linux/utils/usb/usbutils/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(libusb-1.0)
BuildRequires:	pkgconfig(libudev)
Requires:	hwdata >= 0.314
Requires:	udev
# Used to be just a pkgconfig file that is gone in 010
Obsoletes:	%{name}-devel

%description
This package contains the lsusb utility for inspecting the devices 
connected to the USB bus. It shows a graphical representation of the 
devices that are currently plugged in, showing the topology of the 
USB bus. It also displays information on each individual device on 
the bus.

%prep
%autosetup -p1

%build
%configure \
	--disable-zlib
%make_build

%install
%make_install

# do not package usb.ids, handled by hwdata now
rm -f %{buildroot}/%{_datadir}/usb.ids

%files
%{_bindir}/*
%{_mandir}/*/*
