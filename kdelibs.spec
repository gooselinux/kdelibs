%global phonon_ver 4.3.1
%global soprano_ver 2.3.1
%global strigi_ver 0.7

Summary: K Desktop Environment 4 - Libraries
Version: 4.3.4
Release: 10%{?dist}

Name: kdelibs
Epoch: 6
Obsoletes: kdelibs4 < %{version}-%{release}
Provides: kdelibs4 = %{version}-%{release}
%{?_isa:Provides: kdelibs4%{?_isa} = %{version}-%{release}}

# http://techbase.kde.org/Policies/Licensing_Policy
License: LGPLv2+
URL: http://www.kde.org/
Group: System Environment/Libraries
Source0: ftp://ftp.kde.org/pub/kde/stable/%{version}/src/kdelibs-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: kde4-macros(api) >= 2
BuildRequires: kde-filesystem >= 4-23
Requires: coreutils grep
Requires: dbus-x11
Requires: hicolor-icon-theme
Requires: kde-filesystem >= 4-23
Requires: kde-settings
%{?_kde4_macros_api:Requires: kde4-macros(api) = %{_kde4_macros_api} }
Requires: shared-mime-info
Requires: kdelibs-common
Requires: hunspell
Requires: phonon%{?_isa} >= %{phonon_ver} 
Requires: soprano%{?_isa} >= %{soprano_ver} 
Requires: strigi-libs%{?_isa} >= %{strigi_ver} 

Source1: kde4.sh
Source2: kde4.csh

# make -devel packages parallel-installable
Patch0: kdelibs-4.2.96-parallel_devel.patch

# fix kde#149705
Patch2: kdelibs-4.2.85-kde149705.patch

# Hunspell support for K3Spell
# http://fedoraproject.org/wiki/Releases/FeatureDictionary
# http://bugs.kde.org/show_bug.cgi?id=154561
Patch5: kdelibs-4.0.0-k3spell-hunspell.patch

# openssl's SHLIB_VERSION_NUMBER macro can't be used/trusted
Patch6: kdelibs-4.0.0-openssl.patch

# install all .css files and Doxyfile.global in kdelibs-common to build
# kdepimlibs-apidocs against
Patch8: kdelibs-4.0.2-install-all-css.patch

# add Red Hat Enterprice Linux/V-R to KHTML UA string
Patch9: kdelibs-4.3.4-branding.patch

# don't cache kdeglobals paths because they change after profile directories
# are loaded from kde4rc
Patch10: kdelibs-4.1.72-no-cache-kdeglobals-paths.patch

# workaround for policykit
Patch11: kdelibs-4.1.72-policykit-workaround.patch
Patch12: kdelibs-4.1.0-xdg-menu.patch

# patch KStandardDirs to use %{_libexecdir}/kde4 instead of %{_libdir}/kde4/libexec
Patch14: kdelibs-4.2.85-libexecdir.patch

# kstandarddirs changes: search /etc/kde, find /usr/libexec/kde4
Patch18: kdelibs-4.1.72-kstandarddirs.patch
Patch20: kdelibs-4.1.70-cmake.patch

# patch to fix keditbookmarks crash (kde#160679)
Patch22: kdelibs-4.3.0-bookmarks.patch
Patch24: kdelibs-4.3.1-drkonq.patch

# use -fno-var-tracking-assignments on khtml/svg bits, use in a pinch on f12+
# workaound for low-mem systems (ppc64, x86_64)
Patch26: kdelibs-4.3.3-khtml_svg_no_var_tracking_assignments.patch

# disable dot to reduce the size
Patch27: kdelibs-4.3.4-apidoc.patch

# upstream, kubuntu working to upstream this
Patch50: http://bazaar.launchpad.net/~kubuntu-members/kdelibs/ubuntu/download/head:/kubuntu_80_kaction_q-20091014221915-y11xctvidhr0ewmz-1/kubuntu_80_kaction_qt_keys.diff

# make kdeinit4 quiet
Patch51: kdelibs-4.3.4-kdeinit4-quiet.patch

# drop webkit support
Patch52: kdelibs-4.3.4-webkit.patch

# 4.3 branch
Patch100: kdelibs-4.3.5.patch

# 4.4 trunk
# http://websvn.kde.org/?view=revision&revision=1027234
# add adFilteredBy API required for konq-plugins-4.3.3 to build
Patch200: kdelibs-4.3.3-adFilteredBy.patch

# http://websvn.kde.org/?view=revision&revision=1056377
# sonnet was broken with indic, asian, arabic
Patch201: kdelibs-4.4-sonnet.patch

# http://websvn.kde.org/?view=revision&revision=1095342
# fixes printing on pages with form widgets.
Patch202: kdelibs-4.3.4-printing.patch

# http://websvn.kde.org/?view=revision&revision=1089160
# critical performance fix
Patch203: kdelibs-4.3.4-performance-khtmlview.patch

# security fix
Patch300: kdelibs-4.3.1-CVE-2009-2702.patch

BuildRequires: qt4-devel >= 4.5.0
Requires: qt4%{?_isa} >= %{_qt4_version}
Requires: xdg-utils
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

BuildRequires: alsa-lib-devel
BuildRequires: automoc4 >= 0.9.88
BuildRequires: avahi-devel
BuildRequires: bison flex
BuildRequires: bzip2-devel
BuildRequires: cmake >= 2.6.2-3
BuildRequires: cups-devel cups
BuildRequires: enchant-devel
BuildRequires: gamin-devel
BuildRequires: gettext-devel
BuildRequires: giflib-devel
BuildRequires: jasper-devel
BuildRequires: krb5-devel
BuildRequires: libacl-devel libattr-devel
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: libtiff-devel
BuildRequires: libxslt-devel libxml2-devel
BuildRequires: libutempter-devel
BuildRequires: OpenEXR-devel
BuildRequires: openssl-devel
BuildRequires: pcre-devel
BuildRequires: phonon-devel >= %{phonon_ver} 
BuildRequires: shared-mime-info
BuildRequires: soprano-devel >= %{soprano_ver} 
BuildRequires: strigi-devel >= %{strigi_ver} 
BuildRequires: xz-devel
BuildRequires: zlib-devel
# extra X deps (seemingly needed and/or checked-for by most kde4 buildscripts)
%define x_deps libSM-devel libXcomposite-devel libXdamage-devel libxkbfile-devel libXpm-devel libXScrnSaver-devel libXtst-devel libXv-devel libXxf86misc-devel
%{?x_deps:BuildRequires: %{x_deps}}
BuildRequires: openssh-clients
BuildRequires: subversion
BuildRequires: doxygen
BuildRequires: qt4-doc

Provides: kross(javascript) = %{version}-%{release}
Provides: kross(qtscript) = %{version}-%{release}

%description
Libraries for the K Desktop Environment 4.

%package common
Group: System Environment/Libraries
Summary: Common files for KDE 3 and KDE 4 libraries
%description common
This package includes the common files for the KDE 3 and KDE 4 libraries.

