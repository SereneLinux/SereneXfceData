Summary: serene_xfcedata
Name: serene_xfcedata
Version: 1.0.0
Release: 9%{?dist}
Group: User Interface/Desktops
License: NONE
Packager: kokkiemouse
Vendor: INDETAIL

Source0: https://github.com/SereneLinux/SereneXfceData/archive/1ebe42cfaefb7aea86f389c497aa581f728bca9f.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
%global debug_package %{nil}
%description
serenelinux livetools
%prep
rm -rf $RPM_BUILD_ROOT

%autosetup -n SereneXfceData-1ebe42cfaefb7aea86f389c497aa581f728bca9f

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
