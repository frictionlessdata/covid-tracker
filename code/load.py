from frictionless import Resource, Package
from livemark.plugins.cards import CardsPlugin


# General


CardsPlugin.delete_cards()
with Resource("data/packages.csv") as resource:
    for row in resource:
        code = row["code"]
        package = Package(row["content"])
        CardsPlugin.create_card("cards/package.md", code=code, package=package)
