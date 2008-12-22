Summary:	SDL graphics drawing primitives and other support functions
Summary(pl.UTF-8):	Funkcje rysowania grafiki i inne dla SDL
Name:		SDL_gfx
Version:	2.0.18
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://www.ferzkopp.net/Software/SDL_gfx-2.0/%{name}-%{version}.tar.gz
# Source0-md5:	b107fd478d3d1269d7a6ff42906f0482
Patch0:		%{name}-local-labels.patch
URL:		http://www.ferzkopp.net/Software/SDL_gfx-2.0/
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	autoconf >= 2.59-9
BuildRequires:	automake
BuildRequires:	libjpeg-devel
BuildRequires:	libpng >= 1.0.8
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The SDL_gfx library evolved out of the SDL_gfxPrimitives code.

The current components of the SDL_gfx library are:
- Graphic Primitives (SDL_gfxPrimitves.h)
- Rotozoomer (SDL_rotozoom.h)
- Framerate control (SDL_framerate.h)
- MMX image filters (SDL_imageFilter.h)

The library is backwards compatible to the above mentioned code. It's
is written in plain C and can be used in C++ code.

%description -l pl.UTF-8
Biblioteka SDL_gfx wyewoluowała z kodu SDL_gfxPrimitives.

Aktualnie SDL_gfx zawiera następujące komponenty:
- prymitywy graficzne (SDL_gfxPrimitives.h)
- Rotozoomer (SDL_rotozoom.h)
- kontrola szybkości rysowania obrazu (SDL_framerate.h)
- filtry obrazów używające MMX (SDL_imageFilter.h).

Biblioteka jest wstecznie kompatybilna z wyżej wspomnianym kodem. Jest
napisana w czystym C, może też być używana w kodzie C++.

%package devel
Summary:	Header files and more to develop SDL_gfx applications
Summary(pl.UTF-8):	Pliki nagłówkowe do rozwijania aplikacji używających SDL_gfx
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	SDL-devel

%description devel
Header files and more to develop SDL_gfx applications.

%description devel -l pl.UTF-8
Pliki nagłówkowe do rozwijania aplikacji używających SDL_gfx.

%package static
Summary:	Static SDL_gfx libraries
Summary(pl.UTF-8):	Statyczne biblioteki SDL_gfx
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static SDL_gfx libraries.

%description static -l pl.UTF-8
Statyczne biblioteki SDL_gfx.

%prep
%setup -q
%patch0 -p1

%build
rm -f acinclude.m4
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}

%configure \
%ifnarch %{ix86}
	--disable-mmx
%endif

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README AUTHORS ChangeLog
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libSDL_gfx.so.0

%files devel
%defattr(644,root,root,755)
%doc Docs/*
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/SDL/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
