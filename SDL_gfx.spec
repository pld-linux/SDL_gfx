Summary:	SDL graphics drawing primitives and other support functions
Summary(pl):	Funkcje rysowania grafiki i inne dla SDL
Name:		SDL_gfx
Version:	2.0.3
Release:	2
License:	LGPL
Group:		Libraries
Source0:	http://www.ferzkopp.net/Software/%{name}-2.0/%{name}-%{version}.tar.gz
URL:		http://www.ferzkopp.net/Software/%{name}-2.0/index.html
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libjpeg-devel
BuildRequires:	libpng >= 1.0.8
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_includedir	/usr/X11R6/include/SDL

%description
The SDL_gfx library evolved out of the SDL_gfxPrimitives code.

The current components of the SDL_gfx library are:
- Graphic Primitives (SDL_gfxPrimitves.h)
- Rotozoomer (SDL_rotozoom.h)
- Framerate control (SDL_framerate.h)
- MMX image filters (SDL_imageFilter.h)

The library is backwards compatible to the above mentioned code. It's
is written in plain C and can be used in C++ code.

%description -l pl
Biblioteka SDL_gfx wyewoluowa³a z kodu SDL_gfxPrimitives.

Aktualnie SDL_gfx zawiera nastêpuj±ce komponenty:
- prymitywy graficzne (SDL_gfxPrimitives.h)
- Rotozoomer (SDL_rotozoom.h)
- kontrola szybko¶ci rysowania obrazu (SDL_framerate.h)
- filtry obrazów u¿ywaj±ce MMX (SDL_imageFilter.h).

Biblioteka jest wstecznie kompatybilna z wy¿ej wspomnianym kodem. Jest
napisana w czystym C, mo¿e te¿ byæ u¿ywana w kodzie C++.

%package devel
Summary:	Header files and more to develop SDL_gfx applications
Summary(pl):	Pliki nag³ówkowe do rozwijania aplikacji u¿ywaj±cych SDL_gfx
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	SDL-devel

%description devel
Header files and more to develop SDL_gfx applications.

%description devel -l pl
Pliki nag³ówkowe do rozwijania aplikacji u¿ywaj±cych SDL_gfx.

%package static
Summary:	Static SDL_gfx libraries
Summary(pl):	Statyczne biblioteki SDL_gfx
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Statis SDL_gfx libraries.

%description static -l pl
Statyczne biblioteki SDL_gfx.

%prep
%setup -q

%build
rm -f missing acinclude.m4
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}

%ifarch %{ix86}
%configure
%else
%configure --disable-mmx
%endif

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README AUTHORS ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc *.gz Docs
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
