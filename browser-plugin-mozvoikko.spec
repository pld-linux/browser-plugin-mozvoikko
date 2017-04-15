# TODO: where noarch common mozilla extensions should go?
Summary:	mozvoikko2 plugin for Mozilla-based applications
Summary(pl.UTF-8):	Wtyczka mozvoikko2 dla aplikacji opartych na Mozilli
Name:		browser-plugin-mozvoikko
Version:	2.2
Release:	1
License:	GPL v2+
Group:		X11/Applications
#Source0Download: https://github.com/voikko/mozvoikko/releases
Source0:	https://github.com/voikko/mozvoikko/archive/rel-%{version}/mozvoikko-%{version}.tar.gz
# Source0-md5:	7c6d4bb09b60921c4c6a11fcc8d2bc9d
URL:		http://voikko.puimula.org/
BuildRequires:	zip
Requires:	libvoikko >= 3.1
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mozvoikko2 plugin for Mozilla-based applications:
- Firefox 4.0 or above
- Thunderbird 5.0 or above
- SeaMonkey 2.2 or above

%description -l pl.UTF-8
Wtyczka mozvoikko2 dla aplikacji opartych na Mozilli. Obsługiwane są:
- Firefox w wersji 4.0 lub nowszej
- Thunderbird w wersji 5.0 lub nowszej
- SeaMonkey w wersji 2.2 lub nowszej

%prep
%setup -q -n mozvoikko-rel-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/mozilla/extensions/\{89630d4c-c64d-11e0-83d8-00508d9f364f\}

cp -pr components chrome.manifest install.rdf $RPM_BUILD_ROOT%{_libdir}/mozilla/extensions/\{89630d4c-c64d-11e0-83d8-00508d9f364f\}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README README.user
%dir %{_libdir}/mozilla/extensions/{89630d4c-c64d-11e0-83d8-00508d9f364f}
%dir %{_libdir}/mozilla/extensions/{89630d4c-c64d-11e0-83d8-00508d9f364f}/components
%{_libdir}/mozilla/extensions/{89630d4c-c64d-11e0-83d8-00508d9f364f}/components/MozVoikko2.js
%{_libdir}/mozilla/extensions/{89630d4c-c64d-11e0-83d8-00508d9f364f}/chrome.manifest
%{_libdir}/mozilla/extensions/{89630d4c-c64d-11e0-83d8-00508d9f364f}/install.rdf
