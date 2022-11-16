Name:		texlive-esrelation
Version:	37236
Release:	1
Summary:	Provides a symbol set for describing relations between ordered pairs
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/esrelation
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/esrelation.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/esrelation.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/esrelation.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Around 2008, researcher Byron Cook and several colleagues began
developing a new set of interrelated algorithms capable of
automatically reasoning about the behavior of computer programs
and other systems (such as biological systems, circuit designs,
etc). At the center of these algorithms were new ideas about
the relationships between structures expressable as
mathematical sets and relations. Using the language of
mathematics and logic, the researchers communicated these new
results to others in their community via published papers,
research talks, etc. Unfortunately, they found the symbols
already available for reasoning about relations lacking (in
contrast to sets, which have a long-ago developed and robust
symbol vocabulary). Early presentations were unnecessarily
cluttered. To more elegantly express these ideas around
relations, Cook recruited artist Tauba Auerbach to help develop
a set of symbols. This package provides an math symbol font for
describing relations between ordered pairs by using Metafont.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/fonts/esrelation
%{_texmfdistdir}/tex/latex/esrelation
%{_texmfdistdir}/fonts/type1/public/esrelation
%{_texmfdistdir}/fonts/tfm/public/esrelation
%doc %{_texmfdistdir}/fonts/source/public/esrelation
%{_texmfdistdir}/fonts/map/dvips/esrelation
%doc %{_texmfdistdir}/doc/fonts/esrelation

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
