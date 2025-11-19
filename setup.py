from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get long description from README
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="pdpbiogen",
    version="0.1.0",
    description="Programmatic Diagram Pathway Biologist Generator - Automated biological pathway visualization",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tlcagford/PDPBioGen",
    author="tlcagford",
    author_email="YOUR_EMAIL@example.com",  # Update this
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Topic :: Scientific/Engineering :: Visualization",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    keywords="bioinformatics, biology, pathway, visualization, graphviz",
    packages=find_packages(),
    python_requires=">=3.7, <4",
    install_requires=["pyyaml>=5.1", "graphviz>=0.14"],
    entry_points={
        "console_scripts": [
            "pdpbiogen=pdpbiogen.cli:main",
        ],
    },
    project_urls={
        "Bug Reports": "https://github.com/tlcagford/PDPBioGen/issues",
        "Source": "https://github.com/tlcagford/PDPBioGen",
    },
)
