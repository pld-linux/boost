#
# Conditional build:
%bcond_without	python	# without boost-python support
#
%define _ver	1.31.0
%define _fver 	%(echo %{_ver} | tr . _)

Summary:	The Boost C++ Libraries
Summary(pl):	Biblioteki C++ "Boost"
Name:		boost
Version:	%{_ver}
Release:	0.91
License:	Boost Software License and others
Group:		Libraries
Source0:	http://dl.sourceforge.net/boost/%{name}_%{_fver}.tar.bz2
# Source0-md5:	8cc183538eaa5cfc53d88d0e94bd2fd4
Patch0:		%{name}-python.patch
URL:		http://www.boost.org/
BuildRequires:	boost-jam >= 3.1.3
BuildRequires:	libstdc++-devel
BuildRequires:	perl-base
%{?with_python:BuildRequires:	python-devel >= 2.2}
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

%description -l pl
Strona http://www.boost.org/ dostarcza darmowe biblioteki C++ wraz z
kodem ¼ród³owym. Nacisk po³o¿ono na biblioteki, które dobrze
wspó³pracuj± ze standardow± bibliotek± C++. Celem jest ustanowienie
"isniej±cej praktyki" i dostarczenie implementacji, tak ¿e biblioteki
"Boost" nadaj± siê do ewentualnej standaryzacji. Niektóre z bibliotek
ju¿ zosta³y zg³oszone do komitetu standaryzacyjnego C++ w nadchodz±cym
Raporcie Technicznym Biblioteki Standardowej C++

%package devel
Summary:	Boost C++ development libraries and headers
Summary(pl):	Pliki nag³ówkowe i biblioteki statyczne Boost C++
Group:		Development/Libraries
# req'd by <boost/iterator_adaptors.hpp> (also included by <boost/signal.h>)
Requires:	%{name}-concept_check-devel = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
Headers and static libraries for the Boost C++ libraries.

%description devel -l pl
Pliki nag³ówkowe i biblioteki statyczne bibliotek Boost C++.

%package python
Summary:	Boost.Python library
Summary(pl):	biblioteka Boost.Python
Group:		Libraries
%pyrequires_eq	python

%description python
Use the Boost Python Library to quickly and easily export a C++
library to Python such that the Python interface is very similar to
the C++ interface. It is designed to be minimally intrusive on your
C++ design. In most cases, you should not have to alter your C++
classes in any way in order to use them with Boost.Python. The system
should simply ``reflect'' your C++ classes and functions into Python.

%description python -l pl
Biblioteka Boost Python s³u¿y do szybkiego i prostego eksportu
biblioteki C++ do Pythona, tak ¿e interfejs Pythona jest bardzo
podobny do interfejsu C++. Biblioteka jest zaprojektowana tak, ¿eby
narzucaæ jak najmniej wymagañ dotycz±cych konstrukcjii C++. W
wiêkszo¶ci przypadków nie trzeba w ogóle zmieniaæ w³asnych klas C++,
¿eby u¿ywaæ ich z Boost.Python. System powinien po prostu ,,odbiæ''
klasy C++ i funkcje do Pythona.

%package python-devel
Summary:	Boost.Python development headers
Summary(pl):	Pliki nag³ówkowe dla Boost.Python
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-python = %{version}-%{release}
Requires:	%{name}-compressed_pair-devel = %{version}-%{release}

%description python-devel
Headers for the Boost.Python library.

%description python-devel -l pl
Pliki nag³ówkowe dla biblioteki Boost.Python.

%package python-static
Summary:	Static version of Boost.Python library
Summary(pl):	Statyczna wersja biblioteki Boost.Python
Group:		Development/Libraries
Requires:	%{name}-python-devel = %{version}-%{release}

%description python-static
Static version of Boost.Python library.

%description python-static -l pl
Statyczna wersja biblioteki Boost.Python.

%package regex
Summary:	Boost C++ regular expressions library
Summary(pl):	Biblioteka wyra¿eñ regularnych Boost C++
Group:		Libraries

%description regex
Shared library for Boost C++ regular expressions.

%description regex -l pl
Biblioteka wyra¿eñ regularnych dla C++, biblioteki dzielone.

%package regex-devel
Summary:	Boost C++ Regex library headers
Summary(pl):	Pliki nag³ówkowe Boost C++ Regex
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-regex = %{version}-%{release}

%description regex-devel
Boost C++ Regex headers.

%description regex-devel -l pl
Pliki nag³ówkowe dla Boost C++ Regex.

%package regex-static
Summary:	Boost C++ Regex static libraries
Summary(pl):	Biblioteki statyczne Boost C++ Regex
Group:		Development/Libraries
Requires:	%{name}-regex-devel = %{version}-%{release}

%description regex-static
Boost C++ Regex static libraries.

