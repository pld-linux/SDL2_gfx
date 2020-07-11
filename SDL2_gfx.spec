Summary:	Graphics primitives and surface functions for SDL2
Summary(pl.UTF-8):	Funkcje do figur graficznych i powierzchni dla SDL2
Name:		SDL2_gfx
Version:	1.0.4
Release:	1
License:	ZLib (BSD-like)
Group:		Libraries
#Source0Download: https://www.ferzkopp.net/wordpress/2016/01/02/sdl_gfx-sdl2_gfx/
Source0:	https://www.ferzkopp.net/Software/SDL2_gfx/%{name}-%{version}.tar.gz
# Source0-md5:	15f9866c6464ca298f28f62fe5b36d9f
Patch0:		%{name}-local-labels.patch
URL:		https://www.ferzkopp.net/wordpress/2016/01/02/sdl_gfx-sdl2_gfx/
BuildRequires:	SDL2-devel >= 2.0.0
BuildRequires:	autoconf >= 2.59-9
BuildRequires:	automake
BuildRequires:	libtool >= 2:2
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The SDL2_gfx library provides the basic drawing functions such as
lines, circles or polygons provided by SDL_gfx on SDL2 against
renderers of SDL2.

The current components of the SDL_gfx2 library are:
- Graphic Primitives (SDL2_gfxPrimitves.h)
- Surface Rotozoomer (SDL2_rotozoom.h)
- Framerate control (SDL2_framerate.h)
- MMX image filters (SDL2_imageFilter.h).

%description -l pl.UTF-8
Biblioteka SDL2_gfx udostępnia użytkownikom biblioteki SDL2 podstawowe
funkcje do rysowania figur takich jak linie, okręgi czy wielokąty,
udostępniane wcześniej przez SDL_gfx.

Aktualnie SDL2_gfx zawiera następujące komponenty:
- prymitywy graficzne (SDL2_gfxPrimitives.h)
- Rotozoomer (SDL2_rotozoom.h)
- kontrola szybkości rysowania obrazu (SDL2_framerate.h)
- filtry obrazów używające MMX (SDL2_imageFilter.h).

%package devel
Summary:	Header files and more to develop SDL2_gfx applications
Summary(pl.UTF-8):	Pliki nagłówkowe do rozwijania aplikacji używających SDL2_gfx
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	SDL2-devel >= 2.0.0

%description devel
Header files and more to develop SDL2_gfx applications.

%description devel -l pl.UTF-8
Pliki nagłówkowe do rozwijania aplikacji używających SDL2_gfx.

%package static
Summary:	Static SDL2_gfx library
Summary(pl.UTF-8):	Statyczna biblioteka SDL2_gfx
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static SDL2_gfx library.

%description static -l pl.UTF-8
Statyczna biblioteka SDL2_gfx.

%package apidocs
Summary:	API documentation for SDL2_gfx library
Summary(pl.UTF-8):	Dokumentacja API biblioteki SDL2_gfx
Group:		Documentation

%description apidocs
API documentation for SDL2_gfx library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki SDL2_gfx.

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

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libSDL2_gfx.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/libSDL2_gfx-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libSDL2_gfx-1.0.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libSDL2_gfx.so
%{_includedir}/SDL2/SDL2_framerate.h
%{_includedir}/SDL2/SDL2_gfxPrimitives.h
%{_includedir}/SDL2/SDL2_imageFilter.h
%{_includedir}/SDL2/SDL2_rotozoom.h
%{_pkgconfigdir}/SDL2_gfx.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libSDL2_gfx.a

%files apidocs
%defattr(644,root,root,755)
%doc Docs/html/*
