#
# Conditional build:
%bcond_without	doc	# don't mess with & pack docs (time/space-consumming)
%bcond_without	python	# without boost-python support
#
Summary:	The Boost C++ Libraries
Summary(pl):	Biblioteki C++ "Boost"
Name:		boost
Version:	1.33.0
%define	_fver	%(echo %{version} | tr . _)
Release:	0.2
License:	Boost Software License and others
Group:		Libraries
Source0:	http://dl.sourceforge.net/boost/%{name}_%{_fver}.tar.gz
# Source0-md5:	6105340ccdb0e77e684c1cfe40f11056
Patch0:		%{name}-python.patch
URL:		http://www.boost.org/
BuildRequires:	boost-jam >= 3.1.3
BuildRequires:	libstdc++-devel
BuildRequires:	perl-base
%{?with_python:BuildRequires:	python-devel >= 2.2}
BuildConflicts:	gcc = 5:3.3.1
Obsoletes:	boost-date_time
Obsoletes:	boost-filesystem
Obsoletes:	boost-program_options
Obsoletes:	boost-regex
Obsoletes:	boost-signals
Obsoletes:	boost-test
Obsoletes:	boost-thread
Provides:	boost-date_time
Provides:	boost-filesystem
Provides:	boost-program_options
Provides:	boost-regex
Provides:	boost-signals
Provides:	boost-test
Provides:	boost-thread
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
"istniej±cej praktyki" i dostarczenie implementacji, tak ¿e biblioteki
"Boost" nadaj± siê do ewentualnej standaryzacji. Niektóre z bibliotek
ju¿ zosta³y zg³oszone do komitetu standaryzacyjnego C++ w nadchodz±cym
Raporcie Technicznym Biblioteki Standardowej C++

%package devel
Summary:	Boost C++ development libraries and headers
Summary(pl):	Pliki nag³ówkowe i biblioteki statyczne Boost C++
Group:		Development/Libraries
Requires:	libstdc++-devel
Requires:	%{name} = %{version}-%{release}
Obsoletes:	boost-any-devel
Obsoletes:	boost-array-devel
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
Obsoletes:	boost-mem_fn-devel
Obsoletes:	boost-mpl-devel
Obsoletes:	boost-preprocessor-devel
Obsoletes:	boost-program_options-devel
Obsoletes:	boost-ref-devel
Obsoletes:	boost-regex-devel
Obsoletes:	boost-signals-devel
Obsoletes:	boost-spirit-devel
Obsoletes:	boost-static_assert-devel
Obsoletes:	boost-test-devel
Obsoletes:	boost-thread-devel
Obsoletes:	boost-type_traits-devel
Obsoletes:	boost-uBLAS-devel
Obsoletes:	boost-utility-devel
Provides:	boost-any-devel
Provides:	boost-array-devel
Provides:	boost-bind-devel
Provides:	boost-call_traits-devel
Provides:	boost-compatibility-devel
Provides:	boost-compose-devel
Provides:	boost-compressed_pair-devel
Provides:	boost-concept_check-devel
Provides:	boost-conversion-devel
Provides:	boost-crc-devel
Provides:	boost-date_time-devel
Provides:	boost-filesystem-devel
Provides:	boost-mem_fn-devel
Provides:	boost-mpl-devel
Provides:	boost-preprocessor-devel
Provides:	boost-program_options-devel
Provides:	boost-ref-devel
Provides:	boost-regex-devel
Provides:	boost-signals-devel
Provides:	boost-spirit-devel
Provides:	boost-static_assert-devel
Provides:	boost-test-devel
Provides:	boost-thread-devel
Provides:	boost-type_traits-devel
Provides:	boost-uBLAS-devel
Provides:	boost-utility-devel

%description devel
Headers for the Boost C++ libraries.

%description devel -l pl
Pliki nag³ówkowe bibliotek Boost C++.

