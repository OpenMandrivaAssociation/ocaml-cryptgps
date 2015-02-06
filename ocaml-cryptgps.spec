%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	Cryptographic functions for OCaml
Name:		ocaml-cryptgps
Version:	0.2.1
Release:	5
License:	MIT/X11
Group:		Development/Other
Url:		http://projects.camlcity.org/projects/cryptgps.html
Source0:	http://download.camlcity.org/download/cryptgps-%{version}.tar.gz
BuildRequires:	ocaml
BuildRequires:	ocaml-findlib

%description
This library implements the symmetric cryptographic algorithms Blowfish, DES,
and 3DES. The algorithms are written in OCaml, i.e. this is not a binding to
some C library, but the implementation itself.

%files
%doc LICENSE README
%dir %{_libdir}/ocaml/cryptgps
%{_libdir}/ocaml/cryptgps/META
%{_libdir}/ocaml/cryptgps/*.cma
%{_libdir}/ocaml/cryptgps/*.cmi

#----------------------------------------------------------------------------

%package devel
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{name} = %{EVRD}

%description devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%files devel
%doc test
%{_libdir}/ocaml/cryptgps/*.a
%{_libdir}/ocaml/cryptgps/*.cmxa
%{_libdir}/ocaml/cryptgps/*.cmx
%{_libdir}/ocaml/cryptgps/*.mli

#----------------------------------------------------------------------------

%prep
%setup -q -n cryptgps

%build
make all opt

%install
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
export DLLDIR=$OCAMLFIND_DESTDIR/stublibs
mkdir -p $OCAMLFIND_DESTDIR/stublibs
mkdir -p $OCAMLFIND_DESTDIR/cryptgps
make install
install -m 0644 *.cmx $OCAMLFIND_DESTDIR/cryptgps/

