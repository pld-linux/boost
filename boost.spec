#
# TODO:
# - pass %{__cxx}
#
# Conditional build:
%bcond_without	python	# without boost-python support
#
%define	_fver	%(echo %{version} | tr . _)
Summary:	The Boost C++ Libraries
Summary(pl.UTF-8):	Biblioteki C++ "Boost"
Name:		boost
Version:	1.34.1
Release:	2
License:	Boost Software License and others
Group:		Libraries
Source0:	http://dl.sourceforge.net/boost/%{name}_%{_fver}.tar.bz2
# Source0-md5:	2d938467e8a448a2c9763e0a9f8ca7e5
URL:		http://www.boost.org/
BuildRequires:	boost-jam >= 3.1.12
BuildRequires:	bzip2-devel
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
Requires:	%{name}-ref-devel = %{version}-%{release}
Requires:	libstdc++-devel
# temporary Provides (until CVS HEAD stops using it)?
Provides:	boost-call_traits-devel = %{version}-%{release}
Provides:	boost-concept_check-devel = %{version}-%{release}
Provides:	boost-conversion-devel = %{version}-%{release}
Provides:	boost-mpl-devel = %{version}-%{release}
Provides:	boost-preprocessor-devel = %{version}-%{release}
Provides:	boost-static_assert-devel = %{version}-%{release}
Provides:	boost-type_traits-devel = %{version}-%{release}
Provides:	boost-utility-devel = %{version}-%{release}
Obsoletes:	boost-call_traits-devel
Obsoletes:	boost-compose-devel
Obsoletes:	boost-concept_check-devel
Obsoletes:	boost-conversion-devel
Obsoletes:	boost-mpl-devel
Obsoletes:	boost-preprocessor-devel
Obsoletes:	boost-static_assert-devel
Obsoletes:	boost-type_traits-devel
Obsoletes:	boost-utility-devel

%description devel
Header files for the Boost C++ libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek C++ Boost.

%package static
Summary:	Static version of base Boost C++ libraries
Summary(pl.UTF-8):	Statyczne wersje podstawowych bibliotek C++ Boost
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

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
Requires:	%{name}-compressed_pair-devel = %{version}-%{release}
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

%package regex
Summary:	Boost C++ regular expressions library
Summary(pl.UTF-8):	Biblioteka wyrażeń regularnych Boost C++
Group:		Libraries

%description regex
Shared library for Boost C++ regular expressions.

%description regex -l pl.UTF-8
Biblioteka wyrażeń regularnych dla C++, biblioteki dzielone.

%package regex-devel
Summary:	Boost C++ Regex library headers
Summary(pl.UTF-8):	Pliki nagłówkowe Boost C++ Regex
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-regex = %{version}-%{release}

%description regex-devel
Boost C++ Regex headers.

%description regex-devel -l pl.UTF-8
Pliki nagłówkowe dla Boost C++ Regex.

%package regex-static
Summary:	Boost C++ Regex static libraries
Summary(pl.UTF-8):	Biblioteki statyczne Boost C++ Regex
Group:		Development/Libraries
Requires:	%{name}-regex-devel = %{version}-%{release}

%description regex-static
Boost C++ Regex static libraries.

%description regex-static -l pl.UTF-8
Biblioteki statyczne dla Boost C++ Regex.

%package any-devel
Summary:	Header for Boost C++ "Any" Library
Summary(pl.UTF-8):	Plik nagłówkowy dla biblioteki Boost C++ "Any"
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description any-devel
The boost::any class, is a variant value type, which supports copying
of any value type and safe checked extraction of that value strictly
against that type.

I.e. 5 is held strictly as an int and is not implicitly convertible
either to "5" or to 5.0.

%description any-devel -l pl.UTF-8
Klasa boost::any jest typem, który umożliwia kopiowanie ze zmiennej
dowolnego typu i bezpieczne, sprawdzone wydobycie jej wartości
dokładnie tego samego typu.

Np. 5 jest trzymane jako int i nie jest niejawnie konwertowalne ani do
"5" ani do 5.0.

%package array-devel
Summary:	STL compliant container wrapper for arrays of constant size
Summary(pl.UTF-8):	Wrapper na STLowe kontenery dla tablic o stałym rozmiarze
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description array-devel
As replacement for ordinary arrays, the STL provides class vector<>.
However, vector<> provides the semantics of dynamic arrays. Thus, it
manages data to be able to change the number of elements. This results
in some overhead in case only arrays with static size are needed. This
library provides support for such static size arrays.

