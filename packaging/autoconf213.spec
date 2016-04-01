Name:           autoconf213
License:        GPL v2 or later
Group:          Development/Tools/Building
Url:            http://www.gnu.org/software/autoconf
AutoReqProv:    on
Requires:       gawk, m4 >= 1.1, mktemp, perl
Version:        2.13
Release:        1
Summary:        A GNU Tool for Automatically Configuring Source Code
BuildArch:      noarch
Source:         autoconf-%{version}.tar.bz2
Source1001: 	autoconf213.manifest
BuildRequires:  texinfo
BuildRequires:  makeinfo

%description
GNU Autoconf is a tool for configuring source code and makefiles. Using
autoconf, programmers can create portable and configurable packages,
because the person building the package is allowed to specify various
configuration options.

You should install autoconf if you are developing software and would
like to create shell scripts to configure your source code packages.

Note that the autoconf package is not required for the end user who may
be configuring software with an autoconf-generated script; autoconf is
only required for the generation of the scripts, not their use.



Authors:
--------
    Ben Elliston  <bje@cygnus.com>
    David J MacKenzie  <djm@catapult.va.pubnix.com>

%prep
%setup -n autoconf-%{version} -q
cp %{SOURCE1001} .


mv autoconf.texi autoconf213.texi
rm -f autoconf.info

%build
export CFLAGS+=" -fvisibility=hidden"
  export CXXFLAGS+=" -fvisibility=hidden"
  
./configure --prefix=%{_prefix} --infodir=%{_infodir} --mandir=%{_mandir} \
            --program-suffix=-2.13
make

%install
%make_install
# We don't want to include the standards.info stuff in the package,
# because it comes from binutils...
rm -f ${RPM_BUILD_ROOT}%{_infodir}/standards*

%post
%install_info --info-dir=%{_infodir} %{_infodir}/autoconf2.13.info.gz

%postun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/autoconf2.13.info.gz

%clean
rm -rf $RPM_BUILD_ROOT

%files
%manifest %{name}.manifest
%defattr(-,root,root)
%doc AUTHORS COPYING NEWS README TODO
%{_prefix}/bin/*
%{_prefix}/share/autoconf-2.13
%doc %{_infodir}/*.gz
