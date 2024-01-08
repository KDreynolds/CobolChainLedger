from setuptools import setup, find_packages

setup(
    name='COBOL-Python Blockchain Ledger',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A COBOL financial transaction ledger with an attached Python blockchain for immutable record keeping and auditing.',
    packages=find_packages(),
    install_requires=[
        # Add your project dependencies here
        # For example, if you're using a specific version of hashlib, you would specify it like so:
        # 'hashlib==1.0.0'
        # However, hashlib is a built-in Python module, so it does not need to be specified.
        # If there are other dependencies, list them below, for example:
        # 'requests',
        # 'flask',
    ],
    entry_points={
        'console_scripts': [
            # If you have any scripts that should be accessible from the command line,
            # you can list them here. For example:
            # 'run_ledger=ledger_interface:main',
        ],
    },
    include_package_data=True,
    keywords='blockchain ledger cobol python',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Financial and Insurance Industry',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3',
        'Programming Language :: COBOL',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    # If there are data files included in your packages that need to be installed, specify them here. For example:
    # package_data={
    #     'sample': ['package_data.dat'],
    # },
    # If there are data files outside your packages that need to be included, specify them here. For example:
    # data_files=[('my_data', ['data/data_file'])],
    # If your project is meant to be zipped and uploaded to PyPI, set this to True:
    # zip_safe=False,
)
