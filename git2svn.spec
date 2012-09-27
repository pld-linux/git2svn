%include	/usr/lib/rpm/macros.perl
Summary:	git2svn - converts a git branch to a svn ditto
Name:		git2svn
Version:	0.4
Release:	1
License:	MIT
Source0:	http://repo.or.cz/w/git2svn.git/snapshot/be694f8968b25339e5f3f05e462bc85d43148280.tar.gz#/%{name}-%{version}.tgz
# Source0-md5:	53c5cfee8719dbe3f8e04dc7b96636c6
Group:		Development/Languages
URL:		http://repo.or.cz/w/git2svn.git
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.484
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program will convert a git branch to a svn ditto, it also support
incremantal updates.

%prep
%setup -qc
mv %{name}/%{name} %{name}.pl
mv %{name}/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
cp -p %{name}.pl $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README LICENSE doc/*
%attr(755,root,root) %{_bindir}/git2svn
