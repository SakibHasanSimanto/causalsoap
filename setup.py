from setuptools import setup, find_packages

setup(
    name='deepCausal',
    version='0.1.0',
    author='Kazi Sakib Hasan',
    author_email='simanto.alt@gmail.com',
    description='A causal feature selection library using residual-based ATE estimation.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/SakibHasanSimanto/deepCausal',  
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'scikit-learn'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)
