#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : php-krb5
Version  : 1.1.4
Release  : 24
URL      : https://pecl.php.net/get/krb5-1.1.4.tgz
Source0  : https://pecl.php.net/get/krb5-1.1.4.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: php-krb5-lib = %{version}-%{release}
BuildRequires : buildreq-php
BuildRequires : e2fsprogs-dev
BuildRequires : krb5-dev

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

%description lib
lib components for the php-krb5 package.


%prep
%setup -q -n krb5-1.1.4
cd %{_builddir}/krb5-1.1.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
%configure --disable-static
make  %{?_smp_mflags}

%install
%make_install


%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/php/ext/krb5/php_krb5.h
/usr/include/php/ext/krb5/php_krb5_compat.h
/usr/include/php/ext/krb5/php_krb5_gssapi.h

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20210902/krb5.so
