%define rbname RMagick
%define version 1.15.6
%define release %mkrel 1

Summary: ImageMagick extension for Ruby
Name: ruby-%{rbname}
Version: %{version}
Release: %{release}
Group: Development/Ruby
License: BSD-like
URL: http://rmagick.rubyforge.org
Source0: %{rbname}-%{version}.tar.bz2
BuildRequires: imagemagick
BuildRequires: libmagick-devel
BuildRequires: ruby-devel
Provides: ruby-rvg

%description
A binding for ImageMagick and GraphicsMagics.
This release includes RVG. 

%prep
%setup -q -n %rbname-%version

%build
./configure
sed -i -e 's/-ldotneato//' ext/RMagick/extconf.rb
ruby setup.rb config --doc-dir=%{buildroot}%{_datadir}/doc/%{name}-%{version}
make

%install
[ "%{buildroot}" != "/" ] && %__rm -rf %{buildroot}
ruby setup.rb install --prefix=%buildroot
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
%doc README.html README.txt ChangeLog doc examples
%{ruby_sitelibdir}/*.rb
%{ruby_sitelibdir}/rvg
%{ruby_sitearchdir}/*.so


