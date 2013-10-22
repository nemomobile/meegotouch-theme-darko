Name:       meegotouch-theme-darko
# >> macros
%define theme_name darko
# << macros

Summary:    Darko is a theme for MeeGo Handset/Nemo
Version:    0.3.5
Release:    3
Group:      System/GUI/Other
License:    Creative Commons Attribution-NonCommercial 3.0 Unported License
BuildArch:  noarch
URL:        https://github.com/nemomobile/meegotouch-theme-darko
Source0:    %{name}-%{version}.tar.bz2
Requires:   nemo-theme-default
BuildRequires: fdupes

%description
Darko is a theme for MeeGo Handset/Nemo.

%define theme_dir %{buildroot}%{_datadir}/themes/%{theme_name}
%define graphics_dir %{buildroot}%{_datadir}/themes/%{theme_name}/meegotouch
%define package_dir %{_datadir}/themes/%{theme_name}

%define base_theme base
%define base_theme_dir %{buildroot}%{_datadir}/themes/%{base_theme}
%define base_package_dir %{_datadir}/themes/%{base_theme}

%prep
%setup -q -n %{name}-%{version}

%build

%install
rm -rf %{buildroot}

mkdir -p %{theme_dir}/
install -m 644 index.theme %{theme_dir}/

mkdir -p %{graphics_dir}/icons
install -m 644 meegotouch/icons/* %{graphics_dir}/icons/
install -m 644 blanco/meegotouch/icons/* %{graphics_dir}/icons/

mkdir -p %{graphics_dir}/libmeegotouchviews/style/
install -m 644 meegotouch/libmeegotouchviews/style/* %{graphics_dir}/libmeegotouchviews/style/

mkdir -p %{graphics_dir}/libmeegotouchhome/style/
install -m 644 meegotouch/libmeegotouchhome/style/* %{graphics_dir}/libmeegotouchhome/style/
install -m 644 meegotouch/libmeegotouchhome/libmeegotouchhome.conf %{graphics_dir}/libmeegotouchhome/

mkdir -p %{graphics_dir}/meegotouchhome/style/
install -m 644 meegotouch/meegotouchhome/style/meegotouchhome.css %{graphics_dir}/meegotouchhome/style/

mkdir -p %{base_theme_dir}/meegotouch/icons
install -m 644 meegotouch/icons/icon-l-meegotouchtheme-darko.png %{base_theme_dir}/meegotouch/icons/

mkdir -p %{buildroot}/usr/share/sounds/%{theme_name}/stereo
install -m 644 sounds/%{theme_name}/stereo/* %{buildroot}/usr/share/sounds/%{theme_name}/stereo/

%fdupes  %{buildroot}%{_datadir}

%post
Theme_Key="/meegotouch/theme/name"
Config_Src=`/usr/bin/gconftool-2 --get-default-source`

Theme_Name=`/usr/bin/gconftool-2 --direct --config-source $Config_Src \
            -g $Theme_Key`

if [ -z "$Theme_Name" ]; then
    echo "Setting theme name to %{theme_name}"
    /usr/bin/gconftool-2 --direct --config-source $Config_Src \
    -s -t string $Theme_Key %{theme_name}
fi

%files
%defattr(-,root,root,-)
%{package_dir}/*
%{base_package_dir}/meegotouch/icons/icon-l-meegotouchtheme-darko.png
%{_datadir}/sounds/%{theme_name}/stereo/*

