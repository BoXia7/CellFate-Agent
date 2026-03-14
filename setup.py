from setuptools import setup, find_packages

setup(
    name='cellfate_agent',
    version='0.1.0',
    author='Bo Xia',
    description='Autonomous in silico cell fate engineering agent',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    python_requires='>=3.10',
    install_requires=[
        'torch>=2.0.0',
        'transformers>=4.40.0',
        'biopython>=1.80',
        'numpy>=1.25',
        'pandas>=2.0',
    ],
    classifiers=[
        'Programming Language :: Python :: 3.10',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