%package devel
Group: Development/Libraries
Summary: Header files for compiling KDE 4 applications
Conflicts: kdebase-runtime < 4.2.90
Conflicts: kdebase-workspace-devel < 4.2.90
Provides: plasma-devel = %{version}-%{release}
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes: kdelibs4-devel < %{version}-%{release}
Provides:  kdelibs4-devel = %{version}-%{release}
Requires: cmake >= 2.6.2-3
Requires: automoc4 >= 0.9.88
Requires: qt4-devel
Requires: openssl-devel
Requires: phonon-devel
Requires: strigi-devel
Requires: bzip2-devel gamin-devel libacl-devel
%{?x_deps:Requires: %{x_deps}}

%description devel
This package includes the header files you will need to compile
applications for KDE 4.

%package apidocs
Group: Development/Documentation
Summary: KDE 4 API documentation
Requires: kde-filesystem
Provides: kdelibs4-apidocs = %{version}-%{release}
BuildArch: noarch

%description apidocs
This package includes the KDE 4 API documentation in HTML
format for easy browsing.


%prep
%setup -q -n kdelibs-%{version}

%patch0 -p1 -b .parallel_devel
%patch2 -p1 -b .kde149705
%patch5 -p1 -b .k3spell-hunspell
%patch8 -p1 -b .all-css
%patch9 -p1 -b .branding

%patch11 -p1 -b .policykit
%patch12 -p1 -b .Administration-menu
%patch14 -p1 -b .libexecdir
%patch18 -p1 -b .kstandarddirs
%patch20 -p1 -b .xxcmake
%patch22 -p1 -b .bookmarks
%patch24 -p1 -b .drkonq
%patch26 -p1 -b .khtml_svg_no_var_tracking_assignments
%patch27 -p1 -b .disable-dot

%patch50 -p1 -b .kaction_qt_keys
%patch51 -p1 -b .kdeinit4-quiet
%patch52 -p1 -b .nowebkit

# upstream patches
# 4.3
%patch100 -p1 -b .kde435

# 4.4
%patch200 -p0 -b .adFilteredBy
%patch201 -p1 -b .sonnet
%patch202 -p1 -b .printing
%patch203 -p1 -b .performance

# security fix
%patch300 -p1 -b .CVE-2009-2702

%build

# add release version
sed -i -e "s|@@VERSION_RELEASE@@|%{version}-%{release}|" kio/kio/kprotocolmanager.cpp

mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} -DKDE_DISTRIBUTION_TEXT="%{version}-%{release} Red Hat Enterprise Linux" ..
popd

make %{?_smp_mflags} -C %{_target_platform}

# build apidocs
export QTDOCDIR=`pkg-config --variable=docdir Qt`
doc/api/doxygen.sh .


%install
rm -rf %{buildroot}

make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

# see also use-of/patching of XDG_MENU_PREFIX in kdebase/kde-settings
mv %{buildroot}%{_kde4_sysconfdir}/xdg/menus/applications.menu \
   %{buildroot}%{_kde4_sysconfdir}/xdg/menus/kde4-applications.menu

# create/own, see http://bugzilla.redhat.com/483318
mkdir -p %{buildroot}%{_kde4_libdir}/kconf_update_bin

# move devel symlinks
mkdir -p %{buildroot}%{_kde4_libdir}/kde4/devel
pushd %{buildroot}%{_kde4_libdir}
for i in lib*.so
do
  case "$i" in
    libkdeinit4_*.so)
      ;;
    ## FIXME/TODO: imo, should leave everything except for known-conflicts -- Rex
    *)
      linktarget=`readlink "$i"`
      rm -f "$i"
      ln -sf "../../$linktarget" "kde4/devel/$i"
      ;;
  esac
done
popd

# fix Sonnet documentation multilib conflict
bunzip2 %{buildroot}%{_kde4_docdir}/HTML/en/sonnet/index.cache.bz2
sed -i -e 's!<a name="id[0-9]*"></a>!!g' %{buildroot}%{_kde4_docdir}/HTML/en/sonnet/index.cache
bzip2 -9 %{buildroot}%{_kde4_docdir}/HTML/en/sonnet/index.cache

# install apidocs and generator script
install -p -D doc/api/doxygen.sh %{buildroot}%{_kde4_bindir}/kde4-doxygen.sh

mkdir -p %{buildroot}%{_kde4_docdir}/HTML/en
cp -prf kdelibs-%{version}-apidocs %{buildroot}%{_kde4_docdir}/HTML/en/kdelibs4-apidocs

# fix multilib issue in cmake files
pushd %{buildroot}%{_kde4_appsdir}/cmake/modules/

# fix multilib issue in cmake files
cat >KDELibsDependencies.cmake.new <<EOF
EXEC_PROGRAM("/usr/bin/kde4-config" ARGS "--libsuffix" OUTPUT_VARIABLE LIBSUFFIX)
set(KDE4_LIB_INSTALL_DIR     "/usr/lib")
if ("\${LIBSUFFIX}" MATCHES 64)
   set(KDE4_LIB_INSTALL_DIR     "/usr/lib64")
endif ("\${LIBSUFFIX}" MATCHES lib64)

EOF
cat KDELibsDependencies.cmake | grep -v KDE4_LIB_INSTALL_DIR >> KDELibsDependencies.cmake.new
mv KDELibsDependencies.cmake.new KDELibsDependencies.cmake
sed -i -e "s|%{_kde4_libdir}|\${KDE4_LIB_INSTALL_DIR}|g" KDELibs4LibraryTargets-release.cmake
popd

%post
/sbin/ldconfig
touch --no-create %{_kde4_iconsdir}/hicolor &> /dev/null || :

%postun
/sbin/ldconfig ||:
if [ $1 -eq 0 ] ; then
    update-desktop-database -q &> /dev/null
    update-mime-database %{_kde4_datadir}/mime &> /dev/null
    touch --no-create %{_kde4_iconsdir}/hicolor &> /dev/null
    gtk-update-icon-cache %{_kde4_iconsdir}/hicolor &> /dev/null || :
fi

