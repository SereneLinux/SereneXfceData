Summary: serene_xfcedata
Name: serene_xfcedata
Version: 1.0.0
Release: 12%{?dist}
Group: User Interface/Desktops
License: NONE
Packager: kokkiemouse
Vendor: INDETAIL

Source0: https://github.com/SereneLinux/SereneXfceData/archive/8e60f552c3e6a87edf2b2a32d56c44e44224b57b.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
%global debug_package %{nil}
%description
serenelinux livetools
%prep
rm -rf $RPM_BUILD_ROOT

%autosetup -n SereneXfceData-8e60f552c3e6a87edf2b2a32d56c44e44224b57b

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