%description array-devel -l pl.UTF-8
STL dostarcza klasę vector<> jako zamiennik zwykłej tablicy. Jednak
vector<> dostarcza semantykę dynamicznych tablic. Zatem zarządza
danymi tak, by była możliwa zmiana ilości elementów. To skutkuje
pewnym nadmiarem w przypadku kiedy tylko tablice o stałym rozmiarze są
potrzebne. Ta biblioteka dostarcza wsparcie dla takich właśnie tablic
o stałym rozmiarze.

%package bind-devel
Summary:	Generalized binders for function/object/pointers and member functions
Summary(pl.UTF-8):	Uogólnione bindery dla funkcji/obiektów/wskaźników oraz metod
Group:		Development/Libraries
Requires:	%{name}-ref-devel = %{version}-%{release}
Requires:	%{name}-signals-devel = %{version}-%{release}
Provides:	boost-mem_fn-devel = %{version}-%{release}
Obsoletes:	boost-compose-devel
Obsoletes:	boost-mem_fn-devel

%description bind-devel
boost::bind is a generalization of the standard functions std::bind1st
and std::bind2nd. This package contains also boost::mem_fn which is a
generalization of the standard functions std::mem_fun and
std::mem_fun_ref.

%description bind-devel -l pl.UTF-8
boost::bind jest uogólnieniem standardowych funkcji std::bind1st i
std::bind2nd. Ten pakiet zawiera także boost::mem_fn, który jest
uogólnieniem standardowych funkcji std::mem_fun i std::mem_fun_ref.

%package compatibility-devel
Summary:	Help for non-conforming standard libraries
Summary(pl.UTF-8):	Pomoc dla nie trzymających standardu bibliotek
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description compatibility-devel
This library provides workarounds which allow the other Boost
libraries to be used on otherwise non-conforming platforms.

%description compatibility-devel -l pl.UTF-8
Biblioteka dostarcza obejście problemu platform nie trzymających
standardu C++, pozwalające na używanie bibliotek Boost na tych
platformach.

%package compose-devel
Summary:	Functional composition adapters for the STL
Summary(pl.UTF-8):	Funkcjonalne adaptery kompozycji dla STL
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description compose-devel
The boost::compose provides compose function object adapter extensions
for use with the Standard Template Library (STL) portion of the C++
Standard Library. If you aren't currently using the STL, this library
won't be of any interest, but hard-core STL users will appreciate its
usefulness.

%description compose-devel -l pl.UTF-8
boost::compose dostarcza rozszerzenie adaptera obiektu funkcji compose
do użytku z STL-ową częścią Standardu C++. Jeżeli nie używasz STL,
biblioteka będzie poza twoim zainteresowaniem, lecz hardkorowi
użytkownicy STL-a docenią jej użyteczność.

%package compressed_pair-devel
Summary:	Empty member optimization
Summary(pl.UTF-8):	Optymalizacja pustego elementu
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description compressed_pair-devel
The class boost::compressed_pair is very similar to std::pair, but if
either of the template arguments are empty classes, then the "empty
base-class optimisation" is applied to compress the size of the pair.

%description compressed_pair-devel -l pl.UTF-8
Klasa boost::compressed_pair jest bardzo podobna do std::pair, ale
jeżeli któryś z argumentów wzorca jest pustą klasą, wtedy stosowana
jest "optymalizacja pustej klasy bazowej" do kompresji pary.

%package crc-devel
Summary:	CRC computing library
Summary(pl.UTF-8):	Biblioteka obliczająca CRC
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description crc-devel
The boost::crc library provides two implementations of CRC computation
objects and functions. The implementations are template-based.

%description crc-devel -l pl.UTF-8
Bibliteka boost::crc dostarcza dwie implementacje obiektów i funkcji
obliczających CRC. Implementacje są oparte na wzorcach.

%package date_time
Summary:	Date-Time library
Summary(pl.UTF-8):	Biblioteka daty-czasu
Group:		Libraries
Obsoletes:	boost < 1.33

%description date_time
A set of date-time libraries.

%description date_time -l pl.UTF-8
Zbiór bibliotek daty-czasu.

%package date_time-devel
Summary:	Header files for boost::date_time library
Summary(pl.UTF-8):	Pliki nagłówkowe dla biblioteki boost::date_time
Group:		Development/Libraries
Requires:	%{name}-date_time = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
#TODO: make decision if do separate packages include it to main devel package
#Requires:	%{name}-integer-devel = %{version}-%{release}
#Requires:	%{name}-operators-devel = %{version}-%{release}
#Requires:	%{name}-tokenizer-devel = %{version}-%{release}

