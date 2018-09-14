from setuptools import setup, find_packages

# Get the contents of redme file as log_description
with open("README.md", "r") as readme:
    long_description = readme.read()

setup(
    name="pynum-translator",
    version="0.0.2",
    author="Subhendu Ranjan Mishra",
    author_email="subhendu.r.mishra@gmail.com",
    description="A python library for translating numbers to numeric representation in another language.",
    long_description=long_description,
    license="MIT",
    long_description_content_type="text/markdown",
    url="https://github.com/subhrm/pynum-translator",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3",
    keywords="number translation hindi oriya odia indic"
)
