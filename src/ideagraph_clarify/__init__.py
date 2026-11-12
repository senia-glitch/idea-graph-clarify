"""Пакет «Уточнение идеи»: скилл и манифест. Кода, кроме манифеста, здесь нет."""

from pathlib import Path

__version__ = "0.1.0"


def manifest() -> dict:
    return {
        "id": "clarify",
        "name": "Уточнение идеи",
        "description": "Жёстко и критично уточняет сырую идею: один конкретный вопрос за ход, "
                       "готовые варианты решения, ответы превращаются в карточки графа.",
        "kind": "agent",
        "order": 10,
        "reads": ["идея", "ветка", "решение", "граница", "открытый вопрос"],
        "writes": ["ветка", "решение", "граница", "открытый вопрос"],
        "asks": True,
        "web_search": False,
        "model_level": "сильная",
        "outcomes": ["готово"],
        "skill": (Path(__file__).parent / "skill.md").read_text(encoding="utf-8"),
    }
