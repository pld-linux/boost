#
# Conditional build:
%bcond_with	python	# with boost-python support (not working now)
#
Summary:	The Boost C++ Libraries
Summary(pl):	Biblioteki C++ "Boost"
Name:		boost
Version:	1.30.2
Release:	0.1
License:	Freely distributable
Group:		Libraries
Source0:	http://dl.sourceforge.net/boost/%{name}-%{version}.tar.bz2
# Source0-md5:	4aed692a863bb4beaa0b70d6dc53bda5
URL:		http://www.boost.org/
BuildRequires:	boost-jam >= 3.1.3
BuildRequires:	libstdc++-devel
%{?with_python:BuildRequires:	python-devel}
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
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
Headers and static libraries for the Boost C++ libraries.

%description devel -l pl
Pliki nag³ówkowe i biblioteki statyczne bibliotek Boost C++.

#according to ldd (and automatically generated RPM dependencies) it
#doesn't strictly require python, but IMHO it's cleaner to split it
#this way
%package python
Summary:	Boost.Python library
Summary(pl):	biblioteka Boost.Python
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	python

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

%description python-devel
Headers for the Boost.Python library.

%description python-devel -l pl
Pliki nag³ówkowe dla biblioteki Boost.Python.

%package regex
Summary:	Boost C++ regular expressions library
Summary(pl):	Biblioteka wyra¿eñ regularnych Boost C++
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description regex
Shared library for Boost C++ regular expressions.

%description regex -l pl
Biblioteka wyra¿eñ regularnych dla C++, biblioteki dzielone.

%package regex-devel
Summary:	Boost C++ Regex library headers and static libraries
Summary(pl):	Pliki nag³ówkowe i biblioteki statyczne Boost C++ Regex
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-regex = %{version}-%{release}

%description regex-devel
Boost C++ Regex headers and static libraries.

%description regex-devel -l pl
Pliki nag³ówkowe i biblioteki statyczne dla Boost C++ Regex.

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

Np. 5 jest trzymane jako int i nie jest niejawnie konwertowalne ani
do "5" ani do 5.0.

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

%package type_traits-devel
Summary:	Templates for fundamental properties of types
Summary(pl):	Wzorce dla fundamentalnych w³a¶ciwo¶ci typów
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-mpl-devel = %{version}-%{release}
Requires:	%{name}-preprocessor-devel = %{version}-%{release}
Requires:	%{name}-utility-devel = %{version}-%{release}
Requires:	%{name}-static_assert-devel = %{version}-%{release}

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

%package utility-devel
Summary:	Useful utilities: classes and function templates.
Summary(pl):	U¿yteczne narzêdzia: klasy i wzorce funkcji
Group:		Development/Libraries
Requires:	%{name}-type_traits-devel = %{version}

%description utility-devel
Class noncopyable plus checked_delete(), checked_array_delete(),
next(), prior() function templates, plus base-from-member idiom.

%description utility-devel -l pl
Klasy noncopyable i checked_delete, funkcje checked_array_delete(),
next(), prior() oraz idiom base-from-member.

%package static_assert-devel
Summary:	Static assertions (compile time assertions)
Summary(pl):	Statyczne asercje (asercje kompilacyjne)
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

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

%package doc
Summary:	Boost C++ Library documentation
Summary(pl):	Dokumentacja dla biblioteki Boost C++
Group:		Documentation
Requires:	%{name}-devel = %{version}

%description doc
Documentation for the Boost C++ Library.

%description doc -l pl
Dokumentacja dla biblioteki Boost C++.

%prep
%setup -q

%build
%if %{with python}
PYTHON_VERSION=`python -V 2>&1 | sed 's,.* \([0-9]\.[0-9]\)\(\.[0-9]\)\?.*,\1,'`
PYTHON_ROOT=%{_prefix}
%else
PYTHON_ROOT=
PYTHON_VERSION=
%endif
bjam \
	-sBUILD=release \
	-sPYTHON_ROOT=$PYTHON_ROOT \
	-sPYTHON_VERSION=$PYTHON_VERSION

%install
rm -rf $RPM_BUILD_ROOT
rm -f master.list regex.list regex-devel.list python.list devel.list python-devel.list doc.list any.list
# include files
install -d $RPM_BUILD_ROOT%{_includedir}
for i in `find boost -type d`; do
	install -d $RPM_BUILD_ROOT%{_includedir}/$i
done
for i in `find boost -type f`; do
	install -m 644 $i $RPM_BUILD_ROOT%{_includedir}/$i
	if test "`echo $i | sed 's,python,,g'`" = "$i"; then
		echo %{_includedir}/$i >> devel.list
	else
		echo %{_includedir}/$i >> python-devel.list
	fi
