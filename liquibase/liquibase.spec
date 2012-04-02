Name: liquibase
Summary: Liquibase Database Refactoring Tool
Version: 2.0.3
Release: 4%{?dist}
License: ASL 2.0
Group: Applications/Databases

# Liquibase does not distribute source releases. To generate:
#   git clone https://github.com/liquibase/liquibase.git
#   cd liquibase-core/
#   git archive --prefix=liquibase-2.0.3/ liquibase-parent-2.0.3 liquibase-core/ samples/ changelog.txt LICENSE.txt | gzip >liquibase-2.0.3.tar.gz
Source0: %{name}-%{version}.tar.gz
Source1: build.xml
# Our custom launcher script:
Source2: liquibase

#Patch0: liquibase-bin.patch

BuildRequires: java >= 0:1.6.0
BuildRequires: servlet25
BuildRequires: ant >= 0:1.7.0

Requires: java >= 0:1.6.0

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
Url: http://liquibase.org/

%description
LiquiBase is an open source (Apache 2.0 License), database-independent library
for tracking, managing and applying database changes. It is built on a simple
premise: All database changes are stored in a human readable yet trackable form
and checked into source control.

%prep
%setup -q
cp -p %SOURCE1 liquibase-core/
cp -p %SOURCE2 .

# Remove the Spring wrapper, this is not available as a build dependency:
rm liquibase-core/src/main/java/liquibase/integration/spring/SpringLiquibase.java

%build
cd liquibase-core
ant -Dlibdir=%{_datarootdir}/java clean package

%install
rm -rf %{buildroot}
#%{__mkdir} -p %{buildroot}%{_libdir}/%{name}/lib/
%{__install} -d -m 755 %{buildroot}%{_datarootdir}/java/
%{__install} -m 0644 -D -p liquibase-core/dist/lib/liquibase.jar %{buildroot}%{_datarootdir}/java/
%{__mkdir} -p %{buildroot}%{_bindir}
%{__install} -m 0755 -D -p liquibase %{buildroot}%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc samples changelog.txt LICENSE.txt
%{_bindir}/%{name}
%{_datarootdir}/java/liquibase.jar


%changelog
* Mon Apr 02 2012 Devan Goodwin <dgoodwin@rm-rf.ca> 2.0.3-4
- Fix missing javax.servlet during compile. (dgoodwin@redhat.com)

* Fri Mar 30 2012 Devan Goodwin <dgoodwin@rm-rf.ca> 2.0.3-3
- Include documentation, better tar.gz generation. (dgoodwin@redhat.com)
- Add custom launcher script. (dgoodwin@redhat.com)
- Add build.xml to compile. (dgoodwin@redhat.com)

* Thu Mar 29 2012 Devan Goodwin <dgoodwin@redhat.com> 2.0.3-2
- Initial packaging attempt.


