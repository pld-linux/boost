#
# TODO:
#	- think about building MPI.
#	- split shared libs from core package into -iostreams/-serialization.
#
# Conditional build:
%bcond_without	python	# without boost-python support
#
%define		_fver	%(echo %{version} | tr . _)
Summary:	The Boost C++ Libraries
Summary(pl.UTF-8):	Biblioteki C++ "Boost"
Name:		boost
Version:	1.37.0
Release:	2.1
License:	Boost Software License and others
Group:		Libraries
Source0:	http://dl.sourceforge.net/boost/%{name}_%{_fver}.tar.bz2
# Source0-md5:	8d9f990bfb7e83769fa5f1d6f065bc92
Patch0:		%{name}-climits.patch
Patch1:		%{name}-link.patch
Patch2:		%{name}-ticket-2499.patch
Patch3:		%{name}-gcc43.patch
URL:		http://www.boost.org/
BuildRequires:	boost-jam >= 3.1.12
BuildRequires:	bzip2-devel
BuildRequires:	expat-devel
BuildRequires:	libicu-devel
BuildRequires:	libstdc++-devel
BuildRequires:	perl-base
%{?with_python:BuildRequires:	python-devel >= 2.2}
BuildRequires:	rpm-pythonprov
BuildRequires:	zlib-devel
BuildConflicts:	gcc = 5:3.3.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Boost web site provides free peer-reviewed portable C++ source
libraries. The emphasis is on libraries which work well with the C++
Standard Library. One goal is to establish "existing practice" and
provide reference implementations so that the Boost libraries are
suitable for eventual standardization. Some of the libraries have
already been proposed for inclusion in the C++ Standards Committee's
upcoming C++ Standard Library Technical Report.

%description -l pl.UTF-8
Strona http://www.boost.org/ dostarcza darmowe biblioteki C++ wraz z
kodem źródłowym. Nacisk położono na biblioteki, które dobrze
współpracują ze standardową biblioteką C++. Celem jest ustanowienie
"istniejącej praktyki" i dostarczenie implementacji, tak że biblioteki
"Boost" nadają się do ewentualnej standaryzacji. Niektóre z bibliotek
już zostały zgłoszone do komitetu standaryzacyjnego C++ w nadchodzącym
Raporcie Technicznym Biblioteki Standardowej C++

%package devel
Summary:	Boost C++ development headers
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek C++ Boost
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-date_time = %{version}-%{release}
Requires:	%{name}-filesystem = %{version}-%{release}
Requires:	%{name}-graph = %{version}-%{release}
Requires:	%{name}-program_options = %{version}-%{release}
Requires:	%{name}-regex = %{version}-%{release}
Requires:	%{name}-signals = %{version}-%{release}
Requires:	%{name}-system = %{version}-%{release}
Requires:	%{name}-test = %{version}-%{release}
Requires:	%{name}-thread = %{version}-%{release}
Requires:	%{name}-wave = %{version}-%{release}
Requires:	libstdc++-devel
Obsoletes:	boost-any-devel
Obsoletes:	boost-array-devel
Obsoletes:	boost-asio
Obsoletes:	boost-bind-devel
Obsoletes:	boost-call_traits-devel
Obsoletes:	boost-compatibility-devel
Obsoletes:	boost-compose-devel
Obsoletes:	boost-compressed_pair-devel
Obsoletes:	boost-concept_check-devel
Obsoletes:	boost-conversion-devel
Obsoletes:	boost-crc-devel
Obsoletes:	boost-date_time-devel
Obsoletes:	boost-filesystem-devel
Obsoletes:	boost-graph-devel
Obsoletes:	boost-mem_fn-devel
Obsoletes:	boost-mpl-devel
Obsoletes:	boost-preprocessor-devel
Obsoletes:	boost-program_options-devel
Obsoletes:	boost-ref-devel
Obsoletes:	boost-regex-devel
Obsoletes:	boost-signals-devel
Obsoletes:	boost-spirit-devel
Obsoletes:	boost-statechart-devel
Obsoletes:	boost-static_assert-devel
Obsoletes:	boost-test-devel
Obsoletes:	boost-thread-devel
Obsoletes:	boost-tr1-devel
Obsoletes:	boost-type_traits-devel
Obsoletes:	boost-typeof-devel
Obsoletes:	boost-uBLAS-devel
Obsoletes:	boost-utility-devel
Obsoletes:	boost-wave-devel
Obsoletes:	boost-xpressive-devel

