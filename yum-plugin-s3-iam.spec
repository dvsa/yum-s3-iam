Name:      %{name}
Version:   %{version}
Release:   %{release}
Summary:   Yum package manager plugin for private S3 repositories.

Group:     Application/SystemTools
License:   Apache License Version 2.0
URL:       https://github.com/dvsa/yum-s3-iam
Source0:   %{name}-%{version}.tar.gz

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch

Requires:  yum

%description
Yum package manager plugin for private S3 repositories.
Uses Amazon IAM & EC2 Roles.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=%{buildroot}

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root,-)
%doc s3iam.repo
%doc LICENSE NOTICE README.md
%config /etc/yum/pluginconf.d/s3iam.conf
/usr/lib/yum-plugins/s3iam.py*

%changelog
* Mon July 22 2019 Ian Christian <ian.christian@bjss.com> 1.3.3-1
- Adding in retries in case of IO exceptions when connecting to s3

* Tue Feb 05 2019 Callum Massey <callum.massey@bjss.com> 1.3.2-1
- Fix timeout when running on non-windows connecting to http://169.254.169.254/

* Mon Jan 29 2019 Callum Massey <callum.massey@bjss.com> 1.3.1-1
- Fix test cases

* Mon Jan 28 2019 Callum Massey <callum.massey@bjss.com> 1.3.0-1
- Don't retry 404 errors 

* Tue Aug 28 2018 Piotr Kasperski <piotrkas@kainso.com>
- Added https://github.com/seporaitis/yum-s3-iam/pull/64

* Fri May 05 2017 Mathias Brossard <mathias@brossard.org> 1.2.2-1
- Handle special value '__none__' for proxy (@andlam)

* Fri May 05 2017 Mathias Brossard <mathias@brossard.org> 1.2.1-1
- Add support for proxy (@AgarFu)

* Fri May 05 2017 Mathias Brossard <mathias@brossard.org> 1.2.0-1
- Improvements for running outside of EC2 (@mbrossard)
- Fix for cross-region STS authentication (@jonnangle)
- Fix for regression on 'us-east-1' (@mestudd, @mbrossard)

* Tue Feb 21 2017 Mathias Brossard <mathias@brossard.org> 1.1.2-1
- Fix for no-region regression introduced by cn-north-1 region support
  (@mbrossard)

* Thu Feb 16 2017 Mathias Brossard <mathias@brossard.org> 1.1.1-1
- Add support for cn-north-1 region (@mbrossard)

* Wed Jul 11 2016 Mathias Brossard <mathias@brossard.org> 1.1.0-1
- Add support for AWS v4 signature (@mbrossard)
- Add support for s3:// scheme (@asedge, @mbrossard)
- Add retries with exponential back-off (@bemehow, @mbrossard)

* Tue Jul 05 2016 Mathias Brossard <mathias@brossard.org> 1.0.3-1
- Add support for delegated roles (@ToneD)

* Tue Nov 03 2015 Mathias Brossard <mathias@brossard.org> 1.0.2-1
- Fix for trailing line-feed on signature on newer python 2.7 (@mbrossard)

* Fri May 31 2013 Matt Jamison <matt@mattjamison.com> 1.0-1
- Initial packaging
