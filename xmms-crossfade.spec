#
# Conditional build:
%bcond_without	audacious	# without audacious plugin
%bcond_without	xmms		# without xmms plugin
#
Summary:	Plugin for Crossfading and Continuous Output
Summary(pl.UTF-8):	Wtyczka wyjściowa zapewniająca dźwięk bez przerw
Name:		xmms-crossfade
Version:	0.3.14
Release:	1
License:	GPL v2+
Group:		X11/Applications/Sound
Source0:	http://www.eisenlohr.org/xmms-crossfade/%{name}-%{version}.tar.gz
# Source0-md5:	026c52544c7f3193d384288c9f8296aa
Patch0:		%{name}-only-libs.patch
URL:		http://www.eisenlohr.org/xmms-crossfade/
%{?with_audacious:BuildRequires:	audacious-devel >= 1.4.2}
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake
BuildRequires:	gtk+-devel
BuildRequires:	gtk+2-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.125
%{?with_xmms:BuildRequires:	xmms-devel}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xmms-crossfade features:
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
Możliwości xmms-crossfade to:
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

%package -n xmms-output-crossfade
Summary:	XMMS Plugin for Crossfading and Continuous Output
Summary(pl.UTF-8):	Wtyczka wyjściowa dla XMMS-a zapewniająca dźwięk bez przerw
Group:		X11/Applications/Sound
Requires:	xmms
Provides:	xmms-output-plugin

%description -n xmms-output-crossfade
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

%description -n xmms-output-crossfade -l pl.UTF-8
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

%package -n audacious-output-crossfade
Summary:	Audacious Plugin for Crossfading and Continuous Output
Summary(pl.UTF-8):	Wtyczka wyjściowa dla Audacious zapewniająca dźwięk bez przerw
Group:		X11/Applications/Sound
Requires:	audacious
Provides:	audacious-output-plugin

%description -n audacious-output-crossfade
audacious-output-crossfade features:
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

%description -n audacious-output-crossfade -l pl.UTF-8
Możliwości audacious-output-crossfade to:
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
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}

%if %{with xmms}
mkdir -p xmms
cd xmms
../%configure \
	--enable-player=xmms
%{__make}
cd ..
%endif

%if %{with audacious}
mkdir -p audacious
cd audacious
../%configure \
	--enable-player=audacious
%{__make}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with xmms}
%{__make} -C xmms install \
	DESTDIR=$RPM_BUILD_ROOT
%endif

%if %{with audacious}
%{__make} -C audacious install \
	DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_libdir}/audacious/Output/libcrossfade.la
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with xmms}
%files -n xmms-output-crossfade
%defattr(644,root,root,755)
%doc AUTHORS README ChangeLog
%attr(755,root,root) %{_libdir}/xmms
%endif

%if %{with audacious}
%files -n audacious-output-crossfade
%defattr(644,root,root,755)
%doc AUTHORS README ChangeLog
%attr(755,root,root) %{_libdir}/audacious/Output/libcrossfade.so
%endif
