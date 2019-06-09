import json
from flask import Flask, request, jsonify
from googleapiclient.discovery import build

app = Flask(__name__)

def __load_config__() -> tuple:
    """
    Loads the configuration from a JSON file

    Returns:
    - A dictionary with api_key and cse_id read from the config.json file
    """
    with open("config.json") as config:
        data = json.load(config)
        return data["api_key"], data["cse_id"]

def __google_search__(search_term: str) -> dict:
    """
    Searches a specific term on Google

    Params:
    - search_term: A string to be searched on Google

    Returns:
    - A list with the top 5 results and some insights about each one of them.
    """
    query = build("customsearch", "v1", developerKey=__api_key__)
    return query.cse().list(q=search_term, cx=__cse_id__).execute()["items"][:5]

def __format_data__(result:dict) -> dict:
    """
    Removes useless keys from google search data

    Params:
    - result: A dictionary containing data about a result of a Google Search

    Returns:
    - A dictionary with only relevant data 
    """
    data = { "link":result["link"], "snippet": result["snippet"], "htmlSnippet": result["htmlSnippet"] }
    if("fileFormat" in result.keys()):
        data["fileFormat"] = result["fileFormat"]
    return data

@app.route("/search_at_google", methods=["GET"])
def search_content():
    # This function has no tests because it only calls 
    # previously tested functions or functions from Flask.
    # Besides that, some best practices like architectural patterns (MVC, etc)
    # were not applied here to avoid overengineering of this simple problem

    search_term = request.args.get("q")
    search_result = __google_search__(search_term)
    return jsonify({ "data": list(map(__format_data__,search_result)) })

if __name__ == "__main__":
    custom_search_engine_url = "https://cse.google.com/cse/all"
    api_key_url = "https://developers.google.com/custom-search/v1/introduction"
    
    running_instructions = f"""
    To run this, please follow the steps below:
    
    1) Register your own custom search engine at {custom_search_engine_url}
    2) Get you API Key at {api_key_url}
    3) Fulfill this data on configs.example.json and rename it to configs.json
    4) execute pip install -r requirements.txt && python main.py
    
    """
    search_instructions =   """   
                            To google something and get the top 5 results, send a GET request to 
                            http://localhost:5000/search_at_google?q=your_search_string
                            """
    print(search_instructions)

    try:
        __api_key__, __cse_id__ = __load_config__()
        app.run()
    except Exception as ex:
        print(running_instructions)
    

