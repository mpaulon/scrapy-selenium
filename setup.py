import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="scrapy-selenium",
    version="0.0.10",
    description="SCrapy with selenium",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mpaulon/scrapy-selenium",
    packages=setuptools.find_packages(),
    install_requires=[
        "scrapy>=1.0.0",
        "selenium>=3.9.0",
    ],
    python_requires='>=3.6',
)
