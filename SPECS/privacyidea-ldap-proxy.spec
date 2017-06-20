%define source_name privacyIDEA-LDAP-Proxy
%define name privacyidea-ldap-proxy
%define version %{getenv:LP_VERSION} 
%define unmangled_version %{version}
%define unmangled_version %{version}
%define release 1
%define root_dir /opt/privacyidea-ldap-proxy/
Name:           %{name}
Version:        %{version}
Release:        1%{?dist}
Summary:        LDAP Proxy to intercept LDAP binds and authenticate against privacyIDEA

Group:          Applications/System
License:        AGPLv3
URL:            https://www.privacyidea.org
Packager:       Cornelius Kölbel <cornelius.koelbel@netknights.it>
BuildArch:      x86_64

BuildRequires: libxml2-devel, freetype-devel, python-devel, libxslt-devel, zlib-devel, openssl-devel

%description
 privacyIDEA: identity, multifactor authentication, authorization.
 This package contains the python module for privacyIDEA. If you want
 to run it in a productive webserver you might want to install
 privacyidea-server.
 privacyIDEA is an open solution for strong two-factor authentication.
 privacyIDEA aims to not bind you to any decision of the authentication protocol
 or it does not dictate you where your user information should be stored.
 This is achieved by its totally modular architecture.
 privacyIDEA is not only open as far as its modular architecture is concerned.
 But privacyIDEA is completely licensed under the AGPLv3.


%prep

%build
rm -fr %{root_dir}
virtualenv %{root_dir}
source %{root_dir}/bin/activate

rm -fr privacyidea-ldap-proxy
git clone https://github.com/NetKnights-GmbH/privacyidea-ldap-proxy.git 
cd /privacyidea-ldap-proxy
git checkout v%{version}
pip install -r requirements.txt
pip install .

%install
mkdir -p $RPM_BUILD_ROOT/opt/
cp -r /opt/privacyidea-ldap-proxy $RPM_BUILD_ROOT/opt/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{root_dir}

%changelog
* Tue Jun 20 2017 Cornelius Kölbel <cornelius.koelbel@netknights.it> 2.0

  * initial release
