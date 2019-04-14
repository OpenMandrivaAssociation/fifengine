%define _disable_ld_no_undefined 1
%define _disable_lto 1

%define major 0
%define libname %mklibname fife %{major}
%define devname %mklibname fife -d

Name:		fifengine
Version:	0.4.2
Release:	1
Source0:	https://github.com/fifengine/fifengine/archive/%{name}-%{version}.tar.gz
#Patch0:		fifengine-0.4.1-lib64.patch
Summary:	Isometric game engine
URL:		http://fifengine.net/
License:	LGPL
Group:		System/Libraries
BuildRequires:	cmake ninja
BuildRequires:	pkgconfig(glew)
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(sdl2)
BuildRequires:	pkgconfig(SDL2_ttf)
BuildRequires:	pkgconfig(SDL2_image)
BuildRequires:	pkgconfig(ogg)
BuildRequires:	pkgconfig(openal)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(xcursor)
BuildRequires:	fifechan-sdl-devel
BuildRequires:	fifechan-opengl-devel
BuildRequires:	boost-devel
BuildRequires:	swig
BuildRequires:	tinyxml-devel

%description
FIFE is a free, open-source cross-platform game engine.
It features hardware-accelerated 2D graphics, integrated GUI,
audio support, lighting, map editor supporting top-down and
isometric maps, pathfinding, virtual filesystem and more!

The core is written in C++ which means that it is highly
portable. FIFE currently supports Windows, Linux and Mac.

Games utilizing FIFE are programmed through Python scripting
layer on top of the base C++ API.
Games can be also programmed using the C++ layer directly.

FIFE is open-sourced under the terms of the LGPL license
so you can freely use it in non-commercial and commercial projects.

%package -n %{libname}
Summary:	The FIFE game engine library
Group:		System/Libraries

%description -n %{libname}
The FIFE game engine library

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%package -n python-%{name}
Summary:	Python 3.x bindings to the FIFE game engine
Group:		Development/Python
Requires:	%{libname} = %{EVRD}
Requires:	python2

%description -n python-%{name}
Python 3.x bindings to the FIFE game engine

%prep
%autosetup -p1

%build
%cmake \
	-Dbuild-library:BOOL=ON \
	-DPYTHON_SITE_PACKAGES=%{python_sitearch} \
	-DPYTHON_EXECUTABLE="/usr/bin/python" \
	-G Ninja
%ninja

%install
%ninja_install -C build

%files

%files -n %{libname}
%{_libdir}/libfife.so.%{major}*

%files -n %{devname}
%{_libdir}/libfife.so
%{_includedir}/fife

%files -n python-%{name}
%{python_sitearch}/*.so
%{python_sitelib}/fife
