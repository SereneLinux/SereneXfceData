Summary: serene_xfcedata
Name: serene_xfcedata
Version: 1.0.0
Release: 13%{?dist}
Group: User Interface/Desktops
License: NONE
Packager: kokkiemouse
Vendor: INDETAIL

Source0: https://github.com/SereneLinux/SereneXfceData/archive/080b5246c6a6eb0d8dcdeb9fa5ad7edc7c6e9642.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
%global debug_package %{nil}
%description
serenelinux livetools
%prep
rm -rf $RPM_BUILD_ROOT

%autosetup -n SereneXfceData-080b5246c6a6eb0d8dcdeb9fa5ad7edc7c6e9642

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
