from database import add_item, get_all_items

def test_add_item():
    add_item("Sample")
    items = get_all_items()
    assert len(items) > 0

def test_item_structure():
    items = get_all_items()
    if items:
        assert "id" in items[0]
        assert "name" in items[0]