%description regex-static -l pl
Biblioteki statyczne dla Boost C++ Regex.

%package any-devel
Summary:	Header for Boost C++ "Any" Library
Summary(pl):	Plik nag³ówkowy dla biblioteki Boost C++ "Any"
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description any-devel
The boost::any class, is a variant value type, which supports copying
of any value type and safe checked extraction of that value strictly
against that type.

I.e. 5 is held strictly as an int and is not implicitly convertible
either to "5" or to 5.0.

%description any-devel -l pl
Klasa boost::any jest typem, który umo¿liwia kopiowanie ze zmiennej
dowolnego typu i bezpieczne, sprawdzone wydobycie jej warto¶ci
dok³adnie tego samego typu.

Np. 5 jest trzymane jako int i nie jest niejawnie konwertowalne ani do
"5" ani do 5.0.

%package array-devel
Summary:	STL compliant container wrapper for arrays of constant size
Summary(pl):	Wrapper na STLowe kontenery dla tablic o sta³ym rozmiarze
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description array-devel
As replacement for ordinary arrays, the STL provides class vector<>.
However, vector<> provides the semantics of dynamic arrays. Thus, it
manages data to be able to change the number of elements. This results
in some overhead in case only arrays with static size are needed. This
library provides support for such static size arrays.

%description array-devel -l pl
STL dostarcza klasê vector<> jako zamiennik zwyk³ej tablicy. Jednak
vector<> dostarcza semantykê dynamicznych tablic. Zatem zarz±dza
danymi tak, by by³a mo¿liwa zmiana ilo¶ci elementów. To skutkuje
pewnym nadmiarem w przypadku kiedy tylko tablice o sta³ym rozmiarze s±
potrzebne. Ta biblioteka dostarcza wsparcie dla takich w³a¶nie tablic
o sta³ym rozmiarze.

%package bind-devel
Summary:	Generalized binders for function/object/pointers
Summary(pl):	Uogólnione bindery dla funkcji/obiektów/wska¼ników
Group:		Development/Libraries
Requires:	%{name}-mem_fn-devel = %{version}-%{release}
Requires:	%{name}-ref-devel = %{version}-%{release}

%description bind-devel
boost::bind is a generalization of the standard functions std::bind1st
and std::bind2nd.

%description bind-devel -l pl
boost::bind jest uogólnieniem standardowych funkcji std::bind1st i
std::bind2nd.

%package call_traits-devel
Summary:	Defines types for passing parameters
Summary(pl):	Definiowanie typów dla przekazywania parametrów
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-type_traits-devel = %{version}-%{release}

%description call_traits-devel
boost::call_traits<T> encapsulates the "best" method to pass a
parameter of some type T to or from a function. The purpose of
call_traits is to ensure that problems like "references to references"
never occur, and that parameters are passed in the most efficient
manner possible.

%description call_traits-devel -l pl
boost::call_traits<T> zawiera "najlepsz±" metodê przekazywania
parametrów jakiego¶ typu T do lub z funkcji. Celem call_traits jest
zapewnienie ¿e problemy takie jak "referencja referencji" nigdy nie
wyst±pi± i ¿e parametry s± przekazywane w mo¿liwie najbardziej
efektywny sposób.

%package compatibility-devel
Summary:	Help for non-conforming standard libraries
Summary(pl):	Pomoc dla nie trzymaj±cych standardu bibliotek
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description compatibility-devel
This library provides workarounds which allow the other Boost
libraries to be used on otherwise non-conforming platforms.

%description compatibility-devel -l pl
Biblioteka dostarcza obej¶cie problemu platform nie trzymaj±cych
standardu C++, pozwalaj±ce na u¿ywanie bibliotek Boost na tych
platformach.

%package compose-devel
Summary:	Functional composition adapters for the STL
Summary(pl):	Funkcjonalne adaptery kompozycji dla STL
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description compose-devel
The boost::compose provides compose function object adapter extensions
for use with the Standard Template Library (STL) portion of the C++
Standard Library. If you aren't currently using the STL, this library
won't be of any interest, but hard-core STL users will appreciate its
usefulness.

%description compose-devel -l pl
boost::compose dostarcza rozszerzenie adaptera obiektu funkcji compose
do u¿ytku z STL-ow± czê¶ci± Standardu C++. Je¿eli nie u¿ywasz STL,
biblioteka bêdzie poza twoim zainteresowaniem, lecz hardkorowi
u¿ytkownicy STL-a doceni± jej u¿yteczno¶æ.

%package compressed_pair-devel
Summary:	Empty member optimization
Summary(pl):	Optymalizacja pustego elementu
Group:		Development/Libraries
Requires:	%{name}-call_traits-devel = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}

%description compressed_pair-devel
The class boost::compressed_pair is very similar to std::pair, but if
either of the template arguments are empty classes, then the "empty
base-class optimisation" is applied to compress the size of the pair.

