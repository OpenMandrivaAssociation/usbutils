Summary:	Linux USB utilities
Name:		usbutils
Version:	005
Release:	1
License:	GPLv2+
Group:		System/Kernel and hardware
URL:		https://github.com/gregkh/usbutils
Source0:	http://www.kernel.org/pub/linux/utils/usb/usbutils/%{name}_%{version}.orig.tar.gz
BuildRequires:	libusb-devel
#BuildRequires:	zlib-devel
BuildConflicts:	glibc < 2.3.4-5mdk
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
./autogen.sh
%configure2_5x \
	--disable-zlib
%make

%install
%makeinstall_std

rm -f %{buildroot}{%{_includedir}/libusb.h,%{_libdir}/libusb*}

# do not package usb.ids, handled by ldetect-lst now
rm -f %{buildroot}/%{_datadir}/usb.ids

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%{_sbindir}/*
%{_bindir}/*
%{_mandir}/*/*
%{_datadir}/pkgconfig/usbutils.pc
