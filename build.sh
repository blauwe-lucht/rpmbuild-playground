#!/bin/bash

set -euxo pipefail

mkdir -p ~/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS}

cd binary-with-missing-dependency
gcc -fPIC -shared -o libmissing.so libmissing.c
gcc -o test_program test_program.c -L. -lmissing
cp test_program ~/rpmbuild/SOURCES

cd ../rpmbuild
rpmbuild -ba SPECS/test_program.spec

rpm -qpR ~/rpmbuild/RPMS/x86_64/test_program-1.0-1.el7.x86_64.rpm
