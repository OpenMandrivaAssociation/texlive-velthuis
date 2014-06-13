# revision 23224
# category Package
# catalog-ctan /language/devanagari/velthuis
# catalog-date 2011-07-25 14:21:08 +0200
# catalog-license gpl
# catalog-version 2.15.1
Name:		texlive-velthuis
Version:	2.15.1
Release:	7
Summary:	Typeset Devanagari
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/devanagari/velthuis
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/velthuis.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/velthuis.doc.tar.xz
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
%{_texmfdistdir}/fonts/afm/public/velthuis/dvnb10.afm
%{_texmfdistdir}/fonts/afm/public/velthuis/dvnb8.afm
%{_texmfdistdir}/fonts/afm/public/velthuis/dvnb9.afm
%{_texmfdistdir}/fonts/afm/public/velthuis/dvnbb10.afm
%{_texmfdistdir}/fonts/afm/public/velthuis/dvnbb8.afm
%{_texmfdistdir}/fonts/afm/public/velthuis/dvnbb9.afm
%{_texmfdistdir}/fonts/afm/public/velthuis/dvnbbi10.afm
%{_texmfdistdir}/fonts/afm/public/velthuis/dvnbbi8.afm
%{_texmfdistdir}/fonts/afm/public/velthuis/dvnbbi9.afm
%{_texmfdistdir}/fonts/afm/public/velthuis/dvnbi10.afm
%{_texmfdistdir}/fonts/afm/public/velthuis/dvnbi8.afm
%{_texmfdistdir}/fonts/afm/public/velthuis/dvnbi9.afm
%{_texmfdistdir}/fonts/afm/public/velthuis/dvnc10.afm
%{_texmfdistdir}/fonts/afm/public/velthuis/dvnc8.afm
%{_texmfdistdir}/fonts/afm/public/velthuis/dvnc9.afm
%{_texmfdistdir}/fonts/afm/public/velthuis/dvncb10.afm
%{_texmfdistdir}/fonts/afm/public/velthuis/dvncb8.afm
%{_texmfdistdir}/fonts/afm/public/velthuis/dvncb9.afm
%{_texmfdistdir}/fonts/afm/public/velthuis/dvncbi10.afm
%{_texmfdistdir}/fonts/afm/public/velthuis/dvncbi8.afm
%{_texmfdistdir}/fonts/afm/public/velthuis/dvncbi9.afm
%{_texmfdistdir}/fonts/afm/public/velthuis/dvnci10.afm
%{_texmfdistdir}/fonts/afm/public/velthuis/dvnci8.afm
%{_texmfdistdir}/fonts/afm/public/velthuis/dvnci9.afm
%{_texmfdistdir}/fonts/afm/public/velthuis/dvng10.afm
%{_texmfdistdir}/fonts/afm/public/velthuis/dvng8.afm
%{_texmfdistdir}/fonts/afm/public/velthuis/dvng9.afm
%{_texmfdistdir}/fonts/afm/public/velthuis/dvngb10.afm
%{_texmfdistdir}/fonts/afm/public/velthuis/dvngb8.afm
%{_texmfdistdir}/fonts/afm/public/velthuis/dvngb9.afm
%{_texmfdistdir}/fonts/afm/public/velthuis/dvngbi10.afm
%{_texmfdistdir}/fonts/afm/public/velthuis/dvngbi8.afm
%{_texmfdistdir}/fonts/afm/public/velthuis/dvngbi9.afm
%{_texmfdistdir}/fonts/afm/public/velthuis/dvngi10.afm
%{_texmfdistdir}/fonts/afm/public/velthuis/dvngi8.afm
%{_texmfdistdir}/fonts/afm/public/velthuis/dvngi9.afm
%{_texmfdistdir}/fonts/afm/public/velthuis/dvnn10.afm
%{_texmfdistdir}/fonts/afm/public/velthuis/dvnn8.afm
%{_texmfdistdir}/fonts/afm/public/velthuis/dvnn9.afm
%{_texmfdistdir}/fonts/afm/public/velthuis/dvnnb10.afm
%{_texmfdistdir}/fonts/afm/public/velthuis/dvnnb8.afm
%{_texmfdistdir}/fonts/afm/public/velthuis/dvnnb9.afm
%{_texmfdistdir}/fonts/afm/public/velthuis/dvnnbi10.afm
%{_texmfdistdir}/fonts/afm/public/velthuis/dvnnbi8.afm
%{_texmfdistdir}/fonts/afm/public/velthuis/dvnnbi9.afm
%{_texmfdistdir}/fonts/afm/public/velthuis/dvnni10.afm
%{_texmfdistdir}/fonts/afm/public/velthuis/dvnni8.afm
%{_texmfdistdir}/fonts/afm/public/velthuis/dvnni9.afm
%{_texmfdistdir}/fonts/afm/public/velthuis/dvpb10.afm
%{_texmfdistdir}/fonts/afm/public/velthuis/dvpb8.afm
%{_texmfdistdir}/fonts/afm/public/velthuis/dvpb9.afm
%{_texmfdistdir}/fonts/afm/public/velthuis/dvpc10.afm
%{_texmfdistdir}/fonts/afm/public/velthuis/dvpc8.afm
%{_texmfdistdir}/fonts/afm/public/velthuis/dvpc9.afm
%{_texmfdistdir}/fonts/afm/public/velthuis/dvpn10.afm
%{_texmfdistdir}/fonts/afm/public/velthuis/dvpn8.afm
%{_texmfdistdir}/fonts/afm/public/velthuis/dvpn9.afm
%{_texmfdistdir}/fonts/afm/public/velthuis/dvpnn10.afm
%{_texmfdistdir}/fonts/afm/public/velthuis/dvpnn8.afm
%{_texmfdistdir}/fonts/afm/public/velthuis/dvpnn9.afm
%{_texmfdistdir}/fonts/map/dvips/velthuis/dvng.map
%{_texmfdistdir}/fonts/source/public/velthuis/dnchars.mf
%{_texmfdistdir}/fonts/source/public/velthuis/dndefs.mf
%{_texmfdistdir}/fonts/source/public/velthuis/dngen.mf
%{_texmfdistdir}/fonts/source/public/velthuis/dninit.mf
%{_texmfdistdir}/fonts/source/public/velthuis/dvnb10.mf
%{_texmfdistdir}/fonts/source/public/velthuis/dvnb8.mf
%{_texmfdistdir}/fonts/source/public/velthuis/dvnb9.mf
%{_texmfdistdir}/fonts/source/public/velthuis/dvnbb10.mf
%{_texmfdistdir}/fonts/source/public/velthuis/dvnbb8.mf
%{_texmfdistdir}/fonts/source/public/velthuis/dvnbb9.mf
%{_texmfdistdir}/fonts/source/public/velthuis/dvnbbi10.mf
%{_texmfdistdir}/fonts/source/public/velthuis/dvnbbi8.mf
%{_texmfdistdir}/fonts/source/public/velthuis/dvnbbi9.mf
%{_texmfdistdir}/fonts/source/public/velthuis/dvnbi10.mf
%{_texmfdistdir}/fonts/source/public/velthuis/dvnbi8.mf
%{_texmfdistdir}/fonts/source/public/velthuis/dvnbi9.mf
%{_texmfdistdir}/fonts/source/public/velthuis/dvnc10.mf
%{_texmfdistdir}/fonts/source/public/velthuis/dvnc8.mf
%{_texmfdistdir}/fonts/source/public/velthuis/dvnc9.mf
%{_texmfdistdir}/fonts/source/public/velthuis/dvncb10.mf
%{_texmfdistdir}/fonts/source/public/velthuis/dvncb8.mf
%{_texmfdistdir}/fonts/source/public/velthuis/dvncb9.mf
%{_texmfdistdir}/fonts/source/public/velthuis/dvncbi10.mf
%{_texmfdistdir}/fonts/source/public/velthuis/dvncbi8.mf
%{_texmfdistdir}/fonts/source/public/velthuis/dvncbi9.mf
%{_texmfdistdir}/fonts/source/public/velthuis/dvnci10.mf
%{_texmfdistdir}/fonts/source/public/velthuis/dvnci8.mf
%{_texmfdistdir}/fonts/source/public/velthuis/dvnci9.mf
%{_texmfdistdir}/fonts/source/public/velthuis/dvng10.mf
%{_texmfdistdir}/fonts/source/public/velthuis/dvng8.mf
%{_texmfdistdir}/fonts/source/public/velthuis/dvng9.mf
%{_texmfdistdir}/fonts/source/public/velthuis/dvngb10.mf
%{_texmfdistdir}/fonts/source/public/velthuis/dvngb8.mf
%{_texmfdistdir}/fonts/source/public/velthuis/dvngb9.mf
%{_texmfdistdir}/fonts/source/public/velthuis/dvngbi10.mf
%{_texmfdistdir}/fonts/source/public/velthuis/dvngbi8.mf
%{_texmfdistdir}/fonts/source/public/velthuis/dvngbi9.mf
%{_texmfdistdir}/fonts/source/public/velthuis/dvngi10.mf
%{_texmfdistdir}/fonts/source/public/velthuis/dvngi8.mf
%{_texmfdistdir}/fonts/source/public/velthuis/dvngi9.mf
%{_texmfdistdir}/fonts/source/public/velthuis/dvnn10.mf
%{_texmfdistdir}/fonts/source/public/velthuis/dvnn8.mf
%{_texmfdistdir}/fonts/source/public/velthuis/dvnn9.mf
%{_texmfdistdir}/fonts/source/public/velthuis/dvnnb10.mf
%{_texmfdistdir}/fonts/source/public/velthuis/dvnnb8.mf
%{_texmfdistdir}/fonts/source/public/velthuis/dvnnb9.mf
%{_texmfdistdir}/fonts/source/public/velthuis/dvnnbi10.mf
%{_texmfdistdir}/fonts/source/public/velthuis/dvnnbi8.mf
%{_texmfdistdir}/fonts/source/public/velthuis/dvnnbi9.mf
%{_texmfdistdir}/fonts/source/public/velthuis/dvnni10.mf
%{_texmfdistdir}/fonts/source/public/velthuis/dvnni8.mf
%{_texmfdistdir}/fonts/source/public/velthuis/dvnni9.mf
%{_texmfdistdir}/fonts/source/public/velthuis/dvpb10.mf
%{_texmfdistdir}/fonts/source/public/velthuis/dvpb8.mf
%{_texmfdistdir}/fonts/source/public/velthuis/dvpb9.mf
%{_texmfdistdir}/fonts/source/public/velthuis/dvpc10.mf
%{_texmfdistdir}/fonts/source/public/velthuis/dvpc8.mf
%{_texmfdistdir}/fonts/source/public/velthuis/dvpc9.mf
%{_texmfdistdir}/fonts/source/public/velthuis/dvpn10.mf
%{_texmfdistdir}/fonts/source/public/velthuis/dvpn8.mf
%{_texmfdistdir}/fonts/source/public/velthuis/dvpn9.mf
%{_texmfdistdir}/fonts/source/public/velthuis/dvpnn10.mf
%{_texmfdistdir}/fonts/source/public/velthuis/dvpnn8.mf
%{_texmfdistdir}/fonts/source/public/velthuis/dvpnn9.mf
%{_texmfdistdir}/fonts/tfm/public/velthuis/dvnb10.tfm
%{_texmfdistdir}/fonts/tfm/public/velthuis/dvnb8.tfm
%{_texmfdistdir}/fonts/tfm/public/velthuis/dvnb9.tfm
%{_texmfdistdir}/fonts/tfm/public/velthuis/dvnbb10.tfm
%{_texmfdistdir}/fonts/tfm/public/velthuis/dvnbb8.tfm
%{_texmfdistdir}/fonts/tfm/public/velthuis/dvnbb9.tfm
%{_texmfdistdir}/fonts/tfm/public/velthuis/dvnbbi10.tfm
%{_texmfdistdir}/fonts/tfm/public/velthuis/dvnbbi8.tfm
%{_texmfdistdir}/fonts/tfm/public/velthuis/dvnbbi9.tfm
%{_texmfdistdir}/fonts/tfm/public/velthuis/dvnbi10.tfm
%{_texmfdistdir}/fonts/tfm/public/velthuis/dvnbi8.tfm
%{_texmfdistdir}/fonts/tfm/public/velthuis/dvnbi9.tfm
%{_texmfdistdir}/fonts/tfm/public/velthuis/dvnc10.tfm
%{_texmfdistdir}/fonts/tfm/public/velthuis/dvnc8.tfm
%{_texmfdistdir}/fonts/tfm/public/velthuis/dvnc9.tfm
%{_texmfdistdir}/fonts/tfm/public/velthuis/dvncb10.tfm
%{_texmfdistdir}/fonts/tfm/public/velthuis/dvncb8.tfm
%{_texmfdistdir}/fonts/tfm/public/velthuis/dvncb9.tfm
%{_texmfdistdir}/fonts/tfm/public/velthuis/dvncbi10.tfm
%{_texmfdistdir}/fonts/tfm/public/velthuis/dvncbi8.tfm
%{_texmfdistdir}/fonts/tfm/public/velthuis/dvncbi9.tfm
%{_texmfdistdir}/fonts/tfm/public/velthuis/dvnci10.tfm
%{_texmfdistdir}/fonts/tfm/public/velthuis/dvnci8.tfm
%{_texmfdistdir}/fonts/tfm/public/velthuis/dvnci9.tfm
%{_texmfdistdir}/fonts/tfm/public/velthuis/dvng10.tfm
%{_texmfdistdir}/fonts/tfm/public/velthuis/dvng8.tfm
%{_texmfdistdir}/fonts/tfm/public/velthuis/dvng9.tfm
%{_texmfdistdir}/fonts/tfm/public/velthuis/dvngb10.tfm
%{_texmfdistdir}/fonts/tfm/public/velthuis/dvngb8.tfm
%{_texmfdistdir}/fonts/tfm/public/velthuis/dvngb9.tfm
%{_texmfdistdir}/fonts/tfm/public/velthuis/dvngbi10.tfm
%{_texmfdistdir}/fonts/tfm/public/velthuis/dvngbi8.tfm
%{_texmfdistdir}/fonts/tfm/public/velthuis/dvngbi9.tfm
%{_texmfdistdir}/fonts/tfm/public/velthuis/dvngi10.tfm
%{_texmfdistdir}/fonts/tfm/public/velthuis/dvngi8.tfm
%{_texmfdistdir}/fonts/tfm/public/velthuis/dvngi9.tfm
%{_texmfdistdir}/fonts/tfm/public/velthuis/dvnn10.tfm
%{_texmfdistdir}/fonts/tfm/public/velthuis/dvnn8.tfm
%{_texmfdistdir}/fonts/tfm/public/velthuis/dvnn9.tfm
%{_texmfdistdir}/fonts/tfm/public/velthuis/dvnnb10.tfm
%{_texmfdistdir}/fonts/tfm/public/velthuis/dvnnb8.tfm
%{_texmfdistdir}/fonts/tfm/public/velthuis/dvnnb9.tfm
%{_texmfdistdir}/fonts/tfm/public/velthuis/dvnnbi10.tfm
%{_texmfdistdir}/fonts/tfm/public/velthuis/dvnnbi8.tfm
%{_texmfdistdir}/fonts/tfm/public/velthuis/dvnnbi9.tfm
%{_texmfdistdir}/fonts/tfm/public/velthuis/dvnni10.tfm
%{_texmfdistdir}/fonts/tfm/public/velthuis/dvnni8.tfm
%{_texmfdistdir}/fonts/tfm/public/velthuis/dvnni9.tfm
%{_texmfdistdir}/fonts/tfm/public/velthuis/dvpb10.tfm
%{_texmfdistdir}/fonts/tfm/public/velthuis/dvpb8.tfm
%{_texmfdistdir}/fonts/tfm/public/velthuis/dvpb9.tfm
%{_texmfdistdir}/fonts/tfm/public/velthuis/dvpc10.tfm
%{_texmfdistdir}/fonts/tfm/public/velthuis/dvpc8.tfm
%{_texmfdistdir}/fonts/tfm/public/velthuis/dvpc9.tfm
%{_texmfdistdir}/fonts/tfm/public/velthuis/dvpn10.tfm
%{_texmfdistdir}/fonts/tfm/public/velthuis/dvpn8.tfm
%{_texmfdistdir}/fonts/tfm/public/velthuis/dvpn9.tfm
%{_texmfdistdir}/fonts/tfm/public/velthuis/dvpnn10.tfm
%{_texmfdistdir}/fonts/tfm/public/velthuis/dvpnn8.tfm
%{_texmfdistdir}/fonts/tfm/public/velthuis/dvpnn9.tfm
%{_texmfdistdir}/fonts/type1/public/velthuis/dvnb10.pfb
%{_texmfdistdir}/fonts/type1/public/velthuis/dvnb8.pfb
%{_texmfdistdir}/fonts/type1/public/velthuis/dvnb9.pfb
%{_texmfdistdir}/fonts/type1/public/velthuis/dvnbb10.pfb
%{_texmfdistdir}/fonts/type1/public/velthuis/dvnbb8.pfb
%{_texmfdistdir}/fonts/type1/public/velthuis/dvnbb9.pfb
%{_texmfdistdir}/fonts/type1/public/velthuis/dvnbbi10.pfb
%{_texmfdistdir}/fonts/type1/public/velthuis/dvnbbi8.pfb
%{_texmfdistdir}/fonts/type1/public/velthuis/dvnbbi9.pfb
%{_texmfdistdir}/fonts/type1/public/velthuis/dvnbi10.pfb
%{_texmfdistdir}/fonts/type1/public/velthuis/dvnbi8.pfb
%{_texmfdistdir}/fonts/type1/public/velthuis/dvnbi9.pfb
%{_texmfdistdir}/fonts/type1/public/velthuis/dvnc10.pfb
%{_texmfdistdir}/fonts/type1/public/velthuis/dvnc8.pfb
%{_texmfdistdir}/fonts/type1/public/velthuis/dvnc9.pfb
%{_texmfdistdir}/fonts/type1/public/velthuis/dvncb10.pfb
%{_texmfdistdir}/fonts/type1/public/velthuis/dvncb8.pfb
%{_texmfdistdir}/fonts/type1/public/velthuis/dvncb9.pfb
%{_texmfdistdir}/fonts/type1/public/velthuis/dvncbi10.pfb
%{_texmfdistdir}/fonts/type1/public/velthuis/dvncbi8.pfb
%{_texmfdistdir}/fonts/type1/public/velthuis/dvncbi9.pfb
%{_texmfdistdir}/fonts/type1/public/velthuis/dvnci10.pfb
%{_texmfdistdir}/fonts/type1/public/velthuis/dvnci8.pfb
%{_texmfdistdir}/fonts/type1/public/velthuis/dvnci9.pfb
%{_texmfdistdir}/fonts/type1/public/velthuis/dvng10.pfb
%{_texmfdistdir}/fonts/type1/public/velthuis/dvng8.pfb
%{_texmfdistdir}/fonts/type1/public/velthuis/dvng9.pfb
%{_texmfdistdir}/fonts/type1/public/velthuis/dvngb10.pfb
%{_texmfdistdir}/fonts/type1/public/velthuis/dvngb8.pfb
%{_texmfdistdir}/fonts/type1/public/velthuis/dvngb9.pfb
%{_texmfdistdir}/fonts/type1/public/velthuis/dvngbi10.pfb
%{_texmfdistdir}/fonts/type1/public/velthuis/dvngbi8.pfb
%{_texmfdistdir}/fonts/type1/public/velthuis/dvngbi9.pfb
%{_texmfdistdir}/fonts/type1/public/velthuis/dvngi10.pfb
%{_texmfdistdir}/fonts/type1/public/velthuis/dvngi8.pfb
%{_texmfdistdir}/fonts/type1/public/velthuis/dvngi9.pfb
%{_texmfdistdir}/fonts/type1/public/velthuis/dvnn10.pfb
%{_texmfdistdir}/fonts/type1/public/velthuis/dvnn8.pfb
%{_texmfdistdir}/fonts/type1/public/velthuis/dvnn9.pfb
%{_texmfdistdir}/fonts/type1/public/velthuis/dvnnb10.pfb
%{_texmfdistdir}/fonts/type1/public/velthuis/dvnnb8.pfb
%{_texmfdistdir}/fonts/type1/public/velthuis/dvnnb9.pfb
%{_texmfdistdir}/fonts/type1/public/velthuis/dvnnbi10.pfb
%{_texmfdistdir}/fonts/type1/public/velthuis/dvnnbi8.pfb
%{_texmfdistdir}/fonts/type1/public/velthuis/dvnnbi9.pfb
%{_texmfdistdir}/fonts/type1/public/velthuis/dvnni10.pfb
%{_texmfdistdir}/fonts/type1/public/velthuis/dvnni8.pfb
%{_texmfdistdir}/fonts/type1/public/velthuis/dvnni9.pfb
%{_texmfdistdir}/fonts/type1/public/velthuis/dvpb10.pfb
%{_texmfdistdir}/fonts/type1/public/velthuis/dvpb8.pfb
%{_texmfdistdir}/fonts/type1/public/velthuis/dvpb9.pfb
%{_texmfdistdir}/fonts/type1/public/velthuis/dvpc10.pfb
%{_texmfdistdir}/fonts/type1/public/velthuis/dvpc8.pfb
%{_texmfdistdir}/fonts/type1/public/velthuis/dvpc9.pfb
%{_texmfdistdir}/fonts/type1/public/velthuis/dvpn10.pfb
%{_texmfdistdir}/fonts/type1/public/velthuis/dvpn8.pfb
%{_texmfdistdir}/fonts/type1/public/velthuis/dvpn9.pfb
%{_texmfdistdir}/fonts/type1/public/velthuis/dvpnn10.pfb
%{_texmfdistdir}/fonts/type1/public/velthuis/dvpnn8.pfb
%{_texmfdistdir}/fonts/type1/public/velthuis/dvpnn9.pfb
%{_texmfdistdir}/tex/generic/velthuis/hindi.ldf
%{_texmfdistdir}/tex/generic/velthuis/hindi.sty
%{_texmfdistdir}/tex/latex/velthuis/dev.sty
%{_texmfdistdir}/tex/latex/velthuis/dev209.sty
%{_texmfdistdir}/tex/latex/velthuis/devanagari.sty
%{_texmfdistdir}/tex/latex/velthuis/dvngcite.sty
%{_texmfdistdir}/tex/latex/velthuis/udn.fd
%{_texmfdistdir}/tex/latex/velthuis/udnb.fd
%{_texmfdistdir}/tex/latex/velthuis/udnc.fd
%{_texmfdistdir}/tex/latex/velthuis/udnn.fd
%{_texmfdistdir}/tex/latex/velthuis/udnp.fd
%{_texmfdistdir}/tex/latex/velthuis/udnpb.fd
%{_texmfdistdir}/tex/latex/velthuis/udnpc.fd
%{_texmfdistdir}/tex/latex/velthuis/udnpn.fd
%{_texmfdistdir}/tex/plain/velthuis/dnmacs.tex
%{_texmfdistdir}/tex/xelatex/velthuis/hindicaptions.sty
%doc %{_texmfdistdir}/doc/generic/velthuis/README
%doc %{_texmfdistdir}/doc/generic/velthuis/captions.dn
%doc %{_texmfdistdir}/doc/generic/velthuis/changes
%doc %{_texmfdistdir}/doc/generic/velthuis/copying
%doc %{_texmfdistdir}/doc/generic/velthuis/examples.dn
%doc %{_texmfdistdir}/doc/generic/velthuis/examples.pdf
%doc %{_texmfdistdir}/doc/generic/velthuis/hindi.dtx
%doc %{_texmfdistdir}/doc/generic/velthuis/hindi.ins
%doc %{_texmfdistdir}/doc/generic/velthuis/hindi.pdf
%doc %{_texmfdistdir}/doc/generic/velthuis/manual.pdf
%doc %{_texmfdistdir}/doc/generic/velthuis/manual.tex
%doc %{_texmfdistdir}/doc/generic/velthuis/misspaal.dn
%doc %{_texmfdistdir}/doc/generic/velthuis/misspaal.pdf
%doc %{_texmfdistdir}/doc/generic/velthuis/vedasample.dn
%doc %{_texmfdistdir}/doc/generic/velthuis/vedasample.pdf
%doc %{_texmfdistdir}/doc/generic/velthuis/xetex-examples.pdf
%doc %{_texmfdistdir}/doc/generic/velthuis/xetex-examples.tex
%doc %{_texmfdistdir}/doc/generic/velthuis/xetex-misspaal.pdf
%doc %{_texmfdistdir}/doc/generic/velthuis/xetex-misspaal.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
