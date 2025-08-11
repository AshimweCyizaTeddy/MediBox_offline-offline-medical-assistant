
language_map = {
    "English": "English",
    "French": "French",
    "Kinyarwanda": "Kinyarwanda",
    "Ikinyarwanda": "Kinyarwanda",
    "Kiswahili": "Kiswahili",
    "Swahili": "Kiswahili"
}


import tkinter as tk
from tkinter import ttk
import pyttsx3
import threading
import sqlite3

# Initialize text-to-speech engine
tts_engine = pyttsx3.init()
from datetime import datetime

# Initialize main window

import base64
import tempfile

# Embedded base64 icon
icon_ico_base64 = b"""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"""

# Decode and save icon to a temp file
temp_icon = tempfile.NamedTemporaryFile(delete=False, suffix=".ico")
temp_icon.write(base64.b64decode(icon_ico_base64))
temp_icon.close()

root = tk.Tk()

# Show popup tip about double clicking Diagnose for voice output
import tkinter.messagebox as messagebox

popup_message = """💡 Double click 'Diagnose' for voice output
💡 Double-cliquez sur 'Diagnostiquer' pour la sortie vocale
💡 Bonyeza mara mbili 'Tambua' ili kusikia matokeo
💡 Kanda kabiri 'Gusuzuma' kugirango wumve igisubizo"""

root.after(500, lambda: messagebox.showinfo('Tip', popup_message))

root.iconbitmap(temp_icon.name)
root.title("MediBox")
root.geometry("800x600")
root.configure(bg="#faebd7")

# Language and translations
languages = ["English", "French", "Kiswahili", "Kinyarwanda"]
current_language = tk.StringVar(value="English")

translations = {
    "Welcome to MediBox": {
        "English": "Welcome to MediBox",
        "French": "Bienvenue sur MediBox",
        "Kiswahili": "Karibu kwenye MediBox",
        "Kinyarwanda": "Murakaza neza kuri MediBox"
    },
    "Enter your symptoms (comma separated):": {
        "English": "Enter your symptoms (comma separated):",
        "French": "Entrez vos symptômes (séparés par des virgules):",
        "Kiswahili": "Weka dalili zako (tenganisha kwa koma):",
        "Kinyarwanda": "Injiza ibimenyetso (utandukanyije na koma):"
    },
    "Diagnose": {
        "English": "Diagnose",
        "French": "Diagnostiquer",
        "Kiswahili": "Tambua Ugonjwa",
        "Kinyarwanda": "Gupima"
    },
    "Diagnosis": {
        "English": "Diagnosis",
        "French": "Diagnostic",
        "Kiswahili": "Uchunguzi",
        "Kinyarwanda": "Ibisubizo"
    },
    "Advice": {
        "English": "Advice",
        "French": "Conseil",
        "Kiswahili": "Ushauri",
        "Kinyarwanda": "Inama"
    },
    "Diagnosis not found.": {
        "English": "Diagnosis not found.",
        "French": "Diagnostic non trouvé.",
        "Kiswahili": "Uchunguzi haukupatikana.",
        "Kinyarwanda": "Ibisubizo ntibibonetse."
    },
    "Please visit a health center for professional support.": {
        "English": "Please visit a health center for professional support.",
        "French": "Veuillez visiter un centre de santé pour un soutien professionnel.",
        "Kiswahili": "Tafadhali tembelea kituo cha afya kwa msaada wa kitaalamu.",
        "Kinyarwanda": "Nyamuneka jya ku kigo nderabuzima ubone ubufasha bw'umwuga."
    },
    "Language:": {
        "English": "Language:",
        "French": "Langue:",
        "Kiswahili": "Lugha:",
        "Kinyarwanda": "Ururimi:"
    },
    "Menu": {
        "English": "Menu",
        "French": "Menu",
        "Kiswahili": "Menyu",
        "Kinyarwanda": "Menyu"
    },
    "Records": {
        "English": "Records",
        "French": "Dossiers",
        "Kiswahili": "Rekodi",
        "Kinyarwanda": "Amakuru"
    },
    "Diagnose illnesses based on your symptoms.": {
        "English": "Diagnose illnesses based on your symptoms.",
        "French": "Diagnostiquez les maladies selon vos symptômes.",
        "Kiswahili": "Tambua magonjwa kulingana na dalili zako.",
        "Kinyarwanda": "Menya indwara ushingiye ku bimenyetso byawe."
    },
    "Click 'Diagnosis' to begin.": {
        "English": "Click 'Diagnose' to begin.",
        "French": "Cliquez sur 'Diagnostiquer' pour commencer.",
        "Kiswahili": "Bonyeza 'Tambua Ugonjwa' kuanza.",
        "Kinyarwanda": "Kanda 'Gupima' kugira ngo utangire."
    },
    "Delete Selected Record": {
        "English": "Delete Selected Record",
        "French": "Supprimer l'enregistrement sélectionné",
        "Kiswahili": "Futa rekodi uliyoteua",
        "Kinyarwanda": "Siba inyandiko wahisemo"
    },
    "Symptoms": {
        "English": "Symptoms",
        "French": "Symptômes",
        "Kiswahili": "Dalili",
        "Kinyarwanda": "Ibimenyetso"
    },
    "Timestamp": {
        "English": "Timestamp",
        "French": "Horodatage",
        "Kiswahili": "Wakati",
        "Kinyarwanda": "Igihe"
    }
}

def tr(key):
    return translations.get(key, {}).get(current_language.get(), key)
