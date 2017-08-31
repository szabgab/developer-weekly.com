from setuptools import setup

setup(
    name='dw',
    packages=['dw'],
    include_package_data=True,
    install_requires=[
        'flask',
        'jinja2',
        'pyquery',
        'requests', # needed by bin/check_site.py
    ],
    tests_require=[
        'pytest',
    ],
)

# vim: expandtab
