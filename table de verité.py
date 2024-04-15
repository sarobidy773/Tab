def table_de_verite(fonction):
    variables = sorted(set(fonction.replace('~', '').replace('&', '').replace('|', '')))
    print('Table de vérité de la fonction :', fonction)
    print('|', '|'.join(variables), '| Résultat |')
    print('-' * (4 * len(variables) + 9))
    for i in range(2 ** len(variables)):
        values = [int(b) for b in bin(i)[2:].zfill(len(variables))]
        assignments = dict(zip(variables, values))
        result = int(eval(fonction, {}, assignments))
        print('|', '|'.join(str(v) for v in values), '|', result, '|')

def premiere_forme_canonique(fonction):
    variables = sorted(set(fonction.replace('~', '').replace('&', '').replace('|', '')))
    premiere_forme = ' * '.join([f'({v} + ~{v})' for v in variables])
    return premiere_forme

def deuxieme_forme_canonique(fonction):
    variables = sorted(set(fonction.replace('~', '').replace('&', '').replace('|', '')))
    deuxieme_forme = ' + '.join([f'({v} * ~{v})' for v in variables])
    return deuxieme_forme

fonction_logique = input("Entrez la fonction logique en utilisant les opérateurs logiques (& pour AND, | pour OR, ~ pour NOT) : ")
table_de_verite(fonction_logique)
print("Première forme canonique de la fonction :", premiere_forme_canonique(fonction_logique))
print("Deuxième forme canonique de la fonction :", deuxieme_forme_canonique(fonction_logique))
