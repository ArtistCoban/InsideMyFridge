import pandas as pd
import json
import ast
import re

def parse_image(val):
    try:
        if pd.isna(val):
            return ""
        
        val = str(val).strip()

        # if R
        if val.startswith("c(") and val.endswith(")"):
            val = val[2:-1]  
            matches = re.findall(r'"(https?://[^"]+)"', val)
            if matches:
                return matches[0]

        # if ""
        if val.startswith('"') and val.endswith('"'):
            val = val[1:-1]

        # normal url
        if val.startswith("http"):
            return val
        
    except Exception as e:
        print(f"Image parse error: {val} → {e}")
    
    return ""


def parse_r_ingredients(val):
    try:
        val = val.strip()
        if val.startswith("c(") and val.endswith(")"):
            val = val[2:-1]
        
        ingredients = re.findall(r'"(.*?)"', val)
        return [i.strip().lower() for i in ingredients if i.strip()]
    
    except Exception as e:
        print(f"Hata: {val} → {e}")
        return []


csv_path = "recipes.csv" 
output_path = "recipes.json"

# read CSV
df = pd.read_csv(csv_path)

# I will use name, ingredients, instructions,total time and images
target_fields = ["Name", "RecipeIngredientParts", "RecipeInstructions", "TotalTime", "Images"]

# if missing
for col in target_fields:
    if col not in df.columns:
        print(f"Column '{col}' missing.")
        exit()

# if NaN
df = df.dropna(subset=target_fields)


df["RecipeIngredientParts"] = df["RecipeIngredientParts"].apply(parse_r_ingredients)

def parse_instructions(val):
    try:
        val = str(val).strip()

        if val.startswith("c(") and val.endswith(")"):
            val = val[2:-1]  
            steps = re.findall(r'"(.*?)"', val)
            return " ".join(steps)

        parsed = ast.literal_eval(val)
        if isinstance(parsed, list):
            return " ".join(
                [step["text"] if isinstance(step, dict) and "text" in step else str(step) for step in parsed]
            )

        return val
    except:
        return str(val)

df["RecipeInstructions"] = df["RecipeInstructions"].apply(parse_instructions)


df["Images"] = df["Images"].apply(parse_image)

# for JSON
recipes = []
for _, row in df.iterrows():
    recipe = {
        "name": row["Name"],
        "author_name" : row["AuthorName"],
        "description" : row["Description"],
        "ingredients": row["RecipeIngredientParts"],
        "instructions": row["RecipeInstructions"],
        "time": row["TotalTime"],
        "image_url": row["Images"]
    }
    recipes.append(recipe)

# JSON save
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(recipes, f, ensure_ascii=False, indent=2)

print(f"{len(recipes)} recipe(s) saved to {output_path}")

print(df["Images"].head(10))

