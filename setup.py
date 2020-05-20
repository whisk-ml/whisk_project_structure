from setuptools import find_packages, setup

setup(
    name='whisk_project_structure',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    version='0.1.0',
    include_package_data=True,
    # By default only whisk is added as a dependency. whisk is required for
    # accessing the artifacts_dir.
    #
    # You likely need to list more dependencies for your model package.
    # For example: your model framework (Scikit, Torch, etc), numpy, Pandas, etc.
    #
    # See https://whisk.readthedocs.io/en/latest/packaging.html for help on packaging your model.
    install_requires=[
        'whisk==0.1.30'
    ],
    entry_points={
        'console_scripts': [
            'whisk_project_structure=whisk_project_structure.cli.main:cli',
        ],
    },
    description='A short description of the project.',
    author='Your name (or your organization/company/team)',
    author_email='you@example.com',
    python_requires='>=3.6',
    url="https://ADD THE URL TO YOUR PROJECT GITHUB REPO OR DOCS"
)
