# Dockerfile for PDPBioGen benchmark smoke image (Python 3.11 + conda env)
FROM continuumio/miniconda3:py311_23.3.1-0

# Install mamba for faster environment creation
RUN conda install -y -n base -c conda-forge mamba && \
    mamba --version

# Copy environment file and create env
COPY environment.yml /tmp/environment.yml
RUN mamba env create -f /tmp/environment.yml -n pdpbiogen

# Make conda env accessible
SHELL ["conda", "run", "-n", "pdpbiogen", "/bin/bash", "-lc"]

# Copy repository into container
WORKDIR /workspace
COPY . /workspace

# Ensure entrypoint script can be executed
RUN chmod +x /workspace/benchmarks/scripts/run_all_benchmarks.py || true

# Default command: nothing (Nextflow will invoke container processes). Provide helpful entrypoint
ENTRYPOINT [ "conda", "run", "-n", "pdpbiogen", "bash", "-lc" ]
CMD [ "echo \"Container built. Run your tests (e.g. pytest ...) or run Nextflow with -profile docker.\" && bash" ]
