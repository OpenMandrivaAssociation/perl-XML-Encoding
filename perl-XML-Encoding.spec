%define module	XML-Encoding
%define version	2.01
%define release	%mkrel 2

Summary:	A perl module for parsing XML encoding maps
Name:		perl-%{module}
Version:	%{version}
Release:	%{release}
License:	Artistic
Group:		Development/Perl
Source0:	%{module}-%{version}.tar.bz2
Url:		http://www.cpan.org
BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-buildroot/
Requires:	perl
BuildArch:	noarch
BuildRequires: perl(XML::Parser)

%description
The %{module} perl module, which is built as a subclass of
XML::Parser, provides a parser for encoding map files, which are XML
files.


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
%{perl_vendorlib}/XML/*

