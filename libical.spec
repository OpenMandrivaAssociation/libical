Name: libical
Version: 0.43
Release: %mkrel 2
Summary: An implementation of basic iCAL protocols
License: LGPLv2+
Group: System/Libraries
Url: http://sourceforge.net/projects/freeassociation/
Source0: http://downloads.sourceforge.net/freeassociation/%{name}-%{version}.tar.gz
# (fc) 0.43-1mdv fix format security error
Patch0:	libical-0.43-format-security.patch
BuildRequires: db4-devel
BuildRequires: flex
BuildRequires: bison
Buildrequires: cmake
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot

%description
Libical is an Open Source implementation of the IETF's iCalendar
Calendaring and Scheduling protocols (RFC 2445, 2446, and 2447).
It parses iCal components and provides a C API for manipulating
the component properties, parameters, and subcomponents.

#------------------------------------------------------

%define major 0
%define libname %mklibname ical %{major}

%package -n %{libname}
Summary: Files for developing applications that use libical
Group: System/Libraries

%description -n %{libname}
Libical is an Open Source implementation of the IETF's iCalendar
Calendaring and Scheduling protocols (RFC 2445, 2446, and 2447).
It parses iCal components and provides a C API for manipulating
the component properties, parameters, and subcomponents.

%files -n %{libname}
%{_libdir}/*ical.so.%{major}*

#------------------------------------------------------

%define major 0
%define libnamess %mklibname icalss %{major}

%package -n %{libnamess}
Summary: Files for developing applications that use libical
Group: System/Libraries

%description -n %{libnamess}
Libical is an Open Source implementation of the IETF's iCalendar
Calendaring and Scheduling protocols (RFC 2445, 2446, and 2447).
It parses iCal components and provides a C API for manipulating
the component properties, parameters, and subcomponents.

%files -n %{libnamess}
%{_libdir}/*icalss.so.%{major}*

#------------------------------------------------------

%define major 0
%define libnamevcal %mklibname icalvcal %{major}

%package -n %{libnamevcal}
Summary: Files for developing applications that use libical
Group: System/Libraries

%description -n %{libnamevcal}
Libical is an Open Source implementation of the IETF's iCalendar
Calendaring and Scheduling protocols (RFC 2445, 2446, and 2447).
It parses iCal components and provides a C API for manipulating
the component properties, parameters, and subcomponents.

%files -n %{libnamevcal}
%{_libdir}/*vcal.so.%{major}*

#------------------------------------------------------

%define develname %mklibname ical -d

%package -n %{develname}
Summary:	Files for developing applications that use libical
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Requires:	%{libnamess} = %{version}-%{release}
Requires:	%{libnamevcal} = %{version}-%{release}
Obsoletes:	%mklibname ical 0 -d

%description -n %{develname}
The header files and libtool library for
developing applications that use libical.

#------------------------------------------------------

%prep
%setup -q
%patch0 -p1 -b .format-security

%build
%cmake -DICAL_ERRORS_ARE_FATAL=false

# Not ready for nproc
make

%install
rm -fr %buildroot
%makeinstall_std -C build

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files -n %{develname}
%doc README TODO ChangeLog NEWS TEST THANKS
%doc doc/UsingLibical*
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