%posttrans
update-desktop-database -q &> /dev/null
update-mime-database %{_kde4_datadir}/mime >& /dev/null
gtk-update-icon-cache %{_kde4_iconsdir}/hicolor &> /dev/null || :


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc AUTHORS README TODO
%doc COPYING.LIB
%{_kde4_bindir}/*
%exclude %{_kde4_bindir}/kconfig_compiler4
%{_kde4_appsdir}/*
# kdewidgets
%exclude %{_kde4_bindir}/makekdewidgets4
%exclude %{_kde4_bindir}/kde4-doxygen.sh
%exclude %{_kde4_appsdir}/kdewidgets/
%exclude %{_kde4_appsdir}/cmake/
%{_kde4_configdir}/*
%{_datadir}/dbus-1/interfaces/*
%{_kde4_datadir}/mime/packages/kde.xml
%{_kde4_sharedir}/kde4/services/*
%{_kde4_sharedir}/kde4/servicetypes/*
%{_kde4_iconsdir}/hicolor/*/actions/*
%{_kde4_docdir}/HTML/en/sonnet/
%{_kde4_docdir}/HTML/en/kioslave/
%{_kde4_libdir}/lib*.so.*
%{_kde4_libdir}/libkdeinit4_*.so
%{_kde4_libdir}/kconf_update_bin/
%dir %{_kde4_libdir}/kde4/
%{_kde4_libdir}/kde4/*.so
%{_kde4_libexecdir}/*
%{_kde4_libdir}/kde4/plugins/
%{_kde4_sysconfdir}/xdg/menus/*.menu
%doc %{_mandir}/man*/*
%exclude %{_kde4_configdir}/kdebug.areas
%exclude %{_kde4_configdir}/kdebugrc
%exclude %{_kde4_configdir}/ui/ui_standards.rc
%exclude %{_kde4_appsdir}/kdeui
%exclude %{_kde4_configdir}/colors/40.colors
%exclude %{_kde4_configdir}/colors/Rainbow.colors
%exclude %{_kde4_configdir}/colors/Royal.colors
%exclude %{_kde4_configdir}/colors/Web.colors
%exclude %{_kde4_configdir}/ksslcalist
%exclude %{_kde4_bindir}/preparetips

%files common
%defattr(-,root,root,-)
%{_kde4_configdir}/colors/40.colors
%{_kde4_configdir}/colors/Rainbow.colors
%{_kde4_configdir}/colors/Royal.colors
%{_kde4_configdir}/colors/Web.colors
%{_kde4_configdir}/ksslcalist
%{_kde4_bindir}/preparetips
%{_kde4_configdir}/kdebug.areas
%{_kde4_configdir}/kdebugrc
%dir %{_kde4_configdir}/ui
%{_kde4_configdir}/ui/ui_standards.rc
%{_kde4_appsdir}/kdeui
%{_kde4_docdir}/HTML/en/common/
%{_kde4_datadir}/locale/all_languages/

