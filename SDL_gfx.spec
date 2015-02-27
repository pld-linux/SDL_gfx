Summary:	SDL graphics drawing primitives and other support functions
Summary(pl.UTF-8):	Funkcje rysowania grafiki i inne dla SDL
Name:		SDL_gfx
Version:	2.0.22
Release:	2
License:	LGPL v2.1+
Group:		Libraries
#Source0Download: http://www.ferzkopp.net/joomla/software-mainmenu-14/4-ferzkopps-linux-software/19-sdlgfx
Source0:	http://www.ferzkopp.net/Software/SDL_gfx-2.0/%{name}-%{version}.tar.gz
# Source0-md5:	330f291f1f09a1bdf397c9b40d92ca41
Patch0:		%{name}-local-labels.patch
URL:		http://www.ferzkopp.net/joomla/software-mainmenu-14/4-ferzkopps-linux-software/19-sdlgfx
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	autoconf >= 2.59-9
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.566
BuildRequires:	sed >= 4.0
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
%undos SDL_imageFilter.c
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
%doc README AUTHORS ChangeLog
%attr(755,root,root) %{_libdir}/libSDL_gfx.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libSDL_gfx.so.13

%files devel
%defattr(644,root,root,755)
%doc Docs/*
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
