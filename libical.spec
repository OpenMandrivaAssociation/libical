%define major 3
%define libname %mklibname ical %{major}
%define libnamess %mklibname icalss %{major}
%define libnamevcal %mklibname icalvcal %{major}
%define libname_cxx %mklibname ical_cxx %{major}
%define libnamess_cxx %mklibname icalss_cxx %{major}
%define libnameglib %mklibname ical-glib %{major}
%define devname %mklibname ical -d
%define glibdevname %mklibname ical-glib -d
%define girmajor 3.0
%define girname %mklibname ical-gir %{girmajor}
%define girmajorglib 3.0
%define girnameglib %mklibname icalglib-gir %{girmajorglib}

Name:		libical
Version:	3.0.8
Release:	1
Summary:	An implementation of basic iCAL protocols
License:	LGPLv2+
Group:		System/Libraries
Url:		https://github.com/libical/libical
Source0:	https://github.com/libical/libical/releases/download/v%{version}/libical-%{version}.tar.gz
Patch0:		libical-3.0.5-no-Lusrlib.patch
# -Qunused-arguments is invalid for gcc, which is called by some g* crap
# tools
Patch1:		libical-3.0.6-no-Qunused-arguments.patch
BuildRequires:	bison
Buildrequires:	cmake
BuildRequires:	flex
BuildRequires:	ninja
BuildRequires:	db-devel >= 18.1
BuildRequires:  vala
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(gtk-doc)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(vapigen)

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

%package -n %{libname_cxx}
Summary:	Files for developing applications that use libical
Group:		System/Libraries

%description -n %{libname_cxx}
Libical is an Open Source implementation of the IETF's iCalendar
Calendaring and Scheduling protocols (RFC 2445, 2446, and 2447).
It parses iCal components and provides a C API for manipulating
the component properties, parameters, and subcomponents.

%package -n %{libnamess_cxx}
Summary:	Files for developing applications that use libical
Group:		System/Libraries

%description -n %{libnamess_cxx}
Libical is an Open Source implementation of the IETF's iCalendar
Calendaring and Scheduling protocols (RFC 2445, 2446, and 2447).
It parses iCal components and provides a C API for manipulating
the component properties, parameters, and subcomponents.

%package -n %{libnameglib}
Summary:	Files for developing glib applications that use libical
Group:		System/Libraries

%description -n %{libnameglib}
Libical is an Open Source implementation of the IETF's iCalendar
Calendaring and Scheduling protocols (RFC 2445, 2446, and 2447).
It parses iCal components and provides a C API for manipulating
the component properties, parameters, and subcomponents.


%package -n %{girname}
Summary: GObject Introspection interface description for ICal
Group: System/Libraries
Requires: %{libname} = %{version}-%{release}
Conflicts: %{_lib}ical3 < 3.0.5-5

%description -n %{girname}
GObject Introspection interface description for ICal.

%files -n %{girname}
%{_libdir}/girepository-1.0/ICal-%{girmajor}.typelib


%package -n %{girnameglib}
Summary: GObject Introspection interface description for ICalGLib
Group: System/Libraries
Requires: %{libnameglib} = %{version}-%{release}
Conflicts: %{_lib}ical-glib3 < 3.0.5-5

%description -n %{girnameglib}
GObject Introspection interface description for ICalGLib.

%files -n %{girnameglib}
%{_libdir}/girepository-1.0/ICalGLib-%{girmajorglib}.typelib


%package -n %{devname}
Summary:	Files for developing applications that use libical
Group:		Development/C
Provides:	%{name}-devel = %{EVRD}
Requires:	%{libname} = %{EVRD}
Requires:	%{libnamess} = %{EVRD}
Requires:	%{libnamevcal} = %{EVRD}
Requires:	%{libname_cxx} = %{EVRD}
Requires:	%{libnamess_cxx} = %{EVRD}
Requires:	%{girname} = %{version}-%{release}
Requires:	%{girnameglib} = %{version}-%{release}
Requires:	db-devel
Obsoletes:	%mklibname ical 0 -d

%description -n %{devname}
The header files and libtool library for
developing applications that use libical.

%package -n %{glibdevname}
Summary:	Files for developing glib applications that use libical
Group:		Development/C
Requires:	%{devname} = %{EVRD}
Requires:	%{libnameglib} = %{EVRD}

%description -n %{glibdevname}
The header files and libtool library for
developing applications that use libical
and glib.

%prep
%autosetup -p1
%cmake  \
         -DICAL_ERRORS_ARE_FATAL=false \
         -G Ninja \
         -DGOBJECT_INTROSPECTION:BOOL=true \
         -DICAL_GLIB_VAPI:BOOL=true

%build
%ninja_build -C build

%install
%ninja_install -C build

%files -n %{libname}
%{_libdir}/libical.so.%{major}*

%files -n %{libnamess}
%{_libdir}/libicalss.so.%{major}*

%files -n %{libnamevcal}
%{_libdir}/libicalvcal.so.%{major}*

%files -n %{libname_cxx}
%{_libdir}/libical_cxx.so.%{major}*

%files -n %{libnamess_cxx}
%{_libdir}/libicalss_cxx.so.%{major}*

%files -n %{libnameglib}
%{_libdir}/libical-glib.so.%{major}*

%files -n %{devname}
%doc TODO TEST THANKS
%doc doc/UsingLibical*
%{_includedir}/libical
%{_libdir}/*.a
%{_libdir}/*.so
%exclude %{_libdir}/libical-glib.so
%exclude %{_libdir}/libical-glib.a
%{_libdir}/pkgconfig/libical.pc
%{_libdir}/cmake/LibIcal
%{_datadir}/gir-1.0/ICal-%{girmajor}.gir
%{_datadir}/gir-1.0/ICalGLib-%{girmajorglib}.gir
%{_datadir}/vala/vapi/libical-glib.vapi

%files -n %{glibdevname}
%doc %{_datadir}/gtk-doc/html/libical-glib
%{_includedir}/libical-glib
%{_libdir}/libical-glib.so
%{_libdir}/libical-glib.a
%{_libdir}/pkgconfig/libical-glib.pc
