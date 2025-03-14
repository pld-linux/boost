#
# TODO:
#	- think about building MPI.
#	- split shared libs from core package into -iostreams/-serialization.
#
# Conditional build:
%bcond_without	python2		# boost-python[2] support
%bcond_without	python3		# boost-python3 support
%bcond_without	numpy		# boost-numpy support
%bcond_without	doc		# don't package documentation

%define		fver	%(echo %{version} | tr . _)
Summary:	The Boost C++ Libraries
Summary(pl.UTF-8):	Biblioteki C++ "Boost"
Name:		boost
Version:	1.85.0
Release:	7
Epoch:		1
License:	Boost Software License and others
Group:		Libraries
Source0:	https://boostorg.jfrog.io/artifactory/main/release/%{version}/source/%{name}_%{fver}.tar.bz2
# Source0-md5:	429d451cb9197143cc77962c5ff272ef
Patch0:		%{name}-link.patch
Patch1:		%{name}-clean-gcc-flags.patch
Patch2:		%{name}-fallthrough.patch
Patch3:		includes.patch
Patch4:		numpy2.patch
# FC Patches:
Patch201:	%{name}-python-abi_letters.patch
# https://svn.boost.org/trac/boost/ticket/5637
Patch203:	%{name}-1.54.0-mpl-print.patch
# https://svn.boost.org/trac/boost/ticket/8881
Patch221:	%{name}-1.54.0-mpi-unused_typedef.patch
URL:		http://www.boost.org/
BuildRequires:	bzip2-devel
BuildRequires:	expat-devel
BuildRequires:	libicu-devel
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	perl-base
%if %{with python2}
BuildRequires:	python-devel >= 2.2
%{?with_numpy:BuildRequires:	python-numpy-devel}
%endif
%if %{with python3}
BuildRequires:	python3-devel
%{?with_numpy:BuildRequires:	python3-numpy-devel}
%endif
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.750
BuildRequires:	zlib-devel
Obsoletes:	boost-signals < 1.69
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-DBOOST_IOSTREAMS_USE_DEPRECATED=1

%define		py2v %(echo %{py_ver} | tr -d .)
%define		py3v %(echo %{py3_ver} | tr -d .)

%if %{_ver_ge "%{py3_ver}" "3.8"}
%define		py3v_suffix ""
%else
%define		py3v_suffix "m"
%endif

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
Raporcie Technicznym Biblioteki Standardowej C++.

