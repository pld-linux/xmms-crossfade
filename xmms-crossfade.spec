Summary:	XMMS Plugin for Crossfading and Continuous Output
Summary(pl.UTF-8):	Wtyczka wyjściowa dla XMMS-a zapewniająca dźwięk bez przerw
Name:		xmms-output-crossfade
Version:	0.3.8
Release:	1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://www.eisenlohr.org/xmms-crossfade/xmms-crossfade-%{version}.tar.gz
# Source0-md5:	fbfff1bff29118309b0a02c713b13d50
Patch0:		%{name}-xmms.patch
URL:		http://www.eisenlohr.org/xmms-crossfade/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel
BuildRequires:	libtool
BuildRequires:	rpmbuild(macros) >= 1.125
BuildRequires:	xmms-devel
Requires:	xmms
Provides:	xmms-output-plugin
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libdir		%{xmms_output_plugindir}

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
  and/or end of MP3 files. These gaps are caused by some MP3-encoders.
- Automatic detection of live albums: Automatically detects live
  albums and pre-mixed tracks which already are crossfaded. For those
  tracks, crossfading can be disabled automatically.
- High quality: XMMS-crossfade can take special care to avoid the
  clicks some soundcards produce when suddenly being stopped. Also, it
  can improve quality when seeking within a song.
- Secondary effect plugin: XMMS-crossfade allows you to select a
  second effect plugin. This is useful for example when using the
  volume normalizing plugin together with the icecast plugin.

%description -l pl.UTF-8
Możliwości xmms-output-crossfade to:
- płynne przechodzenie między dwoma utworami
- płynne wchodzenie i wyciszanie na początku i końcu odtwarzania
- ciągłe odtwarzanie dźwięku, także przy przechodzeniu między
  utworami; w połączeniu z Gap-Killerem daje to możliwość odtworzenia
  całego albumu bez żadnej słyszalnej przerwy
- Gap-Killer - usuwający fragmenty ciszy na początku i końcu plików
  MP3 (spowodowane przez niektóre kodery)
- automatyczne wykrywanie albumów koncertowych i pre-miksowanych, na
  których ścieżki już mają płynne przejścia - dla nich dodawanie
  płynnych przejść może być automatycznie wyłączane
- wysoka jakość - XMMS-crossfade stara się unikać trzasków
  występujących na niektórych kartach dźwiękowych przy zatrzymywaniu
  odtwarzania
- wtyczka dodatkowego efektu: XMMS-crossfade pozwala wybrać dodatkową
  wtyczkę, np. do normalizacji wraz z wtyczką icecast.

%prep
%setup -q -n xmms-crossfade-%{version}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-player=xmms
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README TODO ChangeLog
%attr(755,root,root) %{_libdir}/*
