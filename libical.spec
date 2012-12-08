Name: libical
Version: 0.48
Release: 1
Summary: An implementation of basic iCAL protocols
License: LGPLv2+
Group: System/Libraries
Url: http://sourceforge.net/projects/freeassociation/
Source0: http://downloads.sourceforge.net/freeassociation/%{name}-%{version}.tar.gz
BuildRequires: db-devel
BuildRequires: flex
BuildRequires: bison
Buildrequires: cmake

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

%build
%cmake -DICAL_ERRORS_ARE_FATAL=false

# Not ready for nproc
make

%install
%makeinstall_std -C build

%files -n %{develname}
%doc README TODO ChangeLog NEWS TEST THANKS
%doc doc/UsingLibical*
%{_includedir}/*
%{_libdir}/*.a
%{_libdir}/*.so
%{_libdir}/pkgconfig/*


%changelog
* Tue Jan 10 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.48-1
+ Revision: 759405
- version update 0.48

* Fri Apr 29 2011 Funda Wang <fwang@mandriva.org> 0.46-2
+ Revision: 660621
- br db

  + Oden Eriksson <oeriksson@mandriva.com>
    - mass rebuild

* Sat Sep 18 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.46-1mdv2011.0
+ Revision: 579724
- update to new version 0.46

* Mon Jan 04 2010 Emmanuel Andry <eandry@mandriva.org> 0.44-1mdv2010.1
+ Revision: 486241
- New version 0.44

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.43-3mdv2010.0
+ Revision: 425565
- rebuild

* Wed Feb 18 2009 Götz Waschk <waschk@mandriva.org> 0.43-2mdv2009.1
+ Revision: 342342
- disable fatal errors for e-d-s

* Thu Jan 15 2009 Frederic Crozat <fcrozat@mandriva.com> 0.43-1mdv2009.1
+ Revision: 329792
- Release 0.43
- Patch0: fix format security error

* Mon Nov 03 2008 Helio Chissini de Castro <helio@mandriva.com> 0.41-1mdv2009.1
+ Revision: 299524
- Update ical to current version, now finally cmake based

  + Tomasz Pawel Gajc <tpg@mandriva.org>
    - update to new version 0.33

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.31-2mdv2009.0
+ Revision: 267817
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Thu Apr 17 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.31-1mdv2009.0
+ Revision: 195308
- add missing buildrequires on bison
- new version

* Sun Feb 03 2008 Funda Wang <fwang@mandriva.org> 0.30-1mdv2008.1
+ Revision: 161695
- Br flex
- New version 0.30

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Nov 20 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.27-3mdv2008.1
+ Revision: 110798
- obsolete really ancient libical devel package (with mdk tag ;)
- SILENt this is not needed also

* Tue Nov 20 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.27-2mdv2008.1
+ Revision: 110618
- add more explicit provides on devel package
- import libical

