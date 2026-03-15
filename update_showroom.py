# -*- coding: utf-8-sig -*-
import os
import glob
import json
import uuid
from PIL import Image
import random

FRENCH_TITLES = [
    "L'Écho de la Lumière (Echo of Light)",
    "Rêverie Nocturne (Nocturnal Reverie)",
    "Silence d'Or (Golden Silence)",
    "Vagues d'Émeraude (Emerald Waves)",
    "Souffle du Vent (Breath of the Wind)",
    "Éternité Fragmentée (Fragmented Eternity)",
    "Miroir de l'Âme (Mirror of the Soul)",
    "Danse Céleste (Celestial Dance)"
]
FRENCH_CATEGORIES = ["Visionary Photography", "Digital Fine Art", "Neo-Classic Impressionism", "Surrealism", "Modernist Abstract"]
FRENCH_DESC = "An exclusive exploration of light, texture, and emotion, curated for the L'Atelier Antigravity collection. The pristine 8000x8000 resolution captures the most delicate nuances of the original vision.\n\n*Œuvre originale, perfectionnée avec l'assistance de l'IA (AI-assisted).*"

SHOWROOM_DIR = os.path.dirname(os.path.abspath(__file__))
VISUALIZATIONS_DIR = os.path.join(os.path.dirname(SHOWROOM_DIR), "visualizations")
THUMBNAILS_DIR = os.path.join(SHOWROOM_DIR, "thumbnails")
JS_PATH = os.path.join(SHOWROOM_DIR, "gallery_data.js")

def main():
    if not os.path.exists(THUMBNAILS_DIR):
        os.makedirs(THUMBNAILS_DIR)

    # Load existing JS Data
    gallery_data = []
    if os.path.exists(JS_PATH):
        try:
            with open(JS_PATH, 'r', encoding='utf-8') as f:
                content = f.read()
                # Remove 'window.galleryData = ' prefix before parsing
                json_str = content.replace("window.galleryData = ", "").strip()
                if json_str:
                    gallery_data = json.loads(json_str)
        except Exception as e:
            print(f"Error loading JS data: {e}")

    # Index existing items by src
    existing_srcs = {item['src']: item for item in gallery_data}
    
    # Find all png and jpg images in visualizations folder
    image_files = glob.glob(os.path.join(VISUALIZATIONS_DIR, "*.png")) + glob.glob(os.path.join(VISUALIZATIONS_DIR, "*.jpg"))
    
    new_items = []
    updated_count = 0

    for img_path in image_files:
        filename = os.path.basename(img_path)
        src_path = f"../visualizations/{filename}"
        thumb_filename = f"thumb_{filename}"
        thumb_rel_path = f"thumbnails/{thumb_filename}"
        thumb_abs_path = os.path.join(THUMBNAILS_DIR, thumb_filename)
        
        # Check if thumbnail exists physically
        needs_thumb = not os.path.exists(thumb_abs_path)
        
        # Determine if we need to load and resize
        if needs_thumb:
            try:
                print(f"Generating thumbnail for {filename}...")
                with Image.open(img_path) as img:
                    # Calculate new size (max width 800)
                    w, h = img.size
                    target_w = 800
                    if w > target_w:
                        target_h = int((target_w / w) * h)
                    else:
                        target_w, target_h = w, h
                    
                    # Resize and save
                    img_resized = img.resize((target_w, target_h), Image.Resampling.LANCZOS)
                    img_resized.save(thumb_abs_path, format="PNG", optimize=True)
            except Exception as e:
                print(f"Failed to generate thumbnail for {filename}: {e}")
                continue
                
        # If the image is not in JSON yet, create new entry
        if src_path not in existing_srcs:
            title = random.choice(FRENCH_TITLES)
            category = random.choice(FRENCH_CATEGORIES)
            
            new_item = {
                "id": str(uuid.uuid4())[:8],
                "src": src_path,
                "thumb_src": thumb_rel_path,
                "fallback_src": f"https://via.placeholder.com/800x800/eeeeee/888888?text=New+Artwork",
                "title": title,
                "category": category,
                "desc": FRENCH_DESC,
                "link": "https://www.redbubble.com"
            }
            new_items.append(new_item)
            print(f"Added new artwork to JS: {title}")
        else:
            # It is in JSON, ensure thumb_src points to the actual thumbnail
            item = existing_srcs[src_path]
            if item.get("thumb_src") != thumb_rel_path:
                item["thumb_src"] = thumb_rel_path
                updated_count += 1
                print(f"Updated thumb_src for existing item: {item['title']}")

    # Prepend new items to gallery_data (so newest are first)
    final_data = new_items + gallery_data
    
    # Save back to JS file
    if len(new_items) > 0 or updated_count > 0:
        with open(JS_PATH, 'w', encoding='utf-8') as f:
            json_str = json.dumps(final_data, indent=2, ensure_ascii=False)
            f.write(f"window.galleryData = {json_str};\n")
        print(f"Successfully updated gallery_data.js. Added: {len(new_items)}, Updated: {updated_count}")
    else:
        print("No new artworks found. Gallery is up to date.")

if __name__ == "__main__":
    main()
