%define upstream_name	 XML-Encoding
%define upstream_version 2.08

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	7

Summary:	A perl module for parsing XML encoding maps
License:	Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/XML/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(XML::Parser)
BuildArch:	noarch

%description
This module, which is built as a subclass of XML::Parser, provides a parser for
encoding map files, which are XML files. The file maps/encmap.dtd in the
distribution describes the structure of these files. Calling a parse method
returns the name of the encoding map (obtained from the name attribute of the
root element). The contents of the map are processed through the callback
functions push_prefix, pop_prefix, and range_set.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make OPTIMIZE="%{optflags}"

%check
make test

%install
%makeinstall_std

%files
%{_mandir}/*/*
%{_bindir}/*
%{perl_vendorlib}/XML

%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 2.80.0-4mdv2012.0
+ Revision: 765839
- rebuilt for perl-5.14.2
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 2.80.0-2
+ Revision: 667416
- mass rebuild

* Fri Nov 12 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2.80.0-1mdv2011.0
+ Revision: 596703
- update to 2.08

* Mon Aug 03 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2.70.0-1mdv2011.0
+ Revision: 408237
- rebuild using %%perl_convert_version

* Fri Jan 30 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.07-1mdv2009.1
+ Revision: 335449
- update to new version 2.07

* Wed Jan 21 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.06-1mdv2009.1
+ Revision: 332124
- update to new version 2.06

* Mon Sep 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.05-1mdv2009.1
+ Revision: 284836
- update to new version 2.05

* Thu Jul 10 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.03-1mdv2009.0
+ Revision: 233439
- update to new version 2.03

* Wed Jul 02 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.02-1mdv2009.0
+ Revision: 230686
- new version

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 2.01-3mdv2009.0
+ Revision: 224616
- rebuild

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 2.01-2mdv2008.1
+ Revision: 180652
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Jul 25 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 2.01-1mdv2008.0
+ Revision: 55600
- new version
- spec file clean

* Sat May 05 2007 Olivier Thauvin <nanardon@mandriva.org> 1.01-8mdv2008.0
+ Revision: 23262
- buildrequires
- add check section and test


* Mon Jan 10 2005 Stefan van der Eijk <stefan@mandrake.org> 1.01-7mdk
- upload to contrib

* Thu Aug 14 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.01-6mdk
- rebuild for new perl
- drop $RPM_OPT_FLAGS, noarch..
- use %%makeinstall_std macro

* Tue May 27 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.01-5mdk
- rebuild for new auto{prov,req}

* Wed Jan 29 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.01-4mdk
- enhanced summary & description
- fix license ("This program is free software; you can redistribute it
  and/or modify it under the same terms as Perl itself")

* Wed Jul 10 2002 Pixel <pixel@mandrakesoft.com> 1.01-3mdk
- rebuild for perl 5.8.0

* Mon Oct 15 2001 Stefan van der Eijk <stefan@eijk.nu> 1.01-2mdk
- BuildRequires: perl-devel

* Mon Jun 18 2001 Till Kamppeter <till@mandrakesoft.com> 1.01-1mdk
- Newly introduced for Foomatic.