%description devel
Header files for the Boost C++ libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek C++ Boost.

%package static
Summary:	Static version of base Boost C++ libraries
Summary(pl.UTF-8):	Statyczne wersje podstawowych bibliotek C++ Boost
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	boost-static < 1.33

%description static
Static version of base Boost C++ libraries.

%description static -l pl.UTF-8
Statyczne wersje podstawowych bibliotek C++ Boost.

%package python
Summary:	Boost.Python library
Summary(pl.UTF-8):	biblioteka Boost.Python
Group:		Libraries
%pyrequires_eq	python

%description python
Use the Boost Python Library to quickly and easily export a C++
library to Python such that the Python interface is very similar to
the C++ interface. It is designed to be minimally intrusive on your
C++ design. In most cases, you should not have to alter your C++
classes in any way in order to use them with Boost.Python. The system
should simply ``reflect'' your C++ classes and functions into Python.

%description python -l pl.UTF-8
Biblioteka Boost Python służy do szybkiego i prostego eksportu
biblioteki C++ do Pythona, tak że interfejs Pythona jest bardzo
podobny do interfejsu C++. Biblioteka jest zaprojektowana tak, żeby
narzucać jak najmniej wymagań dotyczących konstrukcjii C++. W
większości przypadków nie trzeba w ogóle zmieniać własnych klas C++,
żeby używać ich z Boost.Python. System powinien po prostu ,,odbić''
klasy C++ i funkcje do Pythona.

%package python-devel
Summary:	Boost.Python development headers
Summary(pl.UTF-8):	Pliki nagłówkowe dla Boost.Python
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-python = %{version}-%{release}

%description python-devel
Headers for the Boost.Python library.

%description python-devel -l pl.UTF-8
Pliki nagłówkowe dla biblioteki Boost.Python.

%package python-static
Summary:	Static version of Boost.Python library
Summary(pl.UTF-8):	Statyczna wersja biblioteki Boost.Python
Group:		Development/Libraries
Requires:	%{name}-python-devel = %{version}-%{release}

%description python-static
Static version of Boost.Python library.

%description python-static -l pl.UTF-8
Statyczna wersja biblioteki Boost.Python.

%package date_time
Summary:	Date-Time library
Summary(pl.UTF-8):	Biblioteka daty-czasu
Group:		Libraries
Obsoletes:	boost < 1.33

%description date_time
A set of date-time libraries.

%description date_time -l pl.UTF-8
Zbiór bibliotek daty-czasu.

%package filesystem
Summary:	Portable paths, iteration over directories, and other useful filesystem operations
Summary(pl.UTF-8):	Przenośne ścieżki, iteracje katalogów i inne użyteczne operacje na systemie plików
Group:		Libraries
Requires:	%{name}-system = %{version}-%{release}
Obsoletes:	boost < 1.33

%description filesystem
The boost::filesystem library provides portable facilities to query
and manipulate paths, files, and directories.

%description filesystem -l pl.UTF-8
Przenośna biblioteka boost::filesystem dostarcza ułatwienia w
operacjach na ścieżkach, plikach i katalogach.

%package graph
Summary:	General purpose, generic C++ library for graph data structures and graph algorithms
Summary(pl.UTF-8):	Biblioteka ogólnego przeznaczenia w C++ dla struktur danych typu grafy oraz algorytmów związanych z grafami
Group:		Libraries

%description graph
The boost::graph library provides portable facilities to operate on
graph data structures using graph algorithms.

%description graph -l pl.UTF-8
Przenośna biblioteka boost::graph dostarcza ułatwienia w operacjach na
strukturach danych typu graf za pomocą algorytmów związanych z
grafami.

%package program_options
Summary:	Access to program options, via conventional methods such as command line and config file
Summary(pl.UTF-8):	Dostęp do opcji programu za pomocą typowych metod, jak linia poleceń i plik konfiguracyjny
Group:		Libraries

