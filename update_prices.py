import requests
import json
import subprocess

COINS = [
    "bitcoin", "ethereum", "binancecoin", "ripple", "cardano", "solana",
    "dogecoin", "polkadot", "litecoin", "chainlink", "uniswap", "stellar",
    "vechain", "tron", "filecoin", "monero", "tezos", "eos", "theta-token",
    "algorand", "avalanche-2", "cosmos", "bitcoin-cash", "terra-luna",
    "aave", "compound-governance-token", "pancakeswap-token", "neo", "dash",
    "zilliqa", "maker", "celsius-degree-token", "elrond-erd-2", "huobi-token",
    "hedera-hashgraph", "okb", "fantom", "decentraland", "chiliz", "kusama"
]

def fetch_prices():
    ids = ",".join(COINS)
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={ids}&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    return data

def save_prices(data):
    with open("prices.json", "w") as f:
        json.dump(data, f, indent=2)

def git_commit_push():
    subprocess.run(["git", "config", "--local", "user.email", "action@github.com"], check=True)
    subprocess.run(["git", "config", "--local", "user.name", "GitHub Action"], check=True)
    subprocess.run(["git", "add", "prices.json"], check=True)

    result = subprocess.run(["git", "commit", "-m", "Update prices.json"], capture_output=True, text=True)
    if "nothing to commit" in result.stdout.lower():
        print("No changes to commit.")
    else:
        subprocess.run(["git", "push"], check=True)

if __name__ == "__main__":
    prices = fetch_prices()
    save_prices(prices)
    git_commit_push()
