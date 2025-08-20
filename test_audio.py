#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
from pathlib import Path

def test_gtts():
    try:
        from gtts import gTTS
        print("✅ gTTS importé avec succès")
        return True
    except ImportError as e:
        print(f"❌ Erreur d'import gTTS: {e}")
        return False
    except Exception as e:
        print(f"❌ Erreur gTTS: {e}")
        return False

def create_test_audio():
    try:
        from gtts import gTTS
        
        # Créer le dossier audio s'il n'existe pas
        audio_dir = Path("audio")
        audio_dir.mkdir(exist_ok=True)
        
        # Texte de test simple
        text = "Bonjour, ceci est un test de génération audio."
        
        # Créer le fichier audio
        tts = gTTS(text=text, lang='fr', slow=False)
        tts.save("audio/test.mp3")
        
        print("✅ Fichier de test créé : audio/test.mp3")
        return True
        
    except Exception as e:
        print(f"❌ Erreur lors de la création audio: {e}")
        return False

if __name__ == "__main__":
    print("🔍 Test du système audio...")
    
    if test_gtts():
        print("📝 Tentative de création d'un fichier de test...")
        if create_test_audio():
            print("🎉 Test réussi ! Le système fonctionne.")
        else:
            print("❌ Échec du test de création.")
    else:
        print("❌ gTTS n'est pas disponible.")
