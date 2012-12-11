%define rbname RMagick

Summary:	ImageMagick extension for Ruby
Name:		ruby-%{rbname}
Version:	2.13.1
Release:	%mkrel 3
Group:		Development/Ruby
License:	BSD-like
URL:		http://rmagick.rubyforge.org
Source0:	%{rbname}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
BuildRequires:	imagemagick
BuildRequires:	imagemagick-devel
BuildRequires:	ruby-devel
Provides:	ruby-rvg

%description
A Ruby binding for ImageMagick, a graphics manipulation toolkit.
This release includes RVG.

%prep
%setup -q -n %{rbname}-%{version}

%build
sed -i -e 's/-ldotneato//' ext/RMagick/extconf.rb
ruby setup.rb config --doc-dir=%{buildroot}%{_datadir}/doc/%{name}-%{version} --disable-htmldoc
ruby setup.rb setup

%install
[ "%{buildroot}" != "/" ] && %__rm -rf %{buildroot}
ruby setup.rb install --prefix=%{buildroot}
rm -rf %{buildroot}%{_datadir}/doc/%{name}-%{version}

for f in `find doc examples -name \*.rb`
do
	if head -n1 "$f" | grep '^#!' >/dev/null;
	then
		sed -i 's|/usr/local/bin|/usr/bin|' "$f"
		chmod 0755 "$f"
	else
		chmod 0644 "$f"
	fi
done
chmod 0755 %{buildroot}%{ruby_sitearchdir}/*.so

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc README.html ChangeLog doc examples
%{ruby_sitelibdir}/*.rb
%{ruby_sitelibdir}/rvg
%{ruby_sitearchdir}/*.so




%changelog
* Sat Dec 04 2010 Rémy Clouard <shikamaru@mandriva.org> 2.13.1-3mdv2011.0
+ Revision: 609423
- rebuild for new imagemagick

* Sat Nov 13 2010 Rémy Clouard <shikamaru@mandriva.org> 2.13.1-2mdv2011.0
+ Revision: 597359
- rebuild for new ImageMagick

* Thu Jul 15 2010 Funda Wang <fwang@mandriva.org> 2.13.1-1mdv2011.0
+ Revision: 553641
- new version 2.13.1
- rebuild for new imagemagick

* Thu Jan 14 2010 Funda Wang <fwang@mandriva.org> 2.13.0-1mdv2010.1
+ Revision: 491378
- new version 2.13.0

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 2.9.0-3mdv2010.0
+ Revision: 442805
- rebuild

* Thu Jan 29 2009 Götz Waschk <waschk@mandriva.org> 2.9.0-2mdv2009.1
+ Revision: 335088
- rebuild for new libmagick

* Mon Jan 19 2009 Pascal Terjan <pterjan@mandriva.org> 2.9.0-1mdv2009.1
+ Revision: 331256
- Update to 2.9.0
- Disable HTML doc for now, I did not manage to build it

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Thu Sep 04 2008 Jérôme Soyer <saispo@mandriva.org> 2.5.2-1mdv2009.0
+ Revision: 280692
- New Release

* Thu Jul 10 2008 Adam Williamson <awilliamson@mandriva.org> 2.5.1-1mdv2009.0
+ Revision: 233260
- adjust for slightly changed build system
- clean spec
- new release 2.5.1

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuilt against new imagemagick libs

* Tue Jan 08 2008 Pascal Terjan <pterjan@mandriva.org> 1.15.6-2mdv2008.1
+ Revision: 146584
- Remove the installed doc, we already install it with the macro

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuilt against new imagemagick libs (6.3.7)

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon May 07 2007 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 1.15.6-1mdv2008.0
+ Revision: 24920
- Updated to 1.15.6.


* Sun Mar 04 2007 Pascal Terjan <pterjan@mandriva.org> 1.15.3-1mdv2007.0
+ Revision: 131914
- BuildRequires ImageMagick to build the doc
- Use Development/Ruby group
- 1.15.3
- Use standard macro
- rebuild for new libMagick
- Import ruby-RMagick

* Fri Aug 18 2006 Emmanuel Andry <eandry@mandriva.org> 1.13.0-2mdv2007.0
- rebuild for Imagick

* Tue Jul 04 2006 Emmanuel Andry <eandry@mandriva.org> 1.13.0-1mdv2007.0
- 1.13.0

* Sat Jan 21 2006 Pascal Terjan <pterjan@mandriva.org> 1.9.3-2mdk
- rebuilt

* Sun Oct 30 2005 Pascal Terjan <pterjan@mandriva.org> 1.9.3-1mdk
- 1.9.3

* Sat Sep 17 2005 Pascal Terjan <pterjan@mandriva.org> 1.9.2-1mdk
- 1.9.2

* Fri Sep 09 2005 Pascal Terjan <pterjan@mandriva.org> 1.9.1-1mdk
- 1.9.1
- mkrel

* Thu Aug 25 2005 Oden Eriksson <oeriksson@mandriva.com> 1.9.0-2mdk
- rebuilt against new Magick libs

* Mon Jul 18 2005 Pascal Terjan <pterjan@mandriva.org> 1.9.0-1mdk
- 1.9.0

* Fri Jul 08 2005 Pascal Terjan <pterjan@mandriva.org> 1.8.3-2mdk
- Don't own %%{ruby_archdir}

* Sun Jun 19 2005 Pascal Terjan <pterjan@mandriva.org> 1.8.3-1mdk
- 1.8.3
- fix rights on examples

* Sun Jun 12 2005 Pascal Terjan <pterjan@mandriva.org> 1.8.2-1mdk
- 1.8.2

* Fri Jun 03 2005 Pascal Terjan <pterjan@mandriva.org> 1.8.1-1mdk
- First package

