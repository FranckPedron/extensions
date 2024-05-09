fichiers = ("notepad.exe", "mon.fichier.perso.doc", "notes.TXT", "vacances.jpeg", "planning", "data.dat")

definition_extensions = (("doc", "Document Word"),
                         ("exe", "Executable"),
                         ("txt", "Document texte"),
                         ("jpeg", "Image JPEG"),
                         )


def extraire_extension(fichier):
    f_split = fichier.split(".")
    if len(f_split) > 1:
        return f_split[-1]
    return None


def trouver_def_extension(ext, liste_ext):
    for l in liste_ext:
        if ext.lower() == l[0].lower():
            return l[1]
    return "Extension non connue"


def afficher_liste(fichier, liste):
    for f in fichier:
        ext = extraire_extension(f)
        if ext:
            rac = trouver_def_extension(ext, liste)
        else:
            rac = "Aucune extension"
        print(f"{f} ({rac})")


afficher_liste(fichiers, definition_extensions)