%description compressed_pair-devel -l pl
Klasa boost::compressed_pair jest bardzo podobna do std::pair, ale
je¿eli który¶ z argumentów wzorca jest pust± klas±, wtedy stosowana
jest "optymalizacja pustej klasy bazowej" do kompresji pary.

%package concept_check-devel
Summary:	Tools for generic programming
Summary(pl):	Narzêdzia dla programowania generycznego
Group:		Development/Libraries
Requires:	%{name}-static_assert-devel = %{version}-%{release}
Requires:	%{name}-type_traits-devel = %{version}-%{release}

%description concept_check-devel
The boost::concept_check library provides various tools for generic
programming.

%description concept_check-devel -l pl
Biblioteka boost::concept_check dostarcza ró¿ne narzêdzia dla
programowania generycznego.

%package conversion-devel
Summary:	Numeric, polymorphic, and lexical casts
Summary(pl):	Numeryczne, polimorficzne i leksykalne rzutowania
Group:		Development/Libraries
Requires:	%{name}-type_traits-devel = %{version}-%{release}

%description conversion-devel
The boost::conversion library improves program safety and clarity by
performing otherwise messy conversions. It includes cast-style
function templates designed to complement the C++ Standard's built-in
casts.

%description conversion-devel -l pl
Biblioteka boost::conversion zwiêksza bezpieczeñstwo i klarowno¶æ
programu dokonuj±c konwersji które s± w innych przypadkach niechlujne.
Biblioteka zawiera "rzutopodobne" wzorce funkcji uzupe³niaj±ce
wbudowane w Standard C++ rzutowania.

%package crc-devel
Summary:	CRC computing library
Summary(pl):	Biblioteka obliczaj±ca CRC
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description crc-devel
The boost::crc library provides two implementations of CRC computation
objects and functions. The implementations are template-based.

%description crc-devel -l pl
Bibliteka boost::crc dostarcza dwie implementacje obiektów i funkcji
obliczaj±cych CRC. Implementacje s± oparte na wzorcach.

%package date_time
Summary:	Date-Time library
Summary(pl):	Biblioteka daty-czasu
Group:		Libraries
Obsoletes:	boost

%description date_time
A set of date-time libraries.

%description date_time -l pl
Zbiór bibliotek daty-czasu.

%package date_time-devel
Summary:	Header files for boost::date_time library
Summary(pl):	Pliki nag³ówkowe dla biblioteki boost::date_time
Group:		Development/Libraries
Requires:	%{name}-date_time = %{version}-%{release}
#TODO: make decision if do separate packages include it to main devel package
#Requires:	%{name}-operators-devel = %{version}-%{release}
#Requires:	%{name}-integer-devel = %{version}-%{release}
#Requires:	%{name}-tokenizer-devel = %{version}-%{release}
Requires:	%{name}-conversion-devel = %{version}-%{release}

%description date_time-devel
Header files for boost::date_time library.

%description date_time-devel -l pl
Pliki nag³ówkowe dla biblioteki boost::date_time

%package date_time-static
Summary:	Static boost::date_time library
Summary(pl):	Statyczna biblioteka boost::date_time
Group:		Development/Libraries
Requires:	%{name}-date_time-devel = %{version}-%{release}

%description date_time-static
Static boost::date_time library.

%description date_time-devel -l pl
Statyczna biblioteka boost::date_time.

%package filesystem
Summary:	Portable paths, iteration over directories, and other useful filesystem operations
Summary(pl):	Przeno¶ne ¶cie¿ki, iteracje katalogów i inne u¿yteczne operacje na systemie plików
Group:		Libraries
Obsoletes:	boost

%description filesystem
The boost::filesystem library provides portable facilities to query
and manipulate paths, files, and directories.

%description filesystem -l pl
Przeno¶na biblioteka boost::filesystem dostarcza u³atwienia w
operacjach na ¶cie¿kach, plikach i katalogach.

%package filesystem-devel
Summary:	Header files for boost::filesystem
Summary(pl):	Pliki nag³ówkowe dla boost::filesystem
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-filesystem = %{version}-%{release}
#TODO:
#Requires:	%{name}-smart_ptr = %{version}-%{release}

%description filesystem-devel
Header files for boost::filesystem library.

%description filesystem-devel -l pl
Pliki nag³ówkowe dla biblioteki boost::filesystem.

%package filesystem-static
Summary:	Static boost::filesystem library
Summary(pl):	Biblioteka statyczna boost::filesystem
Group:		Development/Libraries
Requires:	%{name}-filesystem-devel = %{version}-%{release}
Obsoletes:	boost-static

%description filesystem-static
Static boost::filesystem library.

%description filesystem-static -l pl
Biblioteka statyczna boost::filesystem.

