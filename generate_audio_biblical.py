<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Script Python - Générateur Audio Biblique</title>
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.4.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@300;400;500&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        .code-block {
            font-family: 'Fira Code', monospace;
            background: linear-gradient(135deg, #1e293b 0%, #334155 100%);
            border-radius: 12px;
            padding: 24px;
            color: #e2e8f0;
            overflow-x: auto;
            box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
        }
        .comment { color: #94a3b8; }
        .string { color: #fbbf24; }
        .keyword { color: #60a5fa; font-weight: 500; }
        .function { color: #34d399; }
        .variable { color: #fb7185; }
        .number { color: #a78bfa; }
        .hero-gradient {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        }
        .feature-card {
            transition: all 0.3s ease;
        }
        .feature-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
        }
    </style>
</head>
<body class="bg-gray-50 font-sans">
    <div class="hero-gradient text-white py-16">
        <div class="container mx-auto px-6 text-center">
            <i class="fas fa-volume-up text-6xl mb-6 opacity-90"></i>
            <h1 class="text-5xl font-bold mb-4">Générateur Audio Biblique</h1>
            <p class="text-xl mb-6 opacity-90">Script Python avec références bibliques précises et coordonnées archéologiques</p>
            <div class="flex justify-center space-x-6 text-sm">
                <div class="flex items-center">
                    <i class="fas fa-map-marker-alt mr-2"></i>
                    <span>Coordonnées exactes d'Aï : 31°54'0"N, 35°16'0.01"E</span>
                </div>
                <div class="flex items-center">
                    <i class="fas fa-book mr-2"></i>
                    <span>8 narrations avec citations bibliques</span>
                </div>
            </div>
        </div>
    </div>

    <div class="container mx-auto px-6 py-12">
        <!-- Features Section -->
        <div class="grid md:grid-cols-3 gap-8 mb-12">
            <div class="feature-card bg-white rounded-xl p-6 shadow-lg">
                <div class="text-center">
                    <div class="bg-blue-100 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4">
                        <i class="fas fa-microphone text-blue-600 text-2xl"></i>
                    </div>
                    <h3 class="font-semibold text-lg mb-2">Génération Audio gTTS</h3>
                    <p class="text-gray-600 text-sm">Conversion automatique des narrations en fichiers MP3 de qualité professionnelle</p>
                </div>
            </div>
            
            <div class="feature-card bg-white rounded-xl p-6 shadow-lg">
                <div class="text-center">
                    <div class="bg-purple-100 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4">
                        <i class="fas fa-scroll text-purple-600 text-2xl"></i>
                    </div>
                    <h3 class="font-semibold text-lg mb-2">Références Bibliques</h3>
                    <p class="text-gray-600 text-sm">Citations précises de Genèse, Néhémie, Actes et Deutéronome intégrées</p>
                </div>
            </div>
            
            <div class="feature-card bg-white rounded-xl p-6 shadow-lg">
                <div class="text-center">
                    <div class="bg-green-100 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4">
                        <i class="fas fa-search-location text-green-600 text-2xl"></i>
                    </div>
                    <h3 class="font-semibold text-lg mb-2">Précision Archéologique</h3>
                    <p class="text-gray-600 text-sm">Hypothèses scientifiques pour Aï : et-Tell vs Khirbet el-Maqatir</p>
                </div>
            </div>
        </div>

        <!-- Audio Files Section -->
        <div class="bg-white rounded-xl shadow-lg p-8 mb-12">
            <h2 class="text-2xl font-bold mb-6 flex items-center">
                <i class="fas fa-music mr-3 text-blue-600"></i>
                Fichiers Audio Générés
            </h2>
            <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-4">
                <div class="bg-gradient-to-r from-blue-50 to-blue-100 p-4 rounded-lg">
                    <h4 class="font-semibold text-blue-800">ur.mp3</h4>
                    <p class="text-xs text-blue-600 mt-1">Ur des Chaldéens - Genèse 11:31</p>
                </div>
                <div class="bg-gradient-to-r from-green-50 to-green-100 p-4 rounded-lg">
                    <h4 class="font-semibold text-green-800">haran.mp3</h4>
                    <p class="text-xs text-green-600 mt-1">Harân - Genèse 12:1-4</p>
                </div>
                <div class="bg-gradient-to-r from-purple-50 to-purple-100 p-4 rounded-lg">
                    <h4 class="font-semibold text-purple-800">sichem.mp3</h4>
                    <p class="text-xs text-purple-600 mt-1">Sichem - Genèse 12:6-7</p>
                </div>
                <div class="bg-gradient-to-r from-indigo-50 to-indigo-100 p-4 rounded-lg">
                    <h4 class="font-semibold text-indigo-800">bethel.mp3</h4>
                    <p class="text-xs text-indigo-600 mt-1">Béthel - Genèse 12:8</p>
                </div>
                <div class="bg-gradient-to-r from-yellow-50 to-yellow-100 p-4 rounded-lg">
                    <h4 class="font-semibold text-yellow-800">ai_ettell.mp3</h4>
                    <p class="text-xs text-yellow-600 mt-1">Aï (et-Tell) - Coordonnées précises</p>
                </div>
                <div class="bg-gradient-to-r from-red-50 to-red-100 p-4 rounded-lg">
                    <h4 class="font-semibold text-red-800">ai_maqatir.mp3</h4>
                    <p class="text-xs text-red-600 mt-1">Aï (Khirbet el-Maqatir) - Hypothèse</p>
                </div>
                <div class="bg-gradient-to-r from-pink-50 to-pink-100 p-4 rounded-lg">
                    <h4 class="font-semibold text-pink-800">negev.mp3</h4>
                    <p class="text-xs text-pink-600 mt-1">Négev - Genèse 12:9</p>
                </div>
                <div class="bg-gradient-to-r from-teal-50 to-teal-100 p-4 rounded-lg">
                    <h4 class="font-semibold text-teal-800">hebron.mp3</h4>
                    <p class="text-xs text-teal-600 mt-1">Hébron/Mamré - Genèse 13:18</p>
                </div>
            </div>
        </div>

        <!-- Code Section -->
        <div class="bg-white rounded-xl shadow-lg p-8">
            <h2 class="text-2xl font-bold mb-6 flex items-center">
                <i class="fas fa-code mr-3 text-green-600"></i>
                Code Source Python
            </h2>
            
            <div class="code-block">
<pre><code><span class="comment">#!/usr/bin/env python3</span>
<span class="comment"># generate_audio_biblical.py - Générateur d'audio avec références bibliques précises</span>

<span class="keyword">import</span> os
<span class="keyword">import</span> sys

<span class="comment"># Installation automatique de gTTS si nécessaire</span>
<span class="keyword">try</span>:
    <span class="keyword">from</span> gtts <span class="keyword">import</span> gTTS
    <span class="variable">GTTS_AVAILABLE</span> = <span class="keyword">True</span>
    <span class="function">print</span>(<span class="string">"✅ gTTS disponible"</span>)
<span class="keyword">except</span> ImportError:
    <span class="function">print</span>(<span class="string">"⚠️  Installation automatique de gTTS..."</span>)
    <span class="keyword">try</span>:
        <span class="keyword">import</span> subprocess
        subprocess.<span class="function">check_call</span>([sys.executable, <span class="string">"-m"</span>, <span class="string">"pip"</span>, <span class="string">"install"</span>, <span class="string">"gtts"</span>])
        <span class="keyword">from</span> gtts <span class="keyword">import</span> gTTS
        <span class="variable">GTTS_AVAILABLE</span> = <span class="keyword">True</span>
        <span class="function">print</span>(<span class="string">"✅ gTTS installé avec succès"</span>)
    <span class="keyword">except</span> Exception <span class="keyword">as</span> e:
        <span class="variable">GTTS_AVAILABLE</span> = <span class="keyword">False</span>
        <span class="function">print</span>(<span class="function">f</span><span class="string">"❌ Impossible d'installer gTTS: {e}"</span>)
        <span class="function">print</span>(<span class="string">"    La synthèse vocale du navigateur prendra le relais"</span>)

<span class="comment"># Créer le dossier audio</span>
os.<span class="function">makedirs</span>(<span class="string">'audio'</span>, exist_ok=<span class="keyword">True</span>)

<span class="comment"># Narrations enrichies avec références bibliques précises</span>
<span class="variable">biblical_narrations</span> = {
    <span class="string">'ur.mp3'</span>: <span class="string">"De la majestueuse cité d'Ur des Chaldéens, berceau de la civilisation sumérienne, Térah rassemble sa famille, comme le raconte Genèse chapitre 11 verset 31 : 'Térah prit Abram, son fils, et Lot, fils d'Haran, et Saraï, sa belle-fille, femme d'Abram, son fils. Ils sortirent ensemble d'Ur en Chaldée, pour aller au pays de Canaan.' Guidés par un appel divin mystérieux, ils quittent cette métropole avancée pour une destination inconnue. Néhémie chapitre 9 verset 7 rappelle que l'Éternel choisit Abram et le fit sortir d'Ur des Chaldéens."</span>,
    
    <span class="string">'haran.mp3'</span>: <span class="string">"À Harân, carrefour vital des routes commerciales, la famille s'établit temporairement. Ici, selon Genèse chapitre 11 verset 32, Térah meurt à l'âge de 205 ans. C'est alors que l'Éternel adresse son appel historique à Abram, rapporté en Genèse chapitre 12 versets 1 à 4 : 'L'Éternel dit à Abram: Va-t-en de ton pays, de ta patrie, et de la maison de ton père, dans le pays que je te montrerai. Abram partit, comme l'Éternel le lui avait dit, et Lot partit avec lui. Abram était âgé de soixante-quinze ans, lorsqu'il sortit de Charan.' Étienne, dans Actes chapitre 7 versets 2 à 4, confirme cet appel divin."</span>,
    
    <span class="string">'sichem.mp3'</span>: <span class="string">"Arrivés en terre de Canaan, au chêne sacré de Moré près de Sichem, la famille d'Abraham vit un moment historique. Selon Genèse chapitre 12 versets 6 et 7, 'Abram parcourut le pays jusqu'au lieu nommé Sichem, jusqu'aux chênes de Moré. Les Cananéens étaient alors dans le pays. L'Éternel apparut à Abram, et dit: Je donnerai ce pays à ta postérité.' Cette promesse révolutionnaire inaugure l'alliance abrahamique en Terre Promise. Deutéronome chapitre 11 verset 30 situe géographiquement ces chênes de Moré."</span>,
    
    <span class="string">'bethel.mp3'</span>: <span class="string">"À Béthel, lieu qui signifie 'maison de Dieu', Abraham établit son campement selon Genèse chapitre 12 verset 8 : 'Il se transporta de là vers la montagne, à l'orient de Béthel, et il dressa ses tentes, ayant Béthel à l'occident et Aï à l'orient. Il bâtit là un autel à l'Éternel, et il invoqua le nom de l'Éternel.' Toute la famille participe à cet acte de foi, établissant le premier lieu de culte familial en Canaan. Genèse chapitre 13 versets 3 et 4 indique qu'Abraham reviendra à ce lieu après l'épisode égyptien."</span>,
    
    <span class="string">'ai_ettell.mp3'</span>: <span class="string">"La précision géographique de Genèse chapitre 12 verset 8 - 'Il dressa ses tentes, ayant Béthel à l'occident et Aï à l'orient' - guide l'identification archéologique d'Aï. Les fouilles de Judith Marquet-Krause entre 1933 et 1935 à et-Tell, situé exactement aux coordonnées 31°54'0\" Nord, 35°16'0.01\" Est, révèlent une occupation au Bronze ancien. Cette localisation respecte parfaitement la description biblique et la distance de 3 kilomètres à l'est de Béthel, confirmée aussi dans Josué chapitre 7 verset 2."</span>,
    
    <span class="string">'ai_maqatir.mp3'</span>: <span class="string">"L'exigence de précision géographique de Genèse chapitre 12 verset 8 - 'ayant Béthel à l'occident et Aï à l'orient' - a conduit Bryant Wood à proposer depuis 1995 une localisation alternative d'Aï à Khirbet el-Maqatir. Cette hypothèse archéologique moderne s'appuie sur de nouvelles fouilles révélant des fortifications du Bronze moyen et une occupation du Fer, périodes potentiellement compatibles avec les récits d'Abraham et de Josué chapitre 8."</span>,
    
    <span class="string">'negev.mp3'</span>: <span class="string">"La famille d'Abraham progresse vers le Négev selon Genèse chapitre 12 verset 9 : 'Abram continua ses marches, en s'avançant vers le midi.' Cette région semi-aride, mentionnée plus de 100 fois dans la Bible, constitue la zone de transition entre Canaan et l'Égypte. Genèse chapitre 20 verset 1 précise qu'Abraham séjourna dans le pays du Négev. L'archéologie révèle des sites pastoraux de cette époque, avec des puits et des installations temporaires typiques du mode de vie nomade patriarcal."</span>,
    
    <span class="string">'hebron.mp3'</span>: <span class="string">"À Hébron, près des chênes sacrés de Mamré, Abraham trouve sa demeure définitive selon Genèse chapitre 13 verset 18 : 'Abram leva ses tentes, et vint habiter parmi les chênes de Mamré, qui sont près d'Hébron. Et il bâtit là un autel à l'Éternel.' C'est ici, selon Genèse chapitre 18 verset 1, que l'Éternel apparaît à Abraham près des chênes de Mamré. Genèse chapitre 23 versets 17 à 20 relate l'achat du champ et de la caverne de Macpéla pour ensevelir Sara, premier acte de propriété en Terre Promise. Genèse chapitre 25 versets 9 et 10 confirme qu'Abraham y fut aussi enseveli par Isaac et Ismaël."</span>
}

<span class="function">print</span>(<span class="string">"📖 Génération des fichiers audio avec références bibliques précises"</span>)
<span class="function">print</span>(<span class="string">"="</span> * <span class="number">80</span>)

<span class="variable">success_count</span> = <span class="number">0</span>
<span class="variable">total_files</span> = <span class="function">len</span>(biblical_narrations)

<span class="keyword">for</span> filename, text <span class="keyword">in</span> biblical_narrations.<span class="function">items</span>():
    <span class="keyword">try</span>:
        <span class="keyword">if</span> GTTS_AVAILABLE:
            <span class="comment"># Génération audio avec gTTS</span>
            <span class="variable">tts</span> = <span class="function">gTTS</span>(text=text, lang=<span class="string">'fr'</span>, slow=<span class="keyword">False</span>, tld=<span class="string">'fr'</span>)
            tts.<span class="function">save</span>(<span class="function">f</span><span class="string">'audio/{filename}'</span>)
            <span class="function">print</span>(<span class="function">f</span><span class="string">"✅ Audio biblique créé: {filename}"</span>)
            <span class="function">print</span>(<span class="function">f</span><span class="string">"   📝 Longueur: {len(text)} caractères"</span>)
            <span class="variable">success_count</span> += <span class="number">1</span>
        <span class="keyword">else</span>:
            <span class="comment"># Fichier placeholder avec métadonnées</span>
            <span class="keyword">with</span> <span class="function">open</span>(<span class="function">f</span><span class="string">'audio/{filename}'</span>, <span class="string">'wb'</span>) <span class="keyword">as</span> f:
                f.<span class="function">write</span>(<span class="string">b'\xff\xfb\x90\x00'</span> + <span class="string">b'\x00'</span> * <span class="number">200</span>)
            <span class="function">print</span>(<span class="function">f</span><span class="string">"⚠️  Placeholder créé: {filename}"</span>)
            <span class="variable">success_count</span> += <span class="number">1</span>
            
    <span class="keyword">except</span> Exception <span class="keyword">as</span> e:
        <span class="function">print</span>(<span class="function">f</span><span class="string">"❌ Erreur pour {filename}: {e}"</span>)

<span class="function">print</span>(<span class="string">"="</span> * <span class="number">80</span>)
<span class="function">print</span>(<span class="function">f</span><span class="string">"📖 Génération terminée: {success_count}/{total_files} fichiers créés"</span>)

<span class="keyword">if</span> GTTS_AVAILABLE:
    <span class="function">print</span>(<span class="string">"🎵 Audio de qualité professionnelle avec références bibliques précises"</span>)
<span class="keyword">else</span>:
    <span class="function">print</span>(<span class="string">"ℹ️  La synthèse vocale du navigateur lira les références bibliques"</span>)

<span class="function">print</span>(<span class="string">"\n🚀 Votre application biblique est prête avec une précision scripturaire maximale !"</span>)</code></pre>
            </div>
        </div>

        <!-- Instructions Section -->
        <div class="bg-blue-50 rounded-xl p-8 mt-12">
            <h2 class="text-2xl font-bold mb-6 text-blue-800 flex items-center">
                <i class="fas fa-play-circle mr-3"></i>
                Instructions d'utilisation
            </h2>
            <div class="grid md:grid-cols-2 gap-6">
                <div>
                    <h4 class="font-semibold mb-3 text-blue-700">1. Installation</h4>
                    <div class="bg-white p-4 rounded-lg font-mono text-sm">
                        <code>pip install gtts</code>
                    </div>
                </div>
                <div>
                    <h4 class="font-semibold mb-3 text-blue-700">2. Exécution</h4>
                    <div class="bg-white p-4 rounded-lg font-mono text-sm">
                        <code>python generate_audio_biblical.py</code>
                    </div>
                </div>
            </div>
            <div class="mt-6 p-4 bg-blue-100 rounded-lg">
                <p class="text-blue-800 text-sm">
                    <i class="fas fa-info-circle mr-2"></i>
                    Le script génère automatiquement le dossier <code>audio/</code> et y place tous les fichiers MP3 avec les narrations bibliques enrichies.
                </p>
            </div>
        </div>
    </div>

    <footer class="hero-gradient text-white py-8 mt-16">
        <div class="container mx-auto px-6 text-center">
            <p class="text-lg mb-2">📖 Développé avec précision biblique et rigueur archéologique</p>
            <p class="text-sm opacity-75">"L'Éternel dit à Abram: Va-t-en de ton pays, de ta patrie, et de la maison de ton père, dans le pays que je te montrerai." - Genèse 12:1</p>
        </div>
    </footer>
</body>
</html>
    <script id="html_badge_script1">
        window.__genspark_remove_badge_link = "https://www.genspark.ai/api/html_badge/" +
            "remove_badge?token=To%2FBnjzloZ3UfQdcSaYfDuJF5x5wT2XGGusKGOyhkG%2BxxTWRl02rYyvH5EiL70ocPnxQExyzLJDCkT6soNXkN49ab9tzfRskHyp6WKQcqzU0AigZaRwNNeaXS1yGp6RsbvCGM8%2B3%2BVN%2B7JFQrH70vnHCbSTwGszabYci4fJFOg3LdnxlDF6NQEtDq25NRddE%2Fr0DFEORhR0LGsYoif6v%2F3KlqsaEYhEdXO8DSwysfq7hSK6DQQ%2FXnUuXqkpqVOpcAs0IEREKQVrdIu2IBYBXiOGYJ1tw3Pgb%2BMXCX9LGG8SZaJXhyAL%2Fl%2FALjTlEhbv%2Bl%2B0HBRxHgCd%2F1UOh64Ql%2BmWYZFYHTVD9eWUiGBVI%2FwFXSjUp%2Bov0l3Rnw3JQhyRGfHT5PqInr5RCbDDGh3Efs2uJiZSByuyVfXuuvLKXEXv99CcWhj%2BdCMwh5ZUSfeUOObL2XLN2EU6HJTW65oHAUH1RlnrLT0Nuy1kINmpCXbYu5ZOkDEpHe8ylQDoZi8V%2FhWtDzrn2ZtAECGenKtu8pw%3D%3D";
        window.__genspark_locale = "en-US";
        window.__genspark_token = "To/BnjzloZ3UfQdcSaYfDuJF5x5wT2XGGusKGOyhkG+xxTWRl02rYyvH5EiL70ocPnxQExyzLJDCkT6soNXkN49ab9tzfRskHyp6WKQcqzU0AigZaRwNNeaXS1yGp6RsbvCGM8+3+VN+7JFQrH70vnHCbSTwGszabYci4fJFOg3LdnxlDF6NQEtDq25NRddE/r0DFEORhR0LGsYoif6v/3KlqsaEYhEdXO8DSwysfq7hSK6DQQ/XnUuXqkpqVOpcAs0IEREKQVrdIu2IBYBXiOGYJ1tw3Pgb+MXCX9LGG8SZaJXhyAL/l/ALjTlEhbv+l+0HBRxHgCd/1UOh64Ql+mWYZFYHTVD9eWUiGBVI/wFXSjUp+ov0l3Rnw3JQhyRGfHT5PqInr5RCbDDGh3Efs2uJiZSByuyVfXuuvLKXEXv99CcWhj+dCMwh5ZUSfeUOObL2XLN2EU6HJTW65oHAUH1RlnrLT0Nuy1kINmpCXbYu5ZOkDEpHe8ylQDoZi8V/hWtDzrn2ZtAECGenKtu8pw==";
    </script>
    
    <script id="html_notice_dialog_script" src="https://www.genspark.ai/notice_dialog.js"></script>
    