%package devel
Summary:	Boost C++ development headers
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek C++ Boost
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name}-chrono = %{epoch}:%{version}-%{release}
Requires:	%{name}-context = %{epoch}:%{version}-%{release}
Requires:	%{name}-date_time = %{epoch}:%{version}-%{release}
Requires:	%{name}-fiber = %{epoch}:%{version}-%{release}
Requires:	%{name}-filesystem = %{epoch}:%{version}-%{release}
Requires:	%{name}-graph = %{epoch}:%{version}-%{release}
Requires:	%{name}-json = %{epoch}:%{version}-%{release}
Requires:	%{name}-locale = %{epoch}:%{version}-%{release}
Requires:	%{name}-log = %{epoch}:%{version}-%{release}
Requires:	%{name}-program_options = %{epoch}:%{version}-%{release}
Requires:	%{name}-regex = %{epoch}:%{version}-%{release}
Requires:	%{name}-system = %{epoch}:%{version}-%{release}
Requires:	%{name}-test = %{epoch}:%{version}-%{release}
Requires:	%{name}-thread = %{epoch}:%{version}-%{release}
Requires:	%{name}-timer = %{epoch}:%{version}-%{release}
Requires:	%{name}-url = %{epoch}:%{version}-%{release}
Requires:	%{name}-wave = %{epoch}:%{version}-%{release}
Requires:	libstdc++-devel >= 6:4.7
Obsoletes:	boost-any-devel < 1.35
Obsoletes:	boost-array-devel < 1.35
Obsoletes:	boost-asio < 1.3.0
Obsoletes:	boost-bind-devel < 1.35
Obsoletes:	boost-call_traits-devel < 1.34.1-2
Obsoletes:	boost-compatibility-devel < 1.35
Obsoletes:	boost-compose-devel < 1.31
Obsoletes:	boost-compressed_pair-devel < 1.35
Obsoletes:	boost-concept_check-devel < 1.33.1-1
Obsoletes:	boost-conversion-devel < 1.33.1-1
Obsoletes:	boost-crc-devel < 1.35
Obsoletes:	boost-date_time-devel < 1.35
Obsoletes:	boost-filesystem-devel < 1.35
Obsoletes:	boost-graph-devel < 1.35
Obsoletes:	boost-mem_fn-devel < 1.33.1-1
Obsoletes:	boost-mpl-devel < 1.33.1-1
Obsoletes:	boost-preprocessor-devel < 1.33.1-1
Obsoletes:	boost-program_options-devel < 1.35
Obsoletes:	boost-ref-devel < 1.34.1-2
Obsoletes:	boost-regex-devel < 1.35
Obsoletes:	boost-signals-devel < 1.35
Obsoletes:	boost-spirit-devel < 1.35
Obsoletes:	boost-statechart-devel < 1.35
Obsoletes:	boost-static_assert-devel < 1.33.1-1
Obsoletes:	boost-test-devel < 1.35
Obsoletes:	boost-thread-devel < 1.35
Obsoletes:	boost-tr1-devel < 1.35
Obsoletes:	boost-type_traits-devel < 1.33.1-1
Obsoletes:	boost-typeof-devel < 1.35
Obsoletes:	boost-uBLAS-devel < 1.35
Obsoletes:	boost-utility-devel < 1.33.1-1
Obsoletes:	boost-wave-devel < 1.35
Obsoletes:	boost-xpressive-devel < 1.35

%description devel
Header files for the Boost C++ libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek C++ Boost.

%package static
Summary:	Static version of base Boost C++ libraries
Summary(pl.UTF-8):	Statyczne wersje podstawowych bibliotek C++ Boost
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}
Obsoletes:	boost-date_time-static < 1.35
Obsoletes:	boost-filesystem-static < 1.35
Obsoletes:	boost-graph-static < 1.35
Obsoletes:	boost-program_options-static < 1.35
Obsoletes:	boost-regex-static < 1.35
Obsoletes:	boost-signals-static < 1.35
Obsoletes:	boost-test-static < 1.35
Obsoletes:	boost-thread-static < 1.35
Obsoletes:	boost-wave-static < 1.35

%description static
Static version of base Boost C++ libraries.

%description static -l pl.UTF-8
Statyczne wersje podstawowych bibliotek C++ Boost.

%package python-devel-common
Summary:	Boost.Python development headers
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Boost.Python
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description python-devel-common
Headers for the Boost.Python library.

%description python-devel-common -l pl.UTF-8
Pliki nagłówkowe biblioteki Boost.Python.

%package python
Summary:	Boost.Python library for Python 2
Summary(pl.UTF-8):	Biblioteka Boost.Python dla Pythona 2
Group:		Libraries
Requires:	python-libs

%description python
Use the Boost Python Library to quickly and easily export a C++
library to Python 2 such that the Python 2 interface is very similar
to the C++ interface. It is designed to be minimally intrusive on your
C++ design. In most cases, you should not have to alter your C++
classes in any way in order to use them with Boost.Python. The system
should simply ``reflect'' your C++ classes and functions into Python
3.

%description python -l pl.UTF-8
Biblioteka Boost Python służy do szybkiego i prostego eksportu
biblioteki C++ do Pythona 2, tak że interfejs Pythona 2 jest bardzo
podobny do interfejsu C++. Biblioteka jest zaprojektowana tak, żeby
narzucać jak najmniej wymagań dotyczących konstrukcjii C++. W
większości przypadków nie trzeba w ogóle zmieniać własnych klas C++,
żeby używać ich z Boost.Python. System powinien po prostu ,,odbić''
klasy C++ i funkcje do Pythona 3.

