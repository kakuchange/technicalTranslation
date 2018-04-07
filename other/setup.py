from setuptools import (find_packages,
                        setup)

setup(
    name='dc_voicedispath',
    version='2.0.0',
    packages=find_packages('src'),
    package_dir={
        '': 'src',
    },
    url='',
    author='kaku',
    description='voice dispatch',
    package_data={
        '': ['*.pkl'],
    },
    install_requires=[
        'grpcio',
        'tensorflow==1.4.1',
    ],
    entry_points={
        'console_scripts': [
            'test_script=package_a.module_a:function_a',
        ],
    }
)
