# setup.py
from setuptools import setup, find_packages

setup(
    name='project_utils',            # Your package name (can be anything)
    version='0.1',
    package_dir={'': 'src'},           # Tell setuptools your packages are under src/
    packages=find_packages(where='src'),  # Find all packages under src/
    install_requires=[                 # Your dependencies
        'pandas',
        'numpy',
        'scikit-learn',
        'seaborn',
        'missingno',
        'category_encoders',
        'pyjanitor',
        'scipy',
        'feature-engine',
        'fuzzywuzzy'
    ],
)

