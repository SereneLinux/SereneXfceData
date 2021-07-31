Summary: serene_xfcedata
Name: serene_xfcedata
Version: 1.0.0
Release: 3%{?dist}
Group: User Interface/Desktops
License: NONE
Packager: kokkiemouse
Vendor: INDETAIL

Source0: https://github.com/SereneLinux/SereneXfceData/archive/e46ab2e3f6be9d613fd4c46316ded20e39f2c15e.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
%global debug_package %{nil}
%description
serenelinux livetools
%prep
rm -rf $RPM_BUILD_ROOT

%autosetup -n SereneXfceData-e46ab2e3f6be9d613fd4c46316ded20e39f2c15e

%build

%install
mkdir -p $RPM_BUILD_ROOT/
cp -arf ./usr $RPM_BUILD_ROOT/


%clean
rm -rf $RPM_BUILD_ROOT

%post

%postun

%files
/usr/share/serenekun

%changelog