%files devel
%defattr(-,root,root,-)
%doc KDE4PORTING.html
%{_kde4_bindir}/kconfig_compiler4
%{_kde4_bindir}/makekdewidgets4
%{_kde4_bindir}/kde4-doxygen.sh
%{_kde4_appsdir}/cmake/
%{_kde4_appsdir}/kdewidgets/
%{_kde4_includedir}/*
%{_kde4_libdir}/kde4/devel/

%files apidocs
%defattr(-,root,root,-)
%{_kde4_docdir}/HTML/en/kdelibs4-apidocs/


%changelog
* Thu Jun 24 2010 Than Ngo <than@redhat.com> - 6:4.3.4-10
- Resolves: bz#587243, MultilibConflicts

* Mon Jun 21 2010 Than Ngo <than@redhat.com> - 6:4.3.4-9
- Resolves: bz#587243, MultilibConflicts

* Tue Jun 01 2010 Than Ngo <than@redhat.com> - 6:4.3.4-8
- Resolves: bz#597271, drop WebKit support in Qt

* Mon May 10 2010 Than Ngo <than@redhat.com> - 6:4.3.4-7
- Resolves: bz#590651, disable dot to reduce the apidoc size

* Sat May 01 2010 Than Ngo <than@redhat.com> - 6:4.3.4-6
- Redhat branding 
- make kdeinit4 quiet
- backport to fix critical performance
- backport to fix issue in printing on pages with form widgets

* Fri Mar 26 2010 Than Ngo <than@redhat.com> - 6:4.3.4-5
- rebuilt against qt-4.6.2

* Fri Jan 22 2010 Than Ngo <than@redhat.com> - 6:4.3.4-4
- backport 4.3.5 fixes

* Fri Dec 18 2009 Than Ngo <than@redhat.com> - 4.3.4-3
- fix bz#531211, backport sonnet patch, fix rendering issue in indic, asian, arabic 
  languages
- drop noarch hack

* Fri Dec 04 2009 Than Ngo <than@redhat.com> - 4.3.4-2
- add workaound for low-mem systems

* Tue Dec 01 2009 Than Ngo <than@redhat.com> - 4.3.4-1
- 4.3.4

* Mon Nov 16 2009 Than Ngo <than@redhat.com> - 4.3.3-5
- fix conditional

* Fri Nov 13 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.3.3-4
- kubuntu_80_kaction_qt_keys.diff (#475247)
- soprano_ver 2.3.1

* Fri Nov 13 2009 Than Ngo <than@redhat.com> - 4.3.3-3
- rhel cleanup, fix conditional for RHEL

* Fri Nov 06 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.3.3-2
- backport adFilteredBy API from trunk, required to build konq-plugins-4.3.3
- BR flex and bison for the Solid predicate parser
- fix build of fakes.c due to missing #include <string.h>

* Fri Oct 30 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.3.3-1
- 4.3.3

* Mon Oct 12 2009 Lukáš Tinkl <ltinkl@redhat.com> - 4.3.2-4
- khtml kpart crasher nr. 2 (rev.1033984)

* Thu Oct 08 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.3.2-3
- khtml kpart crasher (kde #207173/209876)

* Wed Oct 07 2009 Than Ngo <than@redhat.com> - 4.3.2-2
- fix a deadlock in KLocale

* Mon Oct 05 2009 Than Ngo <than@redhat.com> - 4.3.2-1
- 4.3.2

* Wed Sep 23 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.3.1-7
- move /etc/profile.d/kde4.(sh|csh) to kde-settings (F-12+)

* Mon Sep 21 2009 Than Ngo <than@redhat.com> - 4.3.1-6
- use abrt for RHEL

* Sat Sep 19 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.3.1-5
- groupdav connect to egroupware failed (kde#186763)

* Fri Sep 18 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.3.1-4
- ship kde4-doxygen.sh only in -devel (fix duplicate file)

* Fri Sep 04 2009 Than Ngo <than@redhat.com> - 4.3.1-3
- security fix for -CVE-2009-2702

* Wed Sep 02 2009 Ben Boeckel <MathStuf@gmail.com> - 4.3.1-2
- Patch for kde#160679

* Fri Aug 28 2009 Than Ngo <than@redhat.com> - 4.3.1-1
- 4.3.1
- openssl-1.0 build fixes

* Wed Aug 26 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.3.0-8
- BR: xz-devel

* Sun Aug 23 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.3.0-7
- buildsys_phonon patch (to be compatible with newer kde-qt.git qt builds)

* Wed Aug 19 2009 Lukáš Tinkl <ltinkl@redhat.com> - 4.3.0-6
- fix crash when editting toolbars (kdebug:200815)

* Tue Aug 18 2009 Lukáš Tinkl <ltinkl@redhat.com> - 4.3.0.5
- fix KDE bug #19538, copy file after rename uses old file name

* Mon Aug 17 2009 Lukáš Tinkl <ltinkl@redhat.com> - 4.3.0-4
- fix unmounting devices
- fix copying URLs to clipboard (kdebug:170608)

* Fri Aug 14 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.3.0-3
- kde4.(sh|csh): drop KDE_IS_PRELINKED for now (workaround bug #515539)

* Wed Aug 05 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.3.0-2
- microblog crashes plasma on show friends toggle (kdebug#202550)
- khtml crasher (kdebug#199557)

* Thu Jul 30 2009 Than Ngo <than@redhat.com> - 4.3.0-1
- 4.3.0

* Wed Jul 29 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.2.98-4
- -devel: Conflicts: kdebase-runtime < 4.2.90, kdebase-workspace-devel < 4.2.90

* Sun Jul 26 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.2.98-3
- fix CVE-2009-2537 - select length DoS
- fix CVE-2009-1725 - crash, possible ACE in numeric character references
- fix CVE-2009-1687 - possible ACE in KJS (FIXME: now aborts, so still crashes)
- fix CVE-2009-1698 - crash, possible ACE in CSS style attribute handling
- fix minimum strigi version (0.7, not 0.7.0, RPM thinks 0.7 < 0.7.0)

* Fri Jul 24 2009 Lukáš Tinkl <ltinkl@redhat.com> - 4.2.98-2
- respun tarball, to fix KIO HTTP redirects
- fix phonon/strigi versions

* Wed Jul 22 2009 Than Ngo <than@redhat.com> - 4.2.98-1
- 4.3rc3

* Thu Jul 16 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.2.96-2
- soprano_ver 2.3.0
- License: LGPLv2+

* Fri Jul 10 2009 Than Ngo <than@redhat.com> - 4.2.96-1
- 4.3rc2

* Wed Jul 08 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.2.95-4
- fix CMake dependency in parallel_devel patch (#510259, CHIKAMA Masaki)

* Fri Jul 03 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.2.95-3
- plasma animation crasher (kdebug#198338)

* Fri Jul 03 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.2.95-2
- up min versions, phonon, strigi, soprano (#509511)

* Thu Jun 25 2009 Than Ngo <than@redhat.com> - 4.2.95-1
- 4.3 rc1

* Wed Jun 03 2009 Rex Dieter <rdieter@fedoraproject.org> 4.2.90-1
- KDE-4.3 beta2 (4.2.90)

* Tue May 12 2009 Than Ngo <than@redhat.com> 4.2.85-1
- KDE-4.3 beta1 (4.2.85)
- kde4.(sh|csh): drop QT_PLUGINS_PATH munging, kde4-config call (#498809)

* Wed Apr 29 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.2.2-14
- -devel: Provides: kdelibs4-devel%%{?_isa} ...

* Tue Apr 28 2009 Lukáš Tinkl <ltinkl@redhat.com> - 4.2.2-13
- upstream patch to fix GCC4.4 crashes in kjs
  (kdebug:189809)

* Fri Apr 24 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.2.2-12
- drop the PopupApplet configuration backports (#495998) for now, kconf_update
  does not work as expected for Plasma

* Thu Apr 23 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.2.2-11
- fix the kconf_update scriptlet for #495998 again (missing DELETEGROUP)

* Thu Apr 23 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.2.2-10
- fix the kconf_update scriptlet for #495998 (broken .upd syntax)

* Tue Apr 21 2009 Than Ngo <than@redhat.com> - 4.2.2-9
- don't let plasma appear over screensaver

* Mon Apr 20 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.2.2-8
- fix Plasma PopupApplet configuration interfering with weather applet (#495998)

* Sun Apr 19 2009 Rex Dieter <rdieter@fedoraproject.org> 4.2.2-7
- fix and simplify the child struct disposal (kde#180785)

* Sat Apr 18 2009 Rex Dieter <rdieter@fedoraproject.org> 4.2.2-6
- squash leaky file descriptors in kdeinit (kde#180785,rhbz#484370)

* Fri Apr 10 2009 Rex Dieter <rdieter@fedoraproject.org> 4.2.2-5
- fix bidi-related hangs in khtml (kde#189161)

* Wed Apr 08 2009 Than Ngo <than@redhat.com> - 4.2.2-4
- upstream patch fix ReadOnlyPart crash for non-local file

* Tue Apr 07 2009 Than Ngo <than@redhat.com> - 4.2.2-3
- fix kickoff focus issue

* Tue Apr 07 2009 Than Ngo <than@redhat.com> - 4.2.2-2
- upstream patch to fix kio_http issue

* Wed Apr  1 2009 Lukáš Tinkl <ltinkl@redhat.com> - 4.2.2-1
- KDE 4.2.2

* Mon Mar 23 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.2.1-9
- scriptlet optimization

* Thu Mar 19 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.2.1-8
- Provides: kdelibs4%%{?_isa} ... (#491082)

* Wed Mar 18 2009 Rex Dieter <rdieter@fedoraproject.org> 4.2.1-7
- Provides: kross(javascript) kross(qtscript)  (#490586)

* Thu Mar 12 2009 Than Ngo <than@redhat.com> - 4.2.1-6
- apply patch to fix encoding for Qt-4.5.0 

* Mon Mar 09 2009 Than Ngo <than@redhat.com> - 4.2.1-5
- apply patch to fix issue in CSS style that causes konqueror shows a blank page

* Wed Mar 05 2009 Rex Dieter <rdieter@fedorproject.org> - 4.2.1-4 
- move designer plugins to main/runtime (#487622)

* Sun Mar 01 2009 Than Ngo <than@redhat.com> - 4.2.1-2
- respin

* Fri Feb 27 2009 Than Ngo <than@redhat.com> - 4.2.1-1
- 4.2.1

* Thu Feb 26 2009 Than Ngo <than@redhat.com> 4.2.0-17
- fix build issue against gcc44

* Wed Feb 25 2009 Than Ngo <than@redhat.com> - 4.2.0-16
- fix files conflicts with 3.5.x

* Tue Feb 24 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.2.0-15
- fix crash in ~KMainWindow triggered by sending messages in KNode (kde#182322)

* Mon Feb 23 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.2.0-14
- (Build)Req: soprano(-devel) >= 2.2
- devel: drop Req: zlib-devel libutempter-devel

* Wed Feb 18 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.2.0-13
- disable strict aliasing in kjs/dtoa.cpp (GCC 4.4 x86_64 crash) (#485968)

* Thu Feb 12 2009 Than Ngo <than@redhat.com> - 4.2.0-11
- make plasma work better with Qt 4.5 (when built against Qt 4.5)
- add gcc44-workaround

* Fri Feb 06 2009 Than Ngo <than@redhat.com> - 4.2.0-10
- Fix duplicated applications in the K menu and in keditfiletype

* Thu Feb 05 2009 Rex Dieter <rdieter@fedoraproject.org> 4.2.0-9
- ssl/proxy patch (kde#179934)

* Sat Jan 31 2009 Rex Dieter <rdieter@fedoraproject.org> 4.2.0-8
- unowned dirs (#483315,#483318)

* Fri Jan 30 2009 Rex Dieter <rdieter@fedoraproject.org> 4.2.0-7
- kded/kdirwatch patch (kde#182472)

* Fri Jan 30 2009 Lukáš Tinkl <ltinkl@redhat.com> 4.2.0-6
- Emit the correct FilesRemoved signal if the job was aborted in the middle of its operation, 
  otherwise it can result in confusion and data loss (overwriting files with files
  that don't exist). kdebug:118593
- Fix "klauncher hangs when kdeinit4 dies" -- this happened because
  klauncher was doing a blocking read forever.
- Repair klauncher support for unique-applications like konsole.
  kdebug:162729, kdebug:75492

* Fri Jan 30 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.2.0-5
- reenable PolicyKit and NTFS workarounds

* Mon Jan 26 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.2.0-4
- revert Requires: qt4%%{_isa}

* Mon Jan 26 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.2.0-3
- respun tarball

* Mon Jan 26 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.2.0-2
- plasma-on-screensaver-security patch
- (Build)Req: automoc4 >= 0.9.88, phonon(-devel) >= 4.3.0
- Requires: strigi-libs >= 0.6.3
- use %%{?_isa} to avoid potential multilib heartbreak

* Thu Jan 22 2009 Than Ngo <than@redhat.com> - 4.2.0-1
- 4.2.0

* Fri Jan 16 2009 Than Ngo <than@redhat.com> - 4.1.96-9
- drop kdelibs-4.1.85-plasma-default-wallpaper.patch, it's not needed
  since new plasma allows to define default wallpaper, new kde-setting
  is required
- backport fix from trunk to allow symlinks in wallpaper theme

* Fri Jan 16 2009 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.1.96-8
- rebuild for new OpenSSL

* Mon Jan 12 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.1.96-7
- Slight speedup to profile.d/kde.sh (#465370)
- (Build)Req: strigi(-devel) >= 0.6.3

* Mon Jan 12 2009 Than Ngo <than@redhat.com> - 4.1.96-6
- fix a crash (appearing in KSMServer)

* Sat Jan 10 2009 Than Ngo <than@redhat.com> - 4.1.96-5
- kdeworkspace cmake files in correct place

* Fri Jan 09 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.1.96-4
- bump min deps (cmake, kde-filesystem, phonon)
- kde.(sh|csh): cleanup QT_PLUGIN_PATH handling (#477095)
- Requires: coreutils grep

* Fri Jan 09 2009 Than Ngo <than@redhat.com> - 4.1.96-3
- BR soprano >= 2.1.64

* Thu Jan 08 2009 Than Ngo <than@redhat.com> - 4.1.96-2
- kdepim cmake files in correct place

* Wed Jan 07 2009 Than Ngo <than@redhat.com> - 4.1.96-1
- 4.2rc1

* Fri Dec 19 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.1.85-6
- add plasma-default-wallpaper libplasma patch from kdebase-workspace-4.1

* Tue Dec 16 2008 Rex Dieter <rdieter@fedoraproject.org> 4.1.85-5
- respun tarball, integrates kde-l10n-systemsettings patch

* Tue Dec 16 2008 Than Ngo <than@redhat.com> - 4.1.85-4
- add missing ENTITY systemsettings in pt, that fixes kde-l10
  build breakage

* Mon Dec 15 2008 Than Ngo <than@redhat.com> - 4.1.85-3
- add missing ENTITY systemsettings in ru/gl/es/pt, that fixes kde-l10
  build breakage
- rename suffix .xxcmake to avoid install .cmake

* Sun Dec 14 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.1.85-2
- tweak parallel_devel patch to get a -L flag for the symlink directory

* Thu Dec 11 2008 Than Ngo <than@redhat.com> -  4.1.85-1
- 4.2beta2

* Tue Dec 09 2008 Lorenzo Villani <lvillani@binaryhelix.net> - 6:4.1.82-2
- rebase parallel devel patch and kde149705 patch

* Mon Dec 08 2008 Lorenzo Villani <lvillani@binaryhelix.net> - 6:4.1.82-1
- 4.1.82

* Tue Nov 25 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.1.80-5
- remove workaround BR on phonon-backend-gstreamer, it's ineffective since
  phonon now explicitly Requires: phonon-backend-xine and the dependency is no
  longer circular anyway
- update parallel_devel patch
- fix minimum strigi version (only 0.5.9 needed)

* Tue Nov 25 2008 Than Ngo <than@redhat.com> 4.1.80-4
- respin

* Thu Nov 20 2008 Rex Dieter <rdieter@fedoraproject.org> 4.1.80-3
- -devel: Provides: plasma-devel

* Thu Nov 20 2008 Than Ngo <than@redhat.com> 4.1.80-2
- merged

* Thu Nov 20 2008 Lorenzo Villani <lvillani@binaryhelix.net> - 6:4.1.80-1
- 4.1.80
- BR strigi 0.60
- BR cmake 2.6
- make install/fast
- rebase policykit patch
- rebase cmake patch
- rebase a couple of patches and drop _default_patch_fuzz 2

* Wed Nov 12 2008 Than Ngo <than@redhat.com> 4.1.3-1
- 4.1.3

* Fri Nov 07 2008 Rex Dieter <rdieter@fedoraproject.org> 4.1.2-6
- backport http_cache_cleaner fix (kdebug:172182)

* Wed Oct 15 2008 Lukáš Tinkl <ltinkl@redhat.com> 4.1.2-5
- backport fix for faulty window resizing (kdebug:172042)

* Mon Oct 13 2008 Than Ngo <than@redhat.com> 4.1.2-4
- backport patch to fix crash kded startup crash

* Wed Oct 08 2008 Than Ngo <than@redhat.com> 4.1.2-3
- backport fix for google maps

* Sun Sep 28 2008 Rex Dieter <rdieter@fedoraproject.org> 4.1.2-2
- make VERBOSE=1
- respin against new(er) kde-filesystem

* Thu Sep 25 2008 Rex Dieter <rdieter@fedoraproject.org> 4.1.2-1
- kde-4.1.2

* Fri Sep 19 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.1.1-12
- make "Stop Animations" work again in Konqueror (KDE 4 regression kde#157789)

* Thu Sep 18 2008 Than Ngo <than@redhat.com> 4.1.1-11
- apply upstream patch to fix the regression
- drop the kdelibs-4.1.1-bz#461725-regression.patch

* Thu Sep 18 2008 Lukáš Tinkl <ltinkl@redhat.com> 4.1.1-10
- Fix file association bug, the global mimeapps.list file had priority
  over the local one.
- khtml scroll crash fix (kdebug:170880)
- Don't eat text when the emoticons were not installed. This fixes
  mail text not being displayed in KMail when kdebase-runtime wasn't
  installed.

* Wed Sep 17 2008 Than Ngo <than@redhat.com> 4.1.1-9
- #461725, revert the patch to fix the regression

* Sat Sep 13 2008 Than Ngo <than@redhat.com> 4.1.1-8
- fix kdelibs-4.1.1-kdeui-widgets-fixes.patch

* Sat Sep 13 2008 Than Ngo <than@redhat.com> 4.1.1-7
- remove redundant FEDORA, use CMAKE_BUILD_TYPE=release
- fix install problem with cmake > 2.5

* Mon Sep 08 2008 Lukáš Tinkl <ltinkl@redhat.com> 4.1.1-6
- fix crashes in plugin selector
- fix problems in various kdeui widgets

* Wed Sep 03 2008 Lukáš Tinkl <ltinkl@redhat.com> 4.1.1-5
- fixed crash on setting cookies on empty domains (like the file
  system), KDE bug #170147
- fix URL navigator focus in file dialogs, KDE bug #169497, #170211

* Tue Sep 02 2008 Than Ngo <than@redhat.com> 4.1.1-4
- apply patch to fix regression in khtml

* Mon Sep 01 2008 Than Ngo <than@redhat.com> 4.1.1-3
- respun

* Fri Aug 29 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.1.1-2
- fix #455130 (kinit crashing in kglobalconfig with no KComponentData) properly
- drop revert-kinit-regression hack (fixes ioslave translations)

* Fri Aug 29 2008 Than Ngo <than@redhat.com> 4.1.1-1
- 4.1.1

* Fri Aug 29 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.1.0-9
- -devel: +Requires: libutempter-devel (cmake wants to link it in)

* Thu Aug 28 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.1.0-8
- rewrite kstandarddirs patch to fix side effects (#459904 (KDEDIRS), #457633)

* Mon Aug 25 2008 Than Ngo <than@redhat.com> 4.1.0-7
- konsole doesn't write to utmp

* Sat Aug 23 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.1.0-6
- don't hide KDE 3 KCMs in kde4-applications.menu, not needed with our
  OnlyShowIn=KDE3 patch and breaks KDE 3 KCMs (kcmshell, apps) in KDE 4 sessions

* Sun Aug 10 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.1.0-5
- fix kcookiejar crash on invalid cookie file from KDE 3 (patch by David Faure)

* Fri Aug 01 2008 Rex Dieter <rdieter@fedoraproject.org> 4.1.0-4
- -devel: Requires: phonon-devel >= 4.2 (helps multilib upgrades)
- konq processes never terminate (kde#167826, rh#457526)

* Wed Jul 30 2008 Rex Dieter <rdieter@fedoraproject.org> 4.1.0-3
- (Build)Requires: soprano(-devel) >= 2.1 (#456827)

* Thu Jul 24 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.1.0-2
- move Sonnet documentation back to the main package
- fix #341751 (Sonnet documentation multilib conflict) properly

* Wed Jul 23 2008 Than Ngo <than@redhat.com> 4.1.0-1
- 4.1.0

* Sun Jul 20 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.99-3
- fix kstandarddirs patch to always append the installed location last, even if
  it is already present earlier in the search path (#456004)

* Sat Jul 19 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.99-2
- use better fedora-buildtype patch from F-9 branch

* Fri Jul 18 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.99-1
- 4.0.99

* Mon Jul 14 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.98-4
- respun tarball

* Sat Jul 12 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.0.98-2
- revert a kinit patch causing an assertion failure in KComponentData (#455130)

* Thu Jul 10 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.98-1
- 4.0.98
- omit proxy patch (fixed upstream)

* Sun Jul 06 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.85-1
- 4.0.85

* Fri Jun 27 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.84-1
- 4.0.84

* Fri Jun 27 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.0.83-3
- fix kstandarddirs patch so /usr/libexec/kde4 is found (#453063)

* Wed Jun 25 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.83-2
- -common: move %{_kde4_docdir}/HTML/en/sonnet/ here (#341751)

* Thu Jun 19 2008 Than Ngo <than@redhat.com> 4.0.83-1
- 4.0.83 (beta2)

* Fri Jun 13 2008 Than Ngo <than@redhat.com> 4.0.82-1
- 4.0.82

* Fri May 30 2008 Than Ngo <than@redhat.com> 4.0.80-2
- fix #447965, order issue in kde path, thanks to Kevin
- backport patch to check html style version

* Mon May 26 2008 Than Ngo <than@redhat.com> 4.0.80-1
- 4.1 beta1

* Sat May 24 2008 Rex Dieter <rdieter@fedoraproject.org> - 4.0.72-8
- revert previous, don't include kde3-compat symlink (here, anyway)

* Fri May 23 2008 Rex Dieter <rdieter@fedoraproejct.org> - 4.0.72-7
- -common: provide %%_datadir/apps/kdeui for kde3 apps (#447965)

* Thu May 22 2008 Rex Dieter <rdieter@fedoraproject.org> - 4.0.72-6
- kstandarddirs hack to search /etc/kde

* Thu May 22 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.0.72-5
- keep libphonon.so in %%{_libdir} for non-KDE apps (#447831)

* Thu May 15 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.0.72-4
- fix proxy support (#443931, kde#155707)
- move %%{_kde4_appsdir}/ksgmltools2/ from -devel to the main package (#446435)

* Tue May 13 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.0.72-3
- drop no longer needed ALSA default device Phonon hack

* Sun May  4 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.0.72-2
- BR new minimum versions of qt4-devel and soprano-devel

* Fri May  2 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> - 4.0.72-1
- update to 4.0.72 (4.1 alpha 1)
- parallel_devel patch ported by Lorenzo Villani <lvillani@binaryhelix.net>
- update file list (Lorenzo Villani)
- drop upstreamed khtml-security, kconfig_sync_crash and klauncher-crash patches
- update xdg-menu (Administration menu) patch

* Tue Apr 22 2008 Lukáš Tinkl <ltinkl@redhat.com> - 4.0.3-7
- fix buffer overflow in KHTML's image loader (KDE advisory 20080426-1,
  #443766: CVE-2008-1670)

* Fri Apr 04 2008 Than Ngo <than@redhat.com> -  4.0.3-6
- apply upstream patch to fix klauncher crash
- fix kconfig_sync_crash patch

* Fri Apr  4 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.3-5
- kconfig_sync_crash patch

* Thu Apr  3 2008 Lukáš Tinkl <ltinkl@redhat.com> 4.0.3-4
- rebuild for the new %%{_kde4_buildtype}

* Mon Mar 31 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.3-3
- patch and update file list for _kde4_libexecdir

* Mon Mar 31 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.3-2
- add Fedora build type (uses -DNDEBUG)

* Fri Mar 28 2008 Than Ngo <than@redhat.com> 4.0.3-1
- 4.0.3
- -apidocs: drop Requires: %%name

* Fri Mar 28 2008 Than Ngo <than@redhat.com> -  4.0.2-13
- add Administration menu, bz#439378

* Thu Mar 27 2008 Than Ngo <than@redhat.com> 4.0.2-12
- bz#428212, adapted Kevin Kofler's workaround for Policykit

* Thu Mar 20 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.2-11
- apidocs subpackage should be noarch (#436579)

* Mon Mar 10 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.2-10
- work around #436725: BR: libtool-ltdl so graphviz gets a valid libltdl

* Mon Mar 10 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.2-9
- fix kdeglobals not being found in profile (e.g. kde-settings) directory

* Fri Mar 07 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.2-8
- touchup KDE_DISTRIBUTION_TEXT
- add Fedora/V-R to KHTML UA string (thanks caillon)

* Thu Mar 06 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.2-7
- exclude apidocs from the main package

* Thu Mar 06 2008 Than Ngo <than@redhat.com> 4.0.2-6
- apply upstream patch to fix issue in KPropertiesDialog

* Thu Mar 06 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.2-5
- also install Doxyfile.global in -common to build kdepimlibs-apidocs against

* Wed Mar 05 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.2-4
- install all .css files in kdelibs-common to build kdepimlibs-apidocs against
- install doxygen.sh as kde4-doxygen.sh in -devel
- build apidocs and put them into an -apidocs subpackage (can be turned off)
- BR doxygen, graphviz and qt4-doc when building apidocs

* Fri Feb 29 2008 Than Ngo <than@redhat.com> 4.0.2-3
- rebuilt

* Fri Feb 29 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.2-2
- drop obsolete kde#149703 patch (fixed upstream by code rewrite)
- drop backports from 4.0.2: objectembed-handling, autostart, kde#771201-khtml

* Thu Feb 28 2008 Than Ngo <than@redhat.com> 4.0.2-1
- 4.0.2

* Wed Feb 27 2008 Lukáš Tinkl <ltinkl@redhat.com> - 4.0.1-8
- add Fedora branding to the package (#434815)

* Mon Feb 25 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.1-7
- -devel: own %%_kde4_libdir/kde4/plugins (thanks wolfy!)

* Tue Feb 19 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.1-6
- fix running KDE 3 apps as filetype viewers from KDE 4 Dolphin

* Mon Feb 18 2008 Rex Dieter <rdieter@fedoraprojectorg> 4.0.1-5
- -devel: include %%_kde4_appsdir/cmake here (#341751)

* Wed Feb 06 2008 Than Ngo <than@redhat.com> 4.0.1-4
- upstream patch to make sure that static widget is always at position 0,0

* Fri Feb 01 2008 Than Ngo <than@redhat.com> 4.0.1-3
- upstream patch to fix a regression in <object><embed> handling
- autostart upstream patch

* Fri Feb 01 2008 Than Ngo <than@redhat.com> 4.0.1-2
- autostart from XDG_CONFIG_DIRS

* Wed Jan 30 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.1-1
- 4.0.1

* Wed Jan 30 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.0-4
- omit openssl patch (f9+ #429846)
- respin (qt4)

* Wed Jan 23 2008 Rex Dieter <rdieter@fedoraproject.org> 4.0.0-3
- openssl patch

* Sat Jan 19 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 4.0.0-2
- patch K3Spell for hunspell support on F9+ (FeatureDictionary, kde#154561)

* Mon Jan 07 2008 Than Ngo <than@redhat.com> 4.0.0-1
- 4.0.0

* Fri Jan 04 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 3.97.0-11
- force Phonon to use the ALSA default device by default

* Wed Jan 02 2008 Kevin Kofler <Kevin@tigcc.ticalc.org> 3.97.0-10
- apply patch by Alex Merry to support FLAC 1.1.3+ in FindFlac.cmake

* Sat Dec 22 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> 3.97.0-9
- drop BR aspell-devel on F9+, use only enchant (FeatureDictionary)

* Tue Dec 18 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> 3.97.0-8
- don't put binaries into kdelibs-common, they drag in kdelibs (#417251)

* Mon Dec 17 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> 3.97.0-7
- split out kdelibs-common on F9+ (shared with KDE 3) (#417251)
- Requires: kdelibs-common (F9+) (#417251)

* Tue Dec 11 2007 Than Ngo <than@redhat.com> 3.97.0-6
- enable subversion again

* Tue Dec 11 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> 3.97.0-5
- rebuild for changed _kde4_includedir

* Thu Dec 06 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 3.97.0-4
- drop Req: kdebase-runtime oxygen-icon-theme (at least for now)

* Thu Dec 06 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 3.97.0-2
- drop BR: subversion temporarily (due to rawhide breakage)

* Wed Dec 05 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 3.97.0-1
- kde-3.97.0

* Tue Dec 04 2007 Than Ngo <than@redhat.com> 3.96.2-4
- rebuilt against new openssl/openldap

* Sat Dec 01 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> 3.96.2-3
- install profile scripts as 644 instead of 755 (Ville Skyttä, #407521)

* Sat Dec 01 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> 3.96.2-2
- BR openssh-clients and subversion (Sebastian Vahl)
- make this the default kdelibs for F9 again

* Tue Nov 29 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 3.96.2-1
- kde-3.96.2

* Tue Nov 27 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 3.96.1-1
- kde-3.96.1

* Tue Nov 20 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 3.96.0-4
- Requires: kdebase-runtime oxygen-icon-theme (where available)

* Mon Nov 19 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 3.96.0-3
- Requires: dbus-x11 (#390851)

* Mon Nov 19 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 3.96.0-2
- -devel: (Build)Requires: libXcomposite-devel libXdamage-devel
   libxkbfile-devel libXpm-devel libXScrnSaver-devel libXtst-devel
   libXv-devel libXxf86misc-devel
- devel: Requires: strigi-devel >= 0.5.7
- (Build)Requires: kde-filesystem >= 4

* Thu Nov 15 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 3.96.0-1
- kde-3.96.0

* Sat Nov 10 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 3.95.2-2
- BR: strigi-devel >= 0.5.7, soprano-devel >= 1.97.1
- License: LGPLv2 (only)

* Fri Nov 09 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 3.95.2-1
- kde-3.95.2

* Tue Nov 06 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 3.95.0-2
- fix parallel_devel patch (typo in KDE4_KPARTS_LIBRARY)

* Sun Nov 04 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 3.95.0-1
- kde-3.95.0 (kde4 dev platform rc1)

* Thu Oct 18 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> 3.94.0-2
- drop optional BR hspell-devel again due to broken x86_64 static library

* Thu Oct 18 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> 3.94.0-1
- update to 3.94.0
- BR soprano-devel >= 1.95.0
- don't rename js to kjs after installation, fixed upstream
- update parallel-devel patch
- drop kde#149704 patch, fixed upstream
- drop colorscheme-hack patch
- backport upstream fix for unversioned kpty library (rev 724528)
- add new BRs hspell-devel and jasper-devel
- 3.94.0 generates some manpages, add them to the file list

* Thu Oct 4 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> 3.93.0-11
- don't make this the default kdelibs on F9 yet
- retry ppc64 build (#300571)

* Fri Sep 21 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> 3.93.0-10
- ExcludeArch: ppc64 (#300571)

* Thu Sep 20 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 3.93.0-9
- -devel: (re)add Requires: bzip2-devel gamin-devel libacl-devel strigi-devel zlib-devel
- update sources
- sync kde4.(sh|csh) changes wrt KDE_IS_PRELINKED w/ devel/ branch

* Fri Sep 14 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> 3.93.0-8
- rename js to kjs because of file conflict (kde#149840)

* Thu Sep 13 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> 3.93.0-7
- actually install kde4.sh and kde4.csh
- sync KDE_IS_PRELINKED setting in kde4.sh and kde4.csh with kdelibs 3
  (workaround for #244065 no longer needed, fixed in 3.93.0)

* Thu Sep 13 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> 3.93.0-6
- set QT_PLUGIN_PATH in kde4.sh and kde4.csh

* Wed Sep 12 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> 3.93.0-5
- fix strange coloring due to incomplete changes to KColorScheme

* Mon Sep 10 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> 3.93.0-4
- use upstream fix (by David Faure) for kde#149704

* Mon Sep 10 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> 3.93.0-3
- fix kde#149703, kde#149704, kde#149705

* Sun Sep 9 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> 3.93.0-2
- remove files which conflict with KDE 3
- rename kconfig_compiler and makekdewidgets to *4
- move devel symlinks to %%{_kde4_libdir}/kde4/devel/
- drop Conflicts: kdelibs-devel

* Sun Sep 9 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> 3.93.0-1
- update to 3.93.0
- drop kde4home patch (no longer applied)
- drop kdeprint soversion conflict patch (fixed upstream)
- remove icon-related code, pics/ is now in kdebase-runtime
- BR strigi-devel >= 0.5.5 due to API changes
- package hicolor presence_* icons which are not in hicolor-icon-theme
- don't list non-existing ksvgtopng in devel binaries (now in kdebase-runtime)

* Tue Aug 14 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 3.92.0-4
- -devel: omit most (hopefully) extraneous Requires:
- use macros.kde4
- -devel: Conflicts: kdelibs-devel (in %%_bindir,%%_libdir)
- License clarification

* Fri Aug 03 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 3.92.0-3
- name kdelibs4, don't mess with %%_prefix (for now)
- move to -devel: checkXML, kconfig_compiler, (make)kdewidgets, ksgmltools2,
  ksvgtopng, kunittestmodrunner
- set KDE_IS_PRELINKED unconditionally (#244065)
- License: LGPLv2
- Requires: shared-mime-info

* Mon Jul 30 2007 Than Ngo <than@redhat.com> 3.92.0-2
- fix conlict with kde3
- add -DSYSCONF_INSTALL_DIR

* Sat Jul 28 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 3.92.0-1
- kde-3.92.0 (kde4-beta1)

* Thu Jul 19 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> 3.91.0-6
- add missing epoch to main package Requires for -devel if name is kdelibs

* Tue Jul 17 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 3.91.0-5
- BR: soprano-devel
- prefix=/usr cleanups

* Wed Jul 11 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> 3.91.0-4
- apply upstream bugfix for KatePart syntax highlighting (kde #145571)

* Thu Jun 29 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 3.91.0-3
- fix %%_sysconfdir for %%_prefix != /usr case.

* Thu Jun 28 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 3.91.0-2
- updated kde4home.diff
- CMAKE_BUILD_TYPE=RelWithDebInfo (we're already using %%optflags)

* Wed Jun 27 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 3.91.0-1
- kde-3.91.0
- CMAKE_BUILD_TYPE=debug

* Sat Jun 23 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 3.90.1-3
- specfile cleanup (%%prefix issues mostly)

* Wed May 30 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> 3.90.1-2
- add missing BR shared-mime-info

* Sun May 13 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> 3.90.1-1
- update to 3.90.1
- drop backported upstream fixes already in 3.90.1
- bump cmake BR to 2.4.5 as required upstream now
- add BR strigi-devel, alsa-lib-devel, avahi-devel
- don't set execute bits by hand anymore, cmake has been fixed
- use multilibs in /opt/kde4

* Mon Mar 26 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> 3.80.3-5
- apply upstream fixes to build with Qt 4.3 Beta

* Sat Mar 24 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> 3.80.3-4
- restore minimum version requirements for cmake and qt4-devel
- drop visibility hack (no longer needed with latest qt4 package)
- don't set QT4DIR and PATH anymore, qdbuscpp2xml has been fixed
- apply upstream bugfixes:
- * khtml segfault fix
- * message box cancel button fix
- * kprocio received buffer truncation fix (backported)
- * KatePart keyboard shortcut (Ctrl+Right, Shift+Right) fix

* Mon Mar 05 2007 Rex Dieter <rdieter[AT]fedoraproject.org> 3.80.3-3
- +eXecute perms for %%{_prefix}/lib/*

* Fri Feb 23 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> 3.80.3-2
- apply upstream patch to fix klauncher crash
- hack around Qt 4 being built with no visibility support
- install Qt Designer plugin

* Wed Feb 21 2007 Kevin Kofler <Kevin@tigcc.ticalc.org> 3.80.3-1
- update to 3.80.3
- update and improve parallel-installability patch
- set QT4DIR and PATH so CMake's direct $QT4DIR/qdbuscpp2xml calls work
- move libkdeinit_*.so from -devel to main package
- symlink kde4-config into /usr/bin so it can be used for path setting

* Wed Nov 29 2006 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> 3.80.2-0.4.20061003svn
- dropped -DCMAKE_SKIP_RPATH=TRUE from cmake
- compiling with QA_RPATHS=0x0003; export QA_RPATHS

* Sun Nov 26 2006 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> 3.80.2-0.3.20061003svn
- Added foolishly dropped libjpeg-devel, zlib-devel, krb5-devel, libattr-devel again as BR

* Thu Nov 23 2006 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> 3.80.2-0.2.20061003svn
- parallel build support
- added -DCMAKE_SKIP_RPATH=TRUE to cmake to skip rpath
- dropped libjpeg-devel, zlib-devel, krb5-devel, libattr-devel as BR
- dropped duplicate libattr-devel in BR
- spec file cleanups and added clean up in %%install
- fixed missing dependency : libkdeinit_knotify.so

* Sat Oct 07 2006 Kevin Kofler <Kevin@tigcc.ticalc.org> 3.80.2-0.1.20061003svn
- first Fedora RPM (parts borrowed from the OpenSUSE kdelibs 4 RPM and the Fedora kdelibs 3 RPM)
- apply parallel-installability patch
