#
# Conditional build:
%bcond_with	python		#with boost-python support (not working now)
#

Name:		boost
Summary:	The Boost C++ Libraries
Summary(pl):	Biblioteki C++ "Boost"
Version:	1.30.2
Release:	0.1
License:	Freely distributable
URL:		http://www.boost.org/
Group:		Libraries
Source0:	http://dl.sourceforge.net/boost/%{name}-%{version}.tar.bz2
# Source0-md5:	4aed692a863bb4beaa0b70d6dc53bda5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	boost-jam >= 3.1.3 libstdc++-devel %{?_with_python:python-devel:}
BuildConflicts:	gcc = 5:3.3.1

%description
The Boost web site provides free peer-reviewed portable C++ source
libraries. The emphasis is on libraries which work well with the C++
Standard Library. One goal is to establish "existing practice" and
provide reference implementations so that the Boost libraries are
suitable for eventual standardization. Some of the libraries have
already been proposed for inclusion in the C++ Standards Committee's
upcoming C++ Standard Library Technical Report.

%description -l pl
Strona www.boost.org dostarcza wolne biblioteki C++ wraz z kodem
¼ród³owym. Nacisk jest po³o¿ony na biblioteki które dobrze
wspó³pracuj± z Bibliotek± Standardow± C++. Celem jest ustanowiæ
"isniej±c± praktykê" i dostarczaæ implementacje tak ¿e biblioteki
"Boost" nadaj± siê do ewentualnej standaryzacji. Niektóre z bibliotek
ju¿ zosta³y zg³oszone do komitetu standaryzacyjnego C++ w nadchodz±cym
Raporcie Technicznym Biblioteki Standardowej C++


%if %{?_with_python:1}%{!?_with_python:0}
# according to ldd (and automatically generated RPM dependencies) it
# doesn't strictly require python, but IMHO it's cleaner to split it
# this way
%package python
Summary:	Boost.Python library
Group:		Libraries
Requires:	boost python

%description python
Use the Boost Python Library to quickly and easily export a C++
library to Python such that the Python interface is very similar to
the C++ interface. It is designed to be minimally intrusive on your
C++ design. In most cases, you should not have to alter your C++
classes in any way in order to use them with Boost.Python. The system
should simply ``reflect'' your C++ classes and functions into Python.

%description python -l pl
U¿yj Biblioteki Boost Python ¿eby szybko i prosto eksportowaæ
biblioteki C++ do Pythona tak ¿e interfejs Pythona jest bardzo podobny
do interfejsu C++. Biblioteka jest zaprojektowana tak ¿eby narzucaæ
jak najmniej wymagañ dot. twoich konstrukcjii C++. W wiêkszo¶ci
przypadków nie musisz wogóle zmieniaæ twoich klas C++ ¿eby u¿ywaæ ich
z Boost.Python. System powinien po prostu ``odbiæ'' twoje klasy C++ i
funkcje do Pythona.


%package python-devel
Summary:	Boost.Python development headers
Group:		Libraries
Requires:	%{name}-devel

%description python-devel
Headers for the Boost.Python library

%description python-devel -l pl
Nag³ówki dla biblioteki Boost.Python
%endif

%package devel
Summary:	Boost C++ development libraries and headers
Group:		Libraries
Requires:	boost

%description devel
Headers and static libraries for the Boost C++ libraries

%description devel -l pl
Nag³ówki i biblioteki statyczne bibliotek Boost C++

%package regex
Summary:	Boost C++ regular expressions library
Summary(pl):	Biblioteka wyra¿eñ regularnych Boost C++
Group:		Libraries
Requires:	%{name} = %{version}

%description regex
Shared libraries for Boost C++ regular expressions.
%description regex -l pl
Biblioteka wyra¿eñ regularnych dla C++, biblioteki dzielone.

%package regex-devel
Group:		Libraries
Summary:	Boost C++ Regex library headers and static libraries
Summary(pl):	Nag³ówki i statyczne biblioteki Boost C++ Regex
Requires:	%{name}-regex = %{version}

%description regex-devel
%description regex-devel -l pl
Nag³ówi i statyczne biblioteki dla Boost C++ Regex

%package doc
Summary:	Boost C++ Library documentation
Group:		Libraries
Requires:	%{name}-devel = %{version}

%description doc
Documentation for the Boost C++ Library

%description doc
Dokumentacja dla biblioteki Boost C++

%prep
rm -rf $RPM_BUILD_ROOT

%setup -n boost-%{version} -q

%build
%if %{?_with_python:1}%{!?_with_python:0}
PYTHON_VERSION=`python -V 2>&1 | sed 's,.* \([0-9]\.[0-9]\)\(\.[0-9]\)\?.*,\1,'`
PYTHON_ROOT=%{_prefix}
%else
PYTHON_ROOT=
PYTHON_VERSION=
%endif
bjam -sBUILD=release -sPYTHON_ROOT=$PYTHON_ROOT -sPYTHON_VERSION=$PYTHON_VERSION

%install
rm -rf $RPM_BUILD_ROOT
rm -f master.list regex.list regex-devel.list python.list devel.list python-devel.list doc.list
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
mv _master.list master.list

