import json

INPUT_FILE = "recipes_original.json"
OUTPUT_FILE = "recipes.json"
MAX_RECIPES = 90000  # recipe from the big data (from 522516 recipes)

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

# Filter
filtered = []
for recipe in data:
    if (
        recipe.get("ingredients") 
        and recipe.get("instructions") 
        and isinstance(recipe["ingredients"], list) 
        and len(recipe["ingredients"]) > 0
        and len(recipe["instructions"].strip()) > 0
    ):
        filtered.append(recipe)
    if len(filtered) >= MAX_RECIPES:
        break

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(filtered, f, ensure_ascii=False, indent=2)

print(f"✅ {len(filtered)} recipes written to {OUTPUT_FILE}")
