# 🗺️ Voyage Biblique - Famille d'Abraham

Application web immersive retraçant l'itinéraire précis de la famille d'Abraham avec une précision biblique et archéologique maximale.

## 🌐 Application en Ligne

**Accès direct :** [https://VotreUsername.github.io/voyages-biblique/](https://VotreUsername.github.io/voyages-biblique/)

## ✨ Fonctionnalités

- **🗺️ Cartographie 3D** : Visualisation immersive avec MapLibre GL JS
- **📖 Références Bibliques Précises** : Chaque étape avec versets exacts et liens BibleGateway
- **🏺 Précision Archéologique** : Hypothèses scientifiques pour Aï (et-Tell vs Khirbet el-Maqatir)
- **🎵 Narration Audio** : Système hybride MP3 + synthèse vocale
- **📱 Progressive Web App** : Fonctionne hors-ligne, installable sur mobile
- **🎯 Coordonnées Exactes** : Aï localisé à 31°54'0"N, 35°16'0.01"E

## 📱 Utilisation

1. **Ouvrez** l'application dans votre navigateur
2. **Choisissez** le mode 2D ou 3D
3. **Sélectionnez** l'hypothèse archéologique pour Aï
4. **Cliquez** "Démarrer" pour l'animation immersive
5. **Activez** l'audio pour la narration avec références bibliques

## 🏺 Itinéraire Biblique

### Étapes Principales
- **Ur des Chaldéens** (Genèse 11:31) - Point de départ
- **Harân** (Genèse 12:1-4) - Appel divin à Abraham
- **Sichem** (Genèse 12:6-7) - Première promesse en Canaan
- **Béthel** (Genèse 12:8) - Premier autel
- **Aï** (Genèse 12:8) - Repère géographique précis
- **Négev** (Genèse 12:9) - Progression vers le sud
- **Hébron/Mamré** (Genèse 13:18) - Installation définitive

### Précision Archéologique d'Aï
- **et-Tell** : Fouilles Marquet-Krause (1933-1935)
- **Khirbet el-Maqatir** : Hypothèse Bryant Wood (depuis 1995)
- Respect parfait de Genèse 12:8 : "Béthel à l'occident et Aï à l'orient"

## 🛠️ Technologies Open Source

- **MapLibre GL JS** : Cartographie 3D performante
- **OpenStreetMap** : Données cartographiques libres
- **gTTS** : Génération audio de qualité
- **Service Worker** : Mode hors-ligne PWA

## 🚀 Installation et Déploiement

### Installation Locale

```bash
# 1. Cloner ou télécharger le projet
git clone https://github.com/VotreUsername/voyages-biblique.git
cd voyages-biblique

# 2. Installer Python et gTTS
pip install gtts

# 3. Générer les fichiers audio
python generate_audio_biblical.py

# 4. Lancer le serveur local
python -m http.server 8000

# 5. Ouvrir http://localhost:8000
```

### Déploiement GitHub Pages

1. **Créer** un repository GitHub public
2. **Upload** tous les fichiers (index.html, generate_audio_biblical.py, audio/)
3. **Activer** GitHub Pages dans Settings → Pages
4. **Accéder** à votre URL : https://VotreUsername.github.io/voyages-biblique/

## 🎵 Génération Audio

Le script `generate_audio_biblical.py` génère automatiquement les narrations audio avec :

- **Références bibliques précises** intégrées dans chaque narration
- **Citations exactes** des versets pertinents
- **Contexte archéologique** et historique
- **Qualité professionnelle** avec gTTS
- **Fallback** vers synthèse vocale navigateur

**Fichiers générés :**
- `ur.mp3` - Ur des Chaldéens (Genèse 11:31)
- `haran.mp3` - Harân (Genèse 12:1-4)
- `sichem.mp3` - Sichem (Genèse 12:6-7)
- `bethel.mp3` - Béthel (Genèse 12:8)
- `ai_ettell.mp3` - Aï selon et-Tell
- `ai_maqatir.mp3` - Aï selon Khirbet el-Maqatir
- `negev.mp3` - Négev (Genèse 12:9)
- `hebron.mp3` - Hébron/Mamré (Genèse 13:18)

## 🤝 Contribution

Contributions bienvenues ! Ouvrez une issue ou soumettez une pull request pour :
- Améliorer la précision géographique
- Ajouter d'autres itinéraires bibliques
- Enrichir les narrations
- Optimiser l'expérience mobile

## 📄 Licence

Projet open source - Libre utilisation pour l'éducation biblique et la recherche

---

*"L'Éternel dit à Abram: Va-t-en de ton pays, de ta patrie, et de la maison de ton père, dans le pays que je te montrerai."* - **Genèse 12:1**

**Développé avec précision biblique et rigueur archéologique** 📖🏺
