#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from pathlib import Path

def install_gtts():
    """Installe gTTS si nécessaire"""
    try:
        from gtts import gTTS
        return True
    except ImportError:
        print("Installation de gTTS...")
        os.system("pip install gtts")
        from gtts import gTTS
        return True

def create_audio_files():
    """Génère tous les fichiers audio bibliques"""
    
    # Installer gTTS si nécessaire
    if not install_gtts():
        print("❌ Impossible d'installer gTTS")
        return False
    
    from gtts import gTTS
    
    # Créer le dossier audio
    audio_dir = Path("audio")
    audio_dir.mkdir(exist_ok=True)
    
    # Narrations bibliques enrichies
    narrations = {
        "ur": """Ur des Chaldéens, aux coordonnées 30°57'N, 46°06'E. 
                Ici commence le voyage extraordinaire d'Abraham. 
                Cette ancienne cité sumérienne était le foyer de Térah, 
                père d'Abraham, Nahor et Haran. Selon Genèse 11:31, 
                Térah prit Abraham et Saraï pour partir vers Canaan.""",
        
        "haran": """Harân, carrefour commercial aux coordonnées 36°52'N, 39°02'E. 
                   Térah s'établit ici jusqu'à sa mort à 205 ans. 
                   C'est de Harân qu'Abraham, à 75 ans, reçoit l'appel divin : 
                   'Va vers le pays que je te montrerai', selon Genèse 12:1. 
                   Le nom Harân signifie 'carrefour' en akkadien.""",
        
        "sichem": """Sichem, première étape en Terre Promise, coordonnées 32°12'N, 35°17'E. 
                    Abraham y dresse son premier autel au chêne de Moré. 
                    L'Éternel lui apparaît et dit : 'Je donnerai ce pays à ta descendance', 
                    selon Genèse 12:7. Sichem deviendra un lieu saint majeur.""",
        
        "bethel": """Béthel, 'Maison de Dieu', coordonnées 31°55'N, 35°14'E. 
                    Abraham y bâtit un autel entre Béthel et Aï. 
                    Il invoque le nom de l'Éternel en ce lieu sacré. 
                    Plus tard, Jacob y recevra sa vision de l'échelle céleste, 
                    confirmant la sainteté de ce site.""",
        
        "ai_ettell": """Aï selon l'hypothèse et-Tell, coordonnées 31°54'N, 35°16'E. 
                       Les fouilles de Marquet-Krause de 1933 à 1935 révèlent 
                       une occupation à l'âge du Bronze ancien. 
                       Cette théorie place Aï près de Béthel, 
                       conformément à Genèse 12:8.""",
        
        "ai_maqatir": """Aï selon l'hypothèse Khirbet el-Maqatir, coordonnées 31°54'N, 35°16'E. 
                        Bryant Wood propose ce site depuis 1995, 
                        avec des preuves archéologiques du Bronze moyen. 
                        Cette localisation correspondrait mieux 
                        au récit de Josué 7-8.""",
        
        "negev": """Le Négev, désert du sud, région aux coordonnées 30°30'N, 34°55'E. 
                   Abraham y séjourna lors de la famine en Canaan. 
                   Cette région semi-aride fut témoin de sa foi 
                   et de sa patience dans l'épreuve. 
                   Le nom Négev signifie 'terre sèche' en hébreu.""",
        
        "hebron": """Hébron, ville éternelle d'Abraham, coordonnées 31°32'N, 35°06'E. 
                    Abraham s'établit près des chênes de Mamré. 
                    Il y reçoit la visite des trois anges. 
                    Sarah y meurt à 127 ans. Abraham achète 
                    la grotte de Makpéla pour 400 sicles d'argent, 
                    selon Genèse 23. Lieu de sépulture des patriarches."""
    }
    
    print("🎵 Génération des fichiers audio...")
    
    for location, text in narrations.items():
        try:
            print(f"   📝 Création de {location}.mp3...")
            
            # Nettoyer le texte
            clean_text = text.replace('\n', ' ').replace('  ', ' ').strip()
            
            # Créer l'audio
            tts = gTTS(text=clean_text, lang='fr', slow=False)
            audio_file = audio_dir / f"{location}.mp3"
            tts.save(str(audio_file))
            
            print(f"   ✅ {location}.mp3 créé avec succès")
            
        except Exception as e:
            print(f"   ❌ Erreur pour {location}: {e}")
    
    print("\n🎉 Génération terminée !")
    
    # Vérifier les fichiers créés
    audio_files = list(audio_dir.glob("*.mp3"))
    print(f"📂 {len(audio_files)} fichiers audio créés dans le dossier 'audio/'")
    
    for file in audio_files:
        print(f"   �� {file.name}")
    
    return True

if __name__ == "__main__":
    print("🚀 Générateur Audio Biblique - Version Corrigée")
    print("=" * 50)
    create_audio_files()
