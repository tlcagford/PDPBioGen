from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="neuro-symmetry-mapper",
    version="0.1.0",
    author="TL Cagford",
    author_email="your-email@example.com",
    description="A verified multi-agent framework for multi-scale human biological integration",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tlcagford/neuro-symmetry-mapper",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "nsm-download=neuro_symmetry_mapper.data.downloaders.triple_downloader:main",
            "nsm-map=neuro_symmetry_mapper.integration.cross_domain_integrator:main",
            "nsm-visualize=neuro_symmetry_mapper.integration.visualization:main",
        ],
    },
    include_package_data=True,
    package_data={
        "neuro_symmetry_mapper": ["config/*.yaml", "data/unified_ontology/*.json"],
    },
)