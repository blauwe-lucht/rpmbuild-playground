Name:           test_program
Version:        1.0
Release:        1%{?dist}
Summary:        Test program that depends on a missing shared library

License:        GPL
URL:            http://example.com
Source0:        test_program

# Disable automatic dependency generation for libmissing.so
%global __requires_exclude ^libmissing.*$

%description
A test program that depends on a shared library (libmissing.so) that is not included in the system.

%prep
# No preparation needed since we're directly using the binary

%build
# No build step needed since the binary is pre-compiled

%install
# Create the target directory in the build root
mkdir -p %{buildroot}/usr/bin

# Copy the binary to the build root
cp -a %{_sourcedir}/test_program %{buildroot}/usr/bin/test_program

%files
/usr/bin/test_program

%changelog
* Wed Sep 04 2024 Your Name <youremail@example.com> - 1.0-1
- Initial RPM release