%package static
Summary:	Boost C++ static libraries
Summary(pl):	Biblioteki statyczne Boost C++
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	boost-date_time-static
Obsoletes:	boost-filesystem-static
Obsoletes:	boost-regex-static
Obsoletes:	boost-signals-static
Obsoletes:	boost-static_assert
Obsoletes:	boost-test-static
Provides:	boost-date_time-static
Provides:	boost-filesystem-static
Provides:	boost-regex-static
Provides:	boost-signals-static
Provides:	boost-static_assert
Provides:	boost-test-static

%description static
Boost C++ static libraries.

%description static -l pl
Biblioteki statyczne Boost C++.

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
	-sPYTHON_VERSION=$PYTHON_VERSION \
	-sGXX="%{__cxx}" \
	-sGCC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}}

cp -rf boost $RPM_BUILD_ROOT%{_includedir}

install bin/boost/libs/*/build/*.a/*/release/*/lib*.a $RPM_BUILD_ROOT%{_libdir}
install bin/boost/libs/*/build/*.so/*/release/*/*/lib*.so.*.*.* $RPM_BUILD_ROOT%{_libdir}
# use cp -d, install follows symlinks instead of preserving them!
cp -df bin/boost/libs/*/build/*.so/*/release/*/*/lib*.so $RPM_BUILD_ROOT%{_libdir}

