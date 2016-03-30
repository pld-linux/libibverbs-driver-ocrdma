Summary:	Userspace driver for the Emulex OneConnect RDMA adapters
Summary(pl.UTF-8):	Sterownik przestrzeni użytkownika dla kart Emulex OneConnect RDMA
Name:		libibverbs-driver-ocrdma
Version:	1.0.7
Release:	1
License:	BSD or GPL v2
Group:		Libraries
Source0:	https://www.openfabrics.org/downloads/libocrdma/libocrdma-%{version}.tar.gz
# Source0-md5:	1b0115be7b832458a8ecff3ef69999a5
URL:		http://openib.org/
BuildRequires:	libibverbs-devel
# only checked for, not used
#BuildRequires:	sysfsutils-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%undefine	__cxx

%description
libocrdma is a userspace driver for the Emulex OneConnect RDMA
adapters. It works as a plug-in module for libibverbs that allows
programs to use Emulex RDMA hardware directly from userspace.

%description -l pl.UTF-8
libocrdma to sterownik przestrzeni użytkownika dla kart Emulex
OneConnect RDMA. Działa jako moduł ładowany przez libibverbs,
pozwalający programom na dostęp z przestrzeni użytkownika do
sprzętu Emulex RDMA.

%package static
Summary:	Static version of ocrdma driver
Summary(pl.UTF-8):	Statyczna wersja sterownika ocrdma
Group:		Development/Libraries
Requires:	libibverbs-static

%description static
Static version of ocrdma driver, which may be linked directly into
application.

%description static -l pl.UTF-8
Statyczna wersja sterownika ocrdma, którą można wbudować bezpośrednio
w aplikację.

%prep
%setup -q -n libocrdma-%{version}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# dlopened by -rdmav2.so name
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libocrdma.{so,la}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/libocrdma-rdmav2.so
%{_sysconfdir}/libibverbs.d/ocrdma.driver

%files static
%defattr(644,root,root,755)
%{_libdir}/libocrdma.a
