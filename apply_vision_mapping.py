import json
import os

SHOWROOM_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(SHOWROOM_DIR, "gallery_data.js")

# The precise mapping according to actual visual contents of the UUID files
mapping = {
    "grok-image-50d54fb6-8344-4b93-a919-893349619169.png": {
        "title": "Veillée d'Armes (Vigil of Arms)",
        "desc": "A striking juxtaposition of nature's serenity and military machinery, capturing a quiet moment before the storm. Une juxtaposition saisissante de la sérénité naturelle et de la machinerie militaire.\n\n*Œuvre originale, perfectionnée avec l'assistance de l'IA.*",
        "category": "Surreal Landscape"
    },
    "grok-image-6b491642-eb94-4803-8332-dd75d1bd0777.png": {
        "title": "Cœur de Magma (Heart of Magma)",
        "desc": "The raw, fiery power of the earth observed by floating technology, contrasting ancient forces with modern observation. La puissance brute et ardente de la terre observée par la technologie.\n\n*Œuvre originale, perfectionnée avec l'assistance de l'IA.*",
        "category": "Cinematic Drone Art"
    },
    "grok-image-9329acf4-c315-4f13-95bc-7d0229ab36cd.png": {
        "title": "Cavalière d'Émeraude (Emerald Equestrian)",
        "desc": "A poetic harmony between a rider and her vivid green surroundings, evoking stories of folklore and wild freedom. Une harmonie poétique entre une cavalière et son environnement vert émeraude.\n\n*Œuvre originale, perfectionnée avec l'assistance de l'IA.*",
        "category": "Fantasy Portraiture"
    },
    "grok-image-b59b99a6-0dcf-4f42-98e5-f795f994ebc7.png": {
        "title": "Tactique Culinaire (Culinary Tactics)",
        "desc": "A surreal and brilliant satire blending modern tactical gear with the universally comforting form of baked bread. Une satire surréaliste et brillante mêlant équipement tactique et pain.\n\n*Œuvre originale, perfectionnée avec l'assistance de l'IA.*",
        "category": "Pop Surrealism"
    },
    "grok-image-bd387de1-2c03-490b-967b-c73479014b23.png": {
        "title": "Le Voyageur dans la Brume (Wanderer in the Mist)",
        "desc": "A melancholic and timeless silhouette wrapped in dense fog, inviting the viewer into a landscape of quiet introspection. Une silhouette mélancolique et intemporelle enveloppée d'un brouillard dense.\n\n*Œuvre originale, perfectionnée avec l'assistance de l'IA.*",
        "category": "Atmospheric Photography"
    },
    "grok-image-bea9edba-2603-4e92-9a94-28705e3236e3.png": {
        "title": "Ruisseau de Nuit (Night Stream)",
        "desc": "The silent, continuous flow of a forest stream captured in the deep, mysterious hues of the nocturnal wilderness. Le flux silencieux et continu d'un ruisseau forestier.\n\n*Œuvre originale, perfectionnée avec l'assistance de l'IA.*",
        "category": "Nature Abstract"
    },
    "grok-image-cb7f7b61-660d-4a54-912f-537c60962a27.png": {
        "title": "L'Esprit des Abysses (Spirit of the Abyss)",
        "desc": "An ethereal and striking ghostly primate submerged in deep blue waters, representing the untamed souls of the deep. Un primate fantomatique et éthéré submergé dans les eaux d'un bleu profond.\n\n*Œuvre originale, perfectionnée avec l'assistance de l'IA.*",
        "category": "Mythological Concept"
    },
    "grok-image-e5878f4c-3361-496b-ab5c-b7f72b3afdda.png": {
        "title": "Souvenirs Culinaires (Culinary Memories)",
        "desc": "The warmth of a lived-in kitchen and the gentle gaze of an elder, capturing the quiet dignity of daily preparation. La chaleur d'une cuisine vécue et le doux regard d'un aîné.\n\n*Œuvre originale, perfectionnée avec l'assistance de l'IA.*",
        "category": "Cinematic Realism"
    },
    "21fd8ea4-128a-4777-aafd-d536ba0a9d9e.jpg": {
        "title": "Éclat d'Argent (Silver Radiance)",
        "desc": "A glamorous explosion of shimmering sequins and bold crimson silk against a clear sky, embodying strength and high fashion. Une explosion glamour de paillettes scintillantes et de soie cramoisie audacieuse.\n\n*Œuvre originale, perfectionnée avec l'assistance de l'IA.*",
        "category": "Fashion Editorial"
    },
    "37658774-8152-44dc-ba67-b53d1cb6579d.jpg": {
        "title": "Regard Ailé (Winged Gaze)",
        "desc": "A dramatic, sharp focus on a human eye adorned with sweeping, raven-like artistic makeup, penetrating the soul. Un focus dramatique et aigu sur un œil humain orné d'un maquillage artistique en forme d'ailes de corbeau.\n\n*Œuvre originale, perfectionnée avec l'assistance de l'IA.*",
        "category": "Avant-Garde Macro"
    },
    "488ff6c9-4811-4801-aee4-b853ac70172e.jpg": {
        "title": "Fuite dans le Vent (Flight in the Wind)",
        "desc": "A dynamic capture of motion as an individual races through a storm of scattered pages, symbolizing the rush of untamed thoughts. Une capture dynamique du mouvement d'un individu dans une tempête de papier.\n\n*Œuvre originale, perfectionnée avec l'assistance de l'IA.*",
        "category": "Conceptual Action"
    },
    "5e988cd5-387c-4105-9ea8-a7e8d536c61d.jpg": {
        "title": "Masque de Blé (Mask of Wheat)",
        "desc": "A striking surrealist portrait where sustenance becomes anonymity, questioning consumerism and human identity. Un portrait surréaliste frappant où la subsistance devient anonymat.\n\n*Œuvre originale, perfectionnée avec l'assistance de l'IA.*",
        "category": "Dadaist Portrait"
    },
    "640afc44-2cde-48d4-bd04-3412d5e43be7.jpg": {
        "title": "La Tempête des Mots (Storm of Words)",
        "desc": "Intense emotional distress rendered beautifully among chaotic, flying sheets of paper, representing overwhelming narratives. Une détresse émotionnelle intense rendue magnifiquement parmi des feuilles volantes.\n\n*Œuvre originale, perfectionnée avec l'assistance de l'IA.*",
        "category": "Emotional Portraiture"
    },
    "6c1d6f15-ceb7-4684-9b40-b9892e3e2710.jpg": {
        "title": "Lumière Citadine (City Light)",
        "desc": "A cinematic night scene capturing a solitary, brightly dressed figure against the bokeh of urban darkness. Une scène nocturne cinématographique capturant une figure solitaire sous la lumière de la ville.\n\n*Œuvre originale, perfectionnée avec l'assistance de l'IA.*",
        "category": "Urban Neo-Noir"
    },
    "962096fa-582a-495a-8fb7-5641559e854e.jpg": {
        "title": "L'Ombre de Papier (The Paper Shadow)",
        "desc": "A thought-provoking image of a man holding a hollow reflection of humanity, exploring themes of absence and existence. Une image poignante d'un homme tenant un reflet creux de l'humanité.\n\n*Œuvre originale, perfectionnée avec l'assistance de l'IA.*",
        "category": "Conceptual Art"
    },
    "9dcf2542-a42b-4748-9a7f-2485a1381028.jpg": {
        "title": "Murmures du Vent (Whispers of the Wind)",
        "desc": "A serene profile caught in a delicate flurry of floating pages, capturing the poetic intersection of humanity and literature. Un profil serein pris dans une délicate tempête de pages flottantes.\n\n*Œuvre originale, perfectionnée avec l'assistance de l'IA.*",
        "category": "Poetic Surrealism"
    },
    "b26d0268-de43-4b44-9240-2c024ae6cb40.jpg": {
        "title": "Le Regard Doux (The Gentle Gaze)",
        "desc": "A high-contrast monochrome portrait capturing the deeply soulful, gentle eye of a bovine creature. Un portrait monochrome à fort contraste capturant l'œil profondément expressif d'un bovin.\n\n*Œuvre originale, perfectionnée avec l'assistance de l'IA.*",
        "category": "Fine Art Monochrome"
    },
    "f7bf012a-7b79-44b5-af1a-5d7c9c5f04b4.jpg": {
        "title": "Douceur Sanglante (Crimson Sweetness)",
        "desc": "A striking, morbidly playful contrast of a sterile blue glove and vividly red, melting dessert, evoking pop-surrealism. Un contraste frappant et morbidement ludique évoquant le pop-surréalisme.\n\n*Œuvre originale, perfectionnée avec l'assistance de l'IA.*",
        "category": "Pop Art Surrealism"
    }
}

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

# Apply correct mapping based on the filename inside the src property
for item in data:
    filename = item["src"].split("/")[-1]
    if filename in mapping:
        item["title"] = mapping[filename]["title"]
        item["desc"] = mapping[filename]["desc"]
        item["category"] = mapping[filename]["category"]

with open(FILE_PATH, "w", encoding="utf-8") as f:
    f.write("window.galleryData = " + json.dumps(data, indent=2, ensure_ascii=False) + ";\n")

print("Successfully applied 1:1 visually accurate titles and descriptions!")