%package mem_fn-devel
Summary:	Generalized binders for member functions
Summary(pl):	Uogólnione bindery dla metod
Group:		Development/Libraries
Requires:	%{name}-bind-devel = %{version}-%{release}

%description mem_fn-devel
boost::mem_fn is a generalization of the standard functions
std::mem_fun and std::mem_fun_ref.

%description mem_fn-devel -l pl
boost::mem_fn jest uogólnieniem standardowych funkcji std::mem_fun i
std::mem_fun_ref.

%package mpl-devel
Summary:	Compile-time algorithms, sequences and metafunction classes
Summary(pl):	Algorytmy czasu kompilacji, sekwencji i klas metafunkcji
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-preprocessor-devel = %{version}-%{release}
Requires:	%{name}-type_traits-devel = %{version}-%{release}
Requires:	%{name}-utility-devel = %{version}-%{release}

%description mpl-devel
The boost-mpl library is a C++ template metaprogramming framework of
compile-time algorithms, sequences and metafunction classes.

%description mpl-devel -l pl
Biblioteka boost-mpl jest szkieletem wzorców C++ dla algorytmów czasu
kompilacji, sekwencji i klas metafunkcji.

%package preprocessor-devel
Summary:	Preprocessor metaprogramming tools including repetition and recursion
Summary(pl):	Narzêdzia metaprogramowania preprocesora razem z repetycj± i rekursj±
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description preprocessor-devel
This library provides preprocessor metaprogramming tools, including
repetition and recursion.

%description preprocessor-devel -l pl
Biblioteka udostêpnia narzêdzia metaprogramowania preprocesora,
w³±czaj±c w to repetycje i rekursjê.

%package ref-devel
Summary:	Small library useful for passing references to function templates
Summary(pl):	Ma³a biblioteka u¿yteczna przy przekazywaniu referencji do wzorców funkcji
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-mpl-devel = %{version}-%{release}
Requires:	%{name}-utility-devel = %{version}-%{release}

%description ref-devel
boost::ref library is a small library that is useful for passing
references to function templates (algorithms) that would usually take
copies of their arguments.

%description ref-devel -l pl
Biblioteka boost::ref jest ma³± bibliotek± która jest u¿yteczna w
przypadku przekazywania referencji do wzorców funkcji (algorytmów)
które zazwyczaj bior± kopiê swoich argumentów.

%package signals
Summary:	Signals & slots callback implementation
Summary(pl):	Implementacja sygna³ów i slotów
Group:		Libraries
Obsoletes:	boost

%description signals
The boost::signals library is an implementation of a signals and slots
system.

%description signals -l pl
Biblioteka boost::signals jest implementacj± systemu sygna³ów i
slotów.

%package signals-devel
Summary:	Header files for boost::signals library
Summary(pl):	Pliki nag³ówkowe dla biblioteki boost::signals
Group:		Development/Libraries
Requires:	%{name}-any-devel = %{version}-%{release}
#TODO: separate smart_ptr or include to the main devel package
#Requires:	%{name}-iterator_adaptors-devel = %{version}-%{release}
#Requires:	%{name}-operators-devel = %{version}-%{release}
#Requires:	%{name}-smart_ptr-devel = %{version}-%{release}
Requires:	%{name}-mem_fn-devel = %{version}-%{release}
Requires:	%{name}-ref-devel = %{version}-%{release}
Requires:	%{name}-type_traits-devel = %{version}-%{release}
Requires:	%{name}-utility-devel = %{version}-%{release}

%description signals-devel
Header files for boost::signals library.

%description signals-devel -l pl
Pliki nag³ówkowe dla biblioteki boost::signals.

%package signals-static
Summary:	Static library for boost::signals
Summary(pl):	Biblioteka statyczna dla boost::signals
Group:		Development/Libraries
Requires:	%{name}-signals-devel = %{version}-%{release}

%description signals-static
Static library for boost::signals.

%description signals-static -l pl
Biblioteka statyczna dla boost::signals.

%package spirit-devel
Summary:	LL parser framework
Summary(pl):	Szkielet parsera LL
Group:		Development/Libraries
Requires:	%{name}-compressed_pair-devel = %{version}-%{release}
Requires:	%{name}-ref-devel = %{version}-%{release}
Requires:	%{name}-regex-devel = %{version}-%{release}
Requires:	%{name}-static_assert-devel = %{version}-%{release}
Requires:	%{name}-thread-devel = %{version}-%{release}
#TODO:
#?Requires:	%{name}-smart_ptr-devel = %{version}-%{release}
#?Requires:	%{name}-iterators-devel = %{version}-%{release}

%description spirit-devel
LL parser framework represents parsers directly as EBNF grammars in
inlined C++.

%description spirit-devel -l pl
Szkielet parsera LL reprezentuj±cy parsery jako gramatyki EBNF
bezpo¶rednio w kodzie C++.

