%global debug_package   %{nil}

Name:		cfssl
Version:	1.2.0
Release:	1%{?dist}
Summary:	Cloudflare's PKI and TLS toolkit
License:	BSD-2-Clause
URL:		https://github.com/cloudflare/%{name}

%description
CFSSL is CloudFlare's PKI/TLS swiss army knife. It is both a command line tool
and an HTTP API server for signing, verifying, and bundling TLS certificates.
It requires Go 1.6+ to build.

Note that certain linux distributions have certain algorithms removed
(RHEL-based distributions in particular), so the golang from the official
repositories will not work. Users of these distributions should install go
manually to install CFSSL.

CFSSL consists of:

* a set of packages useful for building custom TLS PKI tools
* the cfssl program, which is the canonical command line utility using the
  CFSSL packages.
* the multirootca program, which is a certificate authority server that can
  use multiple signing keys.
* the mkbundle program is used to build certificate pool bundles.
* the cfssljson program, which takes the JSON output from the cfssl and
multirootca programs and writes certificates, keys, CSRs, and bundles to disk.


%prep
export GOPATH=/usr/share/gocode
export PATH=$GOPATH/bin:$PATH


%build


%install
cd $GOPATH/bin
install -D -p -m 0755 $GOPATH/bin/%{name}-bundle %{buildroot}%{_bindir}/%{name}-bundle
install -D -p -m 0755 $GOPATH/bin/%{name}-certinfo %{buildroot}%{_bindir}/%{name}-certinfo
install -D -p -m 0755 $GOPATH/bin/%{name}-newkey %{buildroot}%{_bindir}/%{name}-newkey
install -D -p -m 0755 $GOPATH/bin/%{name}-scan %{buildroot}%{_bindir}/%{name}-scan
install -D -p -m 0755 $GOPATH/bin/%{name} %{buildroot}%{_bindir}/%{name}
install -D -p -m 0755 $GOPATH/bin/%{name}json %{buildroot}%{_bindir}/%{name}json
install -D -p -m 0755 $GOPATH/bin/mkbundle %{buildroot}%{_bindir}/mkbundle
install -D -p -m 0755 $GOPATH/bin/multirootca %{buildroot}%{_bindir}/multirootca


%files
%{_bindir}/%{name}-bundle
%{_bindir}/%{name}-certinfo
%{_bindir}/%{name}-newkey
%{_bindir}/%{name}-scan
%{_bindir}/%{name}
%{_bindir}/%{name}json
%{_bindir}/mkbundle
%{_bindir}/multirootca


%changelog
* Tue Nov 07 2017 Allan Hung <hung.allan@gmail.com> - 1.2.0-1
- Update to 1.2.0