%package python-devel
Summary:	Boost.Python development files for Python 2
Summary(pl.UTF-8):	Pliki programistyczne biblioteki Boost.Python dla Pythona 2
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}
Requires:	%{name}-python = %{epoch}:%{version}-%{release}
Requires:	%{name}-python-devel-common = %{epoch}:%{version}-%{release}

%description python-devel
Boost.Python development files for Python 2.

%description python-devel -l pl.UTF-8
Pliki programistyczne biblioteki Boost.Python dla Pythona 2.

%package python-static
Summary:	Static version of Boost.Python library for Python 2
Summary(pl.UTF-8):	Statyczna wersja biblioteki Boost.Python dla Pythona 2
Group:		Development/Libraries
Requires:	%{name}-python-devel = %{epoch}:%{version}-%{release}

%description python-static
Static version of Boost.Python library for Python 2.

%description python-static -l pl.UTF-8
Statyczna wersja biblioteki Boost.Python dla Pythona 2.

%package python3
Summary:	Boost.Python library for Python 3
Summary(pl.UTF-8):	biblioteka Boost.Python dla Pythona 3
Group:		Libraries
Requires:	python3-libs

%description python3
Use the Boost Python Library to quickly and easily export a C++
library to Python 3 such that the Python 3 interface is very similar
to the C++ interface. It is designed to be minimally intrusive on your
C++ design. In most cases, you should not have to alter your C++
classes in any way in order to use them with Boost.Python. The system
should simply ``reflect'' your C++ classes and functions into Python
3.

%description python3 -l pl.UTF-8
Biblioteka Boost Python służy do szybkiego i prostego eksportu
biblioteki C++ do Pythona 3, tak że interfejs Pythona 3 jest bardzo
podobny do interfejsu C++. Biblioteka jest zaprojektowana tak, żeby
narzucać jak najmniej wymagań dotyczących konstrukcjii C++. W
większości przypadków nie trzeba w ogóle zmieniać własnych klas C++,
żeby używać ich z Boost.Python. System powinien po prostu ,,odbić''
klasy C++ i funkcje do Pythona 3.

%package python3-devel
Summary:	Boost.Python development files for Python 3
Summary(pl.UTF-8):	Pliki programistyczne biblioteki Boost.Python dla Pythona 3
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}
Requires:	%{name}-python-devel-common = %{epoch}:%{version}-%{release}
Requires:	%{name}-python3 = %{epoch}:%{version}-%{release}

%description python3-devel
Boost.Python development files for Python 3.

%description python3-devel -l pl.UTF-8
Pliki programistyczne biblioteki Boost.Python dla Pythona 3.

%package python3-static
Summary:	Static version of Boost.Python library for Python 3
Summary(pl.UTF-8):	Statyczna wersja biblioteki Boost.Python dla Pythona 3
Group:		Development/Libraries
Requires:	%{name}-python3-devel = %{epoch}:%{version}-%{release}

%description python3-static
Static version of Boost.Python library for Python 3.

%description python3-static -l pl.UTF-8
Statyczna wersja biblioteki Boost.Python dla Pythona 3.

%package chrono
Summary:	Useful time utilities
Summary(pl.UTF-8):	Przydatne funkcje związane z czasem
Group:		Libraries
Obsoletes:	boost < 1.33

%description chrono
Useful time utilities.

%description chrono -l pl.UTF-8
Przydatne funkcje związane z czasem.

%package context
Summary:	Boost.Context - context switching library
Summary(pl.UTF-8):	Boost.Context - biblioteka do zmiany kontekstu
Group:		Libraries

%description context
Boost.Context - context switching library, providing a sort of
cooperative multitasking on a single thread.

%description context -l pl.UTF-8
Boost.Context - biblioteka do zmiany kontekstu, zapewniająca pewną
wielozadaniowość kooperatywnąw ramach pojedynczego wątku.

%package date_time
Summary:	Date-Time library
Summary(pl.UTF-8):	Biblioteka daty-czasu
Group:		Libraries
Obsoletes:	boost < 1.33

%description date_time
A set of date-time libraries.

%description date_time -l pl.UTF-8
Zbiór bibliotek daty-czasu.

