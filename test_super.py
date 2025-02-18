import requests

def test_supercali():
    result = requests.get("http://127.0.0.1:8000/index.html")
    assert result.status_code == 200
    print(result.text)
    assert "Supercali" in result.text

if __name__ == "__main__":
    test_supercali()
