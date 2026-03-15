import json
import re
import os

SHOWROOM_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(SHOWROOM_DIR, "gallery_data.js")

if not os.path.exists(FILE_PATH):
    print("gallery_data.js not found.")
    exit(1)

with open(FILE_PATH, "r", encoding="utf-8") as f:
    text = f.read()

json_str = text.replace("window.galleryData = ", "").strip().strip(";")
try:
    data = json.loads(json_str)
except Exception as e:
    print(f"Error parsing JSON: {e}")
    exit(1)

descriptions = {
    "L'Écho de la Lumière (Echo of Light)": "Une étude délicate de la lumière qui se reflète et se brise à travers le prisme de l'émotion humaine. A delicate study of light as it reflects and refracts through the prism of human emotion.\n\n*Œuvre originale, perfectionnée avec l'assistance de l'IA (AI-assisted).* ",
    "Rêverie Nocturne (Nocturnal Reverie)": "Un voyage onirique dans les profondeurs de la nuit, là où les étoiles murmurent des secrets anciens. A dreamlike journey into the depths of the night, where stars whisper ancient secrets.\n\n*Œuvre originale, perfectionnée avec l'assistance de l'IA (AI-assisted).* ",
    "Silence d'Or (Golden Silence)": "L'immobilité pure capturée dans des tons dorés, offrant un moment de paix absolue. Pure stillness captured in golden hues, offering a moment of absolute peace.\n\n*Œuvre originale, perfectionnée avec l'assistance de l'IA (AI-assisted).* ",
    "Vagues d'Émeraude (Emerald Waves)": "L'énergie fluide et hypnotique de la mer traduite en formes abstraites et vibrantes. The fluid, hypnotic energy of the sea translated into vibrant and abstract forms.\n\n*Œuvre originale, perfectionnée avec l'assistance de l'IA (AI-assisted).* ",
    "Souffle du Vent (Breath of the Wind)": "La texture de l'air en mouvement, peinte avec une précision poétique et abstraite. The texture of moving air, painted with poetic and abstract precision.\n\n*Œuvre originale, perfectionnée avec l'assistance de l'IA (AI-assisted).* ",
    "Éternité Fragmentée (Fragmented Eternity)": "Des éclats de temps suspendus dans un vide infini, explorant la nature fragmentaire du souvenir. Splinters of time suspended in an infinite void, exploring the fragmented nature of memory.\n\n*Œuvre originale, perfectionnée avec l'assistance de l'IA (AI-assisted).* ",
    "Miroir de l'Âme (Mirror of the Soul)": "Une introspection visuelle qui reflète la complexité et la beauté de l'esprit intérieur. A visual introspection that reflects the complexity and beauty of the inner mind.\n\n*Œuvre originale, perfectionnée avec l'assistance de l'IA (AI-assisted).* ",
    "Danse Céleste (Celestial Dance)": "Le mouvement cosmique figé dans l'espace, éclatant de couleurs vibrantes et mystérieuses. Cosmic movement frozen in space, bursting with vibrant and mysterious colors.\n\n*Œuvre originale, perfectionnée avec l'assistance de l'IA (AI-assisted).* ",
    "Ombre Douce (Sweet Shadow)": "Un jeu délicat de contrastes où l'obscurité sublime la lumière et réconforte l'âme. A delicate interplay of contrasts where darkness sublimates light and comforts the soul.\n\n*Œuvre originale, perfectionnée avec l'assistance de l'IA (AI-assisted).* ",
    "Fleur de Cristal (Crystal Flower)": "La fragilité de la nature cristallisée en une structure éternelle et lumineuse. The fragility of nature crystallized into an eternal and luminous structure.\n\n*Œuvre originale, perfectionnée avec l'assistance de l'IA (AI-assisted).* ",
    "L'Aube Nouvelle (The New Dawn)": "L'espoir d'un nouveau départ, évoqué par des lueurs douces et des horizons poétiques. The hope of a new beginning, evoked by soft glows and poetic horizons.\n\n*Œuvre originale, perfectionnée avec l'assistance de l'IA (AI-assisted).* ",
    "Secret du Temps (Secret of Time)": "Les couches invisibles de l'histoire accumulées dans des textures riches et énigmatiques. The invisible layers of history accumulated in rich and enigmatic textures.\n\n*Œuvre originale, perfectionnée avec l'assistance de l'IA (AI-assisted).* ",
    "Illusions Perdues (Lost Illusions)": "Une réflexion sur l'éphémère et la beauté des rêves qui s'estompent doucement. A reflection on the ephemeral and the beauty of dreams that gently fade away.\n\n*Œuvre originale, perfectionnée avec l'assistance de l'IA (AI-assisted).* ",
    "Symphonie Visuelle (Visual Symphony)": "Un orchestre de couleurs et de formes qui résonne avec l'harmonie de l'univers. An orchestra of colors and shapes resonating with the harmony of the universe.\n\n*Œuvre originale, perfectionnée avec l'assistance de l'IA (AI-assisted).* ",
    "Mélancolie Bleue (Blue Melancholy)": "Une élégie silencieuse peinte dans des nuances profondes et apaisantes de bleu. A silent elegy painted in deep and soothing shades of blue.\n\n*Œuvre originale, perfectionnée avec l'assistance de l'IA (AI-assisted).* ",
    "Esprit Sauvage (Wild Spirit)": "La force indéniable de la nature brute, capturée avec une passion audacieuse. The undeniable force of raw nature, captured with bold passion.\n\n*Œuvre originale, perfectionnée avec l'assistance de l'IA (AI-assisted).* ",
    "Horizon Infini (Infinite Horizon)": "L'ouverture de l'espace et de l'esprit, où la vue se perd dans une plénitude absolue. The openness of space and mind, where sight loses itself in absolute fullness.\n\n*Œuvre originale, perfectionnée avec l'assistance de l'IA (AI-assisted).* ",
    "Poésie Silencieuse (Silent Poetry)": "Des mots non dits qui trouvent leur expression dans des compositions visuelles pures. Unspoken words finding expression in pure visual compositions.\n\n*Œuvre originale, perfectionnée avec l'assistance de l'IA (AI-assisted).* "
}

for item in data:
    if item["title"] in descriptions:
        item["desc"] = descriptions[item["title"]]
    else:
        # Fallback without the Antigravity/8000x8000 text
        item["desc"] = "Une exploration visuelle de texture et d'émotion. A visual exploration of texture and emotion.\n\n*Œuvre originale, perfectionnée avec l'assistance de l'IA (AI-assisted).*"

with open(FILE_PATH, "w", encoding="utf-8") as f:
    f.write("window.galleryData = " + json.dumps(data, indent=2, ensure_ascii=False) + ";\n")

print("Updated descriptions successfully!")