%package static_assert-devel
Summary:	Static assertions (compile time assertions)
Summary(pl):	Statyczne asercje (asercje kompilacyjne)
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static_assert-devel
The header <boost/static_assert.hpp> supplies a single macro
BOOST_STATIC_ASSERT(x), which generates a compile time error message
if the integral-constant-expression x is not true. In other words it
is the compile time equivalent of the assert macro; this is sometimes
known as a "compile-time-assertion"

One of the aims of BOOST_STATIC_ASSERT is to generate readable error
messages. These immediately tell the user that a library is being used
in a manner that is not supported.

%description static_assert-devel -l pl
Plik nag³ówkowy <boost/static_assert.hpp> dostarcza pojedyncze makro
BOOST_STATIC_ASSERT(x), które generuje komunikat b³êdu kompilacji
je¿eli sta³e wyra¿enie x nie jest prawdziwe. Innymi s³owy jest to
kompilacyjny ekwiwalent makra 'assert'; czasami znane jest jako
"asercja czasu kompilacji"

Jednym z celów BOOST_STATIC_ASSERT jest generowanie czytelnych
komunikatów o b³êdach. One b³yskawicznie powiedz± u¿ytkownikowi ¿e
biblioteka zosta³a u¿yta w sposób który nie jest zalecany.

%package test
Summary:	Support for program testing and  execution monitoring
Summary(pl):	Wsparcie dla testowania i monitorowania programu
Group:		Libraries
Obsoletes:	boost

%description test
Support for simple program testing, full unit testing, and for program
execution monitoring.

%description test -l pl
Wsparcie dla prostego testowania programu, pe³nego testowania i
monitorowania wykonania programu.

%package test-devel
Summary:	Header files for boost::test
Summary(pl):	Pliki nag³ówkowe dla boost::test
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-mpl-devel = %{version}-%{release}
Requires:	%{name}-preprocessor-devel = %{version}-%{release}
Requires:	%{name}-test = %{version}-%{release}
#TODO:
#Requires:	%{name}-smart_ptr = %{version}-%{release}
#?Requires?:	%{name}-function-devel = %{version}-%{release}

%description test-devel
Header files for boost::test.

%description test-devel -l pl
Pliki nag³ówkowe dla boost::test

%package test-static
Summary:	Static boost::test libraries
Summary(pl):	Biblioteki statyczne boost::test
Group:		Development/Libraries
Requires:	%{name}-test-devel = %{version}-%{release}
Obsoletes:	boost-static

%description test-static
Static boost::test libraries.

%description test-static -l pl
Biblioteki statyczne boost::test.

%package thread
Summary:	Portable C++ threads library
Summary(pl):	Przeno¶na biblioteka w±tków C++
Group:		Libraries
Obsoletes:	boost

%description thread
Portable C++ threads library - shared library.

%description thread -l pl
Przeno¶na biblioteka w±tków dla C++ - biblioteka dzielona.

%package thread-devel
Summary:	Header files for boost::thread library
Summary(pl):	Pliki nag³ówkowe dla biblioteki boost::thread
Group:		Development/Libraries
Requires:	%{name}-thread = %{version}-%{release}
Requires:	%{name}-utility-devel = %{version}-%{release}
#TODO:requires boost::function or boost::function to boost-devel

%description thread-devel
Header files for boost::thread library.

%description thread-devel -l pl
Pliki nag³ówkowe dla biblioteki boost::thread.

%package type_traits-devel
Summary:	Templates for fundamental properties of types
Summary(pl):	Wzorce dla fundamentalnych w³a¶ciwo¶ci typów
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-mpl-devel = %{version}-%{release}
Requires:	%{name}-preprocessor-devel = %{version}-%{release}
Requires:	%{name}-static_assert-devel = %{version}-%{release}
Requires:	%{name}-utility-devel = %{version}-%{release}

%description type_traits-devel
The boost-type_traits library defines three kinds of type trait:
 1. The properties of a specific type.
 2. The relationship between two types.
 3. A transformation from one type to another.

%description type_traits-devel -l pl
Biblioteka boost-type_traits definiuje trzy rodzaje cech typów:
 1. w³a¶ciwo¶ci konkretnego typu.
 2. powi±zania miêdzy dwoma typami.
 3. transformacjê z jednego typu do drugiego.

%package uBLAS-devel
Summary:	Basic linear algebra for dense, packed and sparse matrices
Summary(pl):	Prosta liniowa algebra dla gêstych, upakowanych i rzadkich macierzy
Group:		Development/Libraries
Requires:	%{name}-concept_check-devel = %{version}-%{release}
Requires:	%{name}-mpl-devel = %{version}-%{release}
Requires:	%{name}-utility-devel = %{version}-%{release}

