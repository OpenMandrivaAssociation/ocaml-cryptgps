Name:           ocaml-cryptgps
Version:        0.2.1
Release:        3
Summary:        Cryptographic functions 
License:        MIT/X11
Group:          Development/Other
URL:            http://projects.camlcity.org/projects/cryptgps.html
Source0:        http://download.camlcity.org/download/cryptgps-%{version}.tar.gz
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml

%description
This library implements the symmetric cryptographic algorithms Blowfish, DES,
and 3DES. The algorithms are written in OCaml, i.e. this is not a binding to
some C library, but the implementation itself.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n cryptgps

%build
make all opt

%install
rm -rf %{buildroot}
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
export DLLDIR=$OCAMLFIND_DESTDIR/stublibs
mkdir -p $OCAMLFIND_DESTDIR/stublibs
mkdir -p $OCAMLFIND_DESTDIR/cryptgps
make install
install -m 0644 *.cmx $OCAMLFIND_DESTDIR/cryptgps/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc LICENSE README
%dir %{_libdir}/ocaml/cryptgps
%{_libdir}/ocaml/cryptgps/META
%{_libdir}/ocaml/cryptgps/*.cma
%{_libdir}/ocaml/cryptgps/*.cmi

%files devel
%defattr(-,root,root)
%doc test
%{_libdir}/ocaml/cryptgps/*.a
%{_libdir}/ocaml/cryptgps/*.cmxa
%{_libdir}/ocaml/cryptgps/*.cmx
%{_libdir}/ocaml/cryptgps/*.mli



%changelog
* Wed May 09 2012 Crispin Boylan <crisb@mandriva.org> 0.2.1-2
+ Revision: 797771
- Rebuild

* Sat Aug 22 2009 Florent Monnier <blue_prawn@mandriva.org> 0.2.1-1mdv2011.0
+ Revision: 419689
- import ocaml-cryptgps

