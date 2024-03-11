import requests


class URL:
    def __init__(self, query):
        self.query = query
        self.headers = {"X-Api-Key": "JcB+TqcZr4AtvUDD7DMH5g==ujF81TyyYNexrTUh"}
        self.url = "https://api.calorieninjas.com/v1/nutrition?query="
        self.data = self.fetch_data()

    def fetch_data(self):
        try:
            response = requests.get(self.url + self.query, headers=self.headers)
            response.raise_for_status()

            pretty_response = response.json()
            item = pretty_response["items"][0]

            return {
                "name": item["name"].upper(),
                "calories": item["calories"],
                "serving_size": item["serving_size_g"],
                "fat_total": item["fat_total_g"],
                "protein": item["protein_g"],
                "sodium": item["sodium_mg"],
                "cholesterol": item["cholesterol_mg"],
                "carbohydrates_total": item["carbohydrates_total_g"],
                "fiber": item["fiber_g"],
                "sugar": item["sugar_g"],
            }

        except requests.RequestException as e:
            return {"error": f"Error: {e}"}


if __name__ == "__main__":
    query = input("Search: ").lower().strip()
    url_instance = URL(query)
    data = url_instance.data

    if "error" in data:
        print(f"Error: {data['error']}")
    else:
        print(
            f"""\nCalories: {data['calories']}
            \nServing Size: {data['serving_size']}g
            \nFat (Total): {data['fat_total']}g
            \nProtein: {data['protein']}g
            \nSodium: {data['sodium']}mg
            \nCholesterol: {data['cholesterol']}mg
            \nCarbohydrates (Total): {data['carbohydrates_total']}g
            \nFiber: {data['fiber']}g\nSugar: {data['sugar']}g"""
        )
