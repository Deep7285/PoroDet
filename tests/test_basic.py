import porodet

# Test the package import
def test_package_import():
    assert porodet.__name__ == "porodet"

# Test the package version
def test_version_exists():
    assert hasattr(porodet, "__version__")