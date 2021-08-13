#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-beeswarm
Version  : 0.4.0
Release  : 29
URL      : https://cran.r-project.org/src/contrib/beeswarm_0.4.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/beeswarm_0.4.0.tar.gz
Summary  : The Bee Swarm Plot, an Alternative to Stripchart
Group    : Development/Tools
License  : Artistic-2.0
Requires: R-beeswarm-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
"stripchart", but with closely-packed, non-overlapping points.

%package lib
Summary: lib components for the R-beeswarm package.
Group: Libraries

%description lib
lib components for the R-beeswarm package.


%prep
%setup -q -c -n beeswarm
cd %{_builddir}/beeswarm

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1622646508

%install
export SOURCE_DATE_EPOCH=1622646508
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library beeswarm
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library beeswarm
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library beeswarm
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc beeswarm || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/beeswarm/DESCRIPTION
/usr/lib64/R/library/beeswarm/INDEX
/usr/lib64/R/library/beeswarm/Meta/Rd.rds
/usr/lib64/R/library/beeswarm/Meta/data.rds
/usr/lib64/R/library/beeswarm/Meta/features.rds
/usr/lib64/R/library/beeswarm/Meta/hsearch.rds
/usr/lib64/R/library/beeswarm/Meta/links.rds
/usr/lib64/R/library/beeswarm/Meta/nsInfo.rds
/usr/lib64/R/library/beeswarm/Meta/package.rds
/usr/lib64/R/library/beeswarm/NAMESPACE
/usr/lib64/R/library/beeswarm/NEWS
/usr/lib64/R/library/beeswarm/R/beeswarm
/usr/lib64/R/library/beeswarm/R/beeswarm.rdb
/usr/lib64/R/library/beeswarm/R/beeswarm.rdx
/usr/lib64/R/library/beeswarm/data/breast.RData
/usr/lib64/R/library/beeswarm/help/AnIndex
/usr/lib64/R/library/beeswarm/help/aliases.rds
/usr/lib64/R/library/beeswarm/help/beeswarm.rdb
/usr/lib64/R/library/beeswarm/help/beeswarm.rdx
/usr/lib64/R/library/beeswarm/help/paths.rds
/usr/lib64/R/library/beeswarm/html/00Index.html
/usr/lib64/R/library/beeswarm/html/R.css
/usr/lib64/R/library/beeswarm/tests/beeswarm-test.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/beeswarm/libs/beeswarm.so
/usr/lib64/R/library/beeswarm/libs/beeswarm.so.avx2
