%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%global npm_name react-lifecycles-compat

Name: %{?scl_prefix}nodejs-react-lifecycles-compat
Version: 3.0.4
Release: 4%{?dist}
Summary: Backwards compatibility polyfill for React class components
License: MIT
Group: Development/Libraries
URL: https://github.com/reactjs/react-lifecycles-compat#readme
Source0: https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
%if 0%{?scl:1}
BuildRequires: %{?scl_prefix_nodejs}npm
%else
BuildRequires: nodejs-packaging
BuildRequires: npm
%endif
BuildArch: noarch
ExclusiveArch: %{nodejs_arches} noarch
Provides: %{?scl_prefix}npm(%{npm_name}) = %{version}

%description
%{summary}

%prep
%setup -q -n package

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr react-lifecycles-compat.cjs.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr react-lifecycles-compat.es.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr react-lifecycles-compat.js %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr react-lifecycles-compat.min.js %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%check
%{nodejs_symlink_deps} --check

%files
%{nodejs_sitelib}/%{npm_name}
%license LICENSE.md
%doc CHANGELOG.md
%doc README.md

%changelog
* Tue Mar 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 3.0.4-4
- Bump packages to build for el8

* Tue Oct 22 2019 Eric D. Helms <ericdhelms@gmail.com> - 3.0.4-3
- Build for SCL

* Fri Oct 04 2019 Eric D. Helms <ericdhelms@gmail.com> - 3.0.4-2
- Update specs to handle SCL

* Wed Oct 10 2018 Ewoud Kohl van Wijngaarden <ewoud@kohlvanwijngaarden.nl> 3.0.4-1
- Add nodejs-react-lifecycles-compat generated by npm2rpm using the single strategy