done
# static libraries
install -d $RPM_BUILD_ROOT%{_libdir}
for i in `find libs -type f -name '*.a' | grep gcc`; do
	install -m 644 $i $RPM_BUILD_ROOT%{_libdir}/`basename $i`
	if test "`echo $i | sed 's,python,,g'`" = "$i"; then
		echo %{_libdir}/`basename $i` >> devel.list
	else
		echo %{_libdir}/`basename $i` >> python-devel.list
	fi
done


# dynamic libraries
for i in `find libs -type f -name '*.so.%{version}' | grep gcc`; do
	install -m 755 $i $RPM_BUILD_ROOT%{_libdir}/`basename $i`
	#ldconfig fails to generate the symlinks for boost libs :-(
	LINK=`basename $i | sed 's,\.so\..*,.so,'`
	(cd $RPM_BUILD_ROOT%{_libdir} && ln -s `basename $i` $LINK)
	if test "`echo $i | sed 's,python,,g'`" = "$i"; then
		echo %{_libdir}/`basename $i` >> master.list
		echo %{_libdir}/$LINK >> master.list
	else
		echo %{_libdir}/`basename $i` >> python.list
		echo %{_libdir}/$LINK >> python.list
	fi
done

#regex library
grep libboost_regex.so master.list > regex.list
grep -v libboost_regex.so master.list >_master.list
mv {_,}master.list
#regex-devel
RFILES="%{_includedir}/boost/cregex.hpp|"
RFILES="$RFILES%{_includedir}/boost/regex/|"
RFILES="$RFILES%{_includedir}/boost/regex.h(pp){0,1}|"
RFILES="$RFILES%{_includedir}/boost/regex_fwd.hpp|"
RFILES="$RFILES%{_libdir}/libboost_regex.a"

egrep "$RFILES" devel.list > regex-devel.list
egrep -v "$RFILES" devel.list > _devel.list
mv {_,}devel.list

#any-devel library
grep any.hpp devel.list > any.list
grep -v any.hpp devel.list > _devel.list
mv {_,}devel.list

#array-devel library
egrep '/boost/array.hpp$' devel.list >array.list
egrep -v '/boost/array.hpp$' devel.list > _devel.list
mv {_,}devel.list

#preprocessor-devel
RFILES="%{_includedir}/boost/preprocessor"
egrep "$RFILES" devel.list > preprocessor.list
egrep -v $RFILES devel.list > _devel.list
mv {_,}devel.list

#mpl-devel
RFILES="%{_includedir}/boost/mpl/"
egrep "$RFILES" devel.list > mpl.list
egrep -v "$RFILES" devel.list >_devel.list
mv {_,}devel.list

#type_traits-devel
RFILES="%{_includedir}/boost/type_traits/"
RFILES="$RFILES|%{_includedir}/boost/type_traits.hpp"
egrep "$RFILES" devel.list > type_traits.list
egrep -v "$RFILES" devel.list >_devel.list
mv {_,}devel.list

#utility-devel
RFILES="%{_includedir}/boost/noncopyable.hpp"
RFILES="$RFILES|%{_includedir}/boost/checked_delete.hpp"
RFILES="$RFILES|%{_includedir}/boost/next_prior.hpp"
RFILES="$RFILES|%{_includedir}/boost/utility(_fwd){0,1}.hpp"
RFILES="$RFILES|%{_includedir}/boost/utility/"
egrep "$RFILES" devel.list > utility.list
egrep -v "$RFILES" devel.list >_devel.list
mv {_,}devel.list

