from toolchain import CythonRecipe


class ZopeInterfaceRecipe(CythonRecipe):
    name = "zope"
    version = "4.3.2"
    url = 'https://pypi.python.org/packages/44/af/cea1e18bc0d3be0e0824762d3236f0e61088eeed75287e7b854d65ec9916/zope.interface-{version}.tar.gz'
    depends = ["python", "host_setuptools"]
    cythonize = False


recipe = ZopeInterfaceRecipe()

