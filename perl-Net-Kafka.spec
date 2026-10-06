Name:           perl-Net-Kafka
Version:        1.06
Release:        4%{?dist}
Summary:        High-performant Perl client for Apache Kafka
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Net-Kafka/
Source0:        http://www.cpan.org/modules/by-module/Net/Net-Kafka-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  perl >= 0:5.022000
BuildRequires:  perl(AnyEvent)
BuildRequires:  perl(AnyEvent::XSPromises)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(ExtUtils::PkgConfig)
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  perl-devel
BuildRequires:  librdkafka-devel
Requires:       perl(AnyEvent)
Requires:       perl(AnyEvent::XSPromises)
Requires:       perl(Test::More)
Requires:       librdkafka
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This module provides Perl bindings to librdkafka C client library.

%prep
%setup -q -n Net-Kafka-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes META.json README README.md
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Net*
%{_mandir}/man3/*

%changelog
* Tue Oct 06 2026 Michael R. Davis <mrdvt92@yahoo.com> 1.06-4
- Added BuildRequires for librdkafka-devel, perl(ExtUtils::PkgConfig), make, gcc, and perl-devel
- Added Requires for librdkafka
