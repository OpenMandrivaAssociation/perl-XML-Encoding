%define module	XML-Encoding
%define version	2.07
%define release	%mkrel 1

Name:		perl-%{module}
Version:	%{version}
Release:	%{release}
Summary:	A perl module for parsing XML encoding maps
License:	Artistic
Group:		Development/Perl
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/XML/%{module}-%{version}.tar.gz
BuildArch:	    noarch
BuildRequires:  perl(XML::Parser)
BuildRoot:	    %{_tmppath}/%{name}-%{version}

%description
This module, which is built as a subclass of XML::Parser, provides a parser for
encoding map files, which are XML files. The file maps/encmap.dtd in the
distribution describes the structure of these files. Calling a parse method
returns the name of the encoding map (obtained from the name attribute of the
root element). The contents of the map are processed through the callback
functions push_prefix, pop_prefix, and range_set.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make OPTIMIZE="%{optflags}"

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_mandir}/*/*
%{_bindir}/*
%{perl_vendorlib}/XML

