#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Mozilla
%define		pnam	CA
%include	/usr/lib/rpm/macros.perl
Summary:	Mozilla::CA - Mozilla's CA cert bundle in PEM format
Summary(pl.UTF-8):	Mozilla::CA - pakiet certyfikatów CA Mozilli w formacie PEM
Name:		perl-Mozilla-CA
Version:	20120309
Release:	1
License:	MPL v1.1 or GPL v2+ or LGPL v2.1+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Mozilla/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f7fba6902335c5e068e3a576e4dce9ef
URL:		http://search.cpan.org/dist/Mozilla-CA/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mozilla::CA provides a copy of Mozilla's bundle of Certificate
Authority certificates in a form that can be consumed by modules and
libraries based on OpenSSL.

%description -l pl.UTF-8
Mozilla::CA dostarcza kopię pakietu certyfikatów CA (Certificate
Authority) w postaci nadającej się do odczytu przez moduły i
biblioteki oparte na OpenSSL.

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
%doc Changes README
%{perl_vendorlib}/Mozilla/CA.pm
%{perl_vendorlib}/Mozilla/CA
%{_mandir}/man3/Mozilla::CA.3pm*