%define	name	plasma-applet-eventlist
%define	srcname	plasmoid-eventlist
%define	version	 0.2.90
%define	release	%mkrel 1
%define	Summary	 This plasmoid show upcoming events from akonadi ressources

Summary:	%Summary
Name:		%name
Version:	%version
Release:	%release
Source0:	http://kde-look.org/CONTENT/content-files/107779-%srcname-%version.tar.bz2
License:	GPLv2
Group:		Graphical desktop/KDE
URL:		http://kde-look.org/content/show.php/Eventlist?content=107779
BuildRequires:	kdebase4-workspace-devel
BuildRequires:	kdepimlibs4-devel
Provides:	plasma-applet

%description
This is a plasmoid to show the events from Akonadi resources (KOrganizer,
Birthdays etc.).
With the googledata resource also Google calendar items can be shown.

%files  -f eventapplet.lang
%defattr(-,root,root)
%_kde_libdir/kde4/plasma_applet_events.so
%_kde_services/plasma-applet-events.desktop


#------------------------------------------------------------------------------

%prep
%setup -q -n %srcname-%version 

%build
%cmake_kde4
%make

%install
%__rm -rf %buildroot
%makeinstall_std -C build

%find_lang eventapplet

%clean
%__rm -rf %buildroot


%changelog
* Sat Jul 31 2010 John Balcaen <mikala@mandriva.org> 0.2.90-1mdv2011.0
+ Revision: 563826
- Update to 0.2.90
- fix %%files list

* Mon Mar 22 2010 John Balcaen <mikala@mandriva.org> 0.2.4-1mdv2010.1
+ Revision: 526295
- import plasma-applet-eventlist


