Summary:	SDL graphics drawing primitives and other supporting functions
Summary(pl.UTF-8):	Funkcje rysowania grafiki i inne pomocnicze dla SDL
Name:		SDL_gfx
Version:	2.0.26
Release:	2
License:	ZLib (BSD-like)
Group:		Libraries
#Source0Download: http://www.ferzkopp.net/wordpress/2016/01/02/sdl_gfx-sdl2_gfx/
Source0:	http://www.ferzkopp.net/Software/SDL_gfx-2.0/%{name}-%{version}.tar.gz
# Source0-md5:	0b3b5ab5f9e7d10f1faf14d4255db6ba
Patch0:		%{name}-local-labels.patch
URL:		http://www.ferzkopp.net/wordpress/2016/01/02/sdl_gfx-sdl2_gfx/
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	autoconf >= 2.59-9
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig
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
Requires:	SDL-devel >= 1.2.0

%description devel
Header files and more to develop SDL_gfx applications.

%description devel -l pl.UTF-8
Pliki nagłówkowe do rozwijania aplikacji używających SDL_gfx.

%package static
Summary:	Static SDL_gfx library
Summary(pl.UTF-8):	Statyczna biblioteka SDL_gfx
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static SDL_gfx library.

%description static -l pl.UTF-8
Statyczna biblioteka SDL_gfx.

%package apidocs
Summary:	API documentation for SDL_gfx library
Summary(pl.UTF-8):	Dokumentacja API biblioteki SDL_gfx
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for SDL_gfx library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki SDL_gfx.

%prep
%setup -q
%patch0 -p1

%build
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
%doc AUTHORS COPYING ChangeLog LICENSE README
%attr(755,root,root) %{_libdir}/libSDL_gfx.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libSDL_gfx.so.16

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libSDL_gfx.so
%{_libdir}/libSDL_gfx.la
%{_includedir}/SDL/SDL_framerate.h
%{_includedir}/SDL/SDL_gfx*.h
%{_includedir}/SDL/SDL_imageFilter.h
%{_includedir}/SDL/SDL_rotozoom.h
%{_pkgconfigdir}/SDL_gfx.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libSDL_gfx.a

%files apidocs
%defattr(644,root,root,755)
%doc Docs/{Screenshots,html,*.png,index.html}