%description date_time-devel
Header files for boost::date_time library.

%description date_time-devel -l pl.UTF-8
Pliki nagłówkowe dla biblioteki boost::date_time

%package date_time-static
Summary:	Static boost::date_time library
Summary(pl.UTF-8):	Statyczna biblioteka boost::date_time
Group:		Development/Libraries
Requires:	%{name}-date_time-devel = %{version}-%{release}

%description date_time-static
Static boost::date_time library.

%description date_time-devel -l pl.UTF-8
Statyczna biblioteka boost::date_time.

%package filesystem
Summary:	Portable paths, iteration over directories, and other useful filesystem operations
Summary(pl.UTF-8):	Przenośne ścieżki, iteracje katalogów i inne użyteczne operacje na systemie plików
Group:		Libraries
Obsoletes:	boost < 1.33

%description filesystem
The boost::filesystem library provides portable facilities to query
and manipulate paths, files, and directories.

%description filesystem -l pl.UTF-8
Przenośna biblioteka boost::filesystem dostarcza ułatwienia w
operacjach na ścieżkach, plikach i katalogach.

%package filesystem-devel
Summary:	Header files for boost::filesystem
Summary(pl.UTF-8):	Pliki nagłówkowe dla boost::filesystem
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-filesystem = %{version}-%{release}
#TODO:
#Requires:	%{name}-smart_ptr = %{version}-%{release}

%description filesystem-devel
Header files for boost::filesystem library.

%description filesystem-devel -l pl.UTF-8
Pliki nagłówkowe dla biblioteki boost::filesystem.

%package filesystem-static
Summary:	Static boost::filesystem library
Summary(pl.UTF-8):	Biblioteka statyczna boost::filesystem
Group:		Development/Libraries
Requires:	%{name}-filesystem-devel = %{version}-%{release}
Obsoletes:	boost-static < 1.33

%description filesystem-static
Static boost::filesystem library.

%description filesystem-static -l pl.UTF-8
Biblioteka statyczna boost::filesystem.

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

%package graph-devel
Summary:	Header files for boost::graph
Summary(pl.UTF-8):	Pliki nagłówkowe dla boost::graph
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description graph-devel
Header files for boost::graph library.

%description graph-devel -l pl.UTF-8
Pliki nagłówkowe dla biblioteki boost::graph.

%package graph-static
Summary:	Static boost::graph library
Summary(pl.UTF-8):	Biblioteka statyczna boost::graph
Group:		Development/Libraries
Requires:	%{name}-graph-devel = %{version}-%{release}

%description graph-static
Static boost::graph library.

%description graph-static -l pl.UTF-8
Biblioteka statyczna boost::graph.

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

%package program_options-devel
Summary:	Header files for boost::program_options
Summary(pl.UTF-8):	Pliki nagłówkowe dla boost::program_options
Group:		Development/Libraries
Requires:	%{name}-any-devel = %{version}-%{release}
Requires:	%{name}-bind-devel = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-program_options = %{version}-%{release}

%description program_options-devel
Header files for boost::program_options library.

%description program_options-devel -l pl.UTF-8
Pliki nagłówkowe dla biblioteki boost::program_options.

%package program_options-static
Summary:	Static boost::program_options library
Summary(pl.UTF-8):	Biblioteka statyczna boost::program_options
Group:		Development/Libraries
Requires:	%{name}-program_options-devel = %{version}-%{release}
Obsoletes:	boost-static < 1.33

%description program_options-static
Static boost::program_options library.

%description program_options-static -l pl.UTF-8
Biblioteka statyczna boost::program_options.

%package ref-devel
Summary:	Small library useful for passing references to function templates
Summary(pl.UTF-8):	Mała biblioteka użyteczna przy przekazywaniu referencji do wzorców funkcji
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description ref-devel
boost::ref library is a small library that is useful for passing
references to function templates (algorithms) that would usually take
copies of their arguments.

%description ref-devel -l pl.UTF-8
Biblioteka boost::ref jest małą biblioteką która jest użyteczna w
przypadku przekazywania referencji do wzorców funkcji (algorytmów)
które zazwyczaj biorą kopię swoich argumentów.

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

%package signals-devel
Summary:	Header files for boost::signals library
Summary(pl.UTF-8):	Pliki nagłówkowe dla biblioteki boost::signals
Group:		Development/Libraries
Requires:	%{name}-any-devel = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-signals = %{version}-%{release}
#TODO: separate smart_ptr or include to the main devel package
Requires:	%{name}-bind-devel = %{version}-%{release}
#Requires:	%{name}-iterator_adaptors-devel = %{version}-%{release}
#Requires:	%{name}-operators-devel = %{version}-%{release}
Requires:	%{name}-ref-devel = %{version}-%{release}
#Requires:	%{name}-smart_ptr-devel = %{version}-%{release}

