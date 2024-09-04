# rpmbuild playground

Creating an rpm that does exactly what you want is an art.
The documentation is not always explaining everything you need to know.
So I created this playground.

It tests a specific scenario I encountered with one of my clients:
how to exclude a dependency that is installed by a third party installer (so
rpm will not detect it).

The answer to that specific question is:

```rpm
%global __requires_exclude ^libmissing.*$
```

Other gems of knowledge I obtained by playing around:

- When running rpmbuild from a script that contains ```set -x``` you can see what rpmbuild is doing.
- When commenting out ```%global``` statements with just a ```#``` will not work,
they are still executed! Commenting out with ```#%``` disables the %global for real.

## Prerequisites

- Vagrant, tested with 2.4.1
- VirtualBox, tested with 7.0.20

## Instructions

```bash
vagrant up
vagrant ssh
cd /vagrant
./build.sh
```

This will build a C program (test_program) with a dependency on a .so file (libmissing.so).
libmissing.so is not part of the package.
The end of the build script will show the dependencies of the test_program rpm, those will not include libmissing.so.

This means that you'll be able to install the rpm successfully:

```bash
sudo rpm -i ~/rpmbuild/RPMS/x86_64/test_program-1.0-1.el7.x86_64.rpm
```

but running it will result in an error:

```bash
$ /usr/bin/test_program
/usr/bin/test_program: error while loading shared libraries: libmissing.so: cannot open shared object file: No such file or directory
```

## Clean up

Log out of the VM, then

```bash
vagrant destroy -f
```
