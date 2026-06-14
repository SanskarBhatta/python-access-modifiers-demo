import os
os.system('cls')
class ServerVault:
    def __init__(self,name):
        self.vault_name=name
        self._diamonds=100
        self.__auth_key= "OpPass123"
    def open_vault(self, key_input):
        if key_input==self.__auth_key:
            print (f"[ACCESS GRANTED] Opening {self.vault_name}. Inside you have {self._diamonds} diamonds.")
        else:
            print("[SECURITY ALERT] Wrong Auth Key! Vault locked down.")
my_vault=ServerVault("Main_Vault")
print(f"Checking Public Data: {my_vault.vault_name}")
print("\n--- Test 1: Hacker tries to access the private key directly ---")
try:
    print(my_vault.__auth_key)
except AttributeError:
    print("Python blocked direct access to the private __auth_key!")

print("\n--- Test 2: Entering the wrong key ---")
my_vault.open_vault("WrongPassword123")

print("\n--- Test 3: Entering the correct key ---")
my_vault.open_vault("OpPass123")
