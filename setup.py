from setuptools import setup, find_packages

setup(
    name="hwplib",
    version="0.1.0",
    description="A library for parsing and handling HWP files.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Do-woon(Do-Un) Kim",
    url="https://github.com/Do-woon/python-hwplib",
    license="Apache License 2.0",
    packages=find_packages(),
    install_requires=[
        "olefile>=0.46",
    ],
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    zip_safe=False,
)