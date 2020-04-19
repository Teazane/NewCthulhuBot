import re, json, random

class Reactions():
    def __init__(self):
        # Chargement des mots-clefs
        with open("match_pattern.json") as file: 
            data = file.read()
        self.data_json = json.loads(data)
        # Liste de patterns (associés à leur entrée JSON)
        self.pattern_list = {}
        for entry in self.data_json:
            self.pattern_list[entry["pattern"]] = entry
        # Etat mute initialisé à "faux"
        self.muted_state = False

    # Envoie "Toi-même 'spèce d[e']" + le dernier mot de la phrase
    def toi_meme_repeat(self, received_msg):
        repeat_world = re.search("^.* ([A-Za-zzéêèôîïëüö]{4,}).*$", received_msg).group(1)
        answer_msg = "Toi-même, 'spèce d"
        # Le mot commence-t-il par une voyelle ?
        if re.search("^[éêèîêûïüëöaeiouyAEIOUY]", repeat_world) is not None:
            return answer_msg + "'" + repeat_world + " !"
        else:
            return answer_msg + "e" + repeat_world + " !"

    # Recherche de mots-clefs et renvoi de la réponse correspondante
    def search_key_word(self, received_msg):
        for key_word in self.pattern_list.keys():
            # Di un mot-clef est matché dans le message reçu
            if re.search(key_word, received_msg) is not None:
                response = self.data_json[self.pattern_list[key_word]]["response"]
                if response["type"] == "simple":
                    answer_range = len(response["message"])
                    return response["message"][random.randint(0,answer_range)]
                elif response["type"] == "complex":
                    case = response["case"]
                    # Ici on définit les fonctions des réponses complexes:
                    if case == "silence" or case == "gueule":
                        self.muted_state = True
                        answer_range = len(response["message"])
                        return response["message"][random.randint(0,answer_range)]
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

    # Traitement des requêtes Livre d'Or
    def _livre_dor(self, author):
        return "A venir."