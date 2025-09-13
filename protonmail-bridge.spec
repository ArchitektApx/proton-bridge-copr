%global             short_name protonmail
%global             full_name %{short_name}-bridge
%global             debug_package %{nil}

Name:               protonmail-bridge
Version:            3.21.2
Release:            1%{?dist}
Summary:            Proton Mail Bridge for Linux (aarch64)

License:            GPLv3
URL:                https://proton.me/mail/bridge
Source0:            https://github.com/ArchitektApx/proton-bridge-copr/releases/download/v3.21.2/protonmail-bridge-linux-arm64.tar.gz
Source1:            protonmail-bridge

ExclusiveArch:  aarch64

Requires:           dejavu-sans-fonts
Requires:           fontconfig
Requires:           glib2
Requires:           glibc
Requires:           libEGL
Requires:           libgcc
Requires:           libglvnd-glx
Requires:           libstdc++
Requires:           libsecret
Requires:           libxkbcommon-x11

Recommends:         (gnome-keyring if gnome-shell)

Requires(post):     gtk-update-icon-cache

%description
This is a package of the Proton Mail Bridge for aarch64. 
Proton Mail Bridge is a desktop application that runs in the background encrypting and decrypting messages as they enter and leave your computer.

Bugs related to Zen should be reported directly to the Zen Browser GitHub repo: 
<https://github.com/ProtonMail/proton-bridge>

Bugs related to this package should be reported at this Git project:
<https://github.com/ArchitektApx/proton-bridge-copr>

%prep
%setup -q -n %{short_name}

%install
%__rm -rf %{buildroot}

%__install -d %{buildroot}{/usr/lib/%{short_name}/bridge,%{_bindir},%{_datadir}/applications,%{_datadir}/icons/hicolor/scalable/apps,%{_datadir}/doc/%{short_name}/bridge}

%__install -D -m 0644 proton-bridge.desktop -t %{buildroot}%{_datadir}/applications
%__install -D -m 0644 logo.svg -t %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{short_name}-bridge.svg
%__install -D -m 0444 LICENSE -t %{buildroot}%{_datadir}/doc/%{short_name}/bridge
%__install -D -m 0444 Changelog.md -t %{buildroot}%{_datadir}/doc/%{short_name}/bridge
%__install -D -m 0755 %{SOURCE1} -t %{buildroot}%{_bindir}/%{full_name}

%__cp -r * %{buildroot}/usr/lib/%{short_name}/bridge

%post
gtk-update-icon-cache -f -t %{_datadir}/icons/hicolor

%files
%{_datadir}/applications/proton-bridge.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{short_name}-bridge.svg
%{_datadir}/doc/%{short_name}/bridge
%{_bindir}/%{full_name}
/usr/lib/%{short_name}/bridge

%changelog
* Sun Sep 07 2025 ArchitektApx <architektapx@gehinors.ch> - 3.21.2
- Fixed
- BRIDGE-406: Fixed faulty certificate chain validation logic. Made certificate pin checks exclusive to leaf certificates.

* Fri Mar 07 2025 ArchitektApx <architektapx@gehinors.ch> - 3.18.0
- Changed
- BRIDGE-309: Revised update logic and structure.
- BRIDGE-154: Added access token to expiry refresh request.

* Thu Feb 20 2025 ArchitektApx <architektapx@gehinors.ch> - 3.17.0
- Added
- BRIDGE-271: Report version file check failure to Sentry.
- BRIDGE-247: Test: Automate Bridge 0% update rollout.
- BRIDGE-248: Test: Additional Bridge UI e2e automation tests.

- Changed
- BRIDGE-73: Update goopenpgp.
- BRIDGE-287: Update x/net and x/crypto dependencies.
- BRIDGE-303: Update govulncheck to latest release.
- BRIDGE-226: Bump Go version to 1.23.4.
- BRIDGE-288: Extension to synchronization update handler, observability tweaks and gluon update.

- Fixed
- BRIDGE-291: Use correct field for user plan type.
- BRIDGE-143: Add missing QML component attribute, cut/paste disabled on read-only text areas.

* Mon Feb 17 2025 ArchitektApx <architektapx@gehinors.ch> - 3.16.0
- Added
- BRIDGE-205: Add support for the IMAP AUTHENTICATE command.
- BRIDGE-268: Add kill switch feature flag for the IMAP AUTHENTICATE command.
- BRIDGE-261: Delete gluon data during user deletion.
- BRIDGE-246: Test: Add Settings Menu Bridge UI e2e automation tests.
- Changed
- BRIDGE-107: Improved human verification UX.
- BRIDGE-281: Disable keychain test on macOS.
- BRIDGE-266: Heartbeat telemetry update.
- BRIDGE-253: Removed unused telemetry (activation and troubleshooting).
- BRIDGE-252: Restored the -h shortcut for the CLI --help switch.
- BRIDGE-264: Ignore apple notes as UserAgent.
- Fixed
- BRIDGE-256: Fix reversed order of headers with multiple values.
- BRIDGE-258: Fixed issue with draft updates and sending during synchronization.

* Thu Dec 12 2024 ArchitektApx <architektapx@gehinors.ch> - 3.15.1
- Changed
- BRIDGE-281: Disable keychain test on macOS.

* Tue Nov 26 2024 ArchitektApx <architektapx@gehinors.ch> - 3.15.0
- Added
- BRIDGE-238: Added host information to sentry events; new sentry event for keychain issues.
- BRIDGE-236: Added SMTP observability metrics.
- BRIDGE-217: Added missing parameter to the CLI help command.
- BRIDGE-234: Add accessibility name in QML for UI automation.
- BRIDGE-232: Test: Add Home Menu Bridge UI e2e automation tests.
- BRIDGE-220: Test: Add Bridge E2E UI login/logout tests for Windows.
- Changed
- BRIDGE-228: Removed sentry events.
- BRIDGE-218: Observability adapter; gluon observability metrics and tests.
- BRIDGE-215: Tweak wording on macOS profile install page.
- BRIDGE-131: Test: Integration tests for messages from Proton <-> Gmail.
- BRIDGE-142: Bridge icon can be removed from the menu bar on macOS.
- Fixed
- BRIDGE-240: Fix for running against Qt 6.8 (contribution of GitHub user Cimbali).
- BRIDGE-231: Fix reversed header order in messages.
- BRIDGE-235: Fix compilation of Bridge GUI Tester on Windows.
- BRIDGE-120: Use appropriate address key when importing / saving draft.

* Wed Nov 20 2024 ArchitektApx <architektapx@gehinors.ch> - 3.14.0
- Changed
- BRIDGE-207: Failure to download or verify an update now fails silently.
- BRIDGE-204: Removed redundant Sentry events.
- BRIDGE-150: Observability service modification.
- BRIDGE-210: Reduced log level of cache events so they won't be printed to stdout.
- Fixed
- BRIDGE-106: Fixed import of multipart-related messages.
- BRIDGE-108: Fixed GetInitials when empty username is passed.

* Wed Nov 20 2024 ArchitektApx <architektapx@gehinors.ch> - 3.14.0
- Changed
- BRIDGE-207: Failure to download or verify an update now fails silently.
- BRIDGE-204: Removed redundant Sentry events.
- BRIDGE-150: Observability service modification.
- BRIDGE-210: Reduced log level of cache events so they won't be printed to stdout.
- Fixed
- BRIDGE-106: Fixed import of multipart-related messages.
- BRIDGE-108: Fixed GetInitials when empty username is passed.

* Tue Nov 19 2024 ArchitektApx <architektapx@gehinors.ch> - 3.13.0
- Inital arm64 build release
