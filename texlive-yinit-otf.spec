%global tl_name yinit-otf
%global tl_revision 40207

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	OTF conversion of Yannis Haralambous Old German decorative initials
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/gothic/yinit-otf
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/yinit-otf.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/yinit-otf.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package is a conversion of the yinit font into OTF. Original
Metafont files for yinit are in the yinit package.

