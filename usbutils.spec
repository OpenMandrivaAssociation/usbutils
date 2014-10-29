Summary:	Linux USB utilities
Name:		usbutils
Version:	008
Release:	1
License:	GPLv2+
Group:		System/Kernel and hardware
URL:		https://github.com/gregkh/usbutils
Source0:	http://www.kernel.org/pub/linux/utils/usb/usbutils/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(libusb-1.0)
Requires:	ldetect-lst >= 0.1.282
Requires:	udev

%description
This package contains the lsusb utility for inspecting the devices 
connected to the USB bus. It shows a graphical representation of the 
devices that are currently plugged in, showing the topology of the 
USB bus. It also displays information on each individual device on 
the bus.

%package devel
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{name} = %{version}-%{release}

%description devel
Development files and headers for %{name}.


%prep
%setup -q

%build
%configure \
	--disable-zlib
%make

%install
%makeinstall_std

# do not package usb.ids, handled by ldetect-lst now
rm -f %{buildroot}/%{_datadir}/usb.ids

%files
%{_bindir}/*
%{_mandir}/*/*

%files devel
%doc AUTHORS ChangeLog README
%{_datadir}/pkgconfig/usbutils.pc