symptom_diagnosis = {
 "all_diseases_translated": {
       "entries": [
        {
            "symptoms": {
                "English": ["fever", "headache", "abdominal pain"],
                "French": ["fièvre", "mal de tête", "douleur abdominale"],
                "Kiswahili": ["homa", "kichwa kuuma", "maumivu ya tumbo"],
                "Kinyarwanda": ["umuriro", "uburibwe mu mutwe", "uburibwe mu nda"]
            },
            "disease": {
                "English": "Typhoid Fever",
                "French": "Fièvre typhoïde",
                "Kiswahili": "Homa ya matumbo",
                "Kinyarwanda": "Typhoid"
            },
            "advice": {
                "English": "Use antibiotics as prescribed, stay hydrated, and rest.",
                "French": "Utilisez des antibiotiques comme prescrit, restez hydraté et reposez-vous.",
                "Kiswahili": "Tumia antibiotiki kama ulivyoelekezwa, kunywa maji mengi na pumzika.",
                "Kinyarwanda": "Fata antibiotique nk’uko wategetswe, wiyuhagirire kandi uruhuke."
            }
        },
        {
            "symptoms": {
                "English": ["weight loss", "night sweats", "persistent cough"],
                "French": ["perte de poids", "sueurs nocturnes", "toux persistante"],
                "Kiswahili": ["kupungua uzito", "kutokwa jasho usiku", "kikohozi kisichokoma"],
                "Kinyarwanda": ["guta ibiro", "kuzirana nijoro", "inkorora idashira"]
            },
            "disease": {
                "English": "Tuberculosis",
                "French": "Tuberculose",
                "Kiswahili": "Kifua kikuu",
                "Kinyarwanda": "Igituntu"
            },
            "advice": {
                "English": "Take the full course of anti-TB medications.",
                "French": "Prenez le traitement anti-TB jusqu'au bout.",
                "Kiswahili": "Tumia dawa za kifua kikuu hadi mwisho wa dozi.",
                "Kinyarwanda": "Fata imiti yose y’igituntu uko yategetswe kugeza irangiye."
            }
        },
        {
            "symptoms": {
                "English": ["fever", "skin rash", "muscle pain"],
                "French": ["fièvre", "éruption cutanée", "douleurs musculaires"],
                "Kiswahili": ["homa", "vipele vya ngozi", "maumivu ya misuli"],
                "Kinyarwanda": ["umuriro", "udusimba ku mubiri", "uburibwe bw’imitsi"]
            },
            "disease": {
                "English": "Zika Virus",
                "French": "Virus Zika",
                "Kiswahili": "Virusi vya Zika",
                "Kinyarwanda": "Virusu ya Zika"
            },
            "advice": {
                "English": "Rest, fluids, and pain relievers like acetaminophen.",
                "French": "Repos, hydratation et antalgiques comme le paracétamol.",
                "Kiswahili": "Pumzika, kunywa maji na kutumia dawa za maumivu kama paracetamol.",
                "Kinyarwanda": "Ruhuka, unywe amazi kandi ukoreshe imiti irwanya ububabare nka paracetamol."
            }
        },
        {
            "symptoms": {
                "English": ["high fever", "bleeding", "low blood pressure"],
                "French": ["forte fièvre", "saignement", "pression artérielle basse"],
                "Kiswahili": ["homa kali", "kutokwa damu", "shinikizo la chini la damu"],
                "Kinyarwanda": ["umuriro mwinshi", "kuva amaraso", "umuvuduko w’amaraso uri hasi"]
            },
            "disease": {
                "English": "Ebola Virus Disease",
                "French": "Maladie à virus Ebola",
                "Kiswahili": "Ugonjwa wa virusi vya Ebola",
                "Kinyarwanda": "Indwara ya Ebola"
            },
            "advice": {
                "English": "Seek emergency care in a specialized center.",
                "French": "Consultez un centre spécialisé en urgence.",
                "Kiswahili": "Tafuta huduma ya dharura katika kituo maalum.",
                "Kinyarwanda": "Shaka ubufasha bwihuse mu kigo kivura Ebola."
            }
        },
        {
            "symptoms": {
                "English": ["fever", "rash", "red eyes"],
                "French": ["fièvre", "éruption", "yeux rouges"],
                "Kiswahili": ["homa", "vipele", "macho mekundu"],
                "Kinyarwanda": ["umuriro", "udusimba", "amaso atukura"]
            },
            "disease": {
                "English": "Measles",
                "French": "Rougeole",
                "Kiswahili": "Surua",
                "Kinyarwanda": "Iseru"
            },
            "advice": {
                "English": "Isolation, fever control, and vitamin A supplements.",
                "French": "Isolement, contrôle de la fièvre et supplémentation en vitamine A.",
                "Kiswahili": "Kujitenga, kudhibiti homa, na virutubisho vya vitamini A.",
                "Kinyarwanda": "Gushyirwa mu kato, kugabanya umuriro no guhabwa Vitamine A."
            }
        },
        {
            "symptoms": {
                "English": ["fever", "paralysis", "muscle weakness"],
                "French": ["fièvre", "paralysie", "faiblesse musculaire"],
                "Kiswahili": ["homa", "kupooza", "udhaifu wa misuli"],
                "Kinyarwanda": ["umuriro", "gupfa kw’ingingo", "intege nke mu misokoro"]
            },
            "disease": {
                "English": "Polio",
                "French": "Poliomyélite",
                "Kiswahili": "Polio",
                "Kinyarwanda": "Poliyo"
            },
            "advice": {
                "English": "Polio is preventable by vaccine; seek rehab if symptoms appear.",
                "French": "La polio est évitable par vaccin; suivez une rééducation si les symptômes apparaissent.",
                "Kiswahili": "Polio inaweza kuzuilika kwa chanjo; tafuta huduma ya kurekebisha mwili ikiwa dalili zitaonekana.",
                "Kinyarwanda": "Poliyo irakingirwa n’urukingo; shaka ubuvuzi bwo kongera imbaraga nibiba ngombwa."
            }
        },
        {
            "symptoms": {
                "English": ["fatigue", "jaundice", "nausea"],
                "French": ["fatigue", "jaunisse", "nausée"],
                "Kiswahili": ["uchovu", "ngozi ya manjano", "kichefuchefu"],
                "Kinyarwanda": ["umunaniro", "uruhu rwerurutse", "isoka"]
            },
            "disease": {
                "English": "Hepatitis B",
                "French": "Hépatite B",
                "Kiswahili": "Homa ya ini B",
                "Kinyarwanda": "Hepatite B"
            },
            "advice": {
                "English": "Antiviral medication and liver monitoring.",
                "French": "Médicaments antiviraux et surveillance du foie.",
                "Kiswahili": "Dawa za virusi na kufuatilia ini.",
                "Kinyarwanda": "Imiti ivura virusi no gukurikirana imikorere y’umwijima."
            }
        },
        {
            "symptoms": {
                "English": ["skin lesions", "fever", "swollen lymph nodes"],
                "French": ["lésions cutanées", "fièvre", "ganglions enflés"],
                "Kiswahili": ["vidonda vya ngozi", "homa", "kuvimba kwa tezi"],
                "Kinyarwanda": ["ibisebe ku ruhu", "umuriro", "inzira z’amaraso zabyimbye"]
            },
            "disease": {
                "English": "Monkeypox",
                "French": "Variole du singe",
                "Kiswahili": "Monkeypox",
                "Kinyarwanda": "Impetigo y’inguge"
            },
            "advice": {
                "English": "Isolate and manage with antivirals if needed.",
                "French": "Isolement et traitement avec antiviraux si nécessaire.",
                "Kiswahili": "Jitenge na tumia dawa za virusi ikiwa inahitajika.",
                "Kinyarwanda": "Shyirwa mu kato kandi ukoreshe imiti yica virusi niba bikenewe."
            }
        },
        {
            "symptoms": {
                "English": ["fever", "stiff neck", "sensitivity to light"],
                "French": ["fièvre", "raideur de la nuque", "sensibilité à la lumière"],
                "Kiswahili": ["homa", "shingo kukakamaa", "kuona mwangaza kunauma"],
                "Kinyarwanda": ["umuriro", "ijosi rikakaye", "kwanga urumuri"]
            },
            "disease": {
                "English": "Bacterial Meningitis",
                "French": "Méningite bactérienne",
                "Kiswahili": "Meningitis ya bakteria",
                "Kinyarwanda": "Meningite iterwa na mikorobi"
            },
            "advice": {
                "English": "Seek immediate emergency treatment.",
                "French": "Consultez immédiatement un service d'urgence.",
                "Kiswahili": "Pata matibabu ya haraka ya dharura.",
                "Kinyarwanda": "Jya kwa muganga byihutirwa ubone ubuvuzi bw'ako kanya."
            }
        },
        {
            "symptoms": {
                "English": ["genital sores", "swollen lymph nodes", "fever"],
                "French": ["plaies génitales", "ganglions enflés", "fièvre"],
                "Kiswahili": ["vidonda vya sehemu za siri", "kuvimba kwa tezi", "homa"],
                "Kinyarwanda": ["ibisebe ku gitsina", "inzira z’amaraso zabyimbye", "umuriro"]
            },
            "disease": {
                "English": "Syphilis",
                "French": "Syphilis",
                "Kiswahili": "Kaswende",
                "Kinyarwanda": "Sifirisi"
            },
            "advice": {
                "English": "Treat with penicillin injections and test partners.",
                "French": "Traitez avec des injections de pénicilline et testez les partenaires.",
                "Kiswahili": "Tibu kwa sindano za penicillin na pima wapenzi pia.",
                "Kinyarwanda": "Fata penicillin nk’inkingo kandi upimishe n’umukunzi wawe."
            }
        },
        {
            "symptoms": {
                "English": ["weight loss", "recurrent infections", "night sweats"],
                "French": ["perte de poids", "infections récurrentes", "sueurs nocturnes"],
                "Kiswahili": ["kupungua uzito", "maambukizi ya mara kwa mara", "kutokwa jasho usiku"],
                "Kinyarwanda": ["guta ibiro", "indwara zisubira", "kuzirana nijoro"]
            },
            "disease": {
                "English": "HIV/AIDS",
                "French": "VIH/SIDA",
                "Kiswahili": "VVU/UKIMWI",
                "Kinyarwanda": "SIDA"
            },
            "advice": {
                "English": "Start antiretroviral therapy (ART) immediately and maintain follow-up care.",
                "French": "Commencez immédiatement un traitement antirétroviral (TAR) et poursuivez les soins.",
                "Kiswahili": "Anza dawa za ARV mara moja na endelea na ufuatiliaji.",
                "Kinyarwanda": "Tangira imiti igabanya ubukana bw’agakoko ka SIDA kandi ukomeze ubukurikiranire."
            }
        },
        {
            "symptoms": {
                "English": ["fever", "chills", "body pain"],
                "French": ["fièvre", "frissons", "douleur corporelle"],
                "Kiswahili": ["homa", "kutetemeka", "maumivu ya mwili"],
                "Kinyarwanda": ["umuriro", "guhinda umuriro", "ububabare bw'umubiri"]
            },
            "disease": {
                "English": "Malaria",
                "French": "Paludisme",
                "Kiswahili": "Malaria",
                "Kinyarwanda": "Malariya"
            },
            "advice": {
                "English": "Antimalarial medication immediately.",
                "French": "Médicament antipaludique immédiatement.",
                "Kiswahili": "Tumia dawa ya malaria mara moja.",
                "Kinyarwanda": "Fata imiti ya malariya ako kanya."
            }
},
{
 "symptoms": {
                "English": ["chest pain", "arm numbness", "shortness of breath"],
                "French": ["douleur thoracique", "engourdissement du bras", "essoufflement"],
                "Kiswahili": ["maumivu ya kifua", "ganzi kwenye mkono", "kupumua kwa shida"],
                "Kinyarwanda": ["uburibwe mu gatuza", "kubura intege mu kuboko", "kubura umwuka"]
            },
            "disease": {
                "English": "Heart Attack",
                "French": "Crise cardiaque",
                "Kiswahili": "Mshutuko wa moyo",
                "Kinyarwanda": "Kugubwa n’umutima"
            },
            "advice": {
                "English": "Call emergency services immediately.",
                "French": "Appelez immédiatement les services d'urgence.",
                "Kiswahili": "Piga simu kwa huduma za dharura mara moja.",
                "Kinyarwanda": "Hamagara serivisi z’ubutabazi ako kanya."
            }
        },
        {
            "symptoms": {
                "English": ["palpitations", "fainting", "dizziness"],
                "French": ["palpitations", "évanouissement", "étourdissements"],
                "Kiswahili": ["mapigo ya moyo yasiyo ya kawaida", "kuzimia", "kizunguzungu"],
                "Kinyarwanda": ["umuvuduko w’umutima udasanzwe", "guta ubwenge", "guhuzagurika"]
            },
            "disease": {
                "English": "Arrhythmia",
                "French": "Arythmie",
                "Kiswahili": "Mapigo yasiyo ya kawaida ya moyo",
                "Kinyarwanda": "Imbeat y’umutima idasanzwe"
            },
            "advice": {
                "English": "ECG diagnosis and medications or surgery.",
                "French": "Diagnostic par ECG et traitement médicamenteux ou chirurgical.",
                "Kiswahili": "Utambuzi kwa ECG na dawa au upasuaji.",
                "Kinyarwanda": "Gusuzumwa ukoresheje ECG no kuvurwa n’imiti cyangwa kubagwa."
            }
        },
        {
            "symptoms": {
                "English": ["swelling in legs", "fatigue", "shortness of breath"],
                "French": ["gonflement des jambes", "fatigue", "essoufflement"],
                "Kiswahili": ["uvimbe miguuni", "uchovu", "kupumua kwa shida"],
                "Kinyarwanda": ["amaguru abyimbye", "umunaniro", "kubura umwuka"]
            },
            "disease": {
                "English": "Congestive Heart Failure",
                "French": "Insuffisance cardiaque congestive",
                "Kiswahili": "Kushindwa kwa moyo kusukuma damu",
                "Kinyarwanda": "Kunanirwa k’umutima gusunika amaraso"
            },
            "advice": {
                "English": "Take diuretics and limit salt intake.",
                "French": "Prenez des diurétiques et limitez la consommation de sel.",
                "Kiswahili": "Tumia dawa za kutoa maji na punguza chumvi.",
                "Kinyarwanda": "Fata imiti isohora amazi kandi ugabanye umunyu."
            }
        },
        {
            "symptoms": {
                "English": ["leg pain", "swelling", "warmth"],
                "French": ["douleur à la jambe", "gonflement", "chaleur"],
                "Kiswahili": ["maumivu ya mguu", "uvimbe", "joto kwenye eneo"],
                "Kinyarwanda": ["uburibwe mu kuguru", "kubyimba", "ubushyuhe aho hababara"]
            },
            "disease": {
                "English": "Deep Vein Thrombosis",
                "French": "Thrombose veineuse profonde",
                "Kiswahili": "Kuvimba kwa mshipa wa damu wa ndani",
                "Kinyarwanda": "Kuziba k’udutsi tw’amaraso twimbitse"
            },
            "advice": {
                "English": "Use blood thinners and avoid long sitting.",
                "French": "Prenez des anticoagulants et évitez de rester assis longtemps.",
                "Kiswahili": "Tumia dawa za kupunguza mgando wa damu na epuka kukaa muda mrefu.",
                "Kinyarwanda": "Fata imiti irinda amaraso gukomera kandi wirinde kwicara igihe kirekire."
            }
        },
        {
            "symptoms": {
                "English": ["blurred vision", "headache", "high blood pressure"],
                "French": ["vision floue", "mal de tête", "hypertension artérielle"],
                "Kiswahili": ["kuona kwa ukungu", "kichwa kuuma", "shinikizo la damu juu"],
                "Kinyarwanda": ["kutabona neza", "uburibwe bw’umutwe", "umuvuduko w’amaraso uri hejuru"]
            },
            "disease": {
                "English": "Hypertension",
                "French": "Hypertension artérielle",
                "Kiswahili": "Shinikizo la damu juu",
                "Kinyarwanda": "Umuvuduko w’amaraso uri hejuru"
            },
            "advice": {
                "English": "Lifestyle changes and antihypertensive drugs.",
                "French": "Changements de mode de vie et antihypertenseurs.",
                "Kiswahili": "Badilisha mtindo wa maisha na tumia dawa za kushusha shinikizo.",
                "Kinyarwanda": "Hindura imirire n’imyitwarire kandi ukoreshe imiti igabanya umuvuduko."
            }
},
{
"symptoms": {
                "English": ["seizures", "staring spells", "confusion"],
                "French": ["crises d’épilepsie", "regards fixes", "confusion"],
                "Kiswahili": ["degedege", "kutazunguka macho", "kuchanganyikiwa"],
                "Kinyarwanda": ["igifuruto", "guhanga amaso igihe kirekire", "kuyoba"]
            },
            "disease": {
                "English": "Epilepsy",
                "French": "Épilepsie",
                "Kiswahili": "Kifafa",
                "Kinyarwanda": "Ikinyabibiri"
            },
            "advice": {
                "English": "Take prescribed anticonvulsants.",
                "French": "Prenez les anticonvulsivants prescrits.",
                "Kiswahili": "Tumia dawa za kifafa kama ulivyoelekezwa.",
                "Kinyarwanda": "Fata imiti igabanya igifuruto nk’uko yategetswe."
            }
        },
        {
            "symptoms": {
                "English": ["hand tremor", "rigid muscles", "slow movement"],
                "French": ["tremblement des mains", "raideur musculaire", "mouvements lents"],
                "Kiswahili": ["mtetemeko wa mikono", "misuli migumu", "mwendo wa pole"],
                "Kinyarwanda": ["intoki zinyeganyega", "imitsi ikakaye", "kwimuka buhoro"]
            },
            "disease": {
                "English": "Parkinson’s Disease",
                "French": "Maladie de Parkinson",
                "Kiswahili": "Ugonjwa wa Parkinson",
                "Kinyarwanda": "Indwara ya Parkinson"
            },
            "advice": {
                "English": "Medication and therapy for movement.",
                "French": "Médicaments et thérapie pour le mouvement.",
                "Kiswahili": "Dawa na tiba ya kusaidia harakati.",
                "Kinyarwanda": "Imiti n’imyitozo ifasha kwimuka no kugenda neza."
            }
        },
        {
            "symptoms": {
                "English": ["loss of memory", "confusion", "trouble with speech"],
                "French": ["perte de mémoire", "confusion", "troubles de la parole"],
                "Kiswahili": ["kusahau", "kuchanganyikiwa", "ugumu wa kuzungumza"],
                "Kinyarwanda": ["kwibagirwa", "kuyoba", "kugorwa no kuvuga"]
            },
            "disease": {
                "English": "Alzheimer's Disease",
                "French": "Maladie d'Alzheimer",
                "Kiswahili": "Ugonjwa wa kusahau (Alzheimer)",
                "Kinyarwanda": "Indwara yo kwibagirwa (Alzheimer)"
            },
            "advice": {
                "English": "Supportive care and medications.",
                "French": "Soins de soutien et médicaments.",
                "Kiswahili": "Huduma ya kusaidia na dawa.",
                "Kinyarwanda": "Ubuvuzi bufasha n’imiti igabanya ubukana."
            }
        },
        {
            "symptoms": {
                "English": ["one-sided weakness", "drooping face", "slurred speech"],
                "French": ["faiblesse d’un côté", "visage tombant", "parole brouillée"],
                "Kiswahili": ["udhaifu upande mmoja", "uso kuanguka", "kutamka kwa shida"],
                "Kinyarwanda": ["intege nke ku ruhande rumwe", "isura igwa", "gucika ururimi"]
            },
            "disease": {
                "English": "Stroke",
                "French": "Accident vasculaire cérébral (AVC)",
                "Kiswahili": "Kiharusi",
                "Kinyarwanda": "Indwara yo guterwa n’amaraso adatembera mu bwonko"
            },
            "advice": {
                "English": "Emergency care and rehabilitation.",
                "French": "Soins d'urgence et rééducation.",
                "Kiswahili": "Huduma ya dharura na urejesho wa mwili.",
                "Kinyarwanda": "Ubutabazi bwihuse no kongera imyitozo yo gusubirana imbaraga."
            }
        },
        {
            "symptoms": {
                "English": ["headache", "sensitivity to light", "vomiting"],
                "French": ["mal de tête", "sensibilité à la lumière", "vomissements"],
                "Kiswahili": ["kichwa kuuma", "kuona mwangaza kunauma", "kutapika"],
                "Kinyarwanda": ["uburibwe bw’umutwe", "kwanga urumuri", "kuruka"]
            },
            "disease": {
                "English": "Migraine",
                "French": "Migraine",
                "Kiswahili": "Kichwa kinachouma mara kwa mara (Migraine)",
                "Kinyarwanda": "Migraine (Umutwe uhuruma cyane)"
            },
            "advice": {
                "English": "Avoid triggers, take pain relievers and rest.",
                "French": "Évitez les déclencheurs, prenez des analgésiques et reposez-vous.",
                "Kiswahili": "Epuka visababishi, tumia dawa za maumivu, na pumzika.",
                "Kinyarwanda": "Irinde ibibitera, fata imiti irwanya ububabare kandi uruhuke."
            }
},
{
 "symptoms": {
                "English": ["persistent sadness", "loss of interest", "fatigue"],
                "French": ["tristesse persistante", "perte d’intérêt", "fatigue"],
                "Kiswahili": ["huzuni ya muda mrefu", "kukosa hamu", "uchovu"],
                "Kinyarwanda": ["agahinda gahoraho", "kubura inyota y’ibikorwa", "umunaniro"]
            },
            "disease": {
                "English": "Depression",
                "French": "Dépression",
                "Kiswahili": "Msongo wa mawazo",
                "Kinyarwanda": "Agahinda gakabije"
            },
            "advice": {
                "English": "Talk therapy and antidepressants.",
                "French": "Thérapie par la parole et antidépresseurs.",
                "Kiswahili": "Tiba ya kuzungumza na dawa za msongo.",
                "Kinyarwanda": "Kuganira n’inzobere n’imiti igabanya agahinda."
            }
        },
        {
            "symptoms": {
                "English": ["worry", "restlessness", "racing thoughts"],
                "French": ["inquiétude", "agitation", "pensées rapides"],
                "Kiswahili": ["wasiwasi", "kutoishi mahali", "mawazo ya haraka"],
                "Kinyarwanda": ["impungenge", "kutisanzura", "ibitekerezo byinshi bitarangira"]
            },
            "disease": {
                "English": "Anxiety Disorder",
                "French": "Trouble anxieux",
                "Kiswahili": "Shida ya wasiwasi",
                "Kinyarwanda": "Indwara y’ubwoba buhoraho"
            },
            "advice": {
                "English": "Cognitive behavioral therapy and relaxation.",
                "French": "Thérapie comportementale cognitive et relaxation.",
                "Kiswahili": "Tiba ya kitabia na njia za kutuliza akili.",
                "Kinyarwanda": "Ubuvuzi bushingiye ku myitwarire no kuruhuka mu bitekerezo."
            }
        },
        {
            "symptoms": {
                "English": ["mood swings", "risky behavior", "irritability"],
                "French": ["sautes d’humeur", "comportement à risque", "irritabilité"],
                "Kiswahili": ["kubadilika kwa hisia", "tabia za hatari", "hasira"],
                "Kinyarwanda": ["guhinduka kw’amarangamutima", "imyitwarire iteye impungenge", "uburakari bwihuse"]
            },
            "disease": {
                "English": "Bipolar Disorder",
                "French": "Trouble bipolaire",
                "Kiswahili": "Matatizo ya kubadilika kwa hisia",
                "Kinyarwanda": "Indwara y’imihindagurikire y’amarangamutima"
            },
            "advice": {
                "English": "Mood stabilizers and therapy.",
                "French": "Stabilisateurs de l'humeur et thérapie.",
                "Kiswahili": "Dawa za kudhibiti hisia na tiba.",
                "Kinyarwanda": "Imiti itunganya amarangamutima n’ubujyanama."
            }
        },
        {
            "symptoms": {
                "English": ["hallucinations", "delusions", "confused thinking"],
                "French": ["hallucinations", "délires", "pensées confuses"],
                "Kiswahili": ["maono ya uongo", "imani potofu", "mawazo yaliyopotea"],
                "Kinyarwanda": ["kwibwira ibintu bitabayeho", "ibitekerezo bitari ukuri", "kudatekereza neza"]
            },
            "disease": {
                "English": "Schizophrenia",
                "French": "Schizophrénie",
                "Kiswahili": "Ugonjwa wa akili (Schizophrenia)",
                "Kinyarwanda": "Indwara yo kudatekereza neza (Schizophrenia)"
            },
            "advice": {
                "English": "Antipsychotics and psychosocial support.",
                "French": "Antipsychotiques et soutien psychosocial.",
                "Kiswahili": "Dawa za akili na msaada wa kijamii na kisaikolojia.",
                "Kinyarwanda": "Imiti igabanya uburwayi bwo mu mutwe n’ubufasha bwo mu buzima bw’imitekerereze n’imibanire."
            }
        },
        {
            "symptoms": {
                "English": ["difficulty concentrating", "hyperactivity", "impulsiveness"],
                "French": ["difficulté de concentration", "hyperactivité", "impulsivité"],
                "Kiswahili": ["ugumu wa kuzingatia", "kuwa na harakati nyingi", "kutotulia"],
                "Kinyarwanda": ["kubura ubushobozi bwo kwibanda", "guhora uhaguruka", "gukora ibintu utabanje gutekereza"]
            },
            "disease": {
                "English": "ADHD",
                "French": "TDAH (Trouble de déficit de l’attention avec hyperactivité)",
                "Kiswahili": "ADHD (Matatizo ya umakini na kuhamahama)",
                "Kinyarwanda": "ADHD (Guhorana umuvuduko no kudafata ibintu nk’abandi)"
            },
            "advice": {
                "English": "Behavioral therapy and medication.",
                "French": "Thérapie comportementale et médicaments.",
                "Kiswahili": "Tiba ya kitabia na dawa.",
                "Kinyarwanda": "Ubujyanama ku myitwarire hamwe n’imiti."
            }
},
{
"symptoms": {
                "English": ["fatigue", "weight gain", "dry skin"],
                "French": ["fatigue", "prise de poids", "peau sèche"],
                "Kiswahili": ["uchovu", "kuongezeka uzito", "ngozi kavu"],
                "Kinyarwanda": ["umunaniro", "kubyibuha", "uruhu rwumye"]
            },
            "disease": {
                "English": "Hypothyroidism",
                "French": "Hypothyroïdie",
                "Kiswahili": "Upungufu wa homoni ya tezi",
                "Kinyarwanda": "Kutagira imisemburo ihagije ya thyroid"
            },
            "advice": {
                "English": "Thyroid hormone replacement.",
                "French": "Traitement substitutif de l’hormone thyroïdienne.",
                "Kiswahili": "Tumia dawa za kuongeza homoni ya tezi.",
                "Kinyarwanda": "Fata imisemburo isimbura iyabaye nkeya ya thyroid."
            }
        },
        {
            "symptoms": {
                "English": ["weight loss", "frequent urination", "blurred vision"],
                "French": ["perte de poids", "urination fréquente", "vision floue"],
                "Kiswahili": ["kupungua uzito", "kukojoa mara kwa mara", "kuona kwa ukungu"],
                "Kinyarwanda": ["guta ibiro", "kujya kunyara kenshi", "kutabona neza"]
            },
            "disease": {
                "English": "Type 1 Diabetes",
                "French": "Diabète de type 1",
                "Kiswahili": "Kisukari aina ya 1",
                "Kinyarwanda": "Diabete yo mu bwoko bwa mbere"
            },
            "advice": {
                "English": "Insulin therapy and diet control.",
                "French": "Traitement à l’insuline et contrôle alimentaire.",
                "Kiswahili": "Tumia insulini na udhibiti lishe.",
                "Kinyarwanda": "Koresha insuline no kugenzura ibyo urya."
            }
        },
        {
            "symptoms": {
                "English": ["acne", "irregular periods", "excess hair"],
                "French": ["acné", "règles irrégulières", "pilosité excessive"],
                "Kiswahili": ["mapele", "hedhi isiyo ya kawaida", "nywele nyingi mwilini"],
                "Kinyarwanda": ["udukovu", "imihango itameze neza", "ubwoya bwinshi ku mubiri"]
            },
            "disease": {
                "English": "Polycystic Ovary Syndrome (PCOS)",
                "French": "Syndrome des ovaires polykystiques (SOPK)",
                "Kiswahili": "PCOS (Ugonjwa wa ovari zenye uvimbe)",
                "Kinyarwanda": "PCOS (Indwara y’udukoko twinshi ku dusabo tw’intanga)"
            },
            "advice": {
                "English": "Hormonal treatment and exercise.",
                "French": "Traitement hormonal et exercice physique.",
                "Kiswahili": "Tiba ya homoni na mazoezi.",
                "Kinyarwanda": "Imiti y’imisemburo n’imyitozo ngororamubiri."
            }
        },
        {
            "symptoms": {
                "English": ["irritability", "sweating", "shaking"],
                "French": ["irritabilité", "transpiration", "tremblements"],
                "Kiswahili": ["hasira", "kutokwa jasho", "kutetemeka"],
                "Kinyarwanda": ["uburakari", "kuzira ibyuya", "kunyeganyega"]
            },
            "disease": {
                "English": "Hypoglycemia",
                "French": "Hypoglycémie",
                "Kiswahili": "Upungufu wa sukari kwenye damu",
                "Kinyarwanda": "Isukari nke mu maraso (Hypoglycemia)"
            },
            "advice": {
                "English": "Immediate intake of sugar or glucose.",
                "French": "Prendre immédiatement du sucre ou du glucose.",
                "Kiswahili": "Kunywa au kula sukari haraka iwezekanavyo.",
                "Kinyarwanda": "Fata isukari cyangwa glucose ako kanya."
            }
        },
        {
            "symptoms": {
                "English": ["excessive hunger", "weight loss", "fatigue"],
                "French": ["faim excessive", "perte de poids", "fatigue"],
                "Kiswahili": ["njaa kupita kiasi", "kupungua uzito", "uchovu"],
                "Kinyarwanda": ["inzara ikabije", "guta ibiro", "umunaniro"]
            },
            "disease": {
                "English": "Hyperthyroidism",
                "French": "Hyperthyroïdie",
                "Kiswahili": "Uzalishaji mkubwa wa homoni ya tezi",
                "Kinyarwanda": "Kugira imisemburo myinshi ya thyroid"
            },
            "advice": {
                "English": "Antithyroid meds and monitoring.",
                "French": "Médicaments antithyroïdiens et suivi médical.",
                "Kiswahili": "Dawa za kupunguza homoni ya tezi na ufuatiliaji.",
                "Kinyarwanda": "Imiti igabanya imisemburo ya thyroid no kuyikurikiranira hafi."
            }
},
{
 "symptoms": {
                "English": ["pelvic pain", "heavy periods", "painful intercourse"],
                "French": ["douleur pelvienne", "règles abondantes", "rapports sexuels douloureux"],
                "Kiswahili": ["maumivu ya nyonga", "hedhi nzito", "maumivu wakati wa tendo la ndoa"],
                "Kinyarwanda": ["uburibwe mu nda yo hepfo", "imihango myinshi", "uburibwe mu gihe cy’imibonano"]
            },
            "disease": {
                "English": "Endometriosis",
                "French": "Endométriose",
                "Kiswahili": "Endometriosis",
                "Kinyarwanda": "Endometriose"
            },
            "advice": {
                "English": "Hormonal therapy and surgery.",
                "French": "Traitement hormonal et chirurgie.",
                "Kiswahili": "Tiba ya homoni na upasuaji.",
                "Kinyarwanda": "Imiti y’imisemburo n’ubuvuzi bwo kubagwa."
            }
        },
        {
            "symptoms": {
                "English": ["morning sickness", "missed period", "tender breasts"],
                "French": ["nausées matinales", "absence de règles", "seins sensibles"],
                "Kiswahili": ["kichefuchefu asubuhi", "kukosa hedhi", "matiti kuuma"],
                "Kinyarwanda": ["isoka mu gitondo", "kubura imihango", "amasohoro ababara"]
            },
            "disease": {
                "English": "Pregnancy",
                "French": "Grossesse",
                "Kiswahili": "Ujauzito",
                "Kinyarwanda": "Gutwita"
            },
            "advice": {
                "English": "Confirm with test and start prenatal care.",
                "French": "Confirmez avec un test et commencez les soins prénatals.",
                "Kiswahili": "Thibitisha kwa kipimo na uanze huduma za kliniki ya wajawazito.",
                "Kinyarwanda": "Emeza ukoresheje ikizamini hanyuma utangire kwitabwaho nk’umugore utwite."
            }
        },
        {
            "symptoms": {
                "English": ["hot flashes", "irregular periods", "night sweats"],
                "French": ["bouffées de chaleur", "règles irrégulières", "sueurs nocturnes"],
                "Kiswahili": ["hali ya joto ghafla", "hedhi isiyo ya kawaida", "kutokwa jasho usiku"],
                "Kinyarwanda": ["kumva ubushyuhe bwinshi", "imihango idahoraho", "kuzirana nijoro"]
            },
            "disease": {
                "English": "Menopause",
                "French": "Ménopause",
                "Kiswahili": "Hali ya kukoma hedhi (Menopause)",
                "Kinyarwanda": "Guhagarika imihango (Menopause)"
            },
            "advice": {
                "English": "Hormone therapy and lifestyle management.",
                "French": "Traitement hormonal et gestion du mode de vie.",
                "Kiswahili": "Tiba ya homoni na mabadiliko ya mtindo wa maisha.",
                "Kinyarwanda": "Imiti y’imisemburo no guhindura imirire n’imyitwarire."
            }
        },
        {
            "symptoms": {
                "English": ["vaginal itching", "discharge", "odor"],
                "French": ["démangeaisons vaginales", "écoulement", "odeur"],
                "Kiswahili": ["muwasho ukenge", "uchafu", "harufu mbaya"],
                "Kinyarwanda": ["kuribwa mu gitsina", "amazi asohoka", "impumuro mbi"]
            },
            "disease": {
                "English": "Yeast Infection",
                "French": "Infection à levures",
                "Kiswahili": "Maambukizi ya fangasi ukenge",
                "Kinyarwanda": "Indwara iterwa na bagiteri mu gitsina"
            },
            "advice": {
                "English": "Antifungal medication.",
                "French": "Médicament antifongique.",
                "Kiswahili": "Dawa za kuua fangasi.",
                "Kinyarwanda": "Imiti yica udukoko twitwa fungi."
            }
        },
        {
            "symptoms": {
                "English": ["abdominal pain", "no period", "positive test"],
                "French": ["douleur abdominale", "pas de règles", "test positif"],
                "Kiswahili": ["maumivu ya tumbo", "hakuna hedhi", "kipimo chanya"],
                "Kinyarwanda": ["uburibwe mu nda", "kubura imihango", "ikizamini cyerekana ko utwite"]
            },
            "disease": {
                "English": "Ectopic Pregnancy",
                "French": "Grossesse extra-utérine",
                "Kiswahili": "Mimba ya nje ya mfuko wa uzazi",
                "Kinyarwanda": "Gutwita mu buryo butari busanzwe (muri trompe)"
            },
            "advice": {
                "English": "Requires urgent surgery or medication.",
                "French": "Nécessite une chirurgie ou un traitement d'urgence.",
                "Kiswahili": "Inahitaji upasuaji wa haraka au dawa.",
                "Kinyarwanda": "Bisaba kubagwa cyangwa guhabwa imiti byihuse."
            }
},
{

            "symptoms": {
                "English": ["rash", "fever", "swollen glands"],
                "French": ["éruption cutanée", "fièvre", "glandes enflées"],
                "Kiswahili": ["vipele", "homa", "tezi kuvimba"],
                "Kinyarwanda": ["ibisebe ku mubiri", "umuriro", "impyiko zabyimbye"]
            },
            "disease": {
                "English": "Rubella",
                "French": "Rubéole",
                "Kiswahili": "Rubela",
                "Kinyarwanda": "Rubeyile"
            },
            "advice": {
                "English": "Rest and vaccination prevention.",
                "French": "Repos et prévention par vaccination.",
                "Kiswahili": "Pumzika na chanjo kwa kinga.",
                "Kinyarwanda": "Kuruhuka no gukingirwa nk’uburyo bwo kwirinda."
            }
        },
        {
            "symptoms": {
                "English": ["high fever", "seizure", "stiff limbs"],
                "French": ["forte fièvre", "crise convulsive", "membres raides"],
                "Kiswahili": ["homa kali", "degedege", "viungo kuwa ngumu"],
                "Kinyarwanda": ["umuriro mwinshi", "igifuruto", "ingingo zikakaye"]
            },
            "disease": {
                "English": "Febrile Seizure",
                "French": "Convulsions fébriles",
                "Kiswahili": "Kifafa kinachosababishwa na homa",
                "Kinyarwanda": "Igifuruto giturutse ku muriro"
            },
            "advice": {
                "English": "Control fever and seek care.",
                "French": "Contrôlez la fièvre et consultez un médecin.",
                "Kiswahili": "Dhibiti homa na tafuta huduma ya afya.",
                "Kinyarwanda": "Gabanya umuriro kandi ushake ubufasha kwa muganga."
            }
        },
        {
            "symptoms": {
                "English": ["diarrhea", "vomiting", "sunken eyes"],
                "French": ["diarrhée", "vomissements", "yeux enfoncés"],
                "Kiswahili": ["kuharisha", "kutapika", "macho kuingia ndani"],
                "Kinyarwanda": ["impiswi", "kuruka", "amaso yinjira imbere"]
            },
            "disease": {
                "English": "Dehydration",
                "French": "Déshydratation",
                "Kiswahili": "Upungufu wa maji mwilini",
                "Kinyarwanda": "Kunanirwa n’amazi mu mubiri"
            },
            "advice": {
                "English": "Use ORS and monitor fluid intake.",
                "French": "Utilisez des SRO et surveillez l’apport en liquides.",
                "Kiswahili": "Tumia ORS na fatilia unywaji wa maji.",
                "Kinyarwanda": "Koresha ORS kandi ukurikirane uko umwana anywa amazi."
            }
        },
        {
            "symptoms": {
                "English": ["crying during urination", "frequent wetting"],
                "French": ["pleurs pendant la miction", "mictions fréquentes"],
                "Kiswahili": ["kulia wakati wa kukojoa", "kukojoa mara kwa mara"],
                "Kinyarwanda": ["kurira mu gihe cyo kwihagarika", "kwihagarika kenshi"]
            },
            "disease": {
                "English": "UTI in Children",
                "French": "Infection urinaire chez l’enfant",
                "Kiswahili": "Maambukizi ya njia ya mkojo kwa watoto",
                "Kinyarwanda": "Uburwayi bwo mu miyoboro y’inkari mu bana"
            },
            "advice": {
                "English": "Antibiotics and fluids.",
                "French": "Antibiotiques et hydratation.",
                "Kiswahili": "Dawa za viuavijasumu na maji ya kutosha.",
                "Kinyarwanda": "Antibiotiques n’amazi menshi yo kunywa."
            }
        },
        {
            "symptoms": {
                "English": ["irritability", "ear pulling", "fever"],
                "French": ["irritabilité", "tirage d’oreille", "fièvre"],
                "Kiswahili": ["hasira", "kuvuta sikio", "homa"],
                "Kinyarwanda": ["umujinya", "gukurura ugutwi", "umuriro"]
            },
            "disease": {
                "English": "Otitis Media",
                "French": "Otite moyenne",
                "Kiswahili": "Maambukizi ya sikio la kati",
                "Kinyarwanda": "Indwara y’ugutwi kw’imbere"
            },
            "advice": {
                "English": "Pain relief and antibiotics.",
                "French": "Analgésiques et antibiotiques.",
                "Kiswahili": "Dawa ya maumivu na viuavijasumu.",
                "Kinyarwanda": "Imiti igabanya ububabare n’antibiotiques."
            }
},
{
"symptoms": {
                "English": ["red itchy patches", "scaly skin", "flaking"],
                "French": ["plaques rouges qui démangent", "peau squameuse", "desquamation"],
                "Kiswahili": ["madoa mekundu yenye muwasho", "ngozi inayokauka kama magamba", "ngozi kung’oka"],
                "Kinyarwanda": ["utudomo dutukura tw’iribwa", "uruhu rukanyaraye", "uruhu rushirira"]
            },
            "disease": {
                "English": "Psoriasis",
                "French": "Psoriasis",
                "Kiswahili": "Psoriasis",
                "Kinyarwanda": "Psoriasis (uruhu rwumagara rukanishya)"
            },
            "advice": {
                "English": "Use corticosteroids and moisturizers.",
                "French": "Utilisez des corticostéroïdes et des hydratants.",
                "Kiswahili": "Tumia steroidi na krimu za kulainisha ngozi.",
                "Kinyarwanda": "Koresha imiti ya corticostéroïdes n’amavuta yoroshya uruhu."
            }
        },
        {
            "symptoms": {
                "English": ["toothache", "swelling", "bad breath"],
                "French": ["mal de dents", "gonflement", "mauvaise haleine"],
                "Kiswahili": ["maumivu ya jino", "uvimbe", "harufu mbaya mdomoni"],
                "Kinyarwanda": ["kuribwa amenyo", "kubyimba", "impumuro mbi mu kanwa"]
            },
            "disease": {
                "English": "Dental Abscess",
                "French": "Abcès dentaire",
                "Kiswahili": "Majipu ya jino",
                "Kinyarwanda": "Isebe y’iryinyo (Abcès)"
            },
            "advice": {
                "English": "Drain the abscess and use antibiotics.",
                "French": "Drainer l’abcès et prendre des antibiotiques.",
                "Kiswahili": "Toa usaha na tumia viuavijasumu.",
                "Kinyarwanda": "Kuriramo iryinyo ryabaye isesemi no gufata antibiotics."
            }
        },
        {
            "symptoms": {
                "English": ["red eye", "itching", "discharge"],
                "French": ["œil rouge", "démangeaisons", "écoulement"],
                "Kiswahili": ["jicho jekundu", "muwasho", "uchafu kutoka jichoni"],
                "Kinyarwanda": ["ijisho ritukura", "kuribwa", "gusohora amazi"]
            },
            "disease": {
                "English": "Conjunctivitis",
                "French": "Conjonctivite",
                "Kiswahili": "Konjaktivaitisi (macho kuwasha)",
                "Kinyarwanda": "Conjunctivite (indwara y’ijisho ritukura)"
            },
            "advice": {
                "English": "Clean the eye and use eye drops.",
                "French": "Nettoyez l’œil et utilisez des gouttes ophtalmiques.",
                "Kiswahili": "Safisha jicho na tumia dawa za matone ya jicho.",
                "Kinyarwanda": "Sukura ijisho ukoresheje amazi meza kandi ukoreshe amavuta y’ijisho."
            }
        },
        {
            "symptoms": {
                "English": ["double vision", "eye pressure", "halos around light"],
                "French": ["vision double", "pression oculaire", "halos autour des lumières"],
                "Kiswahili": ["kuona mara mbili", "msukumo jichoni", "miali ya mwanga kuzunguka taa"],
                "Kinyarwanda": ["kureba ibintu bibiri", "igitutu mu jisho", "imijyana y’urumuri ku rumuri"]
            },
            "disease": {
                "English": "Glaucoma",
                "French": "Glaucome",
                "Kiswahili": "Glaukoma",
                "Kinyarwanda": "Glaucome (igitutu cy’ijisho)"
            },
            "advice": {
                "English": "Use eye pressure-lowering medication.",
                "French": "Utilisez des médicaments pour réduire la pression oculaire.",
                "Kiswahili": "Tumia dawa za kupunguza presha ya jicho.",
                "Kinyarwanda": "Koresha imiti igabanya igitutu cy’ijisho."
            }
        },
        {
            "symptoms": {
                "English": ["white spot on eye", "blurred vision", "light sensitivity"],
                "French": ["tache blanche sur l’œil", "vision floue", "sensibilité à la lumière"],
                "Kiswahili": ["madoa meupe jichoni", "kuona kwa ukungu", "kusumbuliwa na mwangaza"],
                "Kinyarwanda": ["ikizinga cy’umweru mu jisho", "kutabona neza", "kwanga urumuri"]
            },
            "disease": {
                "English": "Corneal Ulcer",
                "French": "Ulcère cornéen",
                "Kiswahili": "Kidonda cha konia ya jicho",
                "Kinyarwanda": "Igisebe ku gice cy’ijisho (cornea)"
            },
            "advice": {
                "English": "Urgent ophthalmology treatment.",
                "French": "Traitement ophtalmologique urgent.",
                "Kiswahili": "Tiba ya haraka ya daktari wa macho.",
                "Kinyarwanda": "Kwihutira kwa muganga w’amaso kugira ngo atange ubuvuzi."
            }
},
{
 "symptoms": {
                "English": ["nausea", "acid reflux", "chest discomfort"],
                "French": ["nausée", "reflux acide", "gêne thoracique"],
                "Kiswahili": ["kichefuchefu", "rejea ya asidi", "maumivu ya kifua"],
                "Kinyarwanda": ["isoka", "kwijujubika kwa aside", "kubabara mu gatuza"]
            },
            "disease": {
                "English": "GERD",
                "French": "RGO (reflux gastro-œsophagien)",
                "Kiswahili": "GERD (Reflux ya asidi tumboni)",
                "Kinyarwanda": "GERD (gutengurwa kw’aside iva mu gifu ijya mu muhogo)"
            },
            "advice": {
                "English": "Avoid spicy food and use antacids.",
                "French": "Évitez les aliments épicés et utilisez des antiacides.",
                "Kiswahili": "Epuka chakula chenye pilipili na tumia dawa za asidi.",
                "Kinyarwanda": "Irinde ibiryo bikaze kandi ukoreshe imiti igabanya aside."
            }
        },
        {
            "symptoms": {
                "English": ["blood in stool", "constipation", "pain"],
                "French": ["sang dans les selles", "constipation", "douleur"],
                "Kiswahili": ["damu kwenye kinyesi", "kukosa choo", "maumivu"],
                "Kinyarwanda": ["amaraso mu musarane", "kubura inkari", "uburibwe"]
            },
            "disease": {
                "English": "Hemorrhoids",
                "French": "Hémorroïdes",
                "Kiswahili": "Mba (Hemoroidi)",
                "Kinyarwanda": "Imbabura (Hemoroide)"
            },
            "advice": {
                "English": "Use stool softeners and avoid straining.",
                "French": "Utilisez des émollients fécaux et évitez de forcer.",
                "Kiswahili": "Tumia dawa lainishi ya kinyesi na epuka kusukuma sana.",
                "Kinyarwanda": "Koresha imiti yoroshya umusarane kandi wirinde kwishyiraho igitutu."
            }
        },
        {
            "symptoms": {
                "English": ["flank pain", "frequent urination", "fever"],
                "French": ["douleur au flanc", "urination fréquente", "fièvre"],
                "Kiswahili": ["maumivu ya mbavu", "kukojoa mara kwa mara", "homa"],
                "Kinyarwanda": ["uburibwe ku mbavu", "kujya kwihagarika kenshi", "umuriro"]
            },
            "disease": {
                "English": "Kidney Stones",
                "French": "Calculs rénaux",
                "Kiswahili": "Mawe kwenye figo",
                "Kinyarwanda": "Amabuye mu mpyiko"
            },
            "advice": {
                "English": "Pain relief and possibly lithotripsy.",
                "French": "Soulagement de la douleur et éventuellement lithotritie.",
                "Kiswahili": "Dawa za maumivu na labda upasuaji wa kuvunja mawe.",
                "Kinyarwanda": "Imiti igabanya ububabare cyangwa gukuramo amabuye ukoresheje imashini."
            }
        },
        {
            "symptoms": {
                "English": ["bloating", "cramps", "alternating constipation/diarrhea"],
                "French": ["ballonnements", "crampes", "constipation/diarrhée alternée"],
                "Kiswahili": ["tumbo kujaa", "mashambulizi ya tumbo", "choo kigumu na kuharisha kwa zamu"],
                "Kinyarwanda": ["kubyimba inda", "imvune mu nda", "kugenda ubura n’impiswi byisimburanya"]
            },
            "disease": {
                "English": "IBS",
                "French": "SII (Syndrome de l’intestin irritable)",
                "Kiswahili": "IBS (Syndrome ya utumbo usiotulia)",
                "Kinyarwanda": "IBS (Indwara y’urusobe rw’amatembabuzi mu mara)"
            },
            "advice": {
                "English": "Fiber diet and stress management.",
                "French": "Régime riche en fibres et gestion du stress.",
                "Kiswahili": "Lishe yenye nyuzi nyuzi na udhibiti wa msongo.",
                "Kinyarwanda": "Imirire irimo fibre no kugabanya stress."
            }
        },
        {
            "symptoms": {
                "English": ["dark urine", "fever", "back pain"],
                "French": ["urine foncée", "fièvre", "douleur au dos"],
                "Kiswahili": ["mkojo wa rangi ya giza", "homa", "maumivu ya mgongo"],
                "Kinyarwanda": ["inkari z’umukara", "umuriro", "ububabare mu mugongo"]
            },
            "disease": {
                "English": "Pyelonephritis",
                "French": "Pyélonéphrite",
                "Kiswahili": "Pyelonephritis (Maambukizi ya figo)",
                "Kinyarwanda": "Pyelonephritis (Indwara y’uruhago rw’inkari)"
            },
            "advice": {
                "English": "Antibiotics and hydration.",
                "French": "Antibiotiques et hydratation.",
                "Kiswahili": "Viuavijasumu na unywaji wa maji wa kutosha.",
                "Kinyarwanda": "Antibiotiques no kunywa amazi menshi."
            }
},
{
 "symptoms": {
                "English": ["joint pain", "morning stiffness", "fatigue"],
                "French": ["douleur articulaire", "raideur matinale", "fatigue"],
                "Kiswahili": ["maumivu ya viungo", "ukakasi asubuhi", "uchovu"],
                "Kinyarwanda": ["uburibwe mu ngingo", "kugira ingingo zikakaye mu gitondo", "umunaniro"]
            },
            "disease": {
                "English": "Rheumatoid Arthritis",
                "French": "Polyarthrite rhumatoïde",
                "Kiswahili": "Uvimbe wa viungo (Rheumatoid Arthritis)",
                "Kinyarwanda": "Guturika kw’ingingo (Rheumatoid Arthritis)"
            },
            "advice": {
                "English": "Use DMARDs and pain relief medications.",
                "French": "Utilisez des DMARD et des antalgiques.",
                "Kiswahili": "Tumia dawa za DMARD na za kutuliza maumivu.",
                "Kinyarwanda": "Koresha imiti yo kuvura indwara z’ingingo no kugabanya ububabare."
            }
        },
        {
            "symptoms": {
                "English": ["muscle weakness", "difficulty swallowing", "drooping eyelids"],
                "French": ["faiblesse musculaire", "difficulté à avaler", "paupières tombantes"],
                "Kiswahili": ["udhaifu wa misuli", "ugumu kumeza", "macho kushuka"],
                "Kinyarwanda": ["intege nke mu misokoro", "kugorwa no kumira", "amababa y’ijisho amanuka"]
            },
            "disease": {
                "English": "Myasthenia Gravis",
                "French": "Myasthénie grave",
                "Kiswahili": "Myasthenia Gravis",
                "Kinyarwanda": "Myasthenia Gravis"
            },
            "advice": {
                "English": "Anticholinesterase meds and immunotherapy.",
                "French": "Médicaments anticholinestérasiques et immunothérapie.",
                "Kiswahili": "Dawa za anticholinesterase na tiba ya kinga.",
                "Kinyarwanda": "Imiti igabanya cholinesterase n’ubuvuzi bwo kongera ubudahangarwa."
            }
        },
        {
            "symptoms": {
                "English": ["fatigue", "mouth ulcers", "butterfly rash on face"],
                "French": ["fatigue", "ulcères buccaux", "éruption en forme de papillon sur le visage"],
                "Kiswahili": ["uchovu", "vidonda mdomoni", "madoa ya papiloni usoni"],
                "Kinyarwanda": ["umunaniro", "udusebe mu kanwa", "isura ifite uruhu rufite ishusho ya papillon"]
            },
            "disease": {
                "English": "Lupus (SLE)",
                "French": "Lupus (LES)",
                "Kiswahili": "Lupus (SLE)",
                "Kinyarwanda": "Lupus (SLE)"
            },
            "advice": {
                "English": "Steroids and immunosuppressants.",
                "French": "Corticostéroïdes et immunosuppresseurs.",
                "Kiswahili": "Dawa za steroid na za kupunguza kinga mwilini.",
                "Kinyarwanda": "Imiti ya steroid n’iyo igabanya ubudahangarwa."
            }
        },
        {
            "symptoms": {
                "English": ["dry eyes", "dry mouth", "joint pain"],
                "French": ["yeux secs", "bouche sèche", "douleurs articulaires"],
                "Kiswahili": ["macho makavu", "mdomo mkavu", "maumivu ya viungo"],
                "Kinyarwanda": ["ijisho ryumye", "umunwa wumye", "ububabare mu ngingo"]
            },
            "disease": {
                "English": "Sjögren’s Syndrome",
                "French": "Syndrome de Sjögren",
                "Kiswahili": "Syndrome ya Sjögren",
                "Kinyarwanda": "Syndrome ya Sjögren"
            },
            "advice": {
                "English": "Hydration, eye drops, and immune therapy.",
                "French": "Hydratation, gouttes pour les yeux et immunothérapie.",
                "Kiswahili": "Unywaji wa maji, matone ya macho na tiba ya kinga.",
                "Kinyarwanda": "Kunywa amazi, amavuta y’amaso, n’ubuvuzi bwo kongera ubudahangarwa."
            }
        },
        {
            "symptoms": {
                "English": ["muscle pain", "sleep issues", "fatigue"],
                "French": ["douleurs musculaires", "troubles du sommeil", "fatigue"],
                "Kiswahili": ["maumivu ya misuli", "matatizo ya usingizi", "uchovu"],
                "Kinyarwanda": ["ububabare bw’imikaya", "ibibazo byo gusinzira", "umunaniro"]
            },
            "disease": {
                "English": "Fibromyalgia",
                "French": "Fibromyalgie",
                "Kiswahili": "Fibromyalgia",
                "Kinyarwanda": "Fibromyalgia"
            },
            "advice": {
                "English": "Exercise, antidepressants, and lifestyle therapy.",
                "French": "Exercice, antidépresseurs et thérapie du mode de vie.",
                "Kiswahili": "Mazoezi, dawa za msongo wa mawazo na tiba ya maisha.",
                "Kinyarwanda": "Imyitozo, imiti igabanya agahinda no guhindura imyitwarire y’ubuzima."
            }
        },
        {
            "symptoms": {
                "English": ["skin hardening", "Raynaud’s phenomenon", "heartburn"],
                "French": ["durcissement de la peau", "phénomène de Raynaud", "brûlures d’estomac"],
                "Kiswahili": ["ngozi kuwa ngumu", "dalili za Raynaud", "kuungua kwa kifua"],
                "Kinyarwanda": ["uruhu rukomera", "Raynaud’s (intoki zihindura ibara)", "kubabara mu gatuza"]
            },
            "disease": {
                "English": "Scleroderma",
                "French": "Sclérodermie",
                "Kiswahili": "Scleroderma",
                "Kinyarwanda": "Scleroderma"
            },
            "advice": {
                "English": "Vasodilators and symptom-specific treatment.",
                "French": "Vasodilatateurs et traitement symptomatique.",
                "Kiswahili": "Dawa za kupanua mishipa na tiba ya dalili maalum.",
                "Kinyarwanda": "Imiti yongera umuvuduko w’amaraso n’ubuvuzi bwihariye ku bimenyetso."
            }
},
{
"symptoms": {
                "English": ["knee pain", "joint stiffness", "swelling"],
                "French": ["douleur au genou", "raideur articulaire", "gonflement"],
                "Kiswahili": ["maumivu ya goti", "ukakasi wa viungo", "uvimbe"],
                "Kinyarwanda": ["ububabare mu ivi", "gukakara kw’ingingo", "kubyimba"]
            },
            "disease": {
                "English": "Osteoarthritis",
                "French": "Arthrose",
                "Kiswahili": "Osteoarthritis",
                "Kinyarwanda": "Osteoarthritis (gusaza kw’ingingo)"
            },
            "advice": {
                "English": "NSAIDs, physical therapy, and joint care.",
                "French": "AINS, kinésithérapie et soins articulaires.",
                "Kiswahili": "Dawa za kuondoa maumivu (NSAIDs), mazoezi na uangalizi wa viungo.",
                "Kinyarwanda": "Imiti igabanya ububabare (NSAIDs), imyitozo ngororamubiri no kwitaho ingingo."
            }
        },
        {
            "symptoms": {
                "English": ["back pain", "numbness in legs", "weakness"],
                "French": ["douleur au dos", "engourdissement des jambes", "faiblesse"],
                "Kiswahili": ["maumivu ya mgongo", "miguu kufa ganzi", "udhaifu"],
                "Kinyarwanda": ["ububabare mu mugongo", "kubura amarangamutima mu maguru", "intege nke"]
            },
            "disease": {
                "English": "Herniated Disc",
                "French": "Hernie discale",
                "Kiswahili": "Diski iliyoteleza",
                "Kinyarwanda": "Disiki yasohotse (Herniated Disc)"
            },
            "advice": {
                "English": "Rest, physical therapy, and surgery if severe.",
                "French": "Repos, kinésithérapie et chirurgie si nécessaire.",
                "Kiswahili": "Pumzika, fanya mazoezi ya mwili, na upasuaji kama ni mbaya.",
                "Kinyarwanda": "Kuruhuka, gukora imyitozo ngororamubiri, no kubagwa niba bikomeye."
            }
        },
        {
            "symptoms": {
                "English": ["bone pain", "fractures", "height loss"],
                "French": ["douleur osseuse", "fractures", "perte de taille"],
                "Kiswahili": ["maumivu ya mifupa", "mifupa kuvunjika", "kupungua urefu wa mwili"],
                "Kinyarwanda": ["ububabare mu magufa", "kumena amagufa", "kugabanuka ku burebure"]
            },
            "disease": {
                "English": "Osteoporosis",
                "French": "Ostéoporose",
                "Kiswahili": "Osteoporosis",
                "Kinyarwanda": "Osteoporosis (amagufa atangiye kworoha)"
            },
            "advice": {
                "English": "Calcium, vitamin D, and bisphosphonates.",
                "French": "Calcium, vitamine D et bisphosphonates.",
                "Kiswahili": "Calcium, vitamini D na dawa za bisphosphonate.",
                "Kinyarwanda": "Calcium, vitamine D, n’imiti ya bisphosphonates."
            }
},
{
 "symptoms": {
                "English": ["pale skin", "fatigue", "shortness of breath"],
                "French": ["peau pâle", "fatigue", "essoufflement"],
                "Kiswahili": ["ngozi kuwa ya rangi hafifu", "uchovu", "kupumua kwa shida"],
                "Kinyarwanda": ["uruhu ruciye intege", "umunaniro", "kubura umwuka"]
            },
            "disease": {
                "English": "Iron Deficiency Anemia",
                "French": "Anémie par carence en fer",
                "Kiswahili": "Upungufu wa damu kutokana na chuma",
                "Kinyarwanda": "Anemia iterwa n’iburabura ry’icyuma (Fer)"
            },
            "advice": {
                "English": "Iron supplements and dietary changes.",
                "French": "Suppléments de fer et modifications alimentaires.",
                "Kiswahili": "Vidonge vya chuma na mabadiliko ya lishe.",
                "Kinyarwanda": "Ifunguro ririmo icyuma (fer) n’imiti y’inyongera ya fer."
            }
        },
        {
            "symptoms": {
                "English": ["frequent infections", "easy bruising", "fatigue"],
                "French": ["infections fréquentes", "ecchymoses faciles", "fatigue"],
                "Kiswahili": ["maambukizi ya mara kwa mara", "kupata michubuko kirahisi", "uchovu"],
                "Kinyarwanda": ["kwandura kenshi", "gukubitika byoroshye", "umunaniro"]
            },
            "disease": {
                "English": "Leukemia",
                "French": "Leucémie",
                "Kiswahili": "Leukemia",
                "Kinyarwanda": "Leukemia (kanseri y’amaraso)"
            },
            "advice": {
                "English": "Chemotherapy and hematologist care.",
                "French": "Chimiothérapie et soins par un hématologue.",
                "Kiswahili": "Tiba ya mionzi (kemotherapia) na uangalizi wa daktari wa damu.",
                "Kinyarwanda": "Gukoresha imiti ya kanseri (chemotherapy) no kuganira n’inzobere mu maraso."
            }
        },
        {
            "symptoms": {
                "English": ["leg pain after walking", "cold feet", "weak pulse"],
                "French": ["douleur aux jambes après la marche", "pieds froids", "pouls faible"],
                "Kiswahili": ["maumivu ya miguu baada ya kutembea", "miguu kuwa baridi", "mpigo dhaifu wa moyo"],
                "Kinyarwanda": ["ububabare mu maguru iyo ugendagenda", "ibirenge bikonje", "pulsation y’umutima ntoya"]
            },
            "disease": {
                "English": "Peripheral Artery Disease",
                "French": "Maladie artérielle périphérique",
                "Kiswahili": "Ugonjwa wa mishipa ya damu ya pembeni",
                "Kinyarwanda": "Indwara y’imitsi ijyana amaraso ku bice by’inyuma"
            },
            "advice": {
                "English": "Lifestyle changes and vascular treatment.",
                "French": "Changements de mode de vie et traitement vasculaire.",
                "Kiswahili": "Mabadiliko ya maisha na matibabu ya mishipa ya damu.",
                "Kinyarwanda": "Guhindura imibereho no kuvuzwa imitsi y’amaraso."
            }
},
{
 "symptoms": {
                "English": ["fever", "chills", "sweating"],
                "French": ["fièvre", "frissons", "transpiration"],
                "Kiswahili": ["homa", "kutetemeka", "kutokwa jasho"],
                "Kinyarwanda": ["umuriro", "guhinda umuriro", "kugira ibyuya byinshi"]
            },
            "disease": {
                "English": "Malaria",
                "French": "Paludisme",
                "Kiswahili": "Malaria",
                "Kinyarwanda": "Malariya"
            },
            "advice": {
                "English": "Antimalarial medication immediately.",
                "French": "Médicaments antipaludiques immédiatement.",
                "Kiswahili": "Tumia dawa ya malaria haraka.",
                "Kinyarwanda": "Fata imiti ivura malariya ako kanya."
            }
        },
        {
            "symptoms": {
                "English": ["bloody diarrhea", "abdominal cramps", "tenesmus"],
                "French": ["diarrhée sanglante", "crampes abdominales", "ténesme"],
                "Kiswahili": ["kuharisha damu", "maumivu ya tumbo", "hamu ya choo bila kutoa chochote"],
                "Kinyarwanda": ["impiswi ivanze n’amaraso", "kuribwa mu nda", "kumva ushaka kwituma ntubikore"]
            },
            "disease": {
                "English": "Amoebiasis",
                "French": "Amibiase",
                "Kiswahili": "Amoebiasis",
                "Kinyarwanda": "Amoebiasis"
            },
            "advice": {
                "English": "Metronidazole and hydration.",
                "French": "Métronidazole et hydratation.",
                "Kiswahili": "Metronidazole na kunywa maji ya kutosha.",
                "Kinyarwanda": "Metronidazole no kunywa amazi menshi."
            }
        },
        {
            "symptoms": {
                "English": ["ulcers", "swollen lymph nodes", "cough"],
                "French": ["ulcères", "ganglions enflés", "toux"],
                "Kiswahili": ["vidonda", "tezi kuvimba", "kikohozi"],
                "Kinyarwanda": ["udusebe", "kubyimba k’impyiko", "inkorora"]
            },
            "disease": {
                "English": "Leprosy",
                "French": "Lèpre",
                "Kiswahili": "Ukoma",
                "Kinyarwanda": "Icyorezo cy’ububembe"
            },
            "advice": {
                "English": "Multi-drug therapy under supervision.",
                "French": "Polychimiothérapie sous surveillance médicale.",
                "Kiswahili": "Matibabu ya dawa mchanganyiko chini ya uangalizi.",
                "Kinyarwanda": "Gukoresha imiti myinshi icunguwe na muganga."
            }
        },
        {
            "symptoms": {
                "English": ["elephantiasis", "limb swelling", "fever"],
                "French": ["éléphantiasis", "gonflement des membres", "fièvre"],
                "Kiswahili": ["elefantiasi", "uvimbe wa miguu/mikono", "homa"],
                "Kinyarwanda": ["elephantiasis", "kubyimba amaguru cyangwa amaboko", "umuriro"]
            },
            "disease": {
                "English": "Lymphatic Filariasis",
                "French": "Filariose lymphatique",
                "Kiswahili": "Minyoo ya limfu (Filariasis)",
                "Kinyarwanda": "Filariasis y’imiyoboro y’amaraso"
            },
            "advice": {
                "English": "Anti-parasitic medication (DEC or ivermectin).",
                "French": "Médicaments antiparasitaires (DEC ou ivermectine).",
                "Kiswahili": "Dawa za minyoo kama DEC au ivermectin.",
                "Kinyarwanda": "Imiti yica utunyo (nka DEC cyangwa ivermectin)."
            }
},
{
 "symptoms": {
                "English": ["unusual bleeding", "weight loss", "fatigue"],
                "French": ["saignement inhabituel", "perte de poids", "fatigue"],
                "Kiswahili": ["kutokwa na damu isiyo ya kawaida", "kupungua uzito", "uchovu"],
                "Kinyarwanda": ["kuva amaraso kadasanzwe", "kugabanuka ibiro", "umunaniro"]
            },
            "disease": {
                "English": "Cervical Cancer",
                "French": "Cancer du col de l’utérus",
                "Kiswahili": "Saratani ya shingo ya kizazi",
                "Kinyarwanda": "Kanseri y’inkondo y’umura"
            },
            "advice": {
                "English": "Screening, surgery, chemo/radiation.",
                "French": "Dépistage, chirurgie, chimiothérapie/radiothérapie.",
                "Kiswahili": "Upimaji mapema, upasuaji, tiba ya mionzi au dawa.",
                "Kinyarwanda": "Kwisuzumisha kare, kubagwa, cyangwa kuvurwa hakoreshejwe imirasire cyangwa imiti."
            }
        },
        {
            "symptoms": {
                "English": ["change in mole", "irregular border", "dark spot growth"],
                "French": ["changement de grain de beauté", "bord irrégulier", "croissance de tache sombre"],
                "Kiswahili": ["kubadilika kwa doa la ngozi", "pembe zisizo sawa", "doa jeusi kukua"],
                "Kinyarwanda": ["impinduka ku kirango cy’uruhu", "imbibi zitameze neza", "utudomo tw’umukara dukura"]
            },
            "disease": {
                "English": "Skin Cancer (Melanoma)",
                "French": "Cancer de la peau (Mélanome)",
                "Kiswahili": "Saratani ya ngozi (Melanoma)",
                "Kinyarwanda": "Kanseri y’uruhu (Melanome)"
            },
            "advice": {
                "English": "Early surgical removal and biopsy.",
                "French": "Exérèse chirurgicale précoce et biopsie.",
                "Kiswahili": "Ondoa kwa upasuaji mapema na uchunguzi wa tishu (biopsy).",
                "Kinyarwanda": "Kubagwa hakiri kare no gupima igice cy’uruhu cyafashwe (biopsy)."
            }
        },
        {
            "symptoms": {
                "English": ["breast lump", "nipple discharge", "skin dimpling"],
                "French": ["masse mammaire", "écoulement du mamelon", "peau plissée"],
                "Kiswahili": ["uvimbe kwenye titi", "kutoka kwa majimaji kwenye chuchu", "ngozi ya titi kuwa na mashimo"],
                "Kinyarwanda": ["agakoba mu ibere", "gusohora amazi mu ibere", "uruhu rufite udushundura ku ibere"]
            },
            "disease": {
                "English": "Breast Cancer",
                "French": "Cancer du sein",
                "Kiswahili": "Saratani ya titi",
                "Kinyarwanda": "Kanseri y’ibere"
            },
            "advice": {
                "English": "Clinical exam, mammogram, and oncology care.",
                "French": "Examen clinique, mammographie et soins oncologiques.",
                "Kiswahili": "Uchunguzi wa daktari, mammogramu, na matibabu ya saratani.",
                "Kinyarwanda": "Gusuzumwa n’umuganga, gufotora ibere (mammographie), no kwitabwaho n’abaganga bavura kanseri."
            }
},
{
 "symptoms": {
                "English": ["yellow skin", "abdominal pain", "dark urine"],
                "French": ["peau jaune", "douleur abdominale", "urine foncée"],
                "Kiswahili": ["ngozi ya manjano", "maumivu ya tumbo", "mkojo wa giza"],
                "Kinyarwanda": ["uruhu rw’umuhondo", "uburibwe mu nda", "inkari z’umukara"]
            },
            "disease": {
                "English": "Hepatitis C",
                "French": "Hépatite C",
                "Kiswahili": "Hepatitis C",
                "Kinyarwanda": "Hepatite C"
            },
            "advice": {
                "English": "Antiviral therapy and liver support.",
                "French": "Traitement antiviral et soutien hépatique.",
                "Kiswahili": "Matibabu ya virusi na msaada kwa ini.",
                "Kinyarwanda": "Gukoresha imiti irwanya udukoko no kwita ku mwijima."
            }
        },
        {
            "symptoms": {
                "English": ["upper abdominal pain", "vomiting", "fever"],
                "French": ["douleur abdominale haute", "vomissements", "fièvre"],
                "Kiswahili": ["maumivu ya juu ya tumbo", "kutapika", "homa"],
                "Kinyarwanda": ["ububabare hejuru y’inda", "kuruka", "umuriro"]
            },
            "disease": {
                "English": "Pancreatitis",
                "French": "Pancréatite",
                "Kiswahili": "Uvimbaji wa kongosho (Pancreatitis)",
                "Kinyarwanda": "Kubyimba k’urwagashya (Pancreatitis)"
            },
            "advice": {
                "English": "IV fluids, fasting, and pain management.",
                "French": "Perfusion, jeûne, et traitement de la douleur.",
                "Kiswahili": "Maji kwa njia ya mshipa, kufunga kula, na dawa za maumivu.",
                "Kinyarwanda": "Amazi binyuze mu mutsi, kwirinda kurya no kugabanya ububabare."
            }
        },
        {
            "symptoms": {
                "English": ["itching", "jaundice", "fatty stools"],
                "French": ["démangeaisons", "jaunisse", "selles grasses"],
                "Kiswahili": ["miwasho", "manjano ya ngozi", "kinyesi chenye mafuta"],
                "Kinyarwanda": ["kwishimagura", "umuhondo ku ruhu", "umusarani ufite amavuta"]
            },
            "disease": {
                "English": "Primary Biliary Cholangitis",
                "French": "Cholangite biliaire primitive",
                "Kiswahili": "Cholangitis ya njia za nyongo",
                "Kinyarwanda": "Cholangite y’utuyoboro tw’inkari (biliaire)"
            },
            "advice": {
                "English": "Ursodiol and monitoring liver enzymes.",
                "French": "Ursodiol et surveillance des enzymes hépatiques.",
                "Kiswahili": "Ursodiol na kufuatilia viwango vya ini.",
                "Kinyarwanda": "Ursodiol no gukurikirana imisemburo y’umwijima."
            }
},
{
 "symptoms": {
                "English": ["testicular lump", "heaviness", "pain"],
                "French": ["masse testiculaire", "lourdeur", "douleur"],
                "Kiswahili": ["uvimbe kwenye korodani", "uzito", "maumivu"],
                "Kinyarwanda": ["agakoba mu mitsi y’igitsina", "kumva uremerewe", "ububabare"]
            },
            "disease": {
                "English": "Testicular Cancer",
                "French": "Cancer des testicules",
                "Kiswahili": "Saratani ya korodani",
                "Kinyarwanda": "Kanseri y’amabya"
            },
            "advice": {
                "English": "Ultrasound, surgery, and oncology treatment.",
                "French": "Échographie, chirurgie et traitement oncologique.",
                "Kiswahili": "Uchunguzi kwa ultrasound, upasuaji, na tiba ya saratani.",
                "Kinyarwanda": "Gusuzumwa na ultrasound, kubagwa no kuvurwa na muganga w’abahanga muri kanseri."
            }
        },
        {
            "symptoms": {
                "English": ["painful urination", "genital discharge", "pelvic pain"],
                "French": ["miction douloureuse", "écoulement génital", "douleur pelvienne"],
                "Kiswahili": ["maumivu kukojoa", "maji ukeni", "maumivu ya nyonga"],
                "Kinyarwanda": ["kubabara iyo wihagarika", "gusohora ibintu mu gitsina", "ububabare mu nda yo hasi"]
            },
            "disease": {
                "English": "Gonorrhea",
                "French": "Gonorrhée",
                "Kiswahili": "Kisonono",
                "Kinyarwanda": "Imitezi"
            },
            "advice": {
                "English": "Antibiotic treatment for both partners.",
                "French": "Traitement antibiotique pour les deux partenaires.",
                "Kiswahili": "Tiba ya antibiotiki kwa wapenzi wote wawili.",
                "Kinyarwanda": "Guhabwa imiti ya antibiotique ku mpande zombi z’abashakanye cyangwa abakundana."
            }
        },
        {
            "symptoms": {
                "English": ["pain during periods", "abdominal bloating", "infertility"],
                "French": ["douleur pendant les règles", "ballonnement abdominal", "infertilité"],
                "Kiswahili": ["maumivu wakati wa hedhi", "kujaa kwa tumbo", "kutopata mimba"],
                "Kinyarwanda": ["kubabara mu gihe cy’imihango", "inda yabyimbye", "kutabyara"]
            },
            "disease": {
                "English": "Ovarian Cyst",
                "French": "Kyste ovarien",
                "Kiswahili": "Uvimbaji wa mayai ya uzazi (Ovari)",
                "Kinyarwanda": "Agakoba ku murerantanga (ovaire)"
            },
            "advice": {
                "English": "Ultrasound and hormonal therapy.",
                "French": "Échographie et traitement hormonal.",
                "Kiswahili": "Ultrasound na tiba ya homoni.",
                "Kinyarwanda": "Gusuzumwa na ultrasound no gukoresha imiti ivura imisemburo."
            }
},
{
 "symptoms": {
                "English": ["sudden limb pain", "cold skin", "no pulse"],
                "French": ["douleur soudaine dans un membre", "peau froide", "pas de pouls"],
                "Kiswahili": ["maumivu ya ghafla mguuni au mkononi", "ngozi baridi", "hakuna mpigo wa moyo"],
                "Kinyarwanda": ["ububabare butunguranye mu kuboko cyangwa ukuguru", "uruhu rukonje", "nta mutima utera ugaragara"]
            },
            "disease": {
                "English": "Acute Limb Ischemia",
                "French": "Ischémie aiguë d’un membre",
                "Kiswahili": "Ukosefu wa damu ghafla kwenye kiungo",
                "Kinyarwanda": "Kubura amaraso mu kuboko cyangwa ukuguru bitunguranye"
            },
            "advice": {
                "English": "Emergency surgery or thrombolysis.",
                "French": "Chirurgie d'urgence ou thrombolyse.",
                "Kiswahili": "Upasuaji wa dharura au dawa ya kufuta damu iliyoganda.",
                "Kinyarwanda": "Kubagwa byihutirwa cyangwa kuvurwa kugira ngo amaraso atembere neza."
            }
        },
        {
            "symptoms": {
                "English": ["frequent fainting", "slow heart rate", "confusion"],
                "French": ["évanouissements fréquents", "rythme cardiaque lent", "confusion"],
                "Kiswahili": ["kupoteza fahamu mara kwa mara", "mapigo ya moyo polepole", "kuchanganyikiwa"],
                "Kinyarwanda": ["gucika intege kenshi", "umutima utera gahoro", "kuyoba mu mutwe"]
            },
            "disease": {
                "English": "Bradycardia",
                "French": "Bradycardie",
                "Kiswahili": "Mapigo ya moyo ya polepole (Bradycardia)",
                "Kinyarwanda": "Umutima utera gahoro cyane (Bradycardia)"
            },
            "advice": {
                "English": "ECG and possibly pacemaker.",
                "French": "ECG et éventuellement un pacemaker.",
                "Kiswahili": "Pima moyo kwa ECG na weza hitaji kifaa cha kusaidia moyo (pacemaker).",
                "Kinyarwanda": "Gupimisha umutima hifashishijwe ECG no kuba wakenera akuma gashyirwa mu gatuza (pacemaker)."
            }
        },
        {
            "symptoms": {
                "English": ["abdominal pain", "skin darkening", "fatigue"],
                "French": ["douleur abdominale", "assombrissement de la peau", "fatigue"],
                "Kiswahili": ["maumivu ya tumbo", "ngozi kuwa nyeusi", "uchovu"],
                "Kinyarwanda": ["uburibwe mu nda", "uruhu rwirabura", "umunaniro"]
            },
            "disease": {
                "English": "Addison’s Disease",
                "French": "Maladie d'Addison",
                "Kiswahili": "Ugonjwa wa Addison",
                "Kinyarwanda": "Indwara ya Addison"
            },
            "advice": {
                "English": "Steroid hormone replacement.",
                "French": "Remplacement des hormones stéroïdes.",
                "Kiswahili": "Dawa za homoni za steroid.",
                "Kinyarwanda": "Gusimbuza imisemburo ya steroid."
            }
        },
        {
            "symptoms": {
                "English": ["difficulty breathing", "facial swelling", "hives"],
                "French": ["difficulté à respirer", "gonflement du visage", "urticaire"],
                "Kiswahili": ["ugumu wa kupumua", "uso kuvimba", "upele wa mzio (hives)"],
                "Kinyarwanda": ["guhumeka bigoranye", "kubyimba mu maso", "udushishi two ku mubiri (hives)"]
            },
            "disease": {
                "English": "Anaphylaxis",
                "French": "Anaphylaxie",
                "Kiswahili": "Anaphylaxis",
                "Kinyarwanda": "Anaphylaxis (igisubizo gikabije cy’umubiri ku byo utihanganira)"
            },
            "advice": {
                "English": "Administer epinephrine and call emergency.",
                "French": "Administrer de l’épinéphrine et appeler les urgences.",
                "Kiswahili": "Tumia epinephrine na piga simu ya dharura.",
                "Kinyarwanda": "Tanga epinephrine hanyuma hamagara ubuvuzi bwihuse."
            }
        },
        {
            "symptoms": {
                "English": ["frequent fractures", "blue sclera", "short stature"],
                "French": ["fractures fréquentes", "sclérotique bleue", "petite taille"],
                "Kiswahili": ["mifupa kuvunjika mara kwa mara", "macho meupe kuwa ya buluu", "urefu mdogo"],
                "Kinyarwanda": ["kumenerwa amagufwa kenshi", "amaso y’umweru abonerana ubururu", "uburebure buto"]
            },
            "disease": {
                "English": "Osteogenesis Imperfecta",
                "French": "Ostéogenèse imparfaite",
                "Kiswahili": "Uumbaji wa mifupa usio kamili (Osteogenesis Imperfecta)",
                "Kinyarwanda": "Kuremwa nabi kw’amagufwa (Osteogenesis Imperfecta)"
            },
            "advice": {
                "English": "Bone strengthening and orthopedic care.",
                "French": "Renforcement osseux et soins orthopédiques.",
                "Kiswahili": "Kuimarisha mifupa na matibabu ya mifupa.",
                "Kinyarwanda": "Gukomeza amagufwa no kwitabwaho n’inzobere mu magufwa."
            }
        },
        {
            "symptoms": {
                "English": ["delayed growth", "low sex hormones", "infertility"],
                "French": ["croissance retardée", "faibles hormones sexuelles", "infertilité"],
                "Kiswahili": ["ukuaji kuchelewa", "homoni za jinsia za chini", "kutopata watoto"],
                "Kinyarwanda": ["gukura bitinze", "imisemburo y’igitsina iri hasi", "kutabyara"]
            },
            "disease": {
                "English": "Klinefelter Syndrome",
                "French": "Syndrome de Klinefelter",
                "Kiswahili": "Syndrome ya Klinefelter",
                "Kinyarwanda": "Syndrome ya Klinefelter"
            },
            "advice": {
                "English": "Hormone therapy and support.",
                "French": "Traitement hormonal et accompagnement.",
                "Kiswahili": "Tiba ya homoni na msaada wa kitabibu.",
                "Kinyarwanda": "Imiti ivura imisemburo no kugirirwa inama n’ubuvuzi bwunganira."
            }


        }
    ]

    }


}



