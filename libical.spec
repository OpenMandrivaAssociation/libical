%define major 0
%define libname %mklibname ical %{major}
%define develname %mklibname ical -d

Summary:	An implementation of basic iCAL protocols
Name:		libical
Version:	0.27
Release:	%mkrel 1
License:	LGPLv2+
Group:		System/Libraries
Url:		http://sourceforge.net/projects/freeassociation/
Source:		http://downloads.sourceforge.net/freeassociation/%{name}-%{version}.tar.bz2
#BuildRequires:	flex
BuildRequires:	libdb4.2-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Libical is an Open Source implementation of the IETF's iCalendar
Calendaring and Scheduling protocols (RFC 2445, 2446, and 2447).
It parses iCal components and provides a C API for manipulating
the component properties, parameters, and subcomponents.

%package -n %{libname}
Summary:	Files for developing applications that use libical
Group:		System/Libraries

%description -n %{libname}
Libical is an Open Source implementation of the IETF's iCalendar
Calendaring and Scheduling protocols (RFC 2445, 2446, and 2447).
It parses iCal components and provides a C API for manipulating
the component properties, parameters, and subcomponents.

%package -n %{develname}
Summary:	Files for developing applications that use libical
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n %{develname}
The header files and libtool library for
developing applications that use libical.

%prep
%setup -q

%build
%configure2_5x \
	--disable-static \
	--enable-reentrant \
	--with-devel \
	--with-bdb4 \
	--with-bdb4-dir=%{prefix}
%make

%install
%makeinstall_std

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%{_libdir}/*.so.%{major}*
%{_datadir}/%{name}

%files -n %{develname}
%doc README TODO ChangeLog NEWS TEST THANKS
%doc doc/UsingLibical*
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*a*