%package fiber
Summary:	A framework for micro-/userland-threads (fibers) scheduled cooperatively
Summary(pl.UTF-8):	Szkielet mikrowątków przestrzeni użytkownika (fibers), szeregowanych kooperacyjnie
Group:		Libraries

%description fiber
boost::fiber provides a framework for micro-/userland-threads (fibers)
scheduled cooperatively. The API contains classes and functions
to manage and synchronize fibers similiar to boost.thread.

%description fiber -l pl.UTF-8
boost::fiber to szkielt mikrowątków przestrzeni użytkownika (fibers)
szeregowanych kooperacyjnie. API zawiera klasy i funkcje służące do
zarządzania i synchronizacji wątków podobne do boost.thread.

%package filesystem
Summary:	Portable paths, iteration over directories, and other useful filesystem operations
Summary(pl.UTF-8):	Przenośne ścieżki, iteracje katalogów i inne użyteczne operacje na systemie plików
Group:		Libraries
Requires:	%{name}-system = %{epoch}:%{version}-%{release}
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

%package json
Summary:	Boost.JSON - a portable C++ JSON library
Summary(pl.UTF-8):	Boost.JSON - przenośna biblioteka C++ dla formatu JSON
Group:		Development/Libraries

%description json
Boost.JSON is a portable C++ library which provides containers and
algorithms that implement JavaScript Object Notation, or simply
"JSON", a lightweight data-interchange format.

%description json -l pl.UTF-8
Boost.JSON to przenośna biblioteka C++, która dostarcza kontenery oraz
algorytmy implementujące JavaScript Object Notation, lub po prostu
"JSON", lekki format wymiany danych.

%package locale
Summary:	Provide localization and Unicode handling tools for C++
Summary(pl.UTF-8):	Narzędzia do obsługi lokalizacji i Unikodu w C++
Group:		Libraries

%description locale
Provide localization and Unicode handling tools for C++.

%description locale -l pl.UTF-8
Narzędzia do obsługi lokalizacji i Unikodu w C++.

%package log
Summary:	Provide logging tools for C++
Summary(pl.UTF-8):	Narzędzia do logowania w C++
Group:		Libraries

%description log
Provide logging tools for C++.

%description log -l pl.UTF-8
Narzędzia do logowania w C++.

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
Biblioteka współdzielona do obsługi wyrażeń regularnych w C++.

%package system
Summary:	Support for getting system specific error codes
Summary(pl.UTF-8):	Wsparcie dla pobierania specyficznych dla systemu kodów błędów
Group:		Libraries

%description system
The Boost System library provides simple, light-weight error_code
objects that encapsulate system-specific error code values, yet also
provide access to more abstract and portable error conditions objects.

%description system -l pl.UTF-8
Biblioteka Boost System udostępnia proste, lekkie obiekty error_code
obudowujące wartości kodów błędów specyficznych dla systemu, dając
jednocześnie dostęp do bardziej abstrakcyjnych i przenośnych obiektów
błędów.

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

%package timer
Summary:	Event timer, progress timer, and progress display classes
Summary(pl.UTF-8):	Klasy do obsługi pomiarów czasu, postępu i wyświetlania postępu
Group:		Libraries
Obsoletes:	boost < 1.33

%description timer
Event timer, progress timer, and progress display classes.

%description timer -l pl.UTF-8
Klasy do obsługi pomiarów czasu, postępu i wyświetlania postępu.

%package url
Summary:	Library for manipulating Uniform Resource Identifiers and Locators
Summary(pl.UTF-8):	Biblioteka do manipulacji Unfiform Resource Identifier i Locator
Group:		Libraries

%description url
Library for manipulating Uniform Resource Identifiers and Locators.

%description url -l pl.UTF-8
Biblioteka do manipulacji Unfiform Resource Identifier i Locator.

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
BuildArch:	noarch

%description doc
Documentation for the Boost C++ Library.

%description doc -l pl.UTF-8
Dokumentacja dla biblioteki Boost C++.

%prep
%setup -q -n %{name}_%{fver}
%patch -P 0 -p1
%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1
%patch -P 4 -p1 -d libs/python

%patch -P 201 -p1
%patch -P 203 -p0
%patch -P 221 -p1

