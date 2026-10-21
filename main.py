import requests
import json
from typing import Any


def fetch_activity() -> dict[str, Any]:
    url = "https://bored-api.appbrewery.com/random"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        activity = response.json()

        result = {
            "success": True,
            "data": {
                "activity": activity["activity"],
                "type": activity["type"]
            },
            "error": None,
            "source": "Bored API"
        }

    except requests.RequestException as error:
        result = {
            "success": False,
            "data": None,
            "error": str(error)
            
        }

    return result


if __name__ == "__main__":
    output = fetch_activity()
    print(json.dumps(output, indent=4))