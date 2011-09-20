Summary:	mozvoikko plugin for Mozilla-based applications
Summary(pl.UTF-8):	Wtyczka mozvoikko dla aplikacji opartych na Mozilli
Name:		browser-plugin-mozvoikko
Version:	1.10.0
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/voikko/mozvoikko-%{version}.tar.gz
# Source0-md5:	2b88a22a740635760aadbcee7dc3d6ef
URL:		http://voikko.sourceforge.net/
BuildRequires:	libstdc++-devel
BuildRequires:	libvoikko-devel >= 1.7
BuildRequires:	sed >=4.0
BuildRequires:	xulrunner-devel >= 1.9
BuildRequires:	zip
Requires:	xulrunner >= 1.9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mozvoikko plugin for Mozilla-based applications:
- Firefox 3.0 or above
- Thunderbird 3.0 or above
- SeaMonkey 2.0 or above

%description -l pl.UTF-8
Wtyczka mozvoikko dla aplikacji opartych na Mozilli. Obsługiwane są:
- Firefox w wersji 3.0 lub nowszej
- Thunderbird w wersji 3.0 lub nowszej
- SeaMonkey w wersji 2.0 lub nowszej

%prep
%setup -q -n mozvoikko-%{version}

%{__sed} -i -e 's/libxul-unstable/libxul/' src/Makefile.xulrunner
%{__sed} -i -e 's,^CC_LIBS.*,& -L%{_libdir}/xulrunner -lmozalloc,' src/Makefile.xulrunner

%build
%{__make} -f Makefile.xulrunner \
	CC="%{__cxx} -c" \
	CC_LINK="%{__cxx} -shared -Wl,--no-undefined" \
	CFLAGS="%{rpmcxxflags}" \
	XULRUNNER_SDK=%{_libdir}/xulrunner-sdk

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_browserpluginsdir}

%{__make} -f Makefile.xulrunner install-unpacked \
	DESTDIR=$RPM_BUILD_ROOT%{_libdir}/mozilla/extensions

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_libdir}/mozilla/extensions/{b676e3ff-cda7-4e0c-b2b8-74e4bb40a67a}
%dir %{_libdir}/mozilla/extensions/{b676e3ff-cda7-4e0c-b2b8-74e4bb40a67a}/components
%attr(755,root,root) %{_libdir}/mozilla/extensions/{b676e3ff-cda7-4e0c-b2b8-74e4bb40a67a}/components/libmozvoikko.so
%{_libdir}/mozilla/extensions/{b676e3ff-cda7-4e0c-b2b8-74e4bb40a67a}/chrome.manifest
%{_libdir}/mozilla/extensions/{b676e3ff-cda7-4e0c-b2b8-74e4bb40a67a}/install.rdf
