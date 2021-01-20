import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="alxdembo-vtx",
    version="0.0.1",
    author="Alex Dembo",
    author_email="a@dembo.lv",
    description="Extracts cargo movement durations.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alxdembo/vtx",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'pandas==1.2.0'
    ]
)
