%define major 1
%define libname %mklibname ical %{major}
%define libnamess %mklibname icalss %{major}
%define libnamevcal %mklibname icalvcal %{major}
%define devname %mklibname ical -d

Name:		libical
Version:	1.0
Release:	2
Summary:	An implementation of basic iCAL protocols

License:	LGPLv2+
Group:		System/Libraries
Url:		http://sourceforge.net/projects/freeassociation/
Source0:	http://downloads.sourceforge.net/freeassociation/%{name}-%{version}.tar.gz
BuildRequires:	bison
Buildrequires:	cmake
BuildRequires:	flex
BuildRequires:	db-devel

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

%package -n %{libnamess}
Summary:	Files for developing applications that use libical

Group:		System/Libraries

%description -n %{libnamess}
Libical is an Open Source implementation of the IETF's iCalendar
Calendaring and Scheduling protocols (RFC 2445, 2446, and 2447).
It parses iCal components and provides a C API for manipulating
the component properties, parameters, and subcomponents.

%package -n %{libnamevcal}
Summary:	Files for developing applications that use libical

Group:		System/Libraries

%description -n %{libnamevcal}
Libical is an Open Source implementation of the IETF's iCalendar
Calendaring and Scheduling protocols (RFC 2445, 2446, and 2447).
It parses iCal components and provides a C API for manipulating
the component properties, parameters, and subcomponents.

%package -n %{devname}
Summary:	Files for developing applications that use libical

Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Requires:	%{libnamess} = %{version}-%{release}
Requires:	%{libnamevcal} = %{version}-%{release}
Obsoletes:	%mklibname ical 0 -d

%description -n %{devname}
The header files and libtool library for
developing applications that use libical.

%prep
%setup -q

%build
%cmake \
	-DICAL_ERRORS_ARE_FATAL=false

# Not ready for nproc
make

%install
%makeinstall_std -C build

%files -n %{libname}
%{_libdir}/libical.so.%{major}*

%files -n %{libnamess}
%{_libdir}/libicalss.so.%{major}*

%files -n %{libnamevcal}
%{_libdir}/libicalvcal.so.%{major}*

%files -n %{devname}
%doc README TODO ChangeLog NEWS TEST THANKS
%doc doc/UsingLibical*
%{_includedir}/*
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/pkgconfig/*