%if "%{cc_version}" < "6.0"
CPPSTD="-std=c++11"
%else
CPPSTD=
%endif
cat << EOF > tools/build/src/user-config.jam
using gcc : %{cxx_version} : %{__cxx} : <cflags>"%{rpmcflags} -fPIC" <cxxflags>"%{rpmcxxflags} $CPPSTD -fPIC" <linkflags>"%{rpmldflags}" ;
EOF

# cleanup backups after patching
find '(' -name '*~' -o -name '*.orig' ')' -print0 | xargs -0 -r -l512 rm -f

%build
EXPAT_INCLUDE=%{_includedir} \
EXPAT_LIBPATH=%{_libdir} \
ICU_PATH=%{_prefix} \
./bootstrap.sh \
	--prefix=%{_prefix} \
	-without-libraries=python

./b2 \
	%{?__jobs:-j %{__jobs}} \
	-d2 --toolset=gcc \
%ifarch x32
	abi=x32 \
%endif
%ifarch %{ix86}
	boost.stacktrace.from_exception=off \
%endif
	debug-symbols=on \
	inlining=on \
	link=static,shared \
	threading=multi \
	variant=release

%if %{with python3}
echo "using python : %{py3_ver} : %{py3_prefix} : %{py3_incdir} : : : : %{py3v_suffix} ;" >> project-config.jam
./b2 \
	%{?__jobs:-j %{__jobs}} \
	--with-python python=%{py3_ver} \
	-a -d2 --toolset=gcc \
	debug-symbols=on \
	inlining=on \
	link=static,shared \
	threading=multi \
	variant=release
%endif

%if %{with python2}
%{__sed} -i -e '/^using python : 3/d' project-config.jam
echo "using python : %{py_ver} : %{py_prefix} : %{py_incdir} ;" >> project-config.jam
./b2 \
	%{?__jobs:-j %{__jobs}} \
	--with-python python=%{py_ver} \
	-a -d2 --toolset=gcc \
	debug-symbols=on \
	inlining=on \
	link=static,shared \
	threading=multi \
	variant=release
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}}

cp -rf boost $RPM_BUILD_ROOT%{_includedir}

install -p stage/lib/lib*.a $RPM_BUILD_ROOT%{_libdir}
install -p stage/lib/lib*.so.*.*.* $RPM_BUILD_ROOT%{_libdir}
cp -a stage/lib/lib*.so $RPM_BUILD_ROOT%{_libdir}
cp -a stage/lib/cmake $RPM_BUILD_ROOT%{_libdir}

%if %{with doc}
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
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	chrono -p /sbin/ldconfig
%postun	chrono -p /sbin/ldconfig

%post	context -p /sbin/ldconfig
%postun	context -p /sbin/ldconfig

%post	date_time -p /sbin/ldconfig
%postun	date_time -p /sbin/ldconfig

%post	fiber -p /sbin/ldconfig
%postun	fiber -p /sbin/ldconfig

%post	filesystem -p /sbin/ldconfig
%postun	filesystem -p /sbin/ldconfig

%post	graph -p /sbin/ldconfig
%postun	graph -p /sbin/ldconfig

%post	json -p /sbin/ldconfig
%postun	json -p /sbin/ldconfig

%post	locale -p /sbin/ldconfig
%postun	locale -p /sbin/ldconfig

%post	python -p /sbin/ldconfig
%postun	python -p /sbin/ldconfig

%post	python3 -p /sbin/ldconfig
%postun	python3 -p /sbin/ldconfig

%post	program_options -p /sbin/ldconfig
%postun	program_options -p /sbin/ldconfig

%post	regex -p /sbin/ldconfig
%postun regex -p /sbin/ldconfig

%post	system -p /sbin/ldconfig
%postun	system -p /sbin/ldconfig

%post	test -p /sbin/ldconfig
%postun	test -p /sbin/ldconfig

%post	thread -p /sbin/ldconfig
%postun	thread -p /sbin/ldconfig

%post	timer -p /sbin/ldconfig
%postun	timer -p /sbin/ldconfig

%post	url -p /sbin/ldconfig
%postun	url -p /sbin/ldconfig

