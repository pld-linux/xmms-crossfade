Summary:	XMMS Plugin for Crossfading and Continuous Output
Summary(pl):	Wtyczka do XMMS zapewniaj±ca d¼wiêk bez przerw
Name:		xmms-output-crossfade
Version:	0.2.9
Release:	1
Group:		X11/Applications/Multimedia
Group(de):	X11/Applikationen/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
License:	GPL
URL:		http://www.netcologne.de/~nc-eisenlpe2/xmms-crossfade/
Source0:	http://www.netcologne.de/~nc-eisenlpe2/xmms-crossfade/xmms-crossfade-%{name}.tar.gz
BuildRequires:	gtk+-devel
BuildRequires:	xmms-devel
Requires:	xmms
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
# bleh
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

%prep
%setup -n xmms-crossfade-%{version} -q

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf AUTHORS README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*
%doc *.gz