# Dynamically generate symptom list from symptom_diagnosis for current language
def get_all_symptoms_for_language(lang):
    symptoms_set = set()
    entries = symptom_diagnosis.get("all_diseases_translated", {}).get("entries", [])
    for entry in entries:
        lang_symptoms = entry.get("symptoms", {}).get(lang, [])
        for s in lang_symptoms:
            symptoms_set.add(s)
    return sorted(symptoms_set)

# Function to rebuild checkboxes based on language





def build_symptom_checkboxes():
    global checkbox_frame, symptom_vars
    for widget in checkbox_frame.winfo_children():
        widget.destroy()

    lang = language_map.get(current_language.get(), "English")
    all_symptoms = set()

    # Collect symptoms for current language from all entries
    entries = symptom_diagnosis.get("all_diseases_translated", {}).get("entries", [])
    for entry in entries:
        symptoms_by_lang = entry.get("symptoms", {})
        if lang in symptoms_by_lang:
            all_symptoms.update(symptoms_by_lang[lang])

    symptom_vars.clear()

    # Scrollable checkbox area
    canvas = tk.Canvas(checkbox_frame, height=140, width=400, bg="#faebd7", highlightthickness=0)
    scrollbar = ttk.Scrollbar(checkbox_frame, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    inner_frame = tk.Frame(canvas, bg="#faebd7")
    canvas.create_window((0, 0), window=inner_frame, anchor="nw")

    for symptom in sorted(all_symptoms):
        var = tk.BooleanVar()
        cb = tk.Checkbutton(inner_frame, text=symptom, variable=var, bg="#faebd7", anchor="w")
        cb.pack(anchor="w")
        symptom_vars[symptom] = var

    inner_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")


# Text-to-speech
engine = pyttsx3.init()
zira_voice = r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
engine.setProperty("voice", zira_voice)
import threading

tts_lock = threading.Lock()

import threading

tts_lock = threading.Lock()

import threading

import threading
import pyttsx3

def speak(text):
    def run_tts():
        try:
            engine = pyttsx3.init()
            engine.setProperty('rate', 150)
            engine.setProperty('volume', 1.0)
            engine.say(text)
            engine.runAndWait()
        except Exception as e:
            print(f"TTS Error: {e}")
    threading.Thread(target=run_tts, daemon=True).start()
conn = sqlite3.connect("diagnosis_history.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS diagnosis_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    symptoms TEXT,
    diagnosis TEXT,
    advice TEXT,
    timestamp TEXT
)
""")
conn.commit()

# GUI frames
nav_bar = tk.Frame(root, bg="#faebd7")
nav_bar.place(relx=0, rely=0, relwidth=1, relheight=0.1)
menu_frame = tk.Frame(root, bg="#faebd7")
diagnosis_frame = tk.Frame(root, bg="#faebd7")
records_frame = tk.Frame(root, bg="#faebd7")
for frame in (menu_frame, diagnosis_frame, records_frame):
    frame.place(relx=0, rely=0.1, relwidth=1, relheight=0.9)

def show_frame(frame):
    frame.tkraise()


# --- Profile section (top-right above Records) ---
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import tkinter.simpledialog

profile_name = tk.StringVar(value="No Profile")
profile_photo = None
profile_photo_label = None

profile_right_frame = tk.Frame(nav_bar, bg="#faebd7")
profile_right_frame.pack(side="right", padx=10, pady=5)

profile_photo_label = tk.Label(profile_right_frame, bg="#faebd7")
profile_photo_label.pack()

profile_name_label = tk.Label(profile_right_frame, textvariable=profile_name, bg="#faebd7", font=("Arial", 10, "bold"))
profile_name_label.pack()

def add_profile():
    name = tk.simpledialog.askstring("Profile Name", "Enter your name:")
    if not name:
        return
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
    if not file_path:
        return
    img = Image.open(file_path).resize((20,20))
    photo = ImageTk.PhotoImage(img)
    global profile_photo
    profile_name.set(name)
    profile_photo = photo
    profile_photo_label.config(image=photo)
def remove_profile():
    global profile_photo
    if messagebox.askyesno("Remove Profile", "Are you sure you want to remove this profile?"):
        profile_name.set("No Profile")
        profile_photo_label.config(image=None)
        profile_photo_label.image = None  # Clear image reference
        profile_photo = None


tk.Button(profile_right_frame, text="Add Profile", command=add_profile, bg="#faebd7", font=("Arial", 8)).pack()
tk.Button(profile_right_frame, text="Remove Profile", command=remove_profile, bg="#faebd7", font=("Arial", 8)).pack()
# --- End Profile section ---

# Navigation buttons
btn_menu = tk.Button(nav_bar, font=("Arial", 10, "underline"), bd=0, bg="#faebd7", command=lambda: show_frame(menu_frame))
btn_diagnosis = tk.Button(nav_bar, font=("Arial", 10, "underline"), bd=0, bg="#faebd7", command=lambda: show_frame(diagnosis_frame))
btn_records = tk.Button(nav_bar, font=("Arial", 10, "underline"), bd=0, bg="#faebd7", command=lambda: [load_records(), show_frame(records_frame)])
btn_menu.pack(side="left", padx=20)
btn_diagnosis.pack(side="left", padx=20)
btn_records.pack(side="right", padx=20)

# Menu screen
label_language = tk.Label(menu_frame, bg="#faebd7", font=("Arial", 10))
label_language.pack(pady=(10, 0))
lang_dropdown = ttk.Combobox(menu_frame, textvariable=current_language, values=languages, state="readonly", width=20)
lang_dropdown.pack(pady=(0, 10))
lang_dropdown.bind("<<ComboboxSelected>>", lambda e: translate_ui())
menu_labels = [
    tk.Label(menu_frame, bg="#faebd7", font=("Arial", 16, "bold")),
    tk.Label(menu_frame, bg="#faebd7", font=("Arial", 12)),
    tk.Label(menu_frame, bg="#faebd7", font=("Arial", 10))
]
for label in menu_labels:
    label.pack(pady=10)

# Diagnosis screen
label_symptoms = tk.Label(diagnosis_frame, bg="#faebd7", font=("Arial", 12))
label_symptoms.pack(pady=10)
symptom_entry = tk.Entry(diagnosis_frame, width=50)
symptom_entry.pack(pady=5)
# Checkbox symptom UI setup
checkbox_frame = tk.Frame(diagnosis_frame, bg="#faebd7")
checkbox_frame.pack(pady=10)
symptom_vars = {}

# Checkbox symptom UI setup

build_symptom_checkboxes()

# Sample list of symptoms
# Scrollable checkbox area
btn_diagnose = tk.Button(diagnosis_frame, bg="black", fg="white", font=("Arial", 10))
btn_diagnose.pack(pady=10)
diagnosis_result = tk.Label(diagnosis_frame, bg="#faebd7", font=("Arial", 12, "bold"))
diagnosis_result.pack(pady=5)
advice_result = tk.Label(diagnosis_frame, bg="#faebd7", font=("Arial", 12))
advice_result.pack(pady=5)

# Records screen
columns = ("symptoms", "diagnosis", "advice", "timestamp")
record_table = ttk.Treeview(records_frame, columns=columns, show="headings")
for col in columns:
    record_table.heading(col, text=tr(col.capitalize()))
    record_table.column(col, width=180)
record_table.pack(fill="both", expand=True, padx=10, pady=(10, 0))
btn_delete = tk.Button(records_frame, text="", font=("Arial", 10), command=lambda: delete_record())
btn_delete.pack(anchor="w", padx=10, pady=10)

# Translations and logic
def translate_ui():
    build_symptom_checkboxes()
    btn_menu.config(text=tr("Menu"))
    btn_diagnosis.config(text=tr("Diagnose"))
    btn_records.config(text=tr("Records"))
    label_language.config(text=tr("Language:"))
    label_symptoms.config(text=tr("Enter your symptoms (comma separated):"))
    btn_diagnose.config(text=tr("Diagnose"))
    diagnosis_result.config(text=tr("Diagnosis"))
    advice_result.config(text=tr("Advice"))
    btn_delete.config(text=tr("Delete Selected Record"))
    for col in columns:
        record_table.heading(col, text=tr(col.capitalize()))
    menu_labels[0].config(text="🏥" + tr("Welcome to MediBox"))
    menu_labels[1].config(text=tr("Diagnose illnesses based on your symptoms."))
    menu_labels[2].config(text=tr("Click 'Diagnose' to begin."))
def get_diagnosis(symptom_input, lang):
    input_symptoms = [s.strip().lower() for s in symptom_input.split(",") if s.strip()]
    input_symptoms_set = set(input_symptoms)

    for entry in symptom_diagnosis["all_diseases_translated"]["entries"]:
        expected = [s.lower() for s in entry["symptoms"].get(lang, [])]
        if all(symptom in input_symptoms_set for symptom in expected):
            return {
                "diagnosis": f"{tr('Diagnosis')}: {entry['disease'].get(lang, '')}",
                "advice": f"{tr('Advice')}: {entry['advice'].get(lang, '')}"
            }

    return {
        "diagnosis": tr("Diagnosis not found."),
        "advice": tr("Please visit a health center for professional support.")
    }
def diagnose():

    # Combine symptoms from text entry and selected checkboxes
    typed = symptom_entry.get().strip()
    checked = [s for s, var in symptom_vars.items() if var.get()]
    all_symptoms = ', '.join(filter(None, [typed] + checked))

    lang = language_map.get(current_language.get(), "English")
    symptoms_input = all_symptoms
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    results = get_diagnosis(symptoms_input, lang)
    diagnosis_result.config(text=results["diagnosis"])
    advice_result.config(text=results["advice"])
    speak(f"{results['diagnosis']}. {results['advice']}")
    cursor.execute("INSERT INTO diagnosis_history (symptoms, diagnosis, advice, timestamp) VALUES (?, ?, ?, ?)",
                   (symptoms_input, results["diagnosis"], results["advice"], timestamp))
    conn.commit()

def load_records():
    cursor.execute("SELECT symptoms, diagnosis, advice, timestamp FROM diagnosis_history ORDER BY id DESC")
    rows = cursor.fetchall()
    record_table.delete(*record_table.get_children())
    for row in rows:
        record_table.insert("", "end", values=row)

def delete_record():
    selected_item = record_table.selection()
    if selected_item:
        values = record_table.item(selected_item, "values")
        if values:
            symptoms, diagnosis, advice, timestamp = values
            cursor.execute("DELETE FROM diagnosis_history WHERE symptoms=? AND diagnosis=? AND advice=? AND timestamp=?",
                           (symptoms, diagnosis, advice, timestamp))
            conn.commit()
            record_table.delete(selected_item)

btn_diagnose.config(command=diagnose)
translate_ui()
show_frame(menu_frame)
root.mainloop()
