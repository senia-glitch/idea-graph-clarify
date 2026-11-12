from importlib import metadata

from idea_graph_clarify import manifest


def test_manifest_is_complete():
    m = manifest()
    assert m["id"] == "clarify" and m["kind"] == "agent" and m["asks"] is True
    assert m["outcomes"] == ["готово"] and "открытый вопрос" in m["writes"]
    for phrase in ("один", "recommended", "открытый вопрос", "граница", "finish", '"decision":"last"'):
        assert phrase in m["skill"]


def test_entry_point_is_declared():
    names = [p.name for p in metadata.entry_points(group="idea_graph.packages")]
    assert "clarify" in names
