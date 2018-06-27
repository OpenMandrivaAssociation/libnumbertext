%define api	1.0
%define major	0
%define libname	%mklibname numbertext %{api} %{major}
%define devname	%mklibname -d numbertext

Summary:	Library for converting numbers to text
Name:		libnumbertext
Version:	1.0.2
Release:	1
Group:		System/Libraries
License:	LGPLv2+
Url:		https://numbertext.github.io/
Source0:	https://github.com/Numbertext/libnumbertext/releases/download/1.0.beta3/libnumbertext-%{version}.tar.xz


%description
We provide easy to configure, lightweight open source C++, Java, JavaScript,
Python libraries and a LibreOffice Spreadsheet extension for number to
number name conversion, including cardinal and ordinal numbers, ordinal
indicators and money amounts with currencies in more than 30 languages and
numeral systems.

%package -n %{libname}
Summary:	Library for converting numbers to number names
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{libname}
Library for converting numbers to number names

%package -n %{devname}
Summary:	Files for developing with libnumbertext
Group:		Development/C++
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
Includes and definitions for developing with libnumbertext

%prep
%autosetup -p1

%build
%configure
%make 

%install
%makeinstall_std

%files
%{_bindir}/spellout
%{_datadir}/libnumbertext

%files -n %{libname}
%{_libdir}/libnumbertext-%{api}.so.%{major}*

%files -n %{devname}
%{_libdir}/libnumbertext*.so
%{_libdir}/pkgconfig/libnumbertext*.pc
%{_includedir}/*

