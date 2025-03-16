from setuptools import setup, find_packages


# from setuptools import setup, find_packages

# with open("README.md", "r", encoding="utf-8") as f:
#     long_description = f.read()



setup(
    name='datrix',              # Your package name (should be unique on PyPI)
    version='1.1.0',                       # Package version
    packages=find_packages(),              # Automatically find all packages
    install_requires=[
        'faker',
        'pandas',
        'flask'
    ],                                     # Dependencies your package needs
    author='Saad Ur Rehman',
    author_email='saadurr30@gmail.com', # Your email address
    description='A library to generate realistic dummy datasets.',
    # long_description=open('README.md').read(),
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/dataset-generator', # Your project URL (GitHub recommended)
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',              # Minimum Python version requirement
)
