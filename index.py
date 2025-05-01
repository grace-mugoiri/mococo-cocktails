from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

cocktails = [
    {
        "name": "Mango Mojito",
        "ingredients": [
            "1/2 ripe mango, diced",
            "10 fresh mint leaves",
            "1 tbsp sugar",
            "1 oz lime juice",
            "2 oz white rum",
            "Club soda"
        ],
        "instructions": "Muddle mango, mint, and sugar. Add lime juice and rum. Shake with ice. Pour into glass, top with soda, garnish with mint."
    },
    {
        "name": "Berry Breeze",
        "ingredients": [
            "1/4 cup mixed berries",
            "1 oz lemon juice",
            "1 oz vodka",
            "1/2 oz simple syrup",
            "Sparkling water"
        ],
        "instructions": "Muddle berries. Shake with lemon, vodka, and syrup. Strain over ice. Top with sparkling water."
    },
    {
        "name": "Cucumber Gin Fizz",
        "ingredients": [
            "4 cucumber slices",
            "1 oz lime juice",
            "1 oz gin",
            "1/2 oz elderflower syrup",
            "Tonic water"
        ],
        "instructions": "Muddle cucumber and lime. Add gin and syrup, shake. Pour into a glass with ice. Top with tonic water."
    },
    {
        "name": "Watermelon Spritz",
        "ingredients": [
            "1/2 cup watermelon chunks",
            "1 oz lime juice",
            "1 oz tequila",
            "Sparkling wine"
        ],
        "instructions": "Muddle watermelon. Add lime and tequila, shake. Strain into glass and top with sparkling wine."
    },
    {
        "name": "Pineapple Punch",
        "ingredients": [
            "1/2 cup pineapple juice",
            "1 oz coconut rum",
            "1 oz orange juice",
            "Crushed ice"
        ],
        "instructions": "Shake all ingredients with ice. Pour into a glass filled with crushed ice. Garnish with pineapple wedge."
    }
]

template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Mococo Party Cocktails</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gradient-to-br from-blue-100 via-teal-100 to-green-100 min-h-screen p-8 font-sans">
    <div class="max-w-6xl mx-auto">
        <h1 class="text-4xl font-bold text-center text-teal-700 mb-10 shadow-md p-4 rounded-lg bg-white">🍹 Mococo Party Cocktails</h1>
        
        <form method="get" action="/" class="mb-6 flex flex-col md:flex-row gap-4 items-center justify-center">
            <input type="text" name="search" value="{{ request.args.get('search', '') }}" placeholder="Search by name or ingredient" class="w-full md:w-1/2 p-3 border border-teal-400 rounded-xl shadow-md focus:outline-none focus:ring-2 focus:ring-teal-500" />
            <button type="submit" class="bg-teal-600 text-white px-6 py-3 rounded-xl hover:bg-teal-700 transition-colors">Search</button>
        </form>

        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8">
        {% if cocktails %}
            {% for cocktail in cocktails %}
            <div class="bg-white rounded-2xl shadow-xl p-6 hover:scale-[1.05] transition-all">
                <div class="flex items-center gap-4">
                    <i class="{{ cocktail.icon }} text-3xl text-teal-500"></i>
                    <h2 class="text-2xl font-semibold text-pink-700">{{ cocktail.name }}</h2>
                </div>
                <h3 class="mt-4 text-gray-700 font-medium">Ingredients:</h3>
                <ul class="list-disc list-inside text-gray-600 text-sm">
                    {% for item in cocktail.ingredients %}
                    <li>{{ item }}</li>
                    {% endfor %}
                </ul>
                <p class="mt-4 text-gray-700 text-sm"><strong>Instructions:</strong> {{ cocktail.instructions }}</p>
            </div>
            {% endfor %}
        {% else %}
            <p class="text-center text-gray-600 text-lg">No cocktails found for your search.</p>
        {% endif %}
        </div>

        <hr class="my-12 border-t-2 border-teal-400">

        <h2 class="text-3xl text-center text-teal-700 mb-4">➕ Add a New Cocktail</h2>
        <form method="post" action="/add" class="bg-white p-6 rounded-2xl shadow-md max-w-2xl mx-auto space-y-4">
            <input name="name" placeholder="Cocktail name" required class="w-full p-3 border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-teal-500" />
            <textarea name="ingredients" placeholder="Ingredients (comma-separated)" required class="w-full p-3 border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-teal-500"></textarea>
            <textarea name="instructions" placeholder="Instructions" required class="w-full p-3 border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-teal-500"></textarea>
            <button type="submit" class="bg-pink-600 text-white px-6 py-3 rounded-xl hover:bg-pink-700 transition-colors">Add Cocktail</button>
        </form>
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET'])
def index():
    query = request.args.get("search", "").lower()
    if query:
        filtered = [
            c for c in cocktails
            if query in c["name"].lower() or any(query in ing.lower() for ing in c["ingredients"])
        ]
    else:
        filtered = cocktails
    return render_template_string(template, cocktails=filtered)


if __name__ == '__main__':
    app.run(debug=True)
