Name:		texlive-velthuis
Version:	55475
Release:	2
Summary:	Typeset Devanagari
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/devanagari/velthuis
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/velthuis.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/velthuis.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires:	texlive-xetex-devanagari

%description
Frans Velthuis' preprocessor for Devanagari text, and fonts and
macros to use when typesetting the processed text. The macros
provide features that support Sanskrit, Hindi, Marathi, Nepali,
and other languages typically printed in the Devanagari script.
The fonts are available both in Metafont and Type 1 format.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/public/velthuis
%{_texmfdistdir}/fonts/map/dvips/velthuis
%{_texmfdistdir}/fonts/source/public/velthuis
%{_texmfdistdir}/fonts/tfm/public/velthuis
%{_texmfdistdir}/fonts/type1/public/velthuis
%{_texmfdistdir}/tex/generic/velthuis
%{_texmfdistdir}/tex/latex/velthuis
%{_texmfdistdir}/tex/plain/velthuis
%{_texmfdistdir}/tex/xelatex/velthuis
%doc %{_texmfdistdir}/doc/generic/velthuis
%doc %{_texmfdistdir}/doc/man/man1/*

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar texmf-dist/* %{buildroot}%{_texmfdistdir}