%description uBLAS-devel
uBLAS library provides templated C++ classes for dense, unit and
sparse vectors, dense, identity, triangular, banded, symmetric,
hermitian and sparse matrices.

%description uBLAS-devel -l pl
Biblioteka uBLAS dostarcza wzorce klas C++ dla gêstych, jednostkowych
i rzadkich wektorów oraz gêstych, jednostkowych, trójk±tnych,
diagonalnych, symetrycznych, hermitowskich i rzadkich macierzy.

%package utility-devel
Summary:	Useful utilities: classes and function templates
Summary(pl):	U¿yteczne narzêdzia: klasy i wzorce funkcji
Group:		Development/Libraries
Requires:	%{name}-type_traits-devel = %{version}-%{release}

%description utility-devel
Class noncopyable plus checked_delete(), checked_array_delete(),
next(), prior() function templates, plus base-from-member idiom.

%description utility-devel -l pl
Klasy noncopyable i checked_delete, funkcje checked_array_delete(),
next(), prior() oraz idiom base-from-member.

%package doc
Summary:	Boost C++ Library documentation
Summary(pl):	Dokumentacja dla biblioteki Boost C++
Group:		Documentation
Requires:	%{name}-devel = %{version}-%{release}

%description doc
Documentation for the Boost C++ Library.

%description doc -l pl
Dokumentacja dla biblioteki Boost C++.

%prep
%setup -q -n %{name}_%{_fver}
%patch0 -p1

# don't know how to pass it through (b)jam -s (no way?)
# due to oversophisticated build flags system
%{__perl} -pi -e 's/ -O3 / %{rpmcflags} /' tools/build/v1/gcc-tools.jam

%ifarch alpha
# -pthread gcc parameter doesn't add _REENTRANT to cpp macros on alpha (only)
# don't know, is it gcc bug or intentional omission?
# anyway, boost check of -D_REENTRANT in its headers, so it's needed here
%{__perl} -pi -e 's/(CFLAGS.*-pthread)/$1 -D_REENTRANT/' tools/build/v1/gcc-tools.jam
%endif

%build
%if %{with python}
PYTHON_VERSION=`python -V 2>&1 | sed 's,.* \([0-9]\.[0-9]\)\(\.[0-9]\)\?.*,\1,'`
PYTHON_ROOT=%{_prefix}
%else
PYTHON_ROOT=
PYTHON_VERSION=
%endif
bjam \
	-d2 \
	-sBUILD="release <threading>multi" \
	-sPYTHON_ROOT=$PYTHON_ROOT \
	-sPYTHON_VERSION=$PYTHON_VERSION

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}}

cp -rf boost $RPM_BUILD_ROOT%{_includedir}

install bin/boost/libs/*/build/*.a/*/release/*/lib*.a $RPM_BUILD_ROOT%{_libdir}
install bin/boost/libs/*/build/*.so/*/release/*/*/lib*.so.*.*.* $RPM_BUILD_ROOT%{_libdir}
# use cp -d, install follows symlinks instead of preserving them!
cp -df bin/boost/libs/*/build/*.so/*/release/*/*/lib*.so $RPM_BUILD_ROOT%{_libdir}

# documentation
install -d $RPM_BUILD_ROOT%{_docdir}/boost-%{version}
install README $RPM_BUILD_ROOT%{_docdir}/boost-%{version}

# as the documentation doesn't completely reside in a directory of its
# own, we need to find out ourselves... this looks for HTML files and
# then collects everything linked from those.  this is certainly quite
# unoptimized wrt mkdir calls, but does it really matter?
for i in `find -type f -name '*.htm*'`; do
	# bjam docu is included in the boost-jam RPM
	if test "`echo $i | sed 's,jam_src,,'`" = "$i"; then
		install -d $RPM_BUILD_ROOT%{_docdir}/boost-%{version}/`dirname $i`
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
			TARGET=`dirname $i`/$LINKED
			# ignore non-existant linked files
			if test -f $TARGET; then
				install -d $RPM_BUILD_ROOT%{_docdir}/boost-%{version}/`dirname $TARGET`
				install -m 644 $TARGET $RPM_BUILD_ROOT%{_docdir}/boost-%{version}/$TARGET
			fi
		done
	fi
done

%clean
rm -rf $RPM_BUILD_ROOT

%post	date_time -p /sbin/ldconfig
%postun	date_time -p /sbin/ldconfig

%post	filesystem -p /sbin/ldconfig
%postun	filesystem -p /sbin/ldconfig

%post	python	-p /sbin/ldconfig
%postun python	-p /sbin/ldconfig

%post	regex	-p /sbin/ldconfig
%postun regex	-p /sbin/ldconfig

%post	signals	-p /sbin/ldconfig
%postun	signals	-p /sbin/ldconfig

