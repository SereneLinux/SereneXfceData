Summary: serene_xfcedata
Name: serene_xfcedata
Version: 1.0.0
Release: 1%{?dist}
Group: User Interface/Desktops
License: NONE
Packager: kokkiemouse
Vendor: INDETAIL

Source0: https://github.com/SereneLinux/SereneXfceData/archive/f1e05795591889458c3eff4495bbff920f4f80d6.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
%global debug_package %{nil}
%description
serenelinux livetools
%prep
rm -rf $RPM_BUILD_ROOT

%autosetup -n SereneXfceData-f1e05795591889458c3eff4495bbff920f4f80d6

%build

%install
mkdir -p $RPM_BUILD_ROOT/
cp -arf ./etc $RPM_BUILD_ROOT/


%clean
rm -rf $RPM_BUILD_ROOT

%post

%postun

%files
%config /etc

%changelog
