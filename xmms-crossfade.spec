Summary:	XMMS Plugin for Crossfading and Continuous Output
Summary(pl):	Wtyczka do XMMS zapewniaj±ca d¼wiêk bez przerw
Name:		xmms-output-crossfade
Version:	0.2.9
Release:	5
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://www.netcologne.de/~nc-eisenlpe2/xmms-crossfade/xmms-crossfade-%{version}.tar.gz
# Source0-md5:	7427e9f8e79e3532b6c85e36459e453a
URL:		http://www.netcologne.de/~nc-eisenlpe2/xmms-crossfade/
Buildrequires:	autoconf
Buildrequires:	automake
BuildRequires:	gtk+-devel
Buildrequires:	libtool
BuildRequires:	xmms-devel
Requires:	xmms
Provides:	xmms-output-plugin
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_libdir		%{_prefix}/lib/xmms/Output

%description
xmms-output-crossfade features:
- Crossfading: Crossfade between two songs, i.e. fade out the end of
  the current song while fading in the beginning of the next for a
  smooth transition. Length and volume of the fadings can be adjusted
  separately for fading in and out.
- Fadein/Fadeout: Smoothly fadein/fadeout at the beginning or end of
  playback.
- Continuous output: Keeps the audio device opened when switching from
  one song to the next. When used with the Gap-Killer, this allows for
  seamless playback of whole albums without any audible interruption
  between the tracks.
- Gap-Killer: Removes the short gaps of silence at the beginning
  and/or end of mp3 files. These gaps are caused by some mp3-encoders.
- Automatic detection of live albums: Automatically detects live
  albums and pre-mixed tracks which already are crossfaded. For those
  tracks, crossfading can be disabled automatically.
- High quality: XMMS-crossfade can take special care to avoid the
  clicks some soundcards produce when suddenly being stopped. Also, it
  can improve quality when seeking within a song.
- Secondary effect plugin: XMMS-crossfade allows you to select a
  second effect plugin. This is usefull for example when using the
  volume normalizing plugin together with the icecast plugin.

%description -l pl
Mo¿liwo¶ci xmms-output-crossfade to:
- p³ynne przechodzenie miêdzy dwoma utworami
- p³ynne wchodzenie i wyciszanie na pocz±tku i koñcu odtwarzania
- ci±g³e odtwarzanie d¼wiêku, tak¿e przy przechodzeniu miêdzy
  utworami; w po³±czeniu z Gap-Killerem daje to mo¿liwo¶æ odtworzenia
  ca³ego albumu bez ¿adnej s³yszalnej przerwy
- Gap-Killer - usuwaj±cy fragmenty ciszy na pocz±tku i koñcu plików
  mp3 (spowodowane przez niektóre kodery)
- automatyczne wykrywanie albumów koncertowych i pre-miksowanych, na
  których ¶cie¿ki ju¿ maj± p³ynne przej¶cia - dla nich dodawanie
  p³ynnych przej¶æ mo¿e byæ automatycznie wy³±czane
- wysoka jako¶æ - XMMS-crossfade stara siê unikaæ trzasków
  wystêpuj±cych na niektórych kartach d¼wiêkowych przy zatrzymywaniu
  odtwarzania
- wtyczka dodatkowego efektu: XMMS-crossfade pozwala wybraæ dodatkow±
  wtyczkê, np. do normalizcji wraz z wtyczk± icecast.

%prep
%setup -n xmms-crossfade-%{version} -q

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README TODO
%attr(755,root,root) %{_libdir}/*
