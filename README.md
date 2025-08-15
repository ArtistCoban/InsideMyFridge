# InsideMyFridge

**InsideMyFridge is a recipe suggestion app made by a university student (me).**
You write what ingredients you have in your fridge, and it shows you recipes that match — even if it's not an exact match (fuzzy style).

Built using **FastAPI** in Python and some basic HTML/JS for the frontend.

---

## Data Source

I used [Kaggle’s Food.com Recipes and Reviews dataset](https://www.kaggle.com/datasets/irkaal/foodcom-recipes-and-reviews).
I filtered it down to about 85,000 recipes, cleaned the data, and converted it to a simple JSON file to use locally.

---

## What It Can Do

You type some ingredients, like: `egg, tomato`
It searches through the dataset and gives you recipes
It doesn't need exact matches (so "tomatoes" and "tomato" work)

---

## Tools I Used

* Python 3
* FastAPI
* JSON (for the recipe data)
* HTML + JavaScript (basic stuff)
* Works fine locally, but can also be deployed on [Render](https://render.com)

---

## How to Run It Locally

### 1. Install Dependencies

```bash
pip install fastapi uvicorn
```

### 2. Start the Backend

```bash
cd backend
uvicorn main:app --reload
```

Then go to:
 `http://127.0.0.1:8000`

### 3. Open the Frontend

Open `frontend/index.html` in your browser. That's it!

---

## Project Folder Structure

```
SmartRecipeFinder/

├── backend/
│   ├── csvtojson.py        # Converts CSV to JSON for clean data
│   ├── jsonsmall.py        # Shrinks JSON file size
│   ├── main.py             # FastAPI backend
│   └── recipes.json        # Clean-recipe data (big file,filtered)
│
├── frontend/
│   └── index.html          # Web interface
│
├── recipes.csv             # Raw dataset (ignored by git)
├── .gitignore              # To skip big files
└── README.md               # This file!
```

---

## Maybe Later (Ideas)

* Ingredient auto-complete
* Filter by calories or nutrition

---

## 🙋‍♂️ About Me

**Koray Yereli** — Computer Science student at University of Bordeaux.
I made this for fun + learning. Hope it helps or inspires you.

GitHub: [@ArtistCoban](https://github.com/ArtistCoban)

---

## 📄 License

MIT — You can use it freely for personal or academic stuff.