#static_assert-devel
RFILES="%{_includedir}/boost/static_assert.hpp"
egrep "$RFILES" devel.list > static_assert.list
egrep -v "$RFILES" devel.list >_devel.list
mv {_,}devel.list


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
		for LINKED in `perl - $i $RPM_BUILD_ROOT%{_docdir}/boost-%{version}/$i <<'EOT'
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

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post python	-p /sbin/ldconfig
%postun python	-p /sbin/ldconfig

%files -f master.list
%defattr(644,root,root,755)

%files devel -f devel.list
%defattr(644,root,root,755)
%dir %{_includedir}/boost
%dir %{_includedir}/boost/bind
%dir %{_includedir}/boost/compatibility
%dir %{_includedir}/boost/compatibility/cpp_c_headers
%dir %{_includedir}/boost/config
%dir %{_includedir}/boost/config/compiler
%dir %{_includedir}/boost/config/platform
%dir %{_includedir}/boost/config/stdlib
%dir %{_includedir}/boost/date_time
%dir %{_includedir}/boost/date_time/gregorian
%dir %{_includedir}/boost/date_time/posix_time
%dir %{_includedir}/boost/detail
%dir %{_includedir}/boost/filesystem
%dir %{_includedir}/boost/format
%dir %{_includedir}/boost/function
%dir %{_includedir}/boost/function/detail
%dir %{_includedir}/boost/graph
%dir %{_includedir}/boost/graph/detail
%dir %{_includedir}/boost/integer
%dir %{_includedir}/boost/io
%dir %{_includedir}/boost/lambda
%dir %{_includedir}/boost/lambda/detail
%dir %{_includedir}/boost/math
%dir %{_includedir}/boost/math/special_functions
%dir %{_includedir}/boost/multi_array
%dir %{_includedir}/boost/numeric
%dir %{_includedir}/boost/numeric/interval
%dir %{_includedir}/boost/numeric/interval/compare
%dir %{_includedir}/boost/numeric/interval/detail
%dir %{_includedir}/boost/numeric/interval/ext
%dir %{_includedir}/boost/numeric/ublas
%dir %{_includedir}/boost/pending
%dir %{_includedir}/boost/pending/detail
%dir %{_includedir}/boost/pool
%dir %{_includedir}/boost/pool/detail
%dir %{_includedir}/boost/random
%dir %{_includedir}/boost/random/detail
%dir %{_includedir}/boost/signals
%dir %{_includedir}/boost/signals/detail
%dir %{_includedir}/boost/spirit
%dir %{_includedir}/boost/spirit/attribute
%dir %{_includedir}/boost/spirit/core
%dir %{_includedir}/boost/spirit/core/composite
%dir %{_includedir}/boost/spirit/core/composite/impl
%dir %{_includedir}/boost/spirit/core/impl
%dir %{_includedir}/boost/spirit/core/meta
%dir %{_includedir}/boost/spirit/core/meta/impl
%dir %{_includedir}/boost/spirit/core/non_terminal
%dir %{_includedir}/boost/spirit/core/non_terminal/impl
%dir %{_includedir}/boost/spirit/core/primitives
%dir %{_includedir}/boost/spirit/core/primitives/impl
%dir %{_includedir}/boost/spirit/core/scanner
%dir %{_includedir}/boost/spirit/core/scanner/impl
%dir %{_includedir}/boost/spirit/debug
%dir %{_includedir}/boost/spirit/debug/impl
%dir %{_includedir}/boost/spirit/dynamic
%dir %{_includedir}/boost/spirit/dynamic/impl
%dir %{_includedir}/boost/spirit/error_handling
%dir %{_includedir}/boost/spirit/error_handling/impl
%dir %{_includedir}/boost/spirit/iterator
%dir %{_includedir}/boost/spirit/iterator/impl
%dir %{_includedir}/boost/spirit/phoenix
%dir %{_includedir}/boost/spirit/symbols
%dir %{_includedir}/boost/spirit/symbols/impl
%dir %{_includedir}/boost/spirit/tree
%dir %{_includedir}/boost/spirit/tree/impl
%dir %{_includedir}/boost/spirit/utility
%dir %{_includedir}/boost/spirit/utility/impl
%dir %{_includedir}/boost/spirit/utility/impl/chset
%dir %{_includedir}/boost/test
%dir %{_includedir}/boost/test/detail
%dir %{_includedir}/boost/test/included
%dir %{_includedir}/boost/thread
%dir %{_includedir}/boost/thread/detail
%dir %{_includedir}/boost/tuple
%dir %{_includedir}/boost/tuple/detail
%dir %{_includedir}/boost/type_traits
%dir %{_includedir}/boost/type_traits/detail
%dir %{_includedir}/boost/utility

%if %{with python}
%files python -f python.list
%defattr(644,root,root,755)

%files python-devel -f python-devel.list
%defattr(644,root,root,755)
%endif

%files doc
%defattr(644,root,root,755)
%doc %{_docdir}/boost-%{version}

%files regex -f regex.list
%defattr(644,root,root,755)

%files regex-devel -f regex-devel.list
%defattr(644,root,root,755)

%files any-devel -f any.list
%defattr(644,root,root,755)

%files array-devel -f array.list
%defattr(644,root,root,755)

%files preprocessor-devel -f preprocessor.list
%defattr(644,root,root,755)

%files mpl-devel -f mpl.list
%defattr(644,root,root,755)

%files type_traits-devel -f type_traits.list
%defattr(644,root,root,755)

%files utility-devel -f utility.list
%defattr(644,root,root,755)

%files static_assert-devel -f static_assert.list
%defattr(644,root,root,755)
