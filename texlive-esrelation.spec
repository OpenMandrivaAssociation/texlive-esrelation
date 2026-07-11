%global tl_name esrelation
%global tl_revision 76924

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Provides a symbol set for describing relations between ordered pairs
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/esrelation
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/esrelation.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/esrelation.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/esrelation.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Around 2008, researcher Byron Cook and several colleagues began
developing a new set of interrelated algorithms capable of automatically
reasoning about the behavior of computer programs and other systems
(such as biological systems, circuit designs, etc). At the center of
these algorithms were new ideas about the relationships between
structures expressible as mathematical sets and relations. Using the
language of mathematics and logic, the researchers communicated these
new results to others in their community via published papers, research
talks, etc. Unfortunately, they found the symbols already available for
reasoning about relations lacking (in contrast to sets, which have a
long-ago developed and robust symbol vocabulary). Early presentations
were unnecessarily cluttered. To more elegantly express these ideas
around relations, Cook recruited artist Tauba Auerbach to help develop a
set of symbols. This package provides an math symbol font for describing
relations between ordered pairs by using Metafont.

