from web3 import Web3


def connect_to_blockchain():
    try:
        w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
        if w3.isConnected():
            print("Blockchain ağına başarıyla bağlanıldı!")
            return w3
        else:
            print("Blockchain ağına bağlanılamadı.")
            return None
    except Exception as e:
        print("Blockchain bağlantı hatası:", e)
        return None
