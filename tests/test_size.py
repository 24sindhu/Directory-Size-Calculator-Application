from data.seed_data import build_sample_filesystem

def test_directory_size():
    root = build_sample_filesystem()
    assert root.get_size() == 1100