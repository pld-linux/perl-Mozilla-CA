#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		pdir	Mozilla
%define		pnam	CA
%include	/usr/lib/rpm/macros.perl
Summary:	Mozilla::CA - Mozilla's CA cert bundle in PEM format
Summary(pl.UTF-8):	Mozilla::CA - pakiet certyfikatów CA Mozilli w formacie PEM
Name:		perl-Mozilla-CA
Version:	20130114
Release:	1
License:	MPL v1.1 or GPL v2+ or LGPL v2.1+
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Mozilla/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	45a42082dbd68cf25869ceb2aa49d5b2
Patch0:		system-ca-certificates.patch
URL:		http://search.cpan.org/dist/Mozilla-CA/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	ca-certificates
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mozilla::CA provides a path to ca-certificates copy of Mozilla's
bundle of certificate authority certificates in a form that can be
consumed by modules and libraries based on OpenSSL.

%description -l pl.UTF-8
Mozilla::CA dostarcza kopię pakietu certyfikatów CA (Certificate
Authority) w postaci nadającej się do odczytu przez moduły i
biblioteki oparte na OpenSSL.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

# Do not distribute Mozilla downloader, we take certificates from ca-certificates package
rm mk-ca-bundle.pl
sed -i '/^mk-ca-bundle.pl$/d' MANIFEST

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
#%{perl_vendorlib}/Mozilla/CA
%{_mandir}/man3/Mozilla::CA.3pm*
