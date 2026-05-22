from ollama import chat


def suggest_meals(ingredients):

    prompt = f"""
    You are a meal suggestion assistant.

    Available ingredients:
    {ingredients}

    Rules:
    - Suggest exactly 3 lunch meals
    - Prefer using only the given ingredients
    - If ingredients are missing, mention optional ingredients
    - Keep answers short
    - Format as a numbered list
    """

    response = chat(
        model="llama3",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]


while True:

    ingredients = input("Enter available ingredients: ")

    if ingredients.strip() == "":
        print("Please enter some ingredients.")
    else:
        break


result = suggest_meals(ingredients)

print("\nMeal Suggestions:\n")
print(result)