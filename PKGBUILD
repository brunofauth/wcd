# Maintainer: Bruno Fauth <bvfauth@hotmail.com>

_name=wcd
pkgname="python-$_name"
pkgver='0.1.0'
pkgrel=1
pkgdesc="'Wallpaper changing daemon' is exactly what its name suggests. It tries to be the 'mpd' of wallpapers."
arch=('any')
url="https://github.com/brunofauth/wcd"
license=("MIT")

depends=('python' 'python-coloredlogs' 'python-yaml')
makedepends=(python-build python-installer python-wheel)

source=("https://files.pythonhosted.org/packages/source/${_name::1}/$_name/$_name-$pkgver.tar.gz")
sha256sums=('a092794fe51b1742e3ae9d02897faafae01e95c8f06ab9b81314609511af4132')


build() {
    cd "$_name-$pkgver"
    python setup.py build
}


package() {
    cd "$_name-$pkgver"
    python setup.py install --skip-build --root="$pkgdir" --optimize=1
}

