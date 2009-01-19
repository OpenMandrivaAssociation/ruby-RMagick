%define rbname RMagick

Summary:	ImageMagick extension for Ruby
Name:		ruby-%{rbname}
Version:	2.9.0
Release:	%{mkrel 1}
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


