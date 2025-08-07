from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Enable CORS for frontend communication (e.g. local HTML/JS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (for development/testing)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load recipe data from local JSON file
with open("recipes.json", "r", encoding="utf-8") as f:
    ALL_RECIPES = json.load(f)

@app.get("/search-recipes/")
def search_recipes(ingredients: str = Query(..., description="Comma-separated list of ingredients")):
    user_ingredients = set(i.strip().lower() for i in ingredients.split(","))
    matches = []

    for recipe in ALL_RECIPES:
        recipe_ings = set(i.lower() for i in recipe.get("ingredients", []))
        matched_ings = []

        for ing in recipe_ings:
            for u_ing in user_ingredients:
                if u_ing in ing or ing in u_ing:  # fuzzy eşleşme
                    matched_ings.append(ing)

        score = len(set(matched_ings))

        matches.append({
            "name": recipe.get("name"),
            "author_name": recipe.get("author_name"),
            "description": recipe.get("description"),
            "ingredients": list(recipe_ings),
            "matched_ingredients": matched_ings,
            "instructions": recipe.get("instructions"),
            "image_url": recipe.get("image_url"),
            "time": recipe.get("time"),
            "score": score
        })

    matches.sort(key=lambda r: r["score"], reverse=True)
    return matches[:10]

