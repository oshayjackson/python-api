from flask import Flask
import requests

class RW:
    def __init__(self):
        self.headers = {"X-Api-Key": "JcB+TqcZr4AtvUDD7DMH5g==vglzKa2osNr98096"}
        self.url = "https://api.api-ninjas.com/v1/randomword"

    def fetch_data(self):
        try:
            response = requests.get(self.url, headers=self.headers)
            response.raise_for_status()

            pretty_response = response.json()
            word = pretty_response.get("word")

            return {"Random word": word}
        except requests.RequestException as e:
            return {"Error": f"Error: {e}"}

if __name__ == "__main__":
    randomWord = RW()

    while True:
        input("Press Enter: ")
        data = randomWord.fetch_data()

        if "Error" in data:
            print(f"Error: {data['Error']}")
        else:
            print(f"\nRandom Word: ( {data['Random word']} )\n")
