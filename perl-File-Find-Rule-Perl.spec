#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	File
%define		pnam	Find-Rule-Perl
%include	/usr/lib/rpm/macros.perl
Summary:	File::Find::Rule::Perl - Common rules for searching for Perl things
Summary(pl.UTF-8):	File::Find::Rule::Perl - wspólne reguly do szukania rzeczy perlowych
Name:		perl-File-Find-Rule-Perl
Version:	1.15
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/File/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d8b458792b7eed83c744ae30b1bc3348
URL:		http://search.cpan.org/dist/File-Find-Rule-Perl/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(File::Spec) >= 0.82
BuildRequires:	perl-File-Find-Rule >= 0.20
BuildRequires:	perl-Params-Util >= 0.38
BuildRequires:	perl-Parse-CPAN-Meta >= 1.38
BuildRequires:	perl-Test-Simple >= 0.47
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
When one writes a lot of things that muck with Perl files, it's often
annoying that finding "perl files" requires a moderately complex
File::Find::Rule pattern.

File::Find::Rule::Perl provides methods for finding various types
Perl-related files, or replicating search queries run on a
distribution in various parts of the CPAN ecosystem.

%description -l pl.UTF-8
Przy pisaniu wielu rzeczy obrabiających pliki perlowe, często staje
się uciążliwe to, że wyszukiwanie "plików perlowych" wymaga dość
złożonego wzorca File::Find::Rule.

File::Find::Rule::Perl dostarcza metody do wyszukiwania różnych
rodzajów plików związanych z Perlem oraz powtarzalnych zapytań
wyszukiwań uruchamianych na dystrybucji w różnych częściach ekosystemu
CPAN.

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
%doc Changes
%{perl_vendorlib}/File/Find/Rule/Perl.pm
%{_mandir}/man3/File::Find::Rule::Perl.3pm*