%description signals-devel
Header files for boost::signals library.

%description signals-devel -l pl.UTF-8
Pliki nagłówkowe dla biblioteki boost::signals.

%package signals-static
Summary:	Static library for boost::signals
Summary(pl.UTF-8):	Biblioteka statyczna dla boost::signals
Group:		Development/Libraries
Requires:	%{name}-signals-devel = %{version}-%{release}

%description signals-static
Static library for boost::signals.

%description signals-static -l pl.UTF-8
Biblioteka statyczna dla boost::signals.

%package spirit-devel
Summary:	LL parser framework
Summary(pl.UTF-8):	Szkielet parsera LL
Group:		Development/Libraries
Requires:	%{name}-compressed_pair-devel = %{version}-%{release}
Requires:	%{name}-ref-devel = %{version}-%{release}
Requires:	%{name}-regex-devel = %{version}-%{release}
Requires:	%{name}-thread-devel = %{version}-%{release}
#TODO:
#?Requires:	%{name}-iterators-devel = %{version}-%{release}
#?Requires:	%{name}-smart_ptr-devel = %{version}-%{release}

%description spirit-devel
LL parser framework represents parsers directly as EBNF grammars in
inlined C++.

%description spirit-devel -l pl.UTF-8
Szkielet parsera LL reprezentujący parsery jako gramatyki EBNF
bezpośrednio w kodzie C++.

%package statechart-devel
Summary:	C++ library for finite state machines
Summary(pl.UTF-8):	Biblioteka C++ do automatów skończonych
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description statechart-devel
C++ library for finite state machines.

%description statechart-devel -l pl.UTF-8
Biblioteka C++ do automatów skończonych.

%package test
Summary:	Support for program testing and  execution monitoring
Summary(pl.UTF-8):	Wsparcie dla testowania i monitorowania programu
Group:		Libraries
Obsoletes:	boost < 1.33

%description test
Support for simple program testing, full unit testing, and for program
execution monitoring.

%description test -l pl.UTF-8
Wsparcie dla prostego testowania programu, pełnego testowania i
monitorowania wykonania programu.

%package test-devel
Summary:	Header files for boost::test
Summary(pl.UTF-8):	Pliki nagłówkowe dla boost::test
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-test = %{version}-%{release}
#TODO:
#?Requires?:	%{name}-function-devel = %{version}-%{release}
#Requires:	%{name}-smart_ptr = %{version}-%{release}

%description test-devel
Header files for boost::test.

%description test-devel -l pl.UTF-8
Pliki nagłówkowe dla boost::test.

%package test-static
Summary:	Static boost::test libraries
Summary(pl.UTF-8):	Biblioteki statyczne boost::test
Group:		Development/Libraries
Requires:	%{name}-test-devel = %{version}-%{release}
Obsoletes:	boost-static < 1.33

%description test-static
Static boost::test libraries.

%description test-static -l pl.UTF-8
Biblioteki statyczne boost::test.

%package thread
Summary:	Portable C++ threads library
Summary(pl.UTF-8):	Przenośna biblioteka wątków C++
Group:		Libraries
Obsoletes:	boost < 1.33

%description thread
Portable C++ threads library - shared library.

%description thread -l pl.UTF-8
Przenośna biblioteka wątków dla C++ - biblioteka dzielona.

%package thread-devel
Summary:	Header files for boost::thread library
Summary(pl.UTF-8):	Pliki nagłówkowe dla biblioteki boost::thread
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-thread = %{version}-%{release}
#TODO:requires boost::function or boost::function to boost-devel

%description thread-devel
Header files for boost::thread library.

%description thread-devel -l pl.UTF-8
Pliki nagłówkowe dla biblioteki boost::thread.

%package thread-static
Summary:	Portable C++ threads library - static version
Summary(pl.UTF-8):	Przenośna biblioteka wątków C++ - wersja statyczna
Group:		Libraries
Requires:	%{name}-thread-devel = %{version}-%{release}
Obsoletes:	boost < 1.33

%description thread-static
Portable C++ threads library - static library.

%description thread-static -l pl.UTF-8
Przenośna biblioteka wątków dla C++ - biblioteka statyczna.

