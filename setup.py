from setuptools import setup, find_packages


setup(
    name="django-nps",
    version='0.0.2',
    description=(
        "Model, Tests, and API for collecting promoter "
        "score from users."
    ),
    author="Austin Brennan",
    author_email="ab@epantry.com",
    url="https://github.com/epantry/django-netpromoterscore",
    keywords=["promoter score", "net promoter score", "django"],
    install_requires=[],
    packages=find_packages(),
    include_package_data=True,
)