%description program_options
The program_options library allows program developers to obtain
program options, that is (name, value) pairs from the user, via
conventional methods such as command line and config file.

%description program_options -l pl.UTF-8
Biblioteka program_options umożliwia uzyskanie od użytkownika opcji
programu, czyli par (nazwa, wartość), za pomocą typowych metod, takich
jak linia poleceń, czy plik konfiguracyjny.

%package regex
Summary:	Boost C++ regular expressions library
Summary(pl.UTF-8):	Biblioteka wyrażeń regularnych Boost C++
Group:		Libraries

%description regex
Shared library for Boost C++ regular expressions.

%description regex -l pl.UTF-8
Biblioteka wyrażeń regularnych dla C++, biblioteki dzielone.

%package signals
Summary:	Signals & slots callback implementation
Summary(pl.UTF-8):	Implementacja sygnałów i slotów
Group:		Libraries
Obsoletes:	boost < 1.33

%description signals
The boost::signals library is an implementation of a signals and slots
system.

%description signals -l pl.UTF-8
Biblioteka boost::signals jest implementacją systemu sygnałów i
slotów.

%package system
Summary:	Support for getting system specific error codes
Summary(pl.UTF-8):	Wsparcie dla pobierania specyficznych dla systemu kodów błędów
Group:		Libraries

%description system
The Boost System library provides simple, light-weight error_code
objects that encapsulate system-specific error code values, yet also
provide access to more abstract and portable error conditions objects.

%package test
Summary:	Support for program testing and execution monitoring
Summary(pl.UTF-8):	Wsparcie dla testowania i monitorowania programu
Group:		Libraries
Obsoletes:	boost < 1.33

%description test
Support for simple program testing, full unit testing, and for program
execution monitoring.

%description test -l pl.UTF-8
Wsparcie dla prostego testowania programu, pełnego testowania i
monitorowania wykonania programu.

%package thread
Summary:	Portable C++ threads library
Summary(pl.UTF-8):	Przenośna biblioteka wątków C++
Group:		Libraries
Obsoletes:	boost < 1.33

%description thread
Portable C++ threads library - shared library.

%description thread -l pl.UTF-8
Przenośna biblioteka wątków dla C++ - biblioteka dzielona.

%package wave
Summary:	Boost.Wave - a standard compliant C++ preprocessor library
Summary(pl.UTF-8):	Boost.Wave - zgodna ze standardem biblioteka preprocesora C++
Group:		Development/Libraries

%description wave
Boost.Wave - a standard compliant C++ preprocessor library.

%description wave -l pl.UTF-8
Boost.Wave - zgodna ze standardem biblioteka preprocesora C++.

%package doc
Summary:	Boost C++ Library documentation
Summary(pl.UTF-8):	Dokumentacja dla biblioteki Boost C++
Group:		Documentation
Requires:	%{name}-devel = %{version}-%{release}

%description doc
Documentation for the Boost C++ Library.

%description doc -l pl.UTF-8
Dokumentacja dla biblioteki Boost C++.

%prep
%setup -q -n %{name}_%{_fver}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

# - don't know how to pass it through (b)jam -s (no way?)
#   due to oversophisticated build flags system.
# - pass -fPIC due to <shared-linkable> removal.
%{__sed} -i "s/<optimization>speed : -O3/<optimization>speed : ${CXXFLAGS:-%rpmcxxflags} -fPIC/" tools/build/v2/tools/gcc.jam

# cleanup -g switch to avoid override debuginfocflags.
%{__sed} -i 's/<debug-symbols>on : -g/<debug-symbols>on :/' tools/build/v2/tools/gcc.jam
# link against shared expat library.
%{__sed} -i 's:find-static:find-shared:' libs/graph/build/Jamfile.v2

%ifarch alpha
# -pthread gcc parameter doesn't add _REENTRANT to cpp macros on alpha (only)
# don't know, is it gcc bug or intentional omission?
# anyway, boost check of -D_REENTRANT in its headers, so it's needed here
%{__perl} -pi -e 's/(CFLAGS.*-pthread)/$1 -D_REENTRANT/' tools/build/v1/gcc-tools.jam
%endif

