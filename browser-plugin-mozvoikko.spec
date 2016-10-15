# TODO: where noarch common mozilla extensions should go?
Summary:	mozvoikko2 plugin for Mozilla-based applications
Summary(pl.UTF-8):	Wtyczka mozvoikko2 dla aplikacji opartych na Mozilli
Name:		browser-plugin-mozvoikko
Version:	2.0.1
Release:	2
License:	GPL v2+
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/voikko/mozvoikko-%{version}.tar.gz
# Source0-md5:	8d3ded01a39f5c1a9c59b4c394c174ba
URL:		http://voikko.sourceforge.net/
BuildRequires:	zip
Requires:	libvoikko >= 1.7
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
%setup -q -n mozvoikko-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/mozilla/extensions/\{89630d4c-c64d-11e0-83d8-00508d9f364f\}

cp -pr components chrome.manifest install.rdf $RPM_BUILD_ROOT%{_libdir}/mozilla/extensions/\{89630d4c-c64d-11e0-83d8-00508d9f364f\}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%dir %{_libdir}/mozilla/extensions/{89630d4c-c64d-11e0-83d8-00508d9f364f}
%dir %{_libdir}/mozilla/extensions/{89630d4c-c64d-11e0-83d8-00508d9f364f}/components
%{_libdir}/mozilla/extensions/{89630d4c-c64d-11e0-83d8-00508d9f364f}/components/MozVoikko2.js
%{_libdir}/mozilla/extensions/{89630d4c-c64d-11e0-83d8-00508d9f364f}/chrome.manifest
%{_libdir}/mozilla/extensions/{89630d4c-c64d-11e0-83d8-00508d9f364f}/install.rdf