# create symlinks without -gcc-mt-* things in names
for f in $RPM_BUILD_ROOT%{_libdir}/*.so.*; do
	[ -f "$f" ] || continue	
	f=$(basename "$f")
	soname=$(basename "$f" | sed -e 's#-gcc-mt-.*#.so#g')

	ln -s "$f" "$RPM_BUILD_ROOT%{_libdir}/${soname}"
done
for f in $RPM_BUILD_ROOT%{_libdir}/*.a; do
	[ -f "$f" ] || continue	
	f=$(basename "$f")
	soname=$(basename "$f" | sed -e 's#-gcc-mt-.*#.a#g')

	ln -s "$f" "$RPM_BUILD_ROOT%{_libdir}/${soname}"
done

%if %{with doc}
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
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%preun -p /sbin/ldconfig

%post python -p /sbin/ldconfig
%preun python -p /sbin/ldconfig

%files
%attr(755,root,root) %{_libdir}/libboost_date_time-*.so.*.*.*
%attr(755,root,root) %{_libdir}/libboost_filesystem-*.so.*.*.*
%attr(755,root,root) %{_libdir}/libboost_iostreams-*.so.*.*.*
%attr(755,root,root) %{_libdir}/libboost_prg_exec_monitor-*.so.*.*.*
%attr(755,root,root) %{_libdir}/libboost_program_options-*.so.*.*.*
%attr(755,root,root) %{_libdir}/libboost_regex-*.so.*.*.*
%attr(755,root,root) %{_libdir}/libboost_serialization-*.so.*.*.*
%attr(755,root,root) %{_libdir}/libboost_signals-*.so.*.*.*
%attr(755,root,root) %{_libdir}/libboost_test_exec_monitor-*.so.*.*.*
%attr(755,root,root) %{_libdir}/libboost_thread-*.so.*.*.*
%attr(755,root,root) %{_libdir}/libboost_unit_test_framework-*.so.*.*.*
%attr(755,root,root) %{_libdir}/libboost_wserialization-*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libboost_date_time.so
%attr(755,root,root) %{_libdir}/libboost_filesystem.so
%attr(755,root,root) %{_libdir}/libboost_iostreams.so
%attr(755,root,root) %{_libdir}/libboost_prg_exec_monitor.so
%attr(755,root,root) %{_libdir}/libboost_program_options.so
%attr(755,root,root) %{_libdir}/libboost_regex.so
%attr(755,root,root) %{_libdir}/libboost_serialization.so
%attr(755,root,root) %{_libdir}/libboost_signals.so
%attr(755,root,root) %{_libdir}/libboost_test_exec_monitor.so
%attr(755,root,root) %{_libdir}/libboost_thread.so
%attr(755,root,root) %{_libdir}/libboost_unit_test_framework.so
%attr(755,root,root) %{_libdir}/libboost_wserialization.so
%dir %{_includedir}/boost
%{_includedir}/boost/algorithm
%{_includedir}/boost/aligned_storage.hpp
%{_includedir}/boost/any.hpp
%{_includedir}/boost/archive
%{_includedir}/boost/array.hpp
%{_includedir}/boost/assert.hpp
%{_includedir}/boost/assign
%{_includedir}/boost/assign.hpp
%{_includedir}/boost/bind
%{_includedir}/boost/bind.hpp
%{_includedir}/boost/blank.hpp
%{_includedir}/boost/blank_fwd.hpp
%{_includedir}/boost/call_traits.hpp
%{_includedir}/boost/cast.hpp
%{_includedir}/boost/checked_delete.hpp
%{_includedir}/boost/compatibility
%{_includedir}/boost/compressed_pair.hpp
%{_includedir}/boost/concept_archetype.hpp
%{_includedir}/boost/concept_check.hpp
%{_includedir}/boost/config
%{_includedir}/boost/config.hpp
%{_includedir}/boost/crc.hpp
%{_includedir}/boost/cregex.hpp
%{_includedir}/boost/cstdint.hpp
%{_includedir}/boost/cstdlib.hpp
%{_includedir}/boost/current_function.hpp
%{_includedir}/boost/date_time
%{_includedir}/boost/detail
%{_includedir}/boost/dynamic_bitset
%{_includedir}/boost/dynamic_bitset.hpp
%{_includedir}/boost/dynamic_bitset_fwd.hpp
%{_includedir}/boost/dynamic_property_map.hpp
%{_includedir}/boost/enable_shared_from_this.hpp
%{_includedir}/boost/filesystem
%{_includedir}/boost/format
%{_includedir}/boost/format.hpp
%{_includedir}/boost/function
%{_includedir}/boost/function.hpp
%{_includedir}/boost/function_equal.hpp
%{_includedir}/boost/function_output_iterator.hpp
%{_includedir}/boost/functional.hpp
%{_includedir}/boost/functional
%{_includedir}/boost/generator_iterator.hpp
%{_includedir}/boost/get_pointer.hpp
%{_includedir}/boost/graph
%{_includedir}/boost/implicit_cast.hpp
%{_includedir}/boost/indirect_reference.hpp
%{_includedir}/boost/integer
%{_includedir}/boost/integer.hpp
%{_includedir}/boost/integer_fwd.hpp
%{_includedir}/boost/integer_traits.hpp
%{_includedir}/boost/intrusive_ptr.hpp
%{_includedir}/boost/io
%{_includedir}/boost/io_fwd.hpp
%{_includedir}/boost/iostreams
%{_includedir}/boost/iterator
%{_includedir}/boost/iterator.hpp
%{_includedir}/boost/iterator_adaptors.hpp
%{_includedir}/boost/lambda
%{_includedir}/boost/last_value.hpp
%{_includedir}/boost/lexical_cast.hpp
%{_includedir}/boost/limits.hpp
%{_includedir}/boost/logic
%{_includedir}/boost/math
%{_includedir}/boost/math_fwd.hpp
%{_includedir}/boost/mem_fn.hpp
%{_includedir}/boost/mpl
%{_includedir}/boost/multi_array
%{_includedir}/boost/multi_array.hpp
%{_includedir}/boost/multi_index
%{_includedir}/boost/multi_index_container.hpp
%{_includedir}/boost/multi_index_container_fwd.hpp
%{_includedir}/boost/next_prior.hpp
%{_includedir}/boost/non_type.hpp
%{_includedir}/boost/noncopyable.hpp
%{_includedir}/boost/nondet_random.hpp
%{_includedir}/boost/none.hpp
%{_includedir}/boost/none_t.hpp
%{_includedir}/boost/numeric
%{_includedir}/boost/operators.hpp
%{_includedir}/boost/optional
%{_includedir}/boost/optional.hpp
%{_includedir}/boost/parameter
%{_includedir}/boost/parameter.hpp
%{_includedir}/boost/pending
%{_includedir}/boost/pfto.hpp
%{_includedir}/boost/pointee.hpp
%{_includedir}/boost/pool
%{_includedir}/boost/preprocessor
%{_includedir}/boost/preprocessor.hpp
%{_includedir}/boost/program_options
%{_includedir}/boost/program_options.hpp
%{_includedir}/boost/progress.hpp
%{_includedir}/boost/property_map.hpp
%{_includedir}/boost/property_map_iterator.hpp
%{_includedir}/boost/ptr_container
%{_includedir}/boost/random
%{_includedir}/boost/random.hpp
%{_includedir}/boost/range
%{_includedir}/boost/range.hpp
%{_includedir}/boost/rational.hpp
%{_includedir}/boost/ref.hpp
%{_includedir}/boost/regex
%{_includedir}/boost/regex.h
%{_includedir}/boost/regex.hpp
%{_includedir}/boost/regex_fwd.hpp
%{_includedir}/boost/scoped_array.hpp
%{_includedir}/boost/scoped_ptr.hpp
%{_includedir}/boost/serialization
%{_includedir}/boost/shared_array.hpp
%{_includedir}/boost/shared_container_iterator.hpp
%{_includedir}/boost/shared_ptr.hpp
%{_includedir}/boost/signal.hpp
%{_includedir}/boost/signals
%{_includedir}/boost/signals.hpp
%{_includedir}/boost/smart_cast.hpp
%{_includedir}/boost/smart_ptr.hpp
%{_includedir}/boost/spirit
%{_includedir}/boost/spirit.hpp
%{_includedir}/boost/state_saver.hpp
%{_includedir}/boost/static_assert.hpp
%{_includedir}/boost/static_warning.hpp
%{_includedir}/boost/strong_typedef.hpp
%{_includedir}/boost/test
%{_includedir}/boost/thread
%{_includedir}/boost/thread.hpp
%{_includedir}/boost/throw_exception.hpp
%{_includedir}/boost/timer.hpp
%{_includedir}/boost/token_functions.hpp
%{_includedir}/boost/token_iterator.hpp
%{_includedir}/boost/tokenizer.hpp
%{_includedir}/boost/tuple
%{_includedir}/boost/type.hpp
%{_includedir}/boost/type_traits
%{_includedir}/boost/type_traits.hpp
%{_includedir}/boost/utility
%{_includedir}/boost/utility.hpp
%{_includedir}/boost/variant
%{_includedir}/boost/variant.hpp
%{_includedir}/boost/vector_property_map.hpp
%{_includedir}/boost/version.hpp
%{_includedir}/boost/visit_each.hpp
%{_includedir}/boost/wave
%{_includedir}/boost/wave.hpp
%{_includedir}/boost/weak_ptr.hpp

%files static
%{_libdir}/libboost_date_time.a
%{_libdir}/libboost_filesystem.a
%{_libdir}/libboost_iostreams.a
%{_libdir}/libboost_prg_exec_monitor.a
%{_libdir}/libboost_program_options.a
%{_libdir}/libboost_regex.a
%{_libdir}/libboost_serialization.a
%{_libdir}/libboost_signals.a
%{_libdir}/libboost_test_exec_monitor.a
%{_libdir}/libboost_thread.a
%{_libdir}/libboost_unit_test_framework.a
%{_libdir}/libboost_wserialization.a

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

%if %{with doc}
%files doc
%defattr(644,root,root,755)
%{_docdir}/%{name}-%{version}
%endif