RFILES="%{_includedir}/boost/cregex.hpp|"
RFILES="$RFILES%{_includedir}/boost/regex/|"
RFILES="$RFILES%{_includedir}/boost/regex.h(pp){0,1}|"
RFILES="$RFILES%{_includedir}/boost/regex_fwd.hpp|"
RFILES="$RFILES%{_libdir}/libboost_regex.a"

egrep "$RFILES"   devel.list > regex-devel.list
egrep -v "$RFILES"  devel.list > _devel.list
mv _devel.list devel.list



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

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%if %{?_with_python:1}%{!?_with_python:0}
%post python -p /sbin/ldconfig

%postun python -p /sbin/ldconfig
%endif

%files -f master.list
%defattr(644,root,root,755)

%if %{?_with_python:1}%{!?_with_python:0}
%files python -f python.list
%defattr(644,root,root,755)
%endif



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
%dir %{_includedir}/boost/mpl
%dir %{_includedir}/boost/mpl/aux_
%dir %{_includedir}/boost/mpl/aux_/config
%dir %{_includedir}/boost/mpl/aux_/preprocessed
%dir %{_includedir}/boost/mpl/aux_/preprocessed/bcc
%dir %{_includedir}/boost/mpl/aux_/preprocessed/bcc551
%dir %{_includedir}/boost/mpl/aux_/preprocessed/gcc
%dir %{_includedir}/boost/mpl/aux_/preprocessed/msvc60
%dir %{_includedir}/boost/mpl/aux_/preprocessed/msvc70
%dir %{_includedir}/boost/mpl/aux_/preprocessed/mwcw
%dir %{_includedir}/boost/mpl/aux_/preprocessed/no_ctps
%dir %{_includedir}/boost/mpl/aux_/preprocessed/no_ttp
%dir %{_includedir}/boost/mpl/aux_/preprocessed/plain
%dir %{_includedir}/boost/mpl/aux_/preprocessor
%dir %{_includedir}/boost/mpl/aux_/range_c
%dir %{_includedir}/boost/mpl/limits
%dir %{_includedir}/boost/mpl/list
%dir %{_includedir}/boost/mpl/list/aux_
%dir %{_includedir}/boost/mpl/list/aux_/preprocessed
%dir %{_includedir}/boost/mpl/list/aux_/preprocessed/plain
%dir %{_includedir}/boost/mpl/math
%dir %{_includedir}/boost/mpl/vector
%dir %{_includedir}/boost/mpl/vector/aux_
%dir %{_includedir}/boost/mpl/vector/aux_/preprocessed
%dir %{_includedir}/boost/mpl/vector/aux_/preprocessed/no_ctps
%dir %{_includedir}/boost/mpl/vector/aux_/preprocessed/plain
%dir %{_includedir}/boost/mpl/vector/aux_/preprocessed/typeof_based
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
%dir %{_includedir}/boost/preprocessor
%dir %{_includedir}/boost/preprocessor/arithmetic
%dir %{_includedir}/boost/preprocessor/arithmetic/detail
%dir %{_includedir}/boost/preprocessor/array
%dir %{_includedir}/boost/preprocessor/comparison
%dir %{_includedir}/boost/preprocessor/config
%dir %{_includedir}/boost/preprocessor/control
%dir %{_includedir}/boost/preprocessor/control/detail
%dir %{_includedir}/boost/preprocessor/control/detail/edg
%dir %{_includedir}/boost/preprocessor/control/detail/msvc
%dir %{_includedir}/boost/preprocessor/debug
%dir %{_includedir}/boost/preprocessor/detail
%dir %{_includedir}/boost/preprocessor/facilities
%dir %{_includedir}/boost/preprocessor/iteration
%dir %{_includedir}/boost/preprocessor/iteration/detail
%dir %{_includedir}/boost/preprocessor/iteration/detail/bounds
%dir %{_includedir}/boost/preprocessor/iteration/detail/iter
%dir %{_includedir}/boost/preprocessor/list
%dir %{_includedir}/boost/preprocessor/list/detail
%dir %{_includedir}/boost/preprocessor/list/detail/edg
%dir %{_includedir}/boost/preprocessor/logical
%dir %{_includedir}/boost/preprocessor/punctuation
%dir %{_includedir}/boost/preprocessor/repetition
%dir %{_includedir}/boost/preprocessor/repetition/detail
%dir %{_includedir}/boost/preprocessor/repetition/detail/edg
%dir %{_includedir}/boost/preprocessor/repetition/detail/msvc
%dir %{_includedir}/boost/preprocessor/selection
%dir %{_includedir}/boost/preprocessor/seq
%dir %{_includedir}/boost/preprocessor/seq/detail
%dir %{_includedir}/boost/preprocessor/slot
%dir %{_includedir}/boost/preprocessor/slot/detail
%dir %{_includedir}/boost/preprocessor/tuple
%dir %{_includedir}/boost/random
%dir %{_includedir}/boost/random/detail
%dir %{_includedir}/boost/regex
%dir %{_includedir}/boost/regex/v3
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

%if %{?_with_python:1}%{!?_with_python:0}
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
