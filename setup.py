import platform
import setuptools
import sys

with open("README.md", "r") as fh:
    at_top = True
    long_description = ''
    for line in fh:
        if at_top and line[:3] == '[![':
            pass                # Skipping the badge-lines in the github README.md
        else:
            at_top = False      # Now starts the "real" README.md
        long_description += line


with open('robinson_foulds/version.py') as fh:
    exec(fh.read())

if sys.version_info.major < 3:
    sys.exit('\n'
             'Sorry, Python 2 is not supported\n'
             'Did you run pip install robinson_foulds?\n'
             'Try \'pip3 install robinson_foulds\'')

elif sys.version_info.minor < 2:
    sys.exit('\nSorry, Python < 3.2 is not supported\n')

requirements = [
    'ete3',
]

setuptools.setup(
    name="robinson_foulds",
    version=__version__,
    author="Lars Arvestad",
    author_email="arve@math.su.se",
    description="A simple utility for comparing phylogenetic trees",
    scripts = ['bin/rf'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/arvestad/robinson_foulds",
#    test_suite = "tests",
    packages=setuptools.find_packages(),
    python_requires='>=3',
    install_requires=requirements,
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
    ),
)
