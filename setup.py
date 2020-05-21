import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django_jsform",
    version="0.0.0",
    author="Alex Fischer",
    author_email="alex@quadrant.net",
    description="Django integration for jsform",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # url="TODO - github repo",
    # TODO - be sure to include static files
    packages=['django_jsform'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=["Django>=2.2,<3.1"],
    include_package_data=True,
)