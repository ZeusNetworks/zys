from setuptools import setup


with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name="zyspy",
    version="0.4",
    description="zeus API wrapper",
    py_modules=["zyspy"],
    package_dir={'': 'zeus'},
    install_requires=["requests", "typing"],
    extras_require={
                      "dev":[
                          "pytest",
                      ],},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.9.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.10.1",
        "Operating System :: OS Independent",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ZeusNetworks/Zys-Py",
    author="ZeusNetworks"

)
