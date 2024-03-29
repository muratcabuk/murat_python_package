Bu paket şu işe yarar şunları yapar vs vs gibi birşeyler tazması gerkiyor ancak biz paket kurulum örneği yaptığımız için bununla ilgili detayları pyalaşıyoruz.


aslında setup.cfg doyası kullanılmasa  da olur. biz sadece bu da var demek için ekledik. setup.py ile wheel python2 ve 3 için  zaten eskiye uyumluluk problemini çözüyor.

CLI uygulaması geliştirmek için click paketi kullanıldı. Amaç sadece ornek yapmak.


- **twine**: pypi sitesine daha doğrusun api sine bağlanmak ve paketlerimizi deploy etmek için gerekli
- **wheel** : Python Wheel, Python için standart kabul edilen paket dağıtım formatıdır. Wheel özel olarak biçimlendirilmiş (formatlanmış) bir dosya adı ve .whl uzantılı ZIP biçiminde bir arşiv dosyasıdır. Python'un egg formatı yerine getirilmiş ihtiyaç duyulan tüm Python içeriklerinin bir arada bulunmasını sağlayan bir arşiv dosyasıdır. Bu yazının yazıldığı tarih itibariyle PyPI yazılım deposunda en çok indirilen 360 paketten 263'ü wheel formatındadır. pip komutu ya source distribution (sdist) ya da wheel kurulumu yapmaktadır. Eğer PyPI yazılım deposunda her ikisi de mevcutsa pip, wheel formatındaki paketi kullanarak kurulum yapmayı tercih etmektedir. Source distribution (sdist) ile kıyaslandığında wheel ile daha hızlı kurulum yapılmaktadır. Wheel (.whl uzantılı) dosyayı aşağıdaki komutu çalıştırarak bilgisayarınıza kurabilirsiniz.

```
pip install paket_adi.whl
```

If you have a pure Python package that is not using 2to3 for Python 3 support, you've got it easy. Make sure Wheel is installed…
```
pip install wheel
```
…and when you'd normally run python setup.py sdist, run instead python setup.py sdist bdist_wheel. For a more in-depth explanation, see this guide on sharing your labor of love.

Note: If your project is Python 2 and 3 compatible you can create a universal wheel distribution. Create a file called setup.cfg with the following content and upload your package.
```conf
[bdist_wheel]
universal = 1
```
- toml : https://www.python.org/dev/peps/pep-0621/

projenin paket haline getirilirken ihtiyacı olan bağımlılıkları için konulur. tam olarka sektorde oturmamış olsa da bir çok bilinen paket de bu doya kullanılır örneğin django. https://packaging.python.org/tutorials/packaging-projects/#creating-the-package-files

pyproject.toml adında bir dosya oluşturulur 

```toml
[build-system]
requires = [
    "setuptools>=42",
    "wheel"
]
build-backend = "setuptools.build_meta"
```
**build-system.requires** gives a list of packages that are needed to build your package. Listing something here will only make it available during the build, not after it is installed.

**build-system.build-backend** is the name of Python object that will be used to perform the build. If you were to use a different build system, such as flit or poetry, those would go here, and the configuration details would be completely different than the setuptools configuration described below.

## Build ve publish

```
python3 setup.py sdist bdist_wheel

# paketimiz hazır şimdi paketimizi doğrulayalım
twine check dist/*
#Checking dist/murat_python_package-0.0.1-py2.py3-none-any.whl: PASSED
#Checking dist/murat_python_package-0.0.1.tar.gz: PASSED

# upload için doğrulama. pupi.org domaini değl test.pypi.org sitesine ayrıca üye olmak gerekiyor.
twine upload -r testpypi dist/*
# eğer buraya publish yapabildiyseniz artık gerçek yere publish yapılabilir


twine upload dist/*
```


**bazı kaynaklar:**
- https://towardsdatascience.com/create-your-own-python-package-and-publish-it-into-pypi-9306a29bc116
- https://towardsdatascience.com/how-to-effortlessly-publish-your-python-package-to-pypi-using-poetry-44b305362f9f
- https://packaging.python.org/
- https://packaging.python.org/specifications/
- https://packaging.python.org/tutorials/packaging-projects/
- https://docs.python.org/3/distutils/setupscript.html
- https://realpython.com/pypi-publish-python-package/
- https://towardsdatascience.com/whats-init-for-me-d70a312da583
- https://packaging.python.org/guides/packaging-namespace-packages/
- https://docs.python.org/3/reference/import.html
- http://yapayzekalabs.blogspot.com/2018/08/python-wheels-nedir.html
- https://hynek.me/articles/sharing-your-labor-of-love-pypi-quick-and-dirty/
- https://packaging.python.org/guides/using-testpypi/



