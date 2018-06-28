import json
 
 
#En admettant que le json se nomme fichier.json
with open("fichier.json", "r") as f_read:
    dico = json.load(f_read)
print(dico)
print("test")
print(len(dico))
#Enregistrement du nouveau contenu au bon endroit (à définir)
nb= len(dico) + 1
dico[str(nb)] = r"C:\Users\tasnim\Desktop"
 
#Sauvegarde (écrasement)
with open("fichier.json", "w") as f_write:
    json.dump(dico, f_write)