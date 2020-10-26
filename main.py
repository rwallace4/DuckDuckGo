import pytest
import requests

url_ddg = "https://api.duckduckgo.com"

def test_ddg0():

    resp = requests.get(url_ddg + "/?q=DuckDuckGo&format=json")

    rsp_data = resp.json()

    assert "DuckDuckGo" in rsp_data["Heading"]

@pytest.mark.parametrize("url, president", [(url_ddg, "Washington"),(url_ddg, "Adams"),(url_ddg, "Jefferson")
    ,(url_ddg, "Madison"),(url_ddg, "Monroe"),(url_ddg, "Jackson"), (url_ddg, "Buren")
    ,(url_ddg, "Harrison"),(url_ddg, "Tyler"),(url_ddg, "Polk"),(url_ddg, "Taylor"),(url_ddg, "Fillmore"),(url_ddg, "Pierce")
    ,(url_ddg, "Buchanan"),(url_ddg, "Lincoln"),(url_ddg, "Johnson"),(url_ddg, "Grant"),(url_ddg, "Hayes"),(url_ddg, "Garfield")
    ,(url_ddg, "Arthur"),(url_ddg, "Cleveland"),(url_ddg, "Harrison"),(url_ddg, "McKinley"),(url_ddg, "Roosevelt"),(url_ddg, "Taft")
    ,(url_ddg, "Wilson"),(url_ddg, "Harding"),(url_ddg, "Coolidge"),(url_ddg, "Truman"),(url_ddg, "Eisenhower"),(url_ddg, "Kennedy")
    ,(url_ddg, "Johnson"),(url_ddg, "Nixon"),(url_ddg, "Ford"),(url_ddg, "Carter"),(url_ddg, "Reagan"),(url_ddg, "Bush"),(url_ddg, "Clinton")
    ,(url_ddg, "Obama"),(url_ddg, "Trump")]
    
def test_presidents(url, president):
    resp = requests.get(url_ddg + "/?q=DuckDuckGo&format=json")

    rsp_data = resp.json()
    
    assert president in rsp_data
