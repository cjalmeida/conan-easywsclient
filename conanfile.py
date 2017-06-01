from conans import ConanFile, CMake, tools, RunEnvironment
import os


class EasywsclientConan(ConanFile):
    name = "easywsclient"
    version = "aa93a71"
    license = "MIT"
    url = "https://github.com/cjalmeida/conan-easywsclient"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = ["txt"]

    def source(self):
        ghash = 'aa93a7193112307eb8aa6cab8f8d91ccf8cf1956'
        url = 'https://github.com/dhbaird/easywsclient/archive/%s.zip' % ghash
        tools.download(url, './source.zip')
        tools.unzip('./source.zip')
        os.remove('./source.zip')
        os.rename('easywsclient-%s' % ghash, 'source')

    def build(self):
        run_env = RunEnvironment(self)
        with tools.environment_append(run_env.vars):
            self.run('cd source && g++ -c easywsclient.cpp && ar rvs libeasywsclient.a easywsclient.o')

    def package(self):
        self.copy("*.h", dst="include", src="source")
        self.copy("*.a", dst="lib", src="source")

    def package_info(self):
        self.cpp_info.libs = ["easywsclient"]
