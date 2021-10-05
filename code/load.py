from frictionless import Resource
from livemark.plugins.cards import CardsPlugin


# General


CardsPlugin.delete_cards()
with Resource("data/latest.csv") as resource:
    for row in resource:
        code = row["iso_code"]
        CardsPlugin.create_card("cards/location.md", code=code, data=row)
        print(f"Loaded: {row['location']}")
