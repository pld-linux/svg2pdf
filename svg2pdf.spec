Summary:	svg2pdf - convert an SVG file to a PDF file (using cairo)
Summary(pl.UTF-8):   svg2pdf - konwersja plików SVG do PDF przy użyciu cairo
Name:		svg2pdf
Version:	0.1.3
Release:	1
License:	BSD-like
Group:		Applications/Graphics
Source0:	http://cairographics.org/snapshots/%{name}-%{version}.tar.gz
# Source0-md5:	0059ba059ff89931cf37720fcd102d8f
Patch0:		%{name}-fix-as_needed.patch
URL:		http://cairographics.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libsvg-cairo-devel >= 0.1.6
BuildRequires:	pkgconfig
Requires:	libsvg-cairo >= 0.1.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Utility to convert an SVG file to a PDF file (using cairo).

%description -l pl.UTF-8
Narzędzie do konwersji plików SVG do PDF przy użyciu cairo.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
