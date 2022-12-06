# Copyright 2022 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

Name: python-maturin
Epoch: 100
Version: 0.14.4
Release: 1%{?dist}
Summary: Rust/Python Interoperability
License: MIT
URL: https://github.com/PyO3/maturin/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: cargo
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-cython
BuildRequires: python3-devel
BuildRequires: python3-setuptools-rust >= 1.4.0
BuildRequires: python3-tomli >= 1.1.0
BuildRequires: rust >= 1.56.0

%description
Build and publish crates with pyo3, rust-cpython and cffi bindings as
well as rust binaries as python packages.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitearch} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitearch}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-maturin
Summary: Rust/Python Interoperability
Requires: python3
Requires: python3-tomli >= 1.1.0
Provides: python3-maturin = %{epoch}:%{version}-%{release}
Provides: python3dist(maturin) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-maturin = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(maturin) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-maturin = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(maturin) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-maturin
Build and publish crates with pyo3, rust-cpython and cffi bindings as
well as rust binaries as python packages.

%files -n python%{python3_version_nodots}-maturin
%license license-mit
%{_bindir}/*
%{python3_sitearch}/*
%endif

%if !(0%{?suse_version} > 1500)
%package -n python3-maturin
Summary: Rust/Python Interoperability
Requires: python3
Requires: python3-tomli >= 1.1.0
Provides: python3-maturin = %{epoch}:%{version}-%{release}
Provides: python3dist(maturin) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-maturin = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(maturin) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-maturin = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(maturin) = %{epoch}:%{version}-%{release}

%description -n python3-maturin
Build and publish crates with pyo3, rust-cpython and cffi bindings as
well as rust binaries as python packages.

%files -n python3-maturin
%license license-mit
%{_bindir}/*
%{python3_sitearch}/*
%endif

%changelog
