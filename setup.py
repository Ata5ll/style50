if __import__("os").name == "nt":
    raise RuntimeError("style50 does not support Windows directly. Instead, you should install the Windows Subsystem for Linux (https://docs.microsoft.com/en-us/windows/wsl/install-win10) and then install style50 within that.")

from setuptools import find_packages, setup

setup(
    author="CS50",
    author_email="sysadmins@cs50.harvard.edu",
    classifiers=[
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
        "Topic :: Education",
        "Topic :: Utilities"
    ],
    description="This is style50, with which code can be checked against the CS50 style guide",
    long_description=open("README.md").read(),
    install_requires=["argparse", "autopep8>=1.4.3", "icdiff", "jsbeautifier", "python-magic", "termcolor", "jinja2>=2.10"],
    dependency_links=["git+https://github.com/jeffkaufman/icdiff.git"],
    keywords=["style", "style50"],
    name="style50",
    py_requires=">=3.6",
    license="GPLv3",
    packages=["style50", "style50.renderer"],
    entry_points={
        "console_scripts": ["style50=style50.__main__:main"],
    },
    url="https://github.com/cs50/style50",
    version="2.7.5",
    include_package_data=True,
)
