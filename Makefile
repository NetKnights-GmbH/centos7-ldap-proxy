LP_VERSION=2.0
info:
	@echo "buildrpm"
	@echo "repo"
	@echo "clean"

buildrpm:
	LP_VERSION=${LP_VERSION} rpmbuild -ba SPECS/privacyidea-ldap-proxy.spec

repo:
	mkdir -p repository/centos/7/
	cp -r RPMS/* repository/centos/7/
	# Fetch old packages
	(cd repository; rsync -vr root@lancelot:/srv/www/rpmrepo/ centos)
	(cd repository/centos/7/x86_64/; createrepo .)
	(cd repository/centos/7/noarch/; createrepo .)
	(cd repository;	rsync -vr centos root@lancelot:/srv/www/rpmrepo/)

clean:
	rm -fr repository
	rm -fr BUILD/*
	rm -fr RPMS/*
	rm -fr SRPMS/*
