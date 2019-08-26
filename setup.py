import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="extract-codon-alignment",
    version="0.0.1",
    author='Guanliang Meng',
    author_email='linzhi2012@gmail.com',
    description="To extract some codon positions (1st, 2nd, 3rd) from a CDS alignment.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires='>=3',
    url='https://github.com/linzhi2013/extract_codon_alignment',
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=['biopython>=1.54'],

    entry_points={
        'console_scripts': [
            'extract_codon_alignment=extract_codon_alignment.extract_codon_alignment:main',
        ],
    },
    classifiers=(
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
    ),
)
