Summary:	Linux USB utilities
Name:		usbutils
Version:	0.86
Release:	%mkrel 1
License:	GPLv2+
Group:		System/Kernel and hardware
URL:		http://sourceforge.net/projects/linux-usb/
# alternative URL: http://www.kernel.org/pub/linux/utils/usb/usbutils/
Source0:	http://downloads.sourceforge.net/linux-usb/%{name}-%{version}.tar.bz2
BuildRequires:	libusb-devel
BuildConflicts:	glibc < 2.3.4-5mdk
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%{_sbindir}/*
%{_bindir}/*
%{_datadir}/usb.ids
%{_mandir}/*/*
%_datadir/pkgconfig/usbutils.pc
