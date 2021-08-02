Summary: serene_xfcedata
Name: serene_xfcedata
Version: 1.0.0
Release: 4%{?dist}
Group: User Interface/Desktops
License: NONE
Packager: kokkiemouse
Vendor: INDETAIL

Source0: https://github.com/SereneLinux/SereneXfceData/archive/c90930dd7e722be6af486419bd92be0c58b70f79.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
%global debug_package %{nil}
%description
serenelinux livetools
%prep
rm -rf $RPM_BUILD_ROOT

%autosetup -n SereneXfceData-c90930dd7e722be6af486419bd92be0c58b70f79

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
