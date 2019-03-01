Name:     FAudio
Version:  19.02
Release:  1%{?dist}
Summary:  FNA is a reimplementation of the Microsoft XNA Game Studio 4.0 Refresh libraries

License:  zlib
URL:      https://fna-xna.github.io/
Source0:  https://github.com/FNA-XNA/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

# https://github.com/FNA-XNA/FAudio/issues/115
Patch0:   FAudio-soname.patch

BuildRequires: cmake
BuildRequires: gcc
BuildRequires: gcc-c++

BuildRequires: SDL2-devel


%description
This is FAudio, an XAudio reimplementation that focuses solely on developing
fully accurate DirectX Audio runtime libraries for the FNA project, including
XAudio2, X3DAudio, XAPO, and XACT3.


%package -n libFAudio
Summary:  %{summary}


%description -n libFAudio
This is FAudio, an XAudio reimplementation that focuses solely on developing
fully accurate DirectX Audio runtime libraries for the FNA project, including
XAudio2, X3DAudio, XAPO, and XACT3.


%package -n libFAudio-devel
Summary:  Development files for the FAudio library
Requires: libFAudio%{?_isa} = %{version}-%{release}


%description -n libFAudio-devel
Development files for the FAudio library.


%prep
%autosetup


%build
%cmake .
%make_build


%install
%make_install


%files -n libFAudio
%license LICENSE
%doc README
%{_libdir}/libFAudio.so.0*


%files -n libFAudio-devel
%{_libdir}/libFAudio.so
%{_libdir}/cmake/FAudio/
%{_includedir}/F3DAudio.h
%{_includedir}/FACT.h
%{_includedir}/FACT3D.h
%{_includedir}/FAPO.h
%{_includedir}/FAPOBase.h
%{_includedir}/FAPOFX.h
%{_includedir}/FAudio.h
%{_includedir}/FAudioFX.h


%changelog
* Thu Feb 28 2019 Michael Cronenworth <mike@cchtml.com> - 19.02-1
- Initial spec file.

