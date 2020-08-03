from pattern.text.es import verbs, tag, spelling, lexicon, parse, split
import string

def clasificar(palabra,clases_validas):
    """
    """
    aux = parse(palabra).split()[0][0][1]
    if aux in clases_validas:
        return True
    else:
        return False

def es_valida(palabra,dificultad,clases_validas=None):
    """
    """
    if (not palabra.lower() in verbs):
        if (not palabra.lower() in spelling):
            if (not(palabra.lower() in lexicon) and not(palabra.upper() in lexicon) and not(palabra.capitalize() in lexicon)):
                ok=False
            else:
                ok=True
        else:
            ok=True
    else:
        ok=True
    if (ok==True):
        if (dificultad == '-FACIL-'):
            return True
        else:
            return clasificar(palabra.lower(),clases_validas)  #'DT','JJ','JJR','JJS','RB','RBR','RBS': adjetivos /// 'VB','VBD','VBG','VBN','VBP','VBZ': verbos
    else:
        return False
