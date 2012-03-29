Name: liquibase
Summary: Liquibase Database Refactoring Tool
Version: 2.0.3
Release: 1%{?dist}
License: ASL 2.0
Group: Applications/Databases

# Liquibase does not distribute source releases. To generate:
#   git clone https://github.com/liquibase/liquibase.git
#   cd liquibase-core/
#   git archive --prefix=liquibase-2.0.3/ -o liquibase-2.0.3.tar liquibase-parent-2.0.3
#   gzip liquibase-2.0.3.tar
Source0: %{name}-%{version}.tar.gz

#Patch0: liquibase-bin.patch

BuildRequires: java >= 0:1.6.0
BuildRequires: ant >= 0:1.7.0

Requires: java >= 0:1.6.0

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
Url: http://liquibase.org/

%description
LiquiBase is an open source (Apache 2.0 License), database-independent library for tracking,
managing and applying database changes. It is built on a simple premise: All
database changes are stored in a human readable yet trackable form and checked
into source control.

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
#%{__mkdir} -p %{buildroot}%{_libdir}/%{name}/lib/
#%{__mkdir} -p %{buildroot}%{_bindir}
#%{__install} -m 0644 -D -p %{name}-%{version}.jar %{buildroot}%{_libdir}/%{name}
#%{__install} -m 0755 -D -p %{name} %{buildroot}%{_bindir}

# Profile.d file
#%{__mkdir} -p %{buildroot}%{_sysconfdir}/profile.d/
#%{__cat} <<EOF >%{buildroot}%{_sysconfdir}/profile.d/liquibase.sh
#export LIQUIBASE_HOME=%{_libdir}/%{name}/
#EOF

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
#%attr(0755,root,root) %{_sysconfdir}/profile.d/%{name}.sh
#%doc docs/* samples changelog.txt LICENSE.txt
#%{_libdir}/%{name}
#%{_bindir}/%{name}



%changelog
* Thu Mar 29 2012 Devan Goodwin <dgoodwin@redhat.com> - 2.0.3
- Initial packaging.


