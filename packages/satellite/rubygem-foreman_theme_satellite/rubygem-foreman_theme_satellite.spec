# template: foreman_plugin
%global gem_name foreman_theme_satellite
%global plugin_name theme_satellite
%global foreman_min_version 3.7.0

%global downstream_build ("%{?dist}" == ".el8sat" || "%{?dist}" == ".el9sat")

Name: rubygem-%{gem_name}
Version: 13.2.0
Release: 2%{?foremandist}%{?dist}
Summary: This is a plugin that enables building a theme for Foreman
License: GPLv3
URL: https://github.com/RedHatSatellite/foreman_theme_satellite
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

%if %{downstream_build}
BuildRequires: foreman_theme_satellite_assets
Requires: satellite-lifecycle
%endif

# start specfile generated dependencies
Requires: foreman >= %{foreman_min_version}
BuildRequires: foreman-assets >= %{foreman_min_version}
BuildRequires: foreman-plugin >= %{foreman_min_version}
Requires: ruby >= 2.7
BuildRequires: ruby >= 2.7
BuildRequires: rubygems-devel
BuildArch: noarch
Provides: foreman-plugin-%{plugin_name} = %{version}
BuildRequires: rubygem(activesupport)
BuildRequires: rubygem(deface)
# end specfile generated dependencies

# start package.json devDependencies BuildRequires
BuildRequires: npm(@babel/core) >= 7.7.0
BuildRequires: npm(@babel/core) < 8.0.0
BuildRequires: npm(@theforeman/builder) >= 4.12.0
# end package.json devDependencies BuildRequires

# start package.json dependencies BuildRequires
# end package.json dependencies BuildRequires

%description
Theme changes for Satellite 6.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n  %{gem_name}-%{version}

%if %{downstream_build}
  rm -rf app/assets/images/%{gem_name}
  cp -a /usr/share/foreman_theme_satellite_assets/%{gem_name} app/assets/images/
%endif

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%foreman_bundlerd_file
%foreman_precompile_plugin -s

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE
%{gem_instdir}/app
%{gem_instdir}/db
%{gem_libdir}
%{gem_instdir}/locale
%exclude %{gem_instdir}/package.json
%exclude %{gem_instdir}/webpack
%exclude %{gem_cache}
%{gem_spec}
%{foreman_bundlerd_plugin}
%{foreman_assets_plugin}
%{foreman_assets_foreman}
%{foreman_webpack_plugin}
%{foreman_webpack_foreman}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile

%posttrans
%{foreman_plugin_log}

%changelog
* Tue Nov 14 2023 Evgeni Golov 13.2.0-2
- Patch package when building downstream

* Fri Nov 10 2023 Foreman Packaging Automation <packaging@theforeman.org> 13.2.0-1
- Update to 13.2.0

* Tue Oct 31 2023 Evgeni Golov 13.1.0-1
- Add rubygem-foreman_theme_satellite generated by gem2rpm using the foreman_plugin template
