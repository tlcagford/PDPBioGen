#!/usr/bin/env nextflow

/*
 Minimal Nextflow pipeline to run PDPBioGen smoke-test steps inside the Docker container.
 Outputs a reproducibility manifest (JSON) with SHA256 hashes of produced artifacts.
*/

params.outdir = params.outdir ?: 'results'
params.container = params.container ?: 'pdpbiogen/bench:smoke'   // image name to build locally

process PREPROCESS_BCI {
    container params.container
    publishDir "${params.outdir}/bci", mode: 'copy'

    output:
    file('*') into bci_out

    script:
    """
    echo "Running BCI smoke tests..."
    # run the bench runner (this script triggers the small test subset)
    python benchmarks/bci/bench_smoke.py || (echo "BCI smoke tests failed" >&2; exit 1)
    # Collect produced artifacts (if any) into output dir
    mkdir -p ${params.outdir}/bci
    # If bench writes artifacts (tmp), move them (this is illustrative)
    cp -r benchmarks/bci/sample_data ${params.outdir}/bci/ || true
    ls -la ${params.outdir}/bci || true
    """
}

process LOAD_OMICS {
    container params.container
    publishDir "${params.outdir}/omics", mode: 'copy'

    output:
    file('*') into omics_out

    script:
    """
    echo "Running Omics smoke tests..."
    python benchmarks/omics/bench_smoke.py || (echo "Omics smoke tests failed" >&2; exit 1)
    mkdir -p ${params.outdir}/omics
    cp -r benchmarks/omics/sample_data ${params.outdir}/omics/ || true
    ls -la ${params.outdir}/omics || true
    """
}

process RUN_AGENTS {
    container params.container
    publishDir "${params.outdir}/agents", mode: 'copy'

    output:
    file('*') into agents_out

    script:
    """
    echo "Running Agent smoke tests..."
    python benchmarks/agents/bench_smoke.py || (echo "Agent smoke tests failed" >&2; exit 1)
    mkdir -p ${params.outdir}/agents
    cp -r benchmarks/agents ${params.outdir}/agents/ || true
    ls -la ${params.outdir}/agents || true
    """
}

process EVAL_HASHES {
    container params.container
    publishDir "${params.outdir}/manifest", mode: 'copy'

    input:
    val dummy from agents_out.collect()

    output:
    file('manifest.json') into manifest_out

    script:
    """
    echo "Computing SHA256 hashes for produced artifacts..."
    python - <<PY
import os, json, hashlib
root = '${params.outdir}'
manifest = {}
def sha256_file(path):
    h = hashlib.sha256()
    with open(path,'rb') as f:
        for b in iter(lambda: f.read(8192), b''):
            h.update(b)
    return h.hexdigest()

for sub in ('bci','omics','agents'):
    d = os.path.join(root, sub)
    if not os.path.exists(d):
        continue
    manifest[sub] = {}
    for dirpath, _, filenames in os.walk(d):
        for fn in filenames:
            p = os.path.join(dirpath, fn)
            try:
                manifest[sub][os.path.relpath(p, root)] = sha256_file(p)
            except Exception as e:
                manifest[sub][os.path.relpath(p, root)] = "ERROR: " + str(e)

manifest['pipeline'] = {'nextflow_run_id': os.environ.get('NXF_EXECUTOR', 'local')}
with open('manifest.json','w') as fh:
    json.dump(manifest, fh, indent=2)
print('Wrote manifest.json')
PY
    """
}

workflow {
    PREPROCESS_BCI()
    LOAD_OMICS()
    RUN_AGENTS()
    EVAL_HASHES()
}
