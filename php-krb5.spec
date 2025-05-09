#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: phpize
# autospec version: v21
# autospec commit: fbbd4e3
#
Name     : php-krb5
Version  : 1.2.4
Release  : 81
URL      : https://pecl.php.net/get/krb5-1.2.4.tgz
Source0  : https://pecl.php.net/get/krb5-1.2.4.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: php-krb5-lib = %{version}-%{release}
Requires: php-krb5-license = %{version}-%{release}
BuildRequires : buildreq-php
BuildRequires : file
BuildRequires : krb5-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Kerberos, GSSAPI and KADM5 bindings
Features:
+ An interface for maintaining credential caches (KRB5CCache),
that can be used for authenticating against a kerberos5 realm
+ Bindings for nearly the complete GSSAPI (RFC2744)
+ The administrative interface (KADM5)
+ Support for HTTP Negotiate authentication via GSSAPI

%package dev
Summary: dev components for the php-krb5 package.
Group: Development
Requires: php-krb5-lib = %{version}-%{release}
Provides: php-krb5-devel = %{version}-%{release}
Requires: php-krb5 = %{version}-%{release}

%description dev
dev components for the php-krb5 package.


%package lib
Summary: lib components for the php-krb5 package.
Group: Libraries
Requires: php-krb5-license = %{version}-%{release}

%description lib
lib components for the php-krb5 package.


%package license
Summary: license components for the php-krb5 package.
Group: Default

%description license
license components for the php-krb5 package.


%prep
%setup -q -n krb5-1.2.4
cd %{_builddir}/krb5-1.2.4
pushd ..
cp -a krb5-1.2.4 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
%configure --disable-static
make  %{?_smp_mflags}

%install
mkdir -p %{buildroot}/usr/share/package-licenses/php-krb5
cp %{_builddir}/krb5-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/php-krb5/aad4b713782c4db74d175063937b5fc1c97063db || :
%make_install

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/php/ext/krb5/php_krb5.h
/usr/include/php/ext/krb5/php_krb5_compat.h
/usr/include/php/ext/krb5/php_krb5_gssapi.h

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20240924/krb5.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/php-krb5/aad4b713782c4db74d175063937b5fc1c97063db
