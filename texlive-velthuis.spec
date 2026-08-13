%global tl_name velthuis
%global tl_revision 66186
%global tl_version 2.17.1

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
Release:	%{tl_revision}.1
Summary:	Typeset Devanagari
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/language/devanagari/velthuis
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/velthuis.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/velthuis.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(velthuis.bin)
Requires:	texlive(xetex-devanagari)
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
Frans Velthuis' preprocessor for Devanagari text, and fonts and macros
to use when typesetting the processed text. The macros provide features
that support Sanskrit, Hindi, Marathi, Nepali, and other languages
typically printed in the Devanagari script. The package provides fonts,
in both Metafont and Type 1 formats. Users of modern TeX distributions
may care to try the XeTeX based package, which is far preferable for
users who can type Unicode text.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from velthuis:
MixedMap dvng.map
TL_DROPIN_EOF