%post	wave -p /sbin/ldconfig
%postun	wave -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_atomic.so.*.*.*
%attr(755,root,root) %{_libdir}/libboost_charconv.so.*.*.*
%attr(755,root,root) %{_libdir}/libboost_container.so.*.*.*
%attr(755,root,root) %{_libdir}/libboost_contract.so.*.*.*
%attr(755,root,root) %{_libdir}/libboost_coroutine.so.*.*.*
%attr(755,root,root) %{_libdir}/libboost_iostreams.so.*.*.*
%attr(755,root,root) %{_libdir}/libboost_nowide.so.*.*.*
%attr(755,root,root) %{_libdir}/libboost_random.so.*.*.*
%attr(755,root,root) %{_libdir}/libboost_serialization.so.*.*.*
%attr(755,root,root) %{_libdir}/libboost_stacktrace_*.so.*.*.*
%attr(755,root,root) %{_libdir}/libboost_type_erasure.so.*.*.*
%attr(755,root,root) %{_libdir}/libboost_wserialization.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_atomic.so
%attr(755,root,root) %{_libdir}/libboost_charconv.so
%attr(755,root,root) %{_libdir}/libboost_chrono.so
%attr(755,root,root) %{_libdir}/libboost_container.so
%attr(755,root,root) %{_libdir}/libboost_context.so
%attr(755,root,root) %{_libdir}/libboost_contract.so
%attr(755,root,root) %{_libdir}/libboost_coroutine.so
%attr(755,root,root) %{_libdir}/libboost_date_time.so
%attr(755,root,root) %{_libdir}/libboost_fiber.so
%attr(755,root,root) %{_libdir}/libboost_filesystem.so
%attr(755,root,root) %{_libdir}/libboost_graph.so
%attr(755,root,root) %{_libdir}/libboost_iostreams.so
%attr(755,root,root) %{_libdir}/libboost_json.so
%attr(755,root,root) %{_libdir}/libboost_locale.so
%attr(755,root,root) %{_libdir}/libboost_log.so
%attr(755,root,root) %{_libdir}/libboost_log_setup.so
%attr(755,root,root) %{_libdir}/libboost_nowide.so
%attr(755,root,root) %{_libdir}/libboost_prg_exec_monitor.so
%attr(755,root,root) %{_libdir}/libboost_program_options.so
%attr(755,root,root) %{_libdir}/libboost_regex.so
%attr(755,root,root) %{_libdir}/libboost_random.so
%attr(755,root,root) %{_libdir}/libboost_serialization.so
%attr(755,root,root) %{_libdir}/libboost_stacktrace_*.so
%attr(755,root,root) %{_libdir}/libboost_system.so
%attr(755,root,root) %{_libdir}/libboost_thread.so
%attr(755,root,root) %{_libdir}/libboost_timer.so
%attr(755,root,root) %{_libdir}/libboost_type_erasure.so
%attr(755,root,root) %{_libdir}/libboost_unit_test_framework.so
%attr(755,root,root) %{_libdir}/libboost_url.so
%attr(755,root,root) %{_libdir}/libboost_wave.so
%attr(755,root,root) %{_libdir}/libboost_wserialization.so
%{_includedir}/boost
%exclude %{_includedir}/boost/python
%exclude %{_includedir}/boost/python.hpp
%{_libdir}/cmake/Boost*
%{_libdir}/cmake/boost_*
%exclude %{_libdir}/cmake/boost_python-*

