%define modname	XML-Encoding
%define modver	2.08

Summary:	A perl module for parsing XML encoding maps
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	6
License:	Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/XML/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires:	perl(XML::Parser)

%description
This module, which is built as a subclass of XML::Parser, provides a parser for
encoding map files, which are XML files. The file maps/encmap.dtd in the
distribution describes the structure of these files. Calling a parse method
returns the name of the encoding map (obtained from the name attribute of the
root element). The contents of the map are processed through the callback
functions push_prefix, pop_prefix, and range_set.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make OPTIMIZE="%{optflags}"

%check
make test

%install
%makeinstall_std

%files
%{_bindir}/*
%{perl_vendorlib}/XML
%{_mandir}/man1/*
%{_mandir}/man3/*

