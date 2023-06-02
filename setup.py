import setuptools
import numpy

cpp_args = ['-std=c++11']

numpy_includes = numpy.get_include()

sarw_spheres = setuptools.Extension(
    "sarw_spheres",
    sources=["sarw_spheres.cpp"],
    language="c++",
    extra_compile_args=cpp_args,
    include_dirs=[numpy_includes]
)

with open('README.md') as f:
    long_description = f.read()

setuptools.setup(
    name="sarw_spheres",
    version="0.0.8",

    url='https://github.com/RadostW/sarw_spheres',
    author='Radost Waszkiewicz',
    author_email='radost.waszkiewicz@gmail.com',
    long_description=long_description,
    long_description_content_type='text/markdown',  # This is important!
    project_urls = {
      'Documentation': 'https://github.com/RadostW/sarw_spheres',
      'Source': 'https://github.com/RadostW/sarw_spheres'
    },
    license='MIT',

    description="Genrate self avoiding random walks (SARW) for spheres of given sizes.",
    ext_modules=[sarw_spheres],
    install_requires=['numpy>1.16'],
    include_dirs=[numpy_includes],
)
