import json

from hdwallet import HDWallet # https://hdwallet.readthedocs.io/en/v2.2.1/index.html

import hdwallet.utils as WalletUtils


# Creamos un Generador de cartera para Bitcoin, direcciones "Pay to Witness Public Key Hash y
# nosotros creamos las "Deviation Paths"
hdwallet: HDWallet = HDWallet(symbol="BTC", semantic="P2WPKH", use_default_path=False)
# Creamos nuestra cartera principal apartir de una semilla (entropía) aleatoria de 256 bytes y
# con mnemónico en Español
hdwallet.from_entropy(WalletUtils.generate_entropy(256), "spanish")

# Vamos a crear las cuentas dentro de la cartera
for accountIndex in range(4):
    print(f"Account {accountIndex + 1}:")
    # Cada cuenta tendrá 2 subcuentas
    for index in range(2):
        # m/44' significa que es para una cartera HD, el 0' significa que es para Bitcoins
        # NOTA: después de {accountIndex} hay un apóstrofe, ese apóstrofe significa que se
        #    debe crear una nueva llave derivada para esa ruta
        # NOTA: La última parte de la ruta no tiene apóstrofe, significa que comparten la llave
        #    derivada
        accountPath = f"m/44'/0'/{accountIndex}'/{index}".format(accountIndex, index)
        subAccount = hdwallet.from_path(accountPath)
        subAccountPath = subAccount.path()
        address = subAccount.p2wpkh_address()
        print(f"\tAddress {index + 1}: {{ path: '{subAccountPath}', address: '{address}' }}")
        subAccount.clean_derivation()

# Imprimimos el JSON con toda la info de la cartera
print(json.dumps(hdwallet.dumps(), ensure_ascii=False, indent=4))
