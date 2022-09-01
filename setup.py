import setuptools

setuptools.setup(
    name="mhp",
    version="0.1.0",
    url="https://github.com/scohenjanes5/MHP",
    author="Sander Cohen-Janes",
    author_email="scohenjanes@brandeis.edu",
    description="Facilitates solubility calculations on a wide range of polymers.",
    long_description=open('README.md').read(),
    packages=setuptools.find_packages(),
    install_requires=["rdkit", "argparse", "scipy", "pandas"],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
    ],
    entry_points={
        'console_scripts': [ #this section allows us to use functions from the command line. Arguments are ok because main() uses argparse
            # 'command = package.module:function',
            'makePol = mhp.MakePolymer:main',
            'customPol = mhp.custom_input_to_mol_file:main',
            'randomPol = mhp.random_polymer_to_mol_file:main',
        ],
    },
)