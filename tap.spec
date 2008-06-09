%define	name	tap
%define	version	1.01
%define	release	%mkrel 4
%define	major	0
%define	libname	    %mklibname %{name} %{major}
%define develname   %mklibname -d %{name}

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Write tests that implement the Test Anything Protocol
License:	GPL
Group:		System/Libraries
URL:		http://jc.ngo.org.uk/trac-bin/trac.cgi/wiki/LibTap
Source:		http://people.freebsd.org/~nik/public_distfiles/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
The tap library provides functions for writing test scripts that produce output
consistent with the Test Anything Protocol.  A test harness that parses this
protocol can run these tests and produce useful reports indicating their
success or failure.

%package -n	%{libname}
Summary:	Write tests that implement the Test Anything Protocol
Group:		System/Libraries

%description -n	%{libname}
The tap library provides functions for writing test scripts that produce output
consistent with the Test Anything Protocol.  A test harness that parses this
protocol can run these tests and produce useful reports indicating their
success or failure.

%package -n	%{develname} 
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{mklibname -d %{name} 0}

%description -n	%{develname}
This package contains development files for %{name}.

%prep
%setup -q

%build
%configure2_5x
%make CFLAGS+=-UHAVE_LIBPTHREAD

%install
rm -rf %{buildroot}
%makeinstall_std
chmod 644 %{buildroot}%{_libdir}/*.la

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files -n %{libname}
%defattr(-,root,root)
%doc INSTALL README
%{_libdir}/*.so.*

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/*.a
%{_includedir}/*
%{_mandir}/man3/*

