#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libCharon
Version  : 4.11.0
Release  : 34
URL      : https://github.com/Ultimaker/libCharon/archive/4.11.0/libCharon-4.11.0.tar.gz
Source0  : https://github.com/Ultimaker/libCharon/archive/4.11.0/libCharon-4.11.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-3.0
Requires: libCharon-data = %{version}-%{release}
Requires: libCharon-license = %{version}-%{release}
Requires: libCharon-python = %{version}-%{release}
Requires: libCharon-python3 = %{version}-%{release}
Requires: libCharon-services = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-distutils3
BuildRequires : python3
BuildRequires : python3-dev

%description
# libCharon
File metadata and streaming library
The Charon library is the responsibility of the Embedded Applications team.
Pull requests to MASTER have to be verified by the Embedded Applications team.

%package data
Summary: data components for the libCharon package.
Group: Data

%description data
data components for the libCharon package.


%package license
Summary: license components for the libCharon package.
Group: Default

%description license
license components for the libCharon package.


%package python
Summary: python components for the libCharon package.
Group: Default
Requires: libCharon-python3 = %{version}-%{release}
Provides: libcharon-python

%description python
python components for the libCharon package.


%package python3
Summary: python3 components for the libCharon package.
Group: Default
Requires: python3-core

%description python3
python3 components for the libCharon package.


%package services
Summary: services components for the libCharon package.
Group: Systemd services

%description services
services components for the libCharon package.


%prep
%setup -q -n libCharon-4.11.0
cd %{_builddir}/libCharon-4.11.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1635748166
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1635748166
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libCharon
cp %{_builddir}/libCharon-4.11.0/LICENSE %{buildroot}/usr/share/package-licenses/libCharon/2fa84abcb9ebd82e02a9ba263551d24b04e8c691
pushd clr-build
%make_install
popd
## install_append content
for src in %{buildroot}/usr/lib64/python*/site-packages; do dest=$(sed 's!/usr/lib64/!/usr/lib/!' <<< ${src}); mkdir -p $(dirname ${dest}); mv ${src} $(dirname ${dest}); done
## install_append end

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/dbus-1/system.d/nl.ultimaker.charon.conf

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libCharon/2fa84abcb9ebd82e02a9ba263551d24b04e8c691

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/charon.service
