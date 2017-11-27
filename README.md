RPMBUILD for cfssl
=========================

cfssl rpm

How to Build
=========
    git clone https://github.com/allanhung/rpm_cfssl
    cd rpm_cfssl
    docker run --name=cfssl_build --rm -ti -v $(pwd)/rpms:/root/rpmbuild/RPMS/x86_64 -v $(pwd)/rpms:/root/rpmbuild/RPMS/noarch -v $(pwd)/scripts:/usr/local/src/build centos /bin/bash -c "/usr/local/src/build/build_cfssl.sh 1.2.0"

# check
    docker run --name=cfssl_check --rm -ti -v $(pwd)/rpms:/root/rpmbuild/RPMS centos /bin/bash -c "yum localinstall -y /root/rpmbuild/RPMS/cfssl-*.rpm"
