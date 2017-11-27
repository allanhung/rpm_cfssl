CFSSLVER=${1:-'1.2.0'}
RPMVER="${CFSSLVER/-/_}"
export RPMBUILDROOT=/root/rpmbuild
export GOPATH=/usr/share/gocode
export PATH=$GOPATH/bin:$PATH

# go repo
rpm --import https://mirror.go-repo.io/centos/RPM-GPG-KEY-GO-REPO
curl -s https://mirror.go-repo.io/centos/go-repo.repo | tee /etc/yum.repos.d/go-repo.repo
# epel
yum install -y epel-release
yum -y install golang git bzip2 rpm-build
mkdir -p $RPMBUILDROOT/SOURCES && mkdir -p $RPMBUILDROOT/SPECS && mkdir -p $RPMBUILDROOT/SRPMS
# fix rpm marcos
sed -i -e "s#.centos##g" /etc/rpm/macros.dist

# get cfssl
go get -u github.com/cloudflare/cfssl/cmd/cfssl-bundle
go get -u github.com/cloudflare/cfssl/cmd/cfssl-certinfo
go get -u github.com/cloudflare/cfssl/cmd/cfssl-newkey
go get -u github.com/cloudflare/cfssl/cmd/cfssl-scan
go get -u github.com/cloudflare/cfssl/cmd/cfssl
go get -u github.com/cloudflare/cfssl/cmd/cfssljson
go get -u github.com/cloudflare/cfssl/cmd/mkbundle
go get -u github.com/cloudflare/cfssl/cmd/multirootca

# build rpm
sed -e "s/^Version:.*/Version: $RPMVER/g" /usr/local/src/build/cfssl.spec > $RPMBUILDROOT/SPECS/cfssl.spec
rpmbuild -bb $RPMBUILDROOT/SPECS/cfssl.spec