%post	test	-p /sbin/ldconfig
%postun	test	-p /sbin/ldconfig

%post	thread	-p /sbin/ldconfig
%postun	thread	-p /sbin/ldconfig

%files devel
%defattr(644,root,root,755)
%dir %{_includedir}/boost
%{_includedir}/boost/assert.hpp
%{_includedir}/boost/blank_fwd.hpp
%{_includedir}/boost/config
%{_includedir}/boost/config.hpp
%{_includedir}/boost/cstd*.hpp
%{_includedir}/boost/current_function.hpp
%dir %{_includedir}/boost/detail
%{_includedir}/boost/detail/algorithm.hpp
%{_includedir}/boost/detail/allocator.hpp
%{_includedir}/boost/detail/atomic_count*.hpp
%{_includedir}/boost/detail/binary_search.hpp
%{_includedir}/boost/detail/catch_exceptions.hpp
%{_includedir}/boost/detail/dynamic_bitset.hpp
%{_includedir}/boost/detail/is_incrementable.hpp
%{_includedir}/boost/detail/iterator.hpp
%{_includedir}/boost/detail/lightweight_*.hpp
%{_includedir}/boost/detail/limits.hpp
%{_includedir}/boost/detail/lwm_*.hpp
%{_includedir}/boost/detail/named_template_params.hpp
%{_includedir}/boost/detail/numeric_traits.hpp
%{_includedir}/boost/detail/reference_content.hpp
%{_includedir}/boost/detail/quick_allocator.hpp
%{_includedir}/boost/detail/select_type.hpp
%{_includedir}/boost/detail/shared_*.hpp
%{_includedir}/boost/detail/workaround.hpp
%{_includedir}/boost/dynamic_bitset*.hpp
%{_includedir}/boost/enable_shared_from_this.hpp
%{_includedir}/boost/format
%{_includedir}/boost/format.hpp
%{_includedir}/boost/function
%{_includedir}/boost/function.hpp
%{_includedir}/boost/function_output_iterator.hpp
%{_includedir}/boost/functional.hpp
%{_includedir}/boost/generator_iterator.hpp
%{_includedir}/boost/graph
%{_includedir}/boost/half_open_range.hpp
%{_includedir}/boost/indirect_reference.hpp
%{_includedir}/boost/integer
%{_includedir}/boost/integer*.hpp
%{_includedir}/boost/intrusive_ptr.hpp
%{_includedir}/boost/io
%{_includedir}/boost/io_fwd.hpp
%{_includedir}/boost/iterator*.hpp
%{_includedir}/boost/iterator
%{_includedir}/boost/lambda
%{_includedir}/boost/limits.hpp
%{_includedir}/boost/math
%{_includedir}/boost/math_fwd.hpp
%{_includedir}/boost/multi_array
%{_includedir}/boost/multi_array.hpp
%{_includedir}/boost/nondet_random.hpp
%{_includedir}/boost/non_type.hpp
%{_includedir}/boost/numeric/interval*
%{_includedir}/boost/operators.hpp
%{_includedir}/boost/optional.hpp
%{_includedir}/boost/pending
%{_includedir}/boost/pool
%{_includedir}/boost/pointee.hpp
%{_includedir}/boost/progress.hpp
%{_includedir}/boost/property_map*.hpp
%{_includedir}/boost/random
%{_includedir}/boost/random.hpp
%{_includedir}/boost/rational.hpp
%{_includedir}/boost/scoped_*.hpp
%{_includedir}/boost/shared_*.hpp
%{_includedir}/boost/smart_ptr.hpp
%{_includedir}/boost/throw_exception.hpp
%{_includedir}/boost/timer.hpp
%{_includedir}/boost/token*.hpp
%{_includedir}/boost/tuple
%{_includedir}/boost/type.hpp
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
%{_includedir}/boost/detail/in_place_factory*.hpp
%{_includedir}/boost/detail/none.hpp
%{_includedir}/boost/detail/none_t.hpp
%{_includedir}/boost/detail/typed_in_place_factory.hpp

%if %{with python}
%files python
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_python-gcc-mt-1_31.so.*.*.*

%files python-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_python-gcc-mt-1_31.so
%{_includedir}/boost/python
%{_includedir}/boost/python.hpp

%files python-static
%defattr(644,root,root,755)
%{_libdir}/libboost_python-gcc-mt-1_31.a
%endif

%files regex
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_regex-gcc-mt-1_31.so.*.*.*

%files regex-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_regex-gcc-mt-1_31.so
%{_includedir}/boost/cregex.hpp
%{_includedir}/boost/regex.h
%{_includedir}/boost/regex*.hpp
%{_includedir}/boost/regex

%files regex-static
%defattr(644,root,root,755)
%{_libdir}/libboost_regex-gcc-mt-1_31.a

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

