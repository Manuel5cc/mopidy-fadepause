from setuptools import setup, find_packages

setup(
    name='Mopidy-FadePause',
    version='0.1.0',
    url='https://github.com/Manuel5cc/mopidy-fadepause',
    license='Apache License 2.0',
    author='Manuel M',
    author_email='tucorreo@example.com',
    description='Un plugin de Mopidy que hace fade out al pausar.',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Mopidy >= 3.0',
        'Pykka >= 2.0',
    ],
    entry_points={
        'mopidy.ext': [
            'fadepause = mopidy_fadepause:Extension',
        ],
    },
)