%package tr1-devel
Summary:	An implementation of the C++ Technical Report on Standard Library Extensions
Summary(pl.UTF-8):	Implementacja C++ TR dla rozszerzeń biblioteki standardowej
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description tr1-devel
The TR1 library provides an implementation of the C++ Technical Report
on Standard Library Extensions. This library does not itself implement
the TR1 components, rather it's a thin wrapper that will include your
standard library's TR1 implementation (if it has one), otherwise it
will include the Boost Library equivalents, and import them into
namespace std::tr1.

%description tr1-devel -l pl.UTF-8
Biblioteka TR1 udostępnia implementację C++ Technical Report on
Standard Library Extensions (raporto technicznego dotyczącego
rozszerzeń biblioteki standardowej C++). Biblioteka jako taka nie
implementuje komponentów TR1, lecz jest cienkim opakowaniem
zawierającym implementację TR1 z zainstalowanej biblioteki
standardowej (jeśli taka jest) lub zawiera odpowiedniki z biblioteki
Boost zaimportowane do przestrzeni nazw std::tr1.

%package typeof-devel
Summary:	Emulates C++ typeid()
Summary(pl.UTF-8):	Emulacja typeid() z C++
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description typeof-devel
Emulates C++ typeid().

%description typeof-devel -l pl.UTF-8
Emulacja typeid() z C++.

%package uBLAS-devel
Summary:	Basic linear algebra for dense, packed and sparse matrices
Summary(pl.UTF-8):	Prosta liniowa algebra dla gęstych, upakowanych i rzadkich macierzy
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description uBLAS-devel
uBLAS library provides templated C++ classes for dense, unit and
sparse vectors, dense, identity, triangular, banded, symmetric,
hermitian and sparse matrices.

%description uBLAS-devel -l pl.UTF-8
Biblioteka uBLAS dostarcza wzorce klas C++ dla gęstych, jednostkowych
i rzadkich wektorów oraz gęstych, jednostkowych, trójkątnych,
diagonalnych, symetrycznych, hermitowskich i rzadkich macierzy.

%package wave
Summary:	Boost.Wave - a standard compliant C++ preprocessor library
Summary(pl.UTF-8):	Boost.Wave - zgodna ze standardem biblioteka preprocesora C++
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description wave
Boost.Wave - a standard compliant C++ preprocessor library.

%description wave -l pl.UTF-8
Boost.Wave - zgodna ze standardem biblioteka preprocesora C++.

%package wave-devel
Summary:	Boost.Wave - a standard compliant C++ preprocessor library
Summary(pl.UTF-8):	Boost.Wave - zgodna ze standardem biblioteka preprocesora C++
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description wave-devel
Boost.Wave - a standard compliant C++ preprocessor library.
Development files.

%description wave-devel -l pl.UTF-8
Boost.Wave - zgodna ze standardem biblioteka preprocesora C++. Pliki
dla developera.

%package wave-static
Summary:	Boost.Wave - a standard compliant C++ preprocessor library
Summary(pl.UTF-8):	Boost.Wave - zgodna ze standardem biblioteka preprocesora C++
Group:		Development/Libraries
Requires:	%{name}-wave-devel = %{version}-%{release}

%description wave-static
Boost.Wave - a standard compliant C++ preprocessor library. Static
library.

%description wave-static -l pl.UTF-8
Boost.Wave - zgodna ze standardem biblioteka preprocesora C++.
Biblioteka statyczna.

%package xpressive-devel
Summary:	Object-oriented regular expression template library for C++
Summary(pl.UTF-8):	Zorientowana obiektowo biblioteka szablonów wyrażeń regularnych dla C++
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description xpressive-devel
xpressive is an advanced, object-oriented regular expression template
library for C++. Regular expressions can be written as strings that
are parsed at run-time, or as expression templates that are parsed at
compile-time. Regular expressions can refer to each other and to
themselves recursively, allowing you to build arbitrarily complicated
grammars out of them.

%description xpressive-devel -l pl.UTF-8
xpressive to zaawansowana, zorientowana obiektowo biblioteka szablonów
wyrażeń regularnych dla C++. Wyrażenia regularne mogą być pisane jako
łańcuchy znaków analizowane w czasie działania lub szablony wyrażeń
analizowane w czasie kompilacji. Wyrażenia regularne mogą odwoływać
się do siebie nawzajem i rekurencyjnie do siebie samych, co pozwala na
tworzenie z nich dowolnie złożonych gramatyk.

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

# - don't know how to pass it through (b)jam -s (no way?)
#   due to oversophisticated build flags system.
# - pass -fPIC due to <shared-linkable> removal.
%{__perl} -pi -e 's/ -O3 / %{rpmcxxflags} -fPIC /' tools/build/v2/tools/gcc.jam

