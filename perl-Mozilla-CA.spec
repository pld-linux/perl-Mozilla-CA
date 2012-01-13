#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Mozilla
%define		pnam	CA
%include	/usr/lib/rpm/macros.perl
Summary:	Mozilla::CA - Mozilla's CA cert bundle in PEM format
#Summary(pl.UTF-8):	
Name:		perl-Mozilla-CA
Version:	20111025
Release:	1
License:	mozilla_1_1 gpl-2 lgpl_2_1
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Mozilla/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	74026b1a7aa0de8fc17d81efb3629195
# generic URL, check or change before uncommenting
#URL:		http://search.cpan.org/dist/Mozilla-CA/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mozilla::CA provides a copy of Mozilla's bundle of Certificate Authority
certificates in a form that can be consumed by modules and libraries
based on OpenSSL.

The module provide a single function:

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Mozilla/*.pm
%{perl_vendorlib}/Mozilla/CA
%{_mandir}/man3/*
