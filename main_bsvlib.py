from typing import List
from bsvlib.hd import mnemonic_from_entropy, Xprv, derive_xprvs_from_mnemonic, derive_xkeys_from_xkey
from bsvlib import Key
from datetime import datetime
import json
from secrets import randbelow
from sympy import nextprime
import os
import hashlib

current_directory = os.path.dirname(__file__)
file_path = os.path.join(current_directory, 'config.json')


keys_org = []
wallets = []
keys_dep = []
juan = {}

def string_to_bytes(s):
    return bytes.fromhex(hashlib.sha256(s.encode()).hexdigest())

def loadJson(filepath):
    global juan
    with open(filepath, 'r') as f:
        juan = json.load(f)
        print(juan)


def saveJson(filepath):
    with open(filepath, 'w') as f:
        json.dump(juan, f)


def generate_shares(secret, num_shares, threshold):
    prime = nextprime(secret)
    coefficients = [randbelow(prime) for _ in range(threshold - 1)]
    coefficients.insert(0, secret)
    shares = []
    for i in range(1, num_shares + 1):
        share = sum(coeff * (i ** j) % prime for j, coeff in enumerate(coefficients))
        shares.append((i, share))
    return shares


def setup_Organization():
    entropy = 'cd9b819d9c62f0027116c1849e7d497f'
    entropy_as_bytes = string_to_bytes(entropy)
    mnemonic = mnemonic_from_entropy(entropy_as_bytes)

    keys: List[Xprv] = derive_xprvs_from_mnemonic(mnemonic, path="m/44'/0'/0'", change=1, index_start=0, index_end=1)

    for key in keys:
        keys_org.append(key)


def setup_Org_back(xpriv):
    num_shares = 5  # Número total de fragmentos
    threshold = 3   # Número mínimo de fragmentos requeridos para reconstruir el secreto

    org_address = xpriv.address()

    shares = generate_shares(int(org_address), num_shares, threshold)

    juan['org_shares'] = shares
    saveJson()


def setup_department(keys_org):
    for xpriv in keys_org:
        print(f"\nEmpresa con la llave: {xpriv} \nDepartamentos: \n")
        key: List[Xprv] = derive_xkeys_from_xkey(xpriv, index_start=0, index_end=5)
        for keys in key:
            keys_dep.append(keys)
            print(f"\nDepartamento :  {keys} \nWallets:\n")
            key_w: List[Xprv] = derive_xkeys_from_xkey(keys, index_start=0, index_end=5)
            for k in key_w:
                print(f"wallet : {k}")


def department_spend(destination, amount):
    department_check_balance()
    print('Update balance')
    print('Build TX')
    print('Solicita ssss->xpriv->priv(derivation path)')
    print('sigh tx -> publish tx')


def department_check_balance(xpub):
    print("Realiza la actualizacion del contenido de las carteras")


loadJson(file_path)
juan['perez'] = 'placencia'
saveJson(file_path)

setup_Organization()
print("\n\nimprimiendo nuevamente las direcciones de los departamentos\n\n")
setup_department(keys_org)

setup_Org_back(keys_org[0])