cat << EOF > tools/build/v2/user-config.jam
using gcc : %(%{__cxx} -dumpversion) : %{__cxx} ;
EOF

%build
%if %{with python}
PYTHON_VERSION=$(%{__python} -c 'import sys; print sys.version[0:3]')
PYTHON_ROOT=%{_prefix}
%else
PYTHON_ROOT=
PYTHON_VERSION=
%endif
EXPAT_INCLUDE=%{_includedir} \
EXPAT_LIBPATH=%{_libdir} \
ICU_PATH=%{_prefix} \
bjam \
	-d2 --toolset=gcc \
	variant=release debug-symbols=on inlining=on link=static,shared threading=multi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}}

cp -rf boost $RPM_BUILD_ROOT%{_includedir}

install bin.v2/libs/*/build/gcc-*/release/debug-symbols-on/inlining-on/link-static/threading-multi/lib*.a $RPM_BUILD_ROOT%{_libdir}
install bin.v2/libs/*/build/gcc-*/release/debug-symbols-on/inlining-on/threading-multi/lib*.so.*.*.* $RPM_BUILD_ROOT%{_libdir}

# create symlinks without -gccXX-mt-* things in names
for f in $RPM_BUILD_ROOT%{_libdir}/*.so.*.*.*; do
	[ -f "$f" ] || continue
	f=$(basename "$f")
	soname=$(basename "$f" | sed -e 's#-gcc..-mt-.*#.so#g')
	ln -s "$f" "$RPM_BUILD_ROOT%{_libdir}/$soname"
done
for f in $RPM_BUILD_ROOT%{_libdir}/*.a; do
	[ -f "$f" ] || continue
	f=$(basename "$f")
	soname=$(basename "$f" | sed -e 's#-gcc..-mt-.*#.a#g')
	ln -s "$f" "$RPM_BUILD_ROOT%{_libdir}/$soname"
done

# documentation
install -d $RPM_BUILD_ROOT%{_docdir}/boost-%{version}

# as the documentation doesn't completely reside in a directory of its
# own, we need to find out ourselves... this looks for HTML files and
# then collects everything linked from those.  this is certainly quite
# unoptimized wrt mkdir calls, but does it really matter?
installdocs() {
for i in $(find -type f -name '*.htm*'); do
	# bjam docu is included in the boost-jam RPM
	if test "`echo $i | sed 's,jam_src,,'`" = "$i"; then
		install -d $RPM_BUILD_ROOT%{_docdir}/boost-%{version}/${i%/*}
		for LINKED in `%{__perl} - $i $RPM_BUILD_ROOT%{_docdir}/boost-%{version}/$i <<'EOT'
			sub rewrite_link
			{
				my $link = shift;
				# rewrite links from boost/* to %{_includedir}/boost/* and
				# ignore external links as well as document-internal ones.
				# HTML files are also ignored as they get installed anyway.
				if (!($link =~ s,^(?:../)*boost/,%{_includedir}/boost/,) && !($link =~ m,(?:^[^/]+:|^\#|\.html?(?:$|\#)),))
				{
					(my $file = $link) =~ s/\#.*//;
					print "$file\n";
				}
				$link;
			}
			open IN, @ARGV[0];
			open OUT, ">@ARGV[1]";
			my $in_link;
			while (<IN>)
			{
				$in_link and s/^\s*"([^"> ]*)"/'"' . rewrite_link($1) . '"'/e;
				s/(href|src)="([^"> ]*)"/"$1=\"" . rewrite_link($2) . '"'/eig;
				print OUT;
				$in_link = /href|src=\s*$/;
			}
