import re, json, random
from bs4 import BeautifulSoup

# Variable globale
import os
PATTERN_FILE_PATH = os.path.abspath("data/match_pattern.json")
LIVRE_DOR_FILE_PATH = os.path.abspath("data/livredor.xml")

class Reactions():
    """
        Classe Reactions implementant les réactions du bot aux messages utilisateurs.

        :param data_json: Données JSON comprenant les patterns à reconnaître et les réactions associées.
        :param pattern_list: Liste de patterns associés à l'entrée JSON.
        :param PATTERN_FILE_PATH: Variable globale contenant le chemin du fichier JSON contenant les patterns.
        :param LIVRE_DOR_FILE_PATH: Variable globale contenant le chemin du fichier XML contenant les citations du Livre d'Or.
        :type data_json: JSON data
        :type pattern_list: dict{string: string, ...}
        :type PATTERN_FILE_PATH: string
        :type LIVRE_DOR_FILE_PATH: string
    """

    def __init__(self):
        """
            Constructeur de la classe Reactions.

            Charge les données depuis le fichier JSON contenant les patterns et
            leurs réactions associées. On pourra parcourir les clefs et retrouver
            ensuite directemet l'entrée du JSON à exploiter si le pattern (donc la
            clef) match.
        """
        # Chargement des mots-clefs
        with open(PATTERN_FILE_PATH, encoding='utf8') as file: 
            data = file.read()
        self.data_json = json.loads(data)
        # Liste de patterns (associés à leur entrée JSON)
        self.pattern_list = {}
        for entry in self.data_json:
            self.pattern_list.update({self.data_json[entry]["pattern"]: entry})

    def toi_meme_repeat(self, received_msg):
        """
            Méthode implémentant le 'Toi-même, 'spèce de...'.

            :param received_msg: Message de l'utilisateur auquel on répond.
            :type received_msg: string
            :return: Le message de réponse incorporant le mot répété.
            :rtype: string
        """
        search_a_word = re.search("^.* ([A-Za-zéêèôîïëüö]{4,}).*$", received_msg)
        if search_a_word is not None:
            repeat_word = search_a_word.group(1)
        answer_msg = "Toi-même, 'spèce d"
        # Le mot commence-t-il par une voyelle ?
        if re.search("^[éêèîêûïüëöaeiouyAEIOUY]", repeat_word) is not None:
            return answer_msg + "'" + repeat_word + " !"
        else:
            return answer_msg + "e" + repeat_word + " !"

    def search_key_word(self, received_msg):
        """
            Méthode recherchant les mots-clefs dans les messages utilisateurs.

            :param received_msg: Message de l'utilisateur auquel on répond.
            :type received_msg: string
            :return: Le message de réponse correspondant au pattern reconnu.
            :rtype: string
            :raise: Lève une exception si le type de réponse à fournir n'a pas été reconnu.
        """
        print("Recherche d'une réaction en cours...")
        for key_word in self.pattern_list.keys():
            # Si un mot-clef est matché dans le message reçu
            if re.search(key_word, received_msg) is not None:
                response = self.data_json[self.pattern_list[key_word]]["response"]
                if response["type"] == "simple":
                    return response["messages"][random.randint(0, len(response["messages"])-1)]
                elif response["type"] == "complex":
                    case = response["case"]
                    # Ici on définit les fonctions des réponses complexes:
                    if case == "silence" or case == "gueule":
                        # TODO
                        return response["messages"][random.randint(0, len(response["messages"])-1)]
                    elif case == "livredor":
                        is_there_author = re.search("auteur=(.*)$", received_msg)
                        quote_author = ""
                        if is_there_author is not None:
                            quote_author = is_there_author.group(1)
                        return self._livre_dor(quote_author)
                    else:
                        raise Exception("The answer complex type case has not been recognized.")
                else:
                    raise Exception("The answer type has not been recognized.")
        return None

    def _livre_dor(self, author):
        """
            Méthode privée implémentant la réponse en cas de requête au Livre d'Or.

            :param author: [Optionnel] Nom de l'auteur de la citation à retourner.
            :type author: string
            :return: Citation du Livre d'Or.
            :rtype: string
        """
        with open(LIVRE_DOR_FILE_PATH, encoding='utf8') as file: 
            data = file.read()
        if author == "":
            soup = BeautifulSoup(data, 'html.parser')
            citations = soup.find('livredor').find_all('citation')
            chosen_citation = citations[random.randint(0, len(citations)-1)]
            to_print = self.__print_citation(chosen_citation.get('type'), \
                chosen_citation.find('replique'), \
                chosen_citation.find_all('auteur'), \
                chosen_citation.find('date'), \
                chosen_citation.find('commentaire'))
            return to_print
        else:
            return "Fonctionnalité à venir."

    def __print_citation(self, c_type, replique, authors, date, comment):
        """
            Méthode privée mettant en forme une citation du Livre d'Or.

            :param c_type: Type de la citation ("monologue" ou "dialogue").
            :param replique: Citation du Livre d'Or.
            :param authors: Auteur(s) de la citation (liste à un ou plusieurs éléments).
            :param date: Date de la citation.
            :param comment: Commentaire accompagnant la citation (peut être "None").
            :type c_type: string
            :type replique: string
            :type authors: list(string, ...)
            :type date: string
            :type comment: string
            :return: Citation du Livre d'Or mise en forme.
            :rtype: string
        """
        # Citation Discord
        to_print = ">>> \""
        # Si monologue, print la réplique puis passer à la ligne et ajouter l'auteur
        if c_type == "monologue":
            to_print = to_print + replique.string + "\" \n- " + authors[0].string
        # Si dialogue, print la réplique avec passage de ligne puis ajouter les auteurs
        elif c_type == "dialogue":
            # Séparer toutes les phrases du dialogue
            separated_replique = replique.string.split("-")
            for phrase in separated_replique:
                # Ne pas mettre de tiret à la première phrase
                if phrase == separated_replique[0]:
                    to_print = to_print + phrase
                # Passer une ligne et ajouter un tiret
                else:
                    to_print = to_print + "\n-" + phrase
            # Fin de la réplique, fermer les guillemets et passer une ligne
            to_print = to_print + "\" \n- "
            for author in authors:
                # Si c'est le premier auteur de la liste
                if author == authors[0]:
                    to_print = to_print + author.string
                # Si c'est le dernier auteur de la liste, on ajoute "et" avant son nom.
                elif author == authors[len(authors)-1]:
                    to_print = to_print + " et " + author.string
                # Si c'est un auteur du milieu de la liste
                else:
                    to_print = to_print + ", " + author.string
        else:
            raise Exception("The citation type has not been recognized: " + c_type)
        # S'il y a un commentaire, l'ajouter
        if comment is not None:
            to_print = to_print + ", " + comment.string
        # Ajouter la date
        to_print = to_print + ", " + date.string
        return to_print