# libical is used by bluez,
# bluez is used by sbc,
# sbc is used by pulseaudio,
# pulseaudio is used by wine
%ifarch %{x86_64}
%bcond_without compat32
%endif

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
%define lib32name %mklib32name ical %{major}
%define lib32namess %mklib32name icalss %{major}
%define lib32namevcal %mklib32name icalvcal %{major}
%define lib32name_cxx %mklib32name ical_cxx %{major}
%define lib32namess_cxx %mklib32name icalss_cxx %{major}
%define lib32nameglib %mklib32name ical-glib %{major}
%define dev32name %mklib32name ical -d
%define glib32devname %mklib32name ical-glib -d

Name:		libical
Version:	3.0.16
Release:	3
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
BuildRequires:	cmake
BuildRequires:	flex
BuildRequires:	ninja
BuildRequires:	db-devel >= 18.1
BuildRequires:  vala
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(gtk-doc)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(vapigen)
%if %{with compat32}
BuildRequires:	devel(libpcre)
BuildRequires:	devel(libglib-2.0)
BuildRequires:	devel(libxml2)
BuildRequires:	devel(libffi)
%endif

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

%if %{with compat32}
%package -n %{lib32name}
Summary:	Files for developing applications that use libical (32-bit)
Group:		System/Libraries

%description -n %{lib32name}
Libical is an Open Source implementation of the IETF's iCalendar
Calendaring and Scheduling protocols (RFC 2445, 2446, and 2447).
It parses iCal components and provides a C API for manipulating
the component properties, parameters, and subcomponents.

%package -n %{lib32namess}
Summary:	Files for developing applications that use libical (32-bit)
Group:		System/Libraries

%description -n %{lib32namess}
Libical is an Open Source implementation of the IETF's iCalendar
Calendaring and Scheduling protocols (RFC 2445, 2446, and 2447).
It parses iCal components and provides a C API for manipulating
the component properties, parameters, and subcomponents.

%package -n %{lib32namevcal}
Summary:	Files for developing applications that use libical (32-bit)
Group:		System/Libraries

%description -n %{lib32namevcal}
Libical is an Open Source implementation of the IETF's iCalendar
Calendaring and Scheduling protocols (RFC 2445, 2446, and 2447).
It parses iCal components and provides a C API for manipulating
the component properties, parameters, and subcomponents.

%package -n %{lib32name_cxx}
Summary:	Files for developing applications that use libical (32-bit)
Group:		System/Libraries

%description -n %{lib32name_cxx}
Libical is an Open Source implementation of the IETF's iCalendar
Calendaring and Scheduling protocols (RFC 2445, 2446, and 2447).
It parses iCal components and provides a C API for manipulating
the component properties, parameters, and subcomponents.

%package -n %{lib32namess_cxx}
Summary:	Files for developing applications that use libical (32-bit)
Group:		System/Libraries

%description -n %{lib32namess_cxx}
Libical is an Open Source implementation of the IETF's iCalendar
Calendaring and Scheduling protocols (RFC 2445, 2446, and 2447).
It parses iCal components and provides a C API for manipulating
the component properties, parameters, and subcomponents.

%package -n %{lib32nameglib}
Summary:	Files for developing glib applications that use libical (32-bit)
Group:		System/Libraries

%description -n %{lib32nameglib}
Libical is an Open Source implementation of the IETF's iCalendar
Calendaring and Scheduling protocols (RFC 2445, 2446, and 2447).
It parses iCal components and provides a C API for manipulating
the component properties, parameters, and subcomponents.

%package -n %{dev32name}
Summary:	Files for developing applications that use libical (32-bit)
Group:		Development/C
Requires:	%{devname} = %{EVRD}
Requires:	%{lib32name} = %{EVRD}
Requires:	%{lib32namess} = %{EVRD}
Requires:	%{lib32namevcal} = %{EVRD}
Requires:	%{lib32name_cxx} = %{EVRD}
Requires:	%{lib32namess_cxx} = %{EVRD}

%description -n %{dev32name}
The header files and libtool library for
developing applications that use libical.

%package -n %{glib32devname}
Summary:	Files for developing glib applications that use libical (32-bit)
Group:		Development/C
Requires:	%{glibdevname} = %{EVRD}
Requires:	%{dev32name} = %{EVRD}
Requires:	%{lib32nameglib} = %{EVRD}

%description -n %{glib32devname}
The header files and libtool library for
developing applications that use libical
and glib.
%endif

%prep
%autosetup -p1
%if %{with compat32}
# Don't find lib64/libdb.so.* as a valid BDB...
sed -i -e 's,"lib64","libNO64",g' cmake/modules/FindBerkeleyDB.cmake
%cmake32  \
         -DICAL_ERRORS_ARE_FATAL=false \
         -G Ninja \
         -DGOBJECT_INTROSPECTION:BOOL=false \
         -DICAL_GLIB_VAPI:BOOL=false
cd ..
# Make 64bit great again
sed -i -e 's,"libNO64","lib64",g' cmake/modules/FindBerkeleyDB.cmake
touch -d "2022/01/01 00:01:02" cmake/modules/FindBerkeleyDB.cmake
%endif

%cmake  \
         -DICAL_ERRORS_ARE_FATAL=false \
         -G Ninja \
         -DGOBJECT_INTROSPECTION:BOOL=true \
         -DICAL_GLIB_VAPI:BOOL=true

%build
%if %{with compat32}
%ninja_build -C build32
%endif
%ninja_build -C build

%install
%if %{with compat32}
%ninja_install -C build32
%endif
%ninja_install -C build

# remove not needed stuff
rm %{buildroot}/%{_libexecdir}/libical/ical-glib-src-generator

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

%if %{with compat32}
%files -n %{lib32name}
%{_prefix}/lib/libical.so.%{major}*

%files -n %{lib32namess}
%{_prefix}/lib/libicalss.so.%{major}*

%files -n %{lib32namevcal}
%{_prefix}/lib/libicalvcal.so.%{major}*

%files -n %{lib32name_cxx}
%{_prefix}/lib/libical_cxx.so.%{major}*

%files -n %{lib32namess_cxx}
%{_prefix}/lib/libicalss_cxx.so.%{major}*

%files -n %{lib32nameglib}
%{_prefix}/lib/libical-glib.so.%{major}*

%files -n %{dev32name}
%{_prefix}/lib/*.a
%{_prefix}/lib/*.so
%exclude %{_prefix}/lib/libical-glib.so
%exclude %{_prefix}/lib/libical-glib.a
%{_prefix}/lib/pkgconfig/libical.pc
%{_prefix}/lib/cmake/LibIcal

%files -n %{glib32devname}
%{_prefix}/lib/libical-glib.so
%{_prefix}/lib/libical-glib.a
%{_prefix}/lib/pkgconfig/libical-glib.pc
%endif