%ifarch alpha
# -pthread gcc parameter doesn't add _REENTRANT to cpp macros on alpha (only)
# don't know, is it gcc bug or intentional omission?
# anyway, boost check of -D_REENTRANT in its headers, so it's needed here
%{__perl} -pi -e 's/(CFLAGS.*-pthread)/$1 -D_REENTRANT/' tools/build/v1/gcc-tools.jam
%endif

%build
%if %{with python}
PYTHON_VERSION=$(%{__python} -c 'import sys; print sys.version[0:3]')
PYTHON_ROOT=%{_prefix}
%else
PYTHON_ROOT=
PYTHON_VERSION=
%endif
bjam \
	-d2 --toolset=gcc \
	variant=release threading=multi inlining=on debug-symbols=on

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
install README $RPM_BUILD_ROOT%{_docdir}/boost-%{version}

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

%post	python	-p /sbin/ldconfig
%postun python	-p /sbin/ldconfig

%post	program_options	-p /sbin/ldconfig
%postun program_options	-p /sbin/ldconfig

%post	regex	-p /sbin/ldconfig
%postun regex	-p /sbin/ldconfig

%post	signals	-p /sbin/ldconfig
%postun	signals	-p /sbin/ldconfig

%post	test	-p /sbin/ldconfig
%postun	test	-p /sbin/ldconfig

%post   wave    -p /sbin/ldconfig
%postun wave    -p /sbin/ldconfig

