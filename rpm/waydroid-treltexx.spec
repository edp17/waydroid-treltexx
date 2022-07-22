Name:           waydroid-treltexx
Version:        1.0.0
Release:        1
Summary:        Waydroid-treltexx installs the Galaxy Note 4 (treltexx) specific vendor.img, Waydroid.cfg and Waydroid_base.prop.
License:        GPLv3
URL:            https://github.com/edp17/waydroid-treltexx
BuildArch:      noarch
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  systemd
BuildRequires:  desktop-file-utils
Requires:       waydroid

%description
Waydroid uses Linux namespaces (user, pid, uts, net, mount, ipc) to run a full Android system in a container and provide Android applications on any GNU/Linux-based platform.

The Android system inside the container has direct access to any needed hardware.

The Android runtime environment ships with a minimal customized Android system image based on LineageOS. The image is currently based on Android 10.

Waydroid-treltexx installs the Galaxy Note 4 (treltexx) specific vendor.img, Waydroid.cfg and Waydroid_base.prop.

%prep
%setup

%install
mkdir -p %{buildroot}/home/waydroid/images

tar xvzf config/vendor.img.tar.gz -C %{buildroot}/home/waydroid/images/

install -D -m666 config/waydroid.cfg %{buildroot}/home/waydroid/waydroid.cfg
install -D -m644 config/waydroid.prop %{buildroot}/home/waydroid/waydroid.prop
install -D -m644 config/waydroid_base.prop %{buildroot}/home/waydroid/waydroid_base.prop
install -D -m666 config/config_nodes %{buildroot}/home/waydroid/lxc/waydroid/config_nodes
install -D -m666 config/config %{buildroot}/home/waydroid/lxc/waydroid/config

%clean
rm -rf $RPM_BUILD_ROOT

%post
systemctl daemon-reload
systemctl-user daemon-reload
systemctl restart waydroid-container
chmod 777 /home/waydroid

%files
%defattr(-,root,root,-)
%attr(-, defaultuser, users)/home/waydroid
/home/waydroid/images/vendor.img
/home/waydroid/waydroid.cfg
/home/waydroid/waydroid.prop
/home/waydroid/waydroid_base.prop
/home/waydroid/lxc/waydroid/config_nodes
/home/waydroid/lxc/waydroid/config
