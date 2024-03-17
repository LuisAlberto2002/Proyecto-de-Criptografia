from typing import List
from bsvlib.hd import mnemonic_from_entropy, Xprv, derive_xprvs_from_mnemonic,derive_xkeys_from_xkey
from bsvlib import Key,verify_signed_text,Unspent,create_transaction
from datetime import datetime
import json

keys_org=[]
wallets=[]
keys_dep=[]
juan={}

def loadJson():
    with open('./Proyecto Crypto/config.json','r') as f:
        juan = json.load(f)
        print(juan)

def saveJson():
    with open('./Proyecto Crypto/config.json','w') as f:
        json.dump(juan,f)

def setup_Organization():
    #Prueba de generar entropia usando la libreria datetime
    #datetime.now().strftime('"%d/%m/%Y, %H:%M:%S"')
    #entropy = datetime.now().strftime('"%d/%m/%Y, %H:%M:%S"')

    entropy = 'cd9b819d9c62f0027116c1849e7d497f'
    mnemonic: str = mnemonic_from_entropy(entropy)

    keys: List[Xprv] = derive_xprvs_from_mnemonic(mnemonic, path="m/44'/0'/0'", change=1, index_start=0, index_end=1)

    #Modificar el idex para que solo cree una cuenta, de este modo obtenemos la clave privada maestra de toda la organizacion, empleando
    #la funcion de derive_xkeys_from_xkey derivamos los departamentos a partir de la xprv, y repetimos el proceso para las wallets

    for key in keys:
        keys_org.append(key)
        #print(key)
        """keydep: List[Xprv] = derive_xkeys_from_xkey(key,index_start=0,index_end=5)
        print('\n\nWallets dentro del departamento \n\n')
        for keyp in keydep:
            print(keyp)"""
        #print(key.address(), key.private_key().wif())

def setup_Org_back(xpriv):
    print("Uso de shamir para guardar la direccion de la organizacion")

def setup_department(keys_org):

    for xpriv in keys_org:
        print(f"\nEmpresa con la llave: {xpriv} \nDepartamentos: \n")
        key: List[Xprv] = derive_xkeys_from_xkey(xpriv,index_start=0,index_end=5)
        for keys in key:
            keys_dep.append(keys)
            print(f"\nDepartamento :  {keys} \nWallets:\n")
            key_w: List[Xprv] = derive_xkeys_from_xkey(keys,index_start=0,index_end=5)
            for k in key_w:
                print(f"wallet : {k}")
            
            #print(keys)
    #print("Creacion de los departamentos y wallets")


def department_spend(destination,amount):
    department_check_balance()
    print('Update balance')
    print('Build TX')
    print('Solicita ssss->xpriv->priv(derivation path)')
    print('sigh tx -> publish tx')

def department_check_balance(xpub):
    print("Realiza la actualizacion del contenido de las carteras")

loadJson()
juan['perez'] = 'placencia'
saveJson()

setup_Organization()
print("\n\nimprimiendo nuevamente las direcciones de los departamentos\n\n")
setup_department(keys_org)




"""print("\n\n\n\ndirecciones de los departamentos")
for key in keys_org:
    print(key.address(), key.private_key().wif())

print("direcciones de las wallets por departamento")
for key in keys_dep:
    print(key.address(), key.private_key().wif())"""
