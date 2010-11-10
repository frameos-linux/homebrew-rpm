Name:     homebrew
Version:  20101010
Release:  1.frameos
Summary:  The missing package manager for OS X and Linux
Group:    Development/System 
License:  GPL
URL:      http://github.com/mxcl/homebrew
Source0:  %{name}-%{version}.tar.gz
Source1:  README
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: ruby

%description
Homebrew is a cross platform package manager.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}/opt
mkdir -p %{buildroot}/%{_docdir}/%{name}
cp -r $RPM_BUILD_DIR/%{name}-%{version} %{buildroot}/opt/homebrew
cp %{SOURCE1} %{buildroot}/%{_docdir}/%{name}/

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc %{_docdir}/%{name}
/opt/homebrew

%changelog
* Wed Nov 10 2010 Sergio Rubio <rubiojr@frameos.org> 20101010
- Initial Release
