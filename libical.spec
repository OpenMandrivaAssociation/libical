%define major 0
%define libname %mklibname ical %{major}
%define develname %mklibname ical -d

Summary:	An implementation of basic iCAL protocols
Name:		libical
Version:	0.31
Release:	%mkrel 2
License:	LGPLv2+
Group:		System/Libraries
Url:		http://sourceforge.net/projects/freeassociation/
Source:		http://downloads.sourceforge.net/freeassociation/%{name}-%{version}.tar.gz
BuildRequires:	db4-devel
BuildRequires:	flex
BuildRequires:	bison
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
Requires:	%{libname} = %{version}-%{release}
Obsoletes:	%mklibname ical 0 -d

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
	--with-bdb4-dir=%{_prefix}
%make

%install
rm -fr %buildroot
%makeinstall_std

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%doc README TODO ChangeLog NEWS TEST THANKS
%doc doc/UsingLibical*
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.la
