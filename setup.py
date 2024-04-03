from setuptools import setup, find_packages

setup(
    name='enum_with_dict',
    version='0.2.1',
    packages=find_packages(),
    author='Jeremy Harris',
    author_email='jeremy.harris@zenosmosis.com',
    description='Enum with to_dict method.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/jzombie/enum_with_dict',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
    keywords='enum python utilities enum-to-dict enum-with-dict',
)
