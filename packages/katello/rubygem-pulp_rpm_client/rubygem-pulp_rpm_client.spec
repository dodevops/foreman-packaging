# template: scl
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name pulp_rpm_client

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 3.5.0
Release: 1%{?dist}
Summary: Pulp 3 RPM plugin API Ruby Gem
Group: Development/Languages
License: GPLv2
URL: https://github.com/pulp/pulp_rpm/
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start specfile generated dependencies
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby >= 1.9
Requires: %{?scl_prefix_ruby}ruby(rubygems)
Requires: %{?scl_prefix}rubygem(faraday) >= 0.14.0
Requires: %{?scl_prefix_ruby}rubygem(json) >= 2.1.0
Requires: %{?scl_prefix_ruby}rubygem(json) >= 2.1
Requires: %{?scl_prefix_ruby}rubygem(json) < 3
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby >= 1.9
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
# end specfile generated dependencies

%description
Client bindings for the pulp_rpm pulp3 plugin

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}.

%prep
%{?scl:scl enable %{scl} - << \EOF}
gem unpack %{SOURCE0}
%{?scl:EOF}

%setup -q -D -T -n  %{gem_name}-%{version}

%{?scl:scl enable %{scl} - << \EOF}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%{?scl:EOF}

%build
# Create the gem as gem install only works on a gem file
%{?scl:scl enable %{scl} - << \EOF}
gem build %{gem_name}.gemspec
%{?scl:EOF}

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%{?scl:scl enable %{scl} - << \EOF}
%gem_install
%{?scl:EOF}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/git_push.sh
%exclude %{gem_cache}
%{gem_libdir}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%doc %{gem_instdir}/docs
%{gem_instdir}/pulp_rpm_client.gemspec
%{gem_instdir}/spec

%changelog
* Mon Aug 03 2020 Samir Jha <sjha4@ncsu.edu> 3.5.0-1
- Update to 3.5.0

* Fri Jul 17 2020 Justin Sherrill <jsherril@redhat.com> 3.4.2-1
- Update to 3.4.2

* Mon Jun 08 2020 James Jeffers 3.4.1-1
- Update to 3.4.1

* Mon May 04 2020 Justin Sherrill <jsherril@redhat.com> 3.3.0-1
- Update to 3.3.0

* Thu Mar 26 2020 Samir Jha <sjha4@ncsu.edu> 3.2.0-1
- Update to 3.2.0

* Mon Jan 06 2020 Justin Sherrill <jsherril@redhat.com> 3.0.0-1
- Update to 3.0.0

* Thu Oct 10 2019 <Justin Sherrill> 3.0.0b7.dev01570381057-1
- Initial build generated by gem2rpm using the scl template
