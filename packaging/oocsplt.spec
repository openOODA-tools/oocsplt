Name:           oocsplt
Version:        0.2.0
Release:        1%{?dist}
Summary:        Splits files into context-determined sections matched by regex patterns.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oocsplt
Source0:        oocsplt-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oocsplt is a sovereign, capability-bounded CONTEXT SPLITTER written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oocsplt
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oocsplt-uninstall

%files
/usr/bin/oocsplt
/usr/bin/oocsplt-uninstall

%changelog
* Wed Oct 08 2026 openOODA-tools <ops@openooda.org> - 0.2.0-1
- Elevation to pure native openOODA v0.2.0 with MCP and tri-distro packaging