EOT`; do
			TARGET=${i%/*}/$LINKED
			# ignore non-existant linked files
			if test -f $TARGET; then
				install -D -m 644 $TARGET $RPM_BUILD_ROOT%{_docdir}/boost-%{version}/$TARGET
			fi
		done
	fi
done
}; installdocs

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	date_time -p /sbin/ldconfig
%postun	date_time -p /sbin/ldconfig

%post	filesystem -p /sbin/ldconfig
%postun	filesystem -p /sbin/ldconfig

%post	graph -p /sbin/ldconfig
%postun	graph -p /sbin/ldconfig

%post	python -p /sbin/ldconfig
%postun	python -p /sbin/ldconfig

%post	program_options -p /sbin/ldconfig
%postun	program_options -p /sbin/ldconfig

%post	regex -p /sbin/ldconfig
%postun regex -p /sbin/ldconfig

%post	signals -p /sbin/ldconfig
%postun	signals -p /sbin/ldconfig

%post	system -p /sbin/ldconfig
%postun	system -p /sbin/ldconfig

%post	test -p /sbin/ldconfig
%postun	test -p /sbin/ldconfig

%post	wave -p /sbin/ldconfig
%postun	wave -p /sbin/ldconfig

%post	thread -p /sbin/ldconfig
%postun	thread -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_iostreams*.so.*.*.*
%attr(755,root,root) %{_libdir}/libboost_math_*.so.*.*.*
%attr(755,root,root) %{_libdir}/libboost_serialization*.so.*.*.*
%attr(755,root,root) %{_libdir}/libboost_wserialization*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/boost
%attr(755,root,root) %{_libdir}/libboost_date_time*.so
%attr(755,root,root) %{_libdir}/libboost_filesystem*.so
%attr(755,root,root) %{_libdir}/libboost_graph*.so
%attr(755,root,root) %{_libdir}/libboost_iostreams*.so
%attr(755,root,root) %{_libdir}/libboost_math_*.so
%attr(755,root,root) %{_libdir}/libboost_prg_exec_monitor*.so
%attr(755,root,root) %{_libdir}/libboost_program_options*.so
%attr(755,root,root) %{_libdir}/libboost_regex*.so
%attr(755,root,root) %{_libdir}/libboost_serialization*.so
%attr(755,root,root) %{_libdir}/libboost_signals*.so
%attr(755,root,root) %{_libdir}/libboost_system*.so
%attr(755,root,root) %{_libdir}/libboost_thread*.so
%attr(755,root,root) %{_libdir}/libboost_unit_test_framework*.so
%attr(755,root,root) %{_libdir}/libboost_wave*.so
%attr(755,root,root) %{_libdir}/libboost_wserialization*.so

%files static
%defattr(644,root,root,755)
%{_libdir}/libboost_date_time*.a
%{_libdir}/libboost_filesystem*.a
%{_libdir}/libboost_grap*.a
%{_libdir}/libboost_iostreams*.a
%{_libdir}/libboost_math_*.a
%{_libdir}/libboost_prg_exec_monitor*.a
%{_libdir}/libboost_program_options*.a
%{_libdir}/libboost_regex*.a
%{_libdir}/libboost_serialization*.a
%{_libdir}/libboost_signals*.a
%{_libdir}/libboost_system*.a
%{_libdir}/libboost_test_exec_monitor*.a
%{_libdir}/libboost_thread*.a
%{_libdir}/libboost_unit_test_framework*.a
%{_libdir}/libboost_wave*.a
%{_libdir}/libboost_wserialization*.a

%if %{with python}
%files python
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_python*.so.*.*.*

%files python-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_python*.so
%{_includedir}/boost/python
%{_includedir}/boost/python.hpp

%files python-static
%defattr(644,root,root,755)
%{_libdir}/libboost_python*.a
%endif

%files date_time
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_date_time*.so.*.*.*

%files filesystem
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_filesystem*.so.*.*.*

%files graph
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_graph*.so.*.*.*

%files program_options
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_program_options*.so.*.*.*

%files regex
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_regex*.so.*.*.*

%files signals
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_signals*.so.*.*.*

%files system
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_system*.so.*.*.*

%files test
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_prg_exec_monitor*.so.*.*.*
%attr(755,root,root) %{_libdir}/libboost_unit_test_framework*.so.*.*.*

%files thread
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_thread*.so.*.*.*

%files wave
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_wave*.so.*.*.*

%files doc
%defattr(644,root,root,755)
%{_docdir}/%{name}-%{version}