%post	thread	-p /sbin/ldconfig
%postun	thread	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_iostreams*.so.*.*.*
%attr(755,root,root) %{_libdir}/libboost_serialization*.so.*.*.*
%attr(755,root,root) %{_libdir}/libboost_wserialization*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_iostreams*.so
%attr(755,root,root) %{_libdir}/libboost_serialization*.so
%attr(755,root,root) %{_libdir}/libboost_wserialization*.so
%dir %{_includedir}/boost
%{_includedir}/boost/algorithm
%{_includedir}/boost/archive
%{_includedir}/boost/assert.hpp
%{_includedir}/boost/assign
%{_includedir}/boost/assign.hpp
%{_includedir}/boost/blank_fwd.hpp
%{_includedir}/boost/call_traits.hpp
%{_includedir}/boost/cast.hpp
%{_includedir}/boost/checked_delete.hpp
%{_includedir}/boost/concept_archetype.hpp
%{_includedir}/boost/concept_check.hpp
%{_includedir}/boost/config
%{_includedir}/boost/config.hpp
%{_includedir}/boost/cstd*.hpp
%{_includedir}/boost/current_function.hpp
%dir %{_includedir}/boost/detail
%{_includedir}/boost/detail/algorithm.hpp
%{_includedir}/boost/detail/allocator_utilities.hpp
%{_includedir}/boost/detail/atomic_count*.hpp
%{_includedir}/boost/detail/bad_weak_ptr.hpp
%{_includedir}/boost/detail/binary_search.hpp
%{_includedir}/boost/detail/call_traits.hpp
%{_includedir}/boost/detail/catch_exceptions.hpp
%{_includedir}/boost/detail/dynamic_bitset.hpp
%{_includedir}/boost/detail/endian.hpp
%{_includedir}/boost/detail/indirect_traits.hpp
%{_includedir}/boost/detail/interlocked.hpp
%{_includedir}/boost/detail/is_function_ref_tester.hpp
%{_includedir}/boost/detail/is_incrementable.hpp
%{_includedir}/boost/detail/is_xxx.hpp
%{_includedir}/boost/detail/iterator.hpp
%{_includedir}/boost/detail/lightweight_*.hpp
%{_includedir}/boost/detail/limits.hpp
%{_includedir}/boost/detail/lwm_*.hpp
%{_includedir}/boost/detail/named_template_params.hpp
%{_includedir}/boost/detail/no_exceptions_support.hpp
%{_includedir}/boost/detail/numeric_traits.hpp
%{_includedir}/boost/detail/ob_call_traits.hpp
%{_includedir}/boost/detail/quick_allocator.hpp
%{_includedir}/boost/detail/reference_content.hpp
%{_includedir}/boost/detail/select_type.hpp
%{_includedir}/boost/detail/shared_*.hpp
%{_includedir}/boost/detail/sp_counted_*.hpp
%{_includedir}/boost/detail/utf8_codecvt_facet.hpp
%{_includedir}/boost/detail/workaround.hpp
%{_includedir}/boost/dynamic_bitset
%{_includedir}/boost/dynamic_bitset.hpp
%{_includedir}/boost/dynamic_bitset_fwd.hpp
%{_includedir}/boost/dynamic_property_map.hpp
%{_includedir}/boost/enable_shared_from_this.hpp
%{_includedir}/boost/foreach.hpp
%{_includedir}/boost/format
%{_includedir}/boost/format.hpp
%{_includedir}/boost/function
%{_includedir}/boost/function.hpp
%{_includedir}/boost/function_equal.hpp
%{_includedir}/boost/function_output_iterator.hpp
%{_includedir}/boost/functional
%{_includedir}/boost/functional.hpp
%{_includedir}/boost/generator_iterator.hpp
%{_includedir}/boost/implicit_cast.hpp
%{_includedir}/boost/indirect_reference.hpp
%{_includedir}/boost/integer
%{_includedir}/boost/integer*.hpp
%{_includedir}/boost/intrusive_ptr.hpp
%{_includedir}/boost/io
%{_includedir}/boost/iostreams
%{_includedir}/boost/io_fwd.hpp
%{_includedir}/boost/iterator*.hpp
%{_includedir}/boost/iterator
%{_includedir}/boost/lambda
%{_includedir}/boost/lexical_cast.hpp
%{_includedir}/boost/limits.hpp
%{_includedir}/boost/logic
%{_includedir}/boost/math
%{_includedir}/boost/math_fwd.hpp
%{_includedir}/boost/mpl
%{_includedir}/boost/multi_array
%{_includedir}/boost/multi_array.hpp
%{_includedir}/boost/multi_index
%{_includedir}/boost/multi_index_container.hpp
%{_includedir}/boost/multi_index_container_fwd.hpp
%{_includedir}/boost/next_prior.hpp
%{_includedir}/boost/noncopyable.hpp
%{_includedir}/boost/nondet_random.hpp
%{_includedir}/boost/none.hpp
%{_includedir}/boost/non_type.hpp
%dir %{_includedir}/boost/numeric
%{_includedir}/boost/numeric/interval*
%{_includedir}/boost/numeric/conversion
%{_includedir}/boost/operators.hpp
%{_includedir}/boost/optional
%{_includedir}/boost/optional.hpp
%{_includedir}/boost/parameter
%{_includedir}/boost/parameter.hpp
%{_includedir}/boost/pending
%{_includedir}/boost/pfto.hpp
%{_includedir}/boost/pool
%{_includedir}/boost/pointee.hpp
%{_includedir}/boost/pointer_cast.hpp
%{_includedir}/boost/pointer_to_other.hpp
%{_includedir}/boost/preprocessor
%{_includedir}/boost/preprocessor.hpp
%{_includedir}/boost/progress.hpp
%{_includedir}/boost/property_map*.hpp
%{_includedir}/boost/ptr_container
%{_includedir}/boost/random
%{_includedir}/boost/random.hpp
%{_includedir}/boost/range
%{_includedir}/boost/range.hpp
%{_includedir}/boost/rational.hpp
%{_includedir}/boost/scoped_*.hpp
%{_includedir}/boost/serialization
%{_includedir}/boost/shared_*.hpp
%{_includedir}/boost/smart_cast.hpp
%{_includedir}/boost/smart_ptr.hpp
%{_includedir}/boost/state_saver.hpp
%{_includedir}/boost/static_assert.hpp
%{_includedir}/boost/static_warning.hpp
%{_includedir}/boost/strong_typedef.hpp
%{_includedir}/boost/throw_exception.hpp
%{_includedir}/boost/timer.hpp
%{_includedir}/boost/token*.hpp
%{_includedir}/boost/tuple
%{_includedir}/boost/type.hpp
%{_includedir}/boost/type_traits.hpp
%{_includedir}/boost/type_traits
%{_includedir}/boost/utility*.hpp
%{_includedir}/boost/utility
%{_includedir}/boost/version.hpp
%{_includedir}/boost/vector_property_map.hpp
%{_includedir}/boost/weak_ptr.hpp
#boost::variant
%{_includedir}/boost/variant.hpp
%{_includedir}/boost/variant
%{_includedir}/boost/blank.hpp
%{_includedir}/boost/detail/templated_streams.hpp
#boost::optional
%{_includedir}/boost/aligned_storage.hpp
%{_includedir}/boost/detail/none_t.hpp

%files static
%defattr(644,root,root,755)
%{_libdir}/libboost_iostreams*.a
%{_libdir}/libboost_serialization*.a
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

