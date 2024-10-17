Name:		texlive-yinit-otf
Version:	40207
Release:	2
Summary:	OTF conversion of Yannis Haralambous' Old German decorative initials
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/yinit-otf
License:	pd
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/yinit-otf.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/yinit-otf.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package is a conversion of the yinit font into OTF.
Original Metafont files for yinit are in the yinit package.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/fonts/opentype/public/yinit-otf
%doc %{_texmfdistdir}/doc/fonts/yinit-otf

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
