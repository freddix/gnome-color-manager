Summary:	Color profile manager for the GNOME desktop
Name:		gnome-color-manager
Version:	3.12.1
Release:	2
License:	GPL v2
Group:		X11/Applications
Source0:	http://download.gnome.org/sources/gnome-color-manager/3.12/%{name}-%{version}.tar.xz
# Source0-md5:	ab31c36b5f21d25fc27a3a070cdc48ad
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	clutter-gtk-devel
BuildRequires:	colord-gtk-devel
BuildRequires:	exiv2-devel
BuildRequires:	gnome-desktop-devel >= 3.12.0
BuildRequires:	intltool
BuildRequires:	lcms2-devel
BuildRequires:	libcanberra-gtk3-devel
BuildRequires:	libtool
BuildRequires:	mash-devel
BuildRequires:	pkg-config
BuildRequires:	udev-glib-devel
BuildRequires:	vte-devel
BuildRequires:	xorg-libXxf86vm-devel
Requires(post,postun):	/usr/bin/gtk-update-icon-cache
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	hicolor-icon-theme
Requires:	colord
Suggests:	argyllcms
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/%{name}

%description
Color profile manager for the GNOME desktop.

%prep
%setup -q

# kill gnome common deps
sed -i -e 's/GNOME_COMPILE_WARNINGS.*//g'	\
    -i -e 's/GNOME_MAINTAINER_MODE_DEFINES//g'	\
    -i -e 's/GNOME_COMMON_INIT//g'		\
    -i -e 's/GNOME_CXX_WARNINGS.*//g'		\
    -i -e 's/GNOME_DEBUG_CHECK//g' configure.ac

%build
%{__libtoolize}
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome --with-omf

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database
%update_icon_cache hicolor

%postun
%update_desktop_database
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/*
%dir %{_libexecdir}
%attr(755,root,root) %{_libexecdir}/gcm-helper-exiv

%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/*/*/*.png
%{_iconsdir}/hicolor/*/*/*.svg