%files static
%defattr(644,root,root,755)
%{_libdir}/libboost_atomic.a
%{_libdir}/libboost_charconv.a
%{_libdir}/libboost_chrono.a
%{_libdir}/libboost_container.a
%{_libdir}/libboost_context.a
%{_libdir}/libboost_contract.a
%{_libdir}/libboost_coroutine.a
%{_libdir}/libboost_date_time.a
%{_libdir}/libboost_exception.a
%{_libdir}/libboost_fiber.a
%{_libdir}/libboost_filesystem.a
%{_libdir}/libboost_graph.a
%{_libdir}/libboost_iostreams.a
%{_libdir}/libboost_json.a
%{_libdir}/libboost_locale.a
%{_libdir}/libboost_log.a
%{_libdir}/libboost_log_setup.a
%{_libdir}/libboost_nowide.a
%{_libdir}/libboost_prg_exec_monitor.a
%{_libdir}/libboost_program_options.a
%{_libdir}/libboost_random.a
%{_libdir}/libboost_regex.a
%{_libdir}/libboost_serialization.a
%{_libdir}/libboost_stacktrace_*.a
%{_libdir}/libboost_system.a
%{_libdir}/libboost_test_exec_monitor.a
%{_libdir}/libboost_timer.a
%{_libdir}/libboost_url.a
%{_libdir}/libboost_thread.a
%{_libdir}/libboost_type_erasure.a
%{_libdir}/libboost_unit_test_framework.a
%{_libdir}/libboost_wave.a
%{_libdir}/libboost_wserialization.a

%if %{with python2} || %{with python3}
%files python-devel-common
%defattr(644,root,root,755)
%{_includedir}/boost/python
%{_includedir}/boost/python.hpp
%dir %{_libdir}/cmake/boost_python-*
%{_libdir}/cmake/boost_python-*/boost_python-config.cmake
%{_libdir}/cmake/boost_python-*/boost_python-config-version.cmake
%endif

%if %{with python2}
%files python
%defattr(644,root,root,755)
%if %{with numpy}
%attr(755,root,root) %{_libdir}/libboost_numpy%{py2v}.so.*.*.*
%endif
%attr(755,root,root) %{_libdir}/libboost_python%{py2v}.so.*.*.*

%files python-devel
%defattr(644,root,root,755)
%if %{with numpy}
%attr(755,root,root) %{_libdir}/libboost_numpy%{py2v}.so
%endif
%attr(755,root,root) %{_libdir}/libboost_python%{py2v}.so
%{_libdir}/cmake/boost_python-*/libboost_python-variant-*-py2*.cmake

%files python-static
%defattr(644,root,root,755)
%if %{with numpy}
%{_libdir}/libboost_numpy%{py2v}.a
%endif
%{_libdir}/libboost_python%{py2v}.a
%endif

%if %{with python3}
%files python3
%defattr(644,root,root,755)
%if %{with numpy}
%attr(755,root,root) %{_libdir}/libboost_numpy%{py3v}.so.*.*.*
%endif
%attr(755,root,root) %{_libdir}/libboost_python%{py3v}.so.*.*.*

%files python3-devel
%defattr(644,root,root,755)
%if %{with numpy}
%attr(755,root,root) %{_libdir}/libboost_numpy%{py3v}.so
%endif
%attr(755,root,root) %{_libdir}/libboost_python%{py3v}.so
%{_libdir}/cmake/boost_python-*/libboost_python-variant-*-py3*.cmake

%files python3-static
%defattr(644,root,root,755)
%if %{with numpy}
%{_libdir}/libboost_numpy%{py3v}.a
%endif
%{_libdir}/libboost_python%{py3v}.a
%endif

%files chrono
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_chrono.so.*.*.*

%files context
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_context.so.*.*.*

%files date_time
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_date_time.so.*.*.*

%files fiber
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_fiber.so.*.*.*

%files filesystem
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_filesystem.so.*.*.*

%files graph
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_graph.so.*.*.*

%files json
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_json.so.*.*.*

%files locale
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_locale.so.*.*.*

%files log
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_log.so.*.*.*
%attr(755,root,root) %{_libdir}/libboost_log_setup.so.*.*.*

%files program_options
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_program_options.so.*.*.*

%files regex
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_regex.so.*.*.*

%files system
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_system.so.*.*.*

%files test
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_prg_exec_monitor.so.*.*.*
%attr(755,root,root) %{_libdir}/libboost_unit_test_framework.so.*.*.*

%files thread
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_thread.so.*.*.*

%files timer
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_timer.so.*.*.*

%files url
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_url.so.*.*.*

%files wave
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_wave.so.*.*.*

%if %{with doc}
%files doc
%defattr(644,root,root,755)
%{_docdir}/%{name}-%{version}
%endif
