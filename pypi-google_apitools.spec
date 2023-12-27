#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-google_apitools
Version  : 0.5.32
Release  : 76
URL      : https://files.pythonhosted.org/packages/dc/eb/c26c36463a769a3a9f08847b9bf218cb629ca91877a911bbd6dcf37d9e62/google-apitools-0.5.32.tar.gz
Source0  : https://files.pythonhosted.org/packages/dc/eb/c26c36463a769a3a9f08847b9bf218cb629ca91877a911bbd6dcf37d9e62/google-apitools-0.5.32.tar.gz
Summary  : client libraries for humans
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-google_apitools-bin = %{version}-%{release}
Requires: pypi-google_apitools-python = %{version}-%{release}
Requires: pypi-google_apitools-python3 = %{version}-%{release}
Requires: pypi(fasteners)
BuildRequires : buildreq-distutils3
BuildRequires : pypi(fasteners)
BuildRequires : pypi(httplib2)
BuildRequires : pypi(oauth2client)
BuildRequires : pypi(six)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
===============
        
        |pypi| |build| |coverage|
        
        ``google-apitools`` is a collection of utilities to make it easier to build
        client-side tools, especially those that talk to Google APIs.

%package bin
Summary: bin components for the pypi-google_apitools package.
Group: Binaries

%description bin
bin components for the pypi-google_apitools package.


%package python
Summary: python components for the pypi-google_apitools package.
Group: Default
Requires: pypi-google_apitools-python3 = %{version}-%{release}

%description python
python components for the pypi-google_apitools package.


%package python3
Summary: python3 components for the pypi-google_apitools package.
Group: Default
Requires: python3-core
Provides: pypi(google_apitools)
Requires: pypi(fasteners)
Requires: pypi(httplib2)
Requires: pypi(oauth2client)
Requires: pypi(six)

%description python3
python3 components for the pypi-google_apitools package.


%prep
%setup -q -n google-apitools-0.5.32
cd %{_builddir}/google-apitools-0.5.32
pushd ..
cp -a google-apitools-0.5.32 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1672275522
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gen_client

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
