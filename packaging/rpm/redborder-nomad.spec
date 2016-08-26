Name: redborder-nomad
Version: %{__version}
Release: %{__release}%{?dist}
BuildArch: noarch
Summary: Package for redborder nomad init scripts

License: AGPL 3.0
URL: https://github.com/redBorder/redborder-nomad
Source0: %{name}-%{version}.tar.gz

Requires: nomad

%description
%{summary}

%prep
%setup -qn %{name}-%{version}

%build

%install
install -D -m 0644 resources/systemd/nomad-client.service %{buildroot}/usr/lib/systemd/system/nomad-client.service
install -D -m 0644 resources/systemd/nomad-server.service %{buildroot}/usr/lib/systemd/system/nomad-server.service

%pre

%post
systemctl daemon-reload

%files
%defattr(0644,root,root)
/usr/lib/systemd/system/nomad-client.service
/usr/lib/systemd/system/nomad-server.service
%doc

%changelog
* Fri Aug 26 2016 Carlos J. Mateos <cjmateos@redborder.com> - 1.0.0-1
- first spec version