%files regex
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_regex*.so.*.*.*

%files regex-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_regex*.so
%{_includedir}/boost/cregex.hpp
%{_includedir}/boost/regex.h
%{_includedir}/boost/regex*.hpp
%{_includedir}/boost/regex

%files regex-static
%defattr(644,root,root,755)
%{_libdir}/libboost_regex*.a

%files any-devel
%defattr(644,root,root,755)
%{_includedir}/boost/any.hpp

%files array-devel
%defattr(644,root,root,755)
%{_includedir}/boost/array.hpp

%files bind-devel
%defattr(644,root,root,755)
%{_includedir}/boost/bind
%{_includedir}/boost/bind.hpp
%{_includedir}/boost/get_pointer.hpp
%{_includedir}/boost/mem_fn.hpp

%files compatibility-devel
%defattr(644,root,root,755)
%{_includedir}/boost/compatibility

%files compressed_pair-devel
%defattr(644,root,root,755)
%{_includedir}/boost/compressed_pair.hpp
%{_includedir}/boost/detail/compressed_pair.hpp
%{_includedir}/boost/detail/ob_compressed_pair.hpp

%files crc-devel
%defattr(644,root,root,755)
%{_includedir}/boost/crc.hpp

%files date_time
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_date_time*.so.*.*.*

%files date_time-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_date_time*.so
%{_includedir}/boost/date_time.hpp
%{_includedir}/boost/date_time

%files date_time-static
%defattr(644,root,root,755)
%{_libdir}/libboost_date_time*.a

%files filesystem
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_filesystem*.so.*.*.*

%files filesystem-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_filesystem*.so
%{_includedir}/boost/filesystem.hpp
%{_includedir}/boost/filesystem

%files filesystem-static
%defattr(644,root,root,755)
%{_libdir}/libboost_filesystem*.a

%files graph
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_graph*.so.*.*.*

%files graph-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_graph*.so
%{_includedir}/boost/graph

%files graph-static
%defattr(644,root,root,755)
%{_libdir}/libboost_grap*.a

%files program_options
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_program_options*.so.*.*.*

%files program_options-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_program_options*.so
%{_includedir}/boost/program_options
%{_includedir}/boost/program_options.hpp

%files program_options-static
%defattr(644,root,root,755)
%{_libdir}/libboost_program_options*.a

%files ref-devel
%defattr(644,root,root,755)
%{_includedir}/boost/ref.hpp

%files signals
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_signals*.so.*.*.*

%files signals-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_signals*.so
%{_includedir}/boost/signal*.hpp
%{_includedir}/boost/signals
%{_includedir}/boost/last_value.hpp
%{_includedir}/boost/visit_each.hpp

%files signals-static
%defattr(644,root,root,755)
%{_libdir}/libboost_signals*.a

%files spirit-devel
%defattr(644,root,root,755)
%{_includedir}/boost/spirit.hpp
%{_includedir}/boost/spirit

%files statechart-devel
%defattr(644,root,root,755)
%{_includedir}/boost/statechart

%files tr1-devel
%defattr(644,root,root,755)
%{_includedir}/boost/tr1

%files test
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_prg_exec_monitor*.so.*.*.*
%attr(755,root,root) %{_libdir}/libboost_unit_test_framework*.so.*.*.*

%files test-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_prg_exec_monitor*.so
%attr(755,root,root) %{_libdir}/libboost_unit_test_framework*.so
%{_includedir}/boost/test

%files test-static
%defattr(644,root,root,755)
%{_libdir}/libboost_prg_exec_monitor*.a
%{_libdir}/libboost_test_exec_monitor*.a
%{_libdir}/libboost_unit_test_framework*.a

%files thread
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_thread*.so.*.*.*

%files thread-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_thread*.so
%{_includedir}/boost/thread
%{_includedir}/boost/thread.hpp

%files thread-static
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_thread*.a

%files typeof-devel
%defattr(644,root,root,755)
%{_includedir}/boost/typeof

%files uBLAS-devel
%defattr(644,root,root,755)
%{_includedir}/boost/numeric/ublas

%files wave
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_wave*.so.*.*.*

%files wave-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_wave*.so
%{_includedir}/boost/wave
%{_includedir}/boost/wave.hpp

%files wave-static
%defattr(644,root,root,755)
%{_libdir}/libboost_wave*.a

%files xpressive-devel
%defattr(644,root,root,755)
%{_includedir}/boost/xpressive

%files doc
%defattr(644,root,root,755)
%{_docdir}/%{name}-%{version}