%files call_traits-devel
%defattr(644,root,root,755)
%{_includedir}/boost/call_traits.hpp
%{_includedir}/boost/detail/call_traits.hpp
%{_includedir}/boost/detail/ob_call_traits.hpp

%files compatibility-devel
%defattr(644,root,root,755)
%{_includedir}/boost/compatibility

%files compose-devel
%defattr(644,root,root,755)
%{_includedir}/boost/compose.hpp

%files compressed_pair-devel
%defattr(644,root,root,755)
%{_includedir}/boost/compressed_pair.hpp
%{_includedir}/boost/detail/compressed_pair.hpp
%{_includedir}/boost/detail/ob_compressed_pair.hpp

%files concept_check-devel
%defattr(644,root,root,755)
%{_includedir}/boost/concept_archetype.hpp
%{_includedir}/boost/concept_check.hpp

%files conversion-devel
%defattr(644,root,root,755)
%{_includedir}/boost/cast.hpp
%{_includedir}/boost/implicit_cast.hpp
%{_includedir}/boost/lexical_cast.hpp

%files crc-devel
%defattr(644,root,root,755)
%{_includedir}/boost/crc.hpp

%files date_time
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_date_time-gcc-mt-1_31.so.*.*.*

%files date_time-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_date_time-gcc-mt-1_31.so
%{_includedir}/boost/date_time

%files date_time-static
%defattr(644,root,root,755)
%{_libdir}/libboost_date_time-gcc-mt-1_31.a

%files filesystem
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_filesystem-gcc-mt-1_31.so.*.*.*

%files filesystem-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_filesystem-gcc-mt-1_31.so
%{_includedir}/boost/filesystem

%files filesystem-static
%defattr(644,root,root,755)
%{_libdir}/libboost_filesystem-gcc-mt-1_31.a

%files mem_fn-devel
%defattr(644,root,root,755)
%{_includedir}/boost/get_pointer.hpp
%{_includedir}/boost/mem_fn.hpp

%files mpl-devel
%defattr(644,root,root,755)
%{_includedir}/boost/mpl

%files preprocessor-devel
%defattr(644,root,root,755)
%{_includedir}/boost/preprocessor
%{_includedir}/boost/preprocessor.hpp

%files ref-devel
%defattr(644,root,root,755)
%{_includedir}/boost/ref.hpp

%files signals
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_signals-gcc-mt-1_31.so.*.*.*

%files signals-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_signals-gcc-mt-1_31.so
%{_includedir}/boost/signal*.hpp
%{_includedir}/boost/signals
%{_includedir}/boost/last_value.hpp
%{_includedir}/boost/visit_each.hpp

%files signals-static
%defattr(644,root,root,755)
%{_libdir}/libboost_signals-gcc-mt-1_31.a

%files spirit-devel
%defattr(644,root,root,755)
%{_includedir}/boost/spirit.hpp
%{_includedir}/boost/spirit

%files static_assert-devel
%defattr(644,root,root,755)
%{_includedir}/boost/static_assert.hpp

%files test
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_prg_exec_monitor-gcc-mt-1_31.so.*.*.*
%attr(755,root,root) %{_libdir}/libboost_test_exec_monitor-gcc-mt-1_31.so.*.*.*
%attr(755,root,root) %{_libdir}/libboost_unit_test_framework-gcc-mt-1_31.so.*.*.*

%files test-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_prg_exec_monitor-gcc-mt-1_31.so
%attr(755,root,root) %{_libdir}/libboost_test_exec_monitor-gcc-mt-1_31.so
%attr(755,root,root) %{_libdir}/libboost_unit_test_framework-gcc-mt-1_31.so
%{_includedir}/boost/test

%files test-static
%defattr(644,root,root,755)
%{_libdir}/libboost_prg_exec_monitor-gcc-mt-1_31.a
%{_libdir}/libboost_test_exec_monitor-gcc-mt-1_31.a
%{_libdir}/libboost_unit_test_framework-gcc-mt-1_31.a

%files thread
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_thread-gcc-mt-1_31.so.*.*.*

%files thread-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_thread-gcc-mt-1_31.so
%{_includedir}/boost/thread
%{_includedir}/boost/thread.hpp

%files type_traits-devel
%defattr(644,root,root,755)
%{_includedir}/boost/type_traits.hpp
%{_includedir}/boost/type_traits

%files uBLAS-devel
%defattr(644,root,root,755)
%{_includedir}/boost/numeric/ublas

%files utility-devel
%defattr(644,root,root,755)
%{_includedir}/boost/checked_delete.hpp
%{_includedir}/boost/next_prior.hpp
%{_includedir}/boost/noncopyable.hpp
%{_includedir}/boost/utility*.hpp
%{_includedir}/boost/utility

%files doc
%defattr(644,root,root,755)
%{_docdir}/%{name}-%{version}
