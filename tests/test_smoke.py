def test_package_importable():
    """
    Simple smoke test to ensure the main package imports.
    Adapt the import name to your actual package module (pdpbiogen, pdp_biogen, etc.)
    """
    import importlib
    names = ["pdpbiogen", "pdp_biogen", "PDPBioGen"]
    found = False
    for name in names:
        try:
            importlib.import_module(name)
            found = True
            break
        except Exception:
            continue
    assert found, "Could not import PDPBioGen package — adjust test to your package name"

def test_import_core():
    # smoke test to ensure package imports and a fundamental function exists
    import importlib
    mod = importlib.import_module("pdpbiogen")  # adapt to actual package name
    assert hasattr(mod, "ResearchFramework") or hasattr(mod, "main"), \
        "package should expose ResearchFramework or main entrypoint"
import importlib

def test_import_core():
    mod = importlib.import_module("pdpbiogen")
    assert hasattr(mod, "__version__")
