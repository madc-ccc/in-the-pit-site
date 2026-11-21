import json
#!/usr/bin/env python3
"""Génère le site (5 langues) : python3 build.py   →  index.html (en), fr/, es/, it/, de/ + sitemap.xml
Variable d'environnement DOMAIN pour les URL absolues (défaut https://in-the-pit.com)."""
import os, random, html
DOMAIN = os.environ.get('DOMAIN', 'https://site.i.n-t.he-p.it').rstrip('/')
APP = 'https://i.n-t.he-p.it'
KOFI = 'https://ko-fi.com/inthepit'
L = ['en', 'fr', 'es', 'it', 'de']
NAMES = {'en': 'English', 'fr': 'Français', 'es': 'Español', 'it': 'Italiano', 'de': 'Deutsch'}

# Chaque texte : (en, fr, es, it, de)
T = {
'title': ("In The Pit: your concert diary, tickets included", "In The Pit : ton carnet de concerts, billets compris", "In The Pit: tu diario de conciertos, entradas incluidas", "In The Pit: il tuo diario dei concerti, biglietti inclusi", "In The Pit: dein Konzerttagebuch, Tickets inklusive"),
'desc': ("Keep every concert you have seen or will see, with tickets, photos and friends. Free, on your phone.", "Garde chaque concert vu ou à venir, avec les billets, les photos et tes amis. Gratuit, sur ton téléphone.", "Guarda cada concierto visto o por ver, con entradas, fotos y amigos. Gratis, en tu móvil.", "Conserva ogni concerto visto o in programma, con biglietti, foto e amici. Gratis, sul telefono.", "Bewahre jedes Konzert, das du gesehen hast oder sehen wirst, samt Tickets, Fotos und Freunden. Kostenlos, auf deinem Handy."),
'nav_f': ("Features", "Fonctions", "Funciones", "Funzioni", "Funktionen"),
'nav_q': ("FAQ", "Questions", "Preguntas", "Domande", "Fragen"),
'open': ("Open the app", "Ouvrir l’app", "Abrir la app", "Apri l’app", "App öffnen"),
'see': ("See what it does", "Voir ce qu’elle fait", "Ver qué hace", "Scopri cosa fa", "Funktionen ansehen"),
'h1': ("Your concert diary, tickets included.", "Ton carnet de concerts, billets compris.", "Tu diario de conciertos, entradas incluidas.", "Il tuo diario dei concerti, biglietti inclusi.", "Dein Konzerttagebuch, Tickets inklusive."),
'hp': ("In The Pit keeps every concert you have seen or will see, with the tickets, the photos and your friends. Free, on your phone.", "In The Pit garde chaque concert vu ou à venir, avec les billets, les photos et tes amis. Gratuit, sur ton téléphone.", "In The Pit guarda cada concierto al que has ido o irás, con las entradas, las fotos y tus amigos. Gratis, en tu móvil.", "In The Pit conserva ogni concerto a cui sei stato o andrai, con i biglietti, le foto e gli amici. Gratis, sul telefono.", "In The Pit bewahrt jedes Konzert, das du besucht hast oder besuchen wirst, samt Tickets, Fotos und Freunden. Kostenlos, auf deinem Handy."),

'f1t': ("Tickets ready at the door", "Les billets prêts à l’entrée", "Las entradas listas en la puerta", "I biglietti pronti all’ingresso", "Die Tickets bereit am Einlass"),
'f1p': ("Drop in the PDF you received. In The Pit reads the artist, date, venue and price for you. At the entrance, one tap opens a black screen with only the QR code (or the barcode), big and sharp. It is prepared in advance, so it shows instantly, even with no signal at the venue. The PDF stays one icon away for the staff.", "Dépose le PDF reçu. In The Pit lit l’artiste, la date, la salle et le prix à ta place. À l’entrée, un appui ouvre un écran noir avec le seul QR code (ou code-barres), grand et net. Il est préparé à l’avance : il s’affiche instantanément, même sans réseau dans la salle. Le PDF reste à une icône de distance pour le personnel.", "Sube el PDF que recibiste. In The Pit lee el artista, la fecha, la sala y el precio por ti. En la entrada, un toque abre una pantalla negra solo con el código QR (o el código de barras), grande y nítido. Se prepara con antelación: aparece al instante, incluso sin cobertura en la sala. El PDF queda a un icono de distancia para el personal.", "Carica il PDF ricevuto. In The Pit legge artista, data, locale e prezzo al posto tuo. All’ingresso, un tocco apre uno schermo nero con il solo codice QR (o il codice a barre), grande e nitido. È preparato in anticipo: appare subito, anche senza segnale in sala. Il PDF resta a un’icona di distanza per il personale.", "Lade das erhaltene PDF hoch. In The Pit liest Künstler, Datum, Halle und Preis für dich aus. Am Einlass öffnet ein Fingertipp einen schwarzen Bildschirm nur mit dem QR-Code (oder dem Barcode), groß und scharf. Er wird vorab vorbereitet und erscheint sofort, selbst ohne Empfang in der Halle. Das PDF ist für das Personal ein Symbol entfernt."),
'f1a': ("Paper ticket? Photograph it. It is straightened, cropped and stored as a very light image.", "Un billet papier ? Photographie-le. Il est redressé, recadré et gardé en image très légère.", "¿Entrada de papel? Fotografíala. Se endereza, se recorta y se guarda como una imagen muy ligera.", "Biglietto cartaceo? Fotografalo. Viene raddrizzato, ritagliato e salvato come immagine leggerissima.", "Papierticket? Fotografiere es. Es wird begradigt, zugeschnitten und als sehr leichtes Bild gespeichert."),
'f1b': ("Add a note to the photo. Friends read it translated into their own language.", "Ajoute une note à la photo. Tes amis la lisent traduite dans leur langue.", "Añade una nota a la foto. Tus amigos la leen traducida a su idioma.", "Aggiungi una nota alla foto. Gli amici la leggono tradotta nella loro lingua.", "Füge der Foto eine Notiz hinzu. Freunde lesen sie in ihre Sprache übersetzt."),
'f1c': ("Venue membership cards go in too, with their own QR screen one tap away from your ticket. Bought on DICE? Tick “DICE ticket” and the same button opens the DICE app.", "Les cartes d’abonnement aux salles aussi, avec leur propre écran QR à un appui de ton billet. Billet acheté sur DICE ? Coche « Billet DICE » et le même bouton ouvre l’appli DICE.", "Las tarjetas de socio de las salas también, con su propia pantalla QR a un toque de tu entrada. ¿Entrada comprada en DICE? Marca «Entrada DICE» y el mismo botón abre la app DICE.", "Anche le tessere di abbonamento ai locali, con la loro schermata QR a un tocco dal biglietto. Biglietto comprato su DICE? Spunta «Biglietto DICE» e lo stesso pulsante apre l’app DICE.", "Auch Mitgliedskarten von Hallen, mit eigenem QR-Bildschirm einen Fingertipp von deinem Ticket entfernt. Ticket bei DICE gekauft? Hake „DICE-Ticket“ an, und dieselbe Schaltfläche öffnet die DICE-App."),

'f2t': ("Find any concert in seconds", "Retrouve n’importe quel concert en quelques secondes", "Encuentra cualquier concierto en segundos", "Trova qualsiasi concerto in pochi secondi", "Finde jedes Konzert in Sekunden"),
'f2p': ("Switches for your concerts, your friends’ concerts, the public list, past, upcoming, opening acts and not seen yet. Sort by date either way, and combine two keywords with and / or.", "Des interrupteurs pour tes concerts, ceux de tes amis, la liste publique, passés, à venir, premières parties et pas encore vus. Tri par date dans les deux sens, et deux mots-clés combinés par et / ou.", "Interruptores para tus conciertos, los de tus amigos, la lista pública, pasados, próximos, teloneros y aún no vistos. Orden por fecha en ambos sentidos y dos palabras clave combinadas con y / o.", "Interruttori per i tuoi concerti, quelli degli amici, l’elenco pubblico, passati, futuri, gruppi spalla e non ancora visti. Ordine per data in entrambi i sensi e due parole chiave combinate con e / o.", "Schalter für deine Konzerte, die deiner Freunde, die öffentliche Liste, vergangene, kommende, Vorbands und noch nicht gesehene. Sortierung nach Datum in beide Richtungen, zwei Stichwörter mit und / oder."),
'f2a': ("A slider keeps only what is within reach of home, and the distance shows on every concert.", "Un curseur ne garde que ce qui est à portée de chez toi, et la distance s’affiche sur chaque concert.", "Un control deslizante deja solo lo que está cerca de casa, y la distancia aparece en cada concierto.", "Un cursore tiene solo ciò che è vicino a casa, e la distanza compare su ogni concerto.", "Ein Schieberegler zeigt nur, was von zu Hause erreichbar ist, und die Entfernung steht bei jedem Konzert."),
'f2b': ("Your filters are remembered, and one blue button resets them all.", "Tes filtres sont mémorisés, et un bouton bleu les remet tous à zéro.", "Tus filtros se recuerdan y un botón azul los reinicia todos.", "I filtri vengono ricordati e un pulsante blu li azzera tutti.", "Deine Filter werden gemerkt, und ein blauer Knopf setzt alle zurück."),
'f2c': ("The search also finds friends, by name or email.", "La recherche trouve aussi les amis, par nom ou e-mail.", "La búsqueda también encuentra amigos, por nombre o correo.", "La ricerca trova anche gli amici, per nome o e-mail.", "Die Suche findet auch Freunde, nach Name oder E-Mail."),

'f2d': ("A heart for the artists you love, a ban sign for the ones you never want to see again: they vanish from your list. A “Blacklist” filter brings them back if you change your mind.", "Un cœur pour les artistes que tu aimes, un sens interdit pour ceux que tu ne veux plus voir : ils disparaissent de ta liste. Un filtre « Liste noire » les retrouve si tu changes d’avis.", "Un corazón para los artistas que te encantan, una señal de prohibido para los que no quieres volver a ver: desaparecen de tu lista. Un filtro «Lista negra» los recupera si cambias de opinión.", "Un cuore per gli artisti che ami, un divieto per quelli che non vuoi più vedere: spariscono dalla tua lista. Un filtro «Lista nera» li ritrova se cambi idea.", "Ein Herz für die Künstler, die du liebst, ein Verbotsschild für die, die du nie wieder sehen willst: Sie verschwinden aus deiner Liste. Ein Filter „Schwarze Liste“ holt sie zurück, wenn du es dir anders überlegst."),
'f3t': ("Concerts are better with friends", "Les concerts, c’est mieux entre amis", "Los conciertos son mejores con amigos", "I concerti sono più belli con gli amici", "Konzerte sind mit Freunden besser"),
'f3p': ("Share your list by email. Your friends’ concerts appear in yours, tagged with their name, and you can rename them however you like. You get a notification when a friend adds a concert. When you open the app, the concerts your friends added since your last visit are waiting for you.", "Partage ta liste par e-mail. Les concerts de tes amis apparaissent dans la tienne, avec leur nom, et tu peux les renommer comme tu veux. Tu es prévenu quand un ami ajoute un concert. À l’ouverture de l’app, les concerts ajoutés par tes amis depuis ta dernière visite t’attendent.", "Comparte tu lista por correo. Los conciertos de tus amigos aparecen en la tuya, con su nombre, y puedes renombrarlos como quieras. Recibes un aviso cuando un amigo añade un concierto. Al abrir la app, te esperan los conciertos que tus amigos añadieron desde tu última visita.", "Condividi la tua lista via e-mail. I concerti degli amici compaiono nella tua, con il loro nome, e puoi rinominarli come preferisci. Ricevi una notifica quando un amico aggiunge un concerto. All’apertura dell’app ti aspettano i concerti aggiunti dai tuoi amici dalla tua ultima visita.", "Teile deine Liste per E-Mail. Die Konzerte deiner Freunde erscheinen in deiner, mit ihrem Namen, und du kannst sie beliebig umbenennen. Du wirst benachrichtigt, wenn ein Freund ein Konzert hinzufügt. Beim Öffnen der App warten die Konzerte auf dich, die deine Freunde seit deinem letzten Besuch hinzugefügt haben."),
'f3a': ("Your venue memberships stay private. Only photos and notes of old tickets are shown to your friends.", "Tes abonnements restent privés. Seules les photos et notes de vieux billets sont montrées à tes amis.", "Tus abonos siguen siendo privados. Solo se muestran a tus amigos las fotos y notas de entradas antiguas.", "I tuoi abbonamenti restano privati. Solo foto e note dei vecchi biglietti sono mostrate agli amici.", "Deine Mitgliedschaften bleiben privat. Nur Fotos und Notizen alter Tickets sehen deine Freunde."),
'tile_a': ("Marée Noire", "Marée Noire", "Marée Noire", "Marée Noire", "Marée Noire"),
'note': ("“Front row, Hellfest 2009. Still the loudest night of my life.”", "« Premier rang, Hellfest 2009. La nuit la plus bruyante de ma vie. »", "«Primera fila, Hellfest 2009. La noche más ruidosa de mi vida.»", "«Prima fila, Hellfest 2009. La notte più rumorosa della mia vita.»", "„Erste Reihe, Hellfest 2009. Die lauteste Nacht meines Lebens.“"),
'note_c': ("Translated automatically from Spanish", "Traduit automatiquement de l’espagnol", "Traducido automáticamente del italiano", "Tradotto automaticamente dallo spagnolo", "Automatisch aus dem Spanischen übersetzt"),

'f6t': ("Upcoming concerts, found for you", "Les prochains concerts, trouvés pour toi", "Los próximos conciertos, encontrados para ti", "I prossimi concerti, trovati per te", "Kommende Konzerte, für dich gefunden"),
'f6p': ("Every day, In The Pit reads the agendas of the venues its members go to and adds the missing concerts to the public list. You see them alongside your own, and one tap imports a concert into your list.", "Chaque jour, In The Pit lit l’agenda des salles où vont ses membres et ajoute les concerts manquants à la liste publique. Tu les vois à côté des tiens, et un appui suffit pour en importer un dans ta liste.", "Cada día, In The Pit lee la agenda de las salas a las que van sus miembros y añade los conciertos que faltan a la lista pública. Los ves junto a los tuyos, y basta un toque para importar uno a tu lista.", "Ogni giorno In The Pit legge l’agenda dei locali frequentati dai suoi membri e aggiunge i concerti mancanti all’elenco pubblico. Li vedi accanto ai tuoi e basta un tocco per importarne uno nella tua lista.", "In The Pit liest jeden Tag die Programme der Locations, die seine Mitglieder besuchen, und ergänzt fehlende Konzerte in der öffentlichen Liste. Du siehst sie neben deinen eigenen, und ein Tippen übernimmt ein Konzert in deine Liste."),
'f6a': ("Opening acts, base ticket price and a link to the concert page, with a red “Sold out” mark as soon as the venue announces it.", "Premières parties, prix de base et lien vers la page du concert, avec une mention rouge « Complet » dès que la salle l’annonce.", "Teloneros, precio base y enlace a la página del concierto, con una mención roja «Agotado» en cuanto la sala lo anuncia.", "Gruppi di apertura, prezzo base e link alla pagina del concerto, con la dicitura rossa «Sold out» appena il locale lo annuncia.", "Vorbands, Grundpreis und Link zur Konzertseite, mit rotem Hinweis „Ausverkauft“, sobald die Location es meldet."),
'f6b': ("A bell at the top of your list shows what was added since your last visit, your favourite artists first. Choose your favourites only or every artist except your blacklist, and get them as a notification or by e-mail every day or every Monday.", "Une cloche en haut de ta liste montre ce qui a été ajouté depuis ton dernier passage, tes artistes favoris en premier. Choisis tes favoris seulement ou tous les artistes sauf ta liste noire, et reçois-les en notification ou par e-mail chaque jour ou chaque lundi.", "Una campana arriba de tu lista muestra lo añadido desde tu última visita, tus artistas favoritos primero. Elige solo tus favoritos o todos los artistas salvo tu lista negra, y recíbelos como notificación o por correo cada día o cada lunes.", "Una campanella in cima alla tua lista mostra cosa è stato aggiunto dalla tua ultima visita, prima i tuoi artisti preferiti. Scegli solo i preferiti o tutti gli artisti tranne la lista nera, e ricevili come notifica o via e-mail ogni giorno o ogni lunedì.", "Eine Glocke oben in deiner Liste zeigt, was seit deinem letzten Besuch hinzugekommen ist, deine Lieblingskünstler zuerst. Wähle nur deine Favoriten oder alle Künstler außer deiner schwarzen Liste und erhalte sie als Benachrichtigung oder jeden Tag oder jeden Montag per E-Mail."),
'f6c': ("You choose how far from home: 10 km by default, up to unlimited.", "Tu choisis jusqu’où depuis chez toi : 10 km par défaut, jusqu’à illimité.", "Tú eliges hasta dónde desde tu casa: 10 km por defecto, hasta ilimitado.", "Scegli fin dove da casa tua: 10 km di default, fino a illimitato.", "Du wählst, wie weit von zu Hause: standardmäßig 10 km, bis unbegrenzt."),
'f6_n': ("2 new concerts for you", "2 nouveaux concerts pour toi", "2 nuevos conciertos para ti", "2 nuovi concerti per te", "2 neue Konzerte für dich"),
'f6_so': ("Sold out", "Complet", "Agotado", "Sold out", "Ausverkauft"),
'f6_src': ("Found on the venue’s website", "Trouvé sur le site de la salle", "Encontrado en la web de la sala", "Trovato sul sito del locale", "Auf der Website der Location gefunden"),
'f4t': ("Your concerts in numbers", "Tes concerts en chiffres", "Tus conciertos en cifras", "I tuoi concerti in numeri", "Deine Konzerte in Zahlen"),
'f4p': ("Concerts per year, most-seen artists, most-visited venues, countries, and how your year is spread by week or month. Tap a bar to see the concerts behind it.", "Concerts par année, artistes les plus vus, salles les plus fréquentées, pays, et répartition de ton année par semaine ou par mois. Touche une barre pour voir les concerts derrière.", "Conciertos por año, artistas más vistos, salas más frecuentadas, países y cómo se reparte tu año por semanas o meses. Toca una barra para ver los conciertos que hay detrás.", "Concerti per anno, artisti più visti, locali più frequentati, paesi e come si distribuisce il tuo anno per settimane o mesi. Tocca una barra per vedere i concerti che la compongono.", "Konzerte pro Jahr, meistgesehene Künstler, meistbesuchte Hallen, Länder und wie sich dein Jahr nach Wochen oder Monaten verteilt. Tippe auf einen Balken, um die Konzerte dahinter zu sehen."),

'f5t': ("Never miss the day", "Ne rate jamais le jour J", "No te pierdas el día", "Non perdere il giorno giusto", "Verpasse nie den Tag"),
'f5p': ("Push reminders one week before, the evening before and on the day itself. Choose which ones you want. Today’s concerts are pinned at the top of your upcoming list.", "Des rappels une semaine avant, la veille et le jour même. Tu choisis lesquels. Les concerts du jour sont épinglés en tête de ta liste à venir.", "Avisos una semana antes, la víspera y el mismo día. Tú eliges cuáles. Los conciertos de hoy se fijan arriba en tu lista de próximos.", "Promemoria una settimana prima, la vigilia e il giorno stesso. Scegli quali. I concerti di oggi sono fissati in cima all’elenco dei prossimi.", "Erinnerungen eine Woche vorher, am Vortag und am Tag selbst. Du wählst, welche. Die Konzerte von heute stehen oben in deiner Liste der kommenden."),
'n1': ("Tomorrow: Velvet Static, Le Trianon", "Demain : Velvet Static, Le Trianon", "Mañana: Velvet Static, Le Trianon", "Domani: Velvet Static, Le Trianon", "Morgen: Velvet Static, Le Trianon"),
'n2': ("In 7 days: Marée Noire, L’Olympia", "Dans 7 jours : Marée Noire, L’Olympia", "En 7 días: Marée Noire, L’Olympia", "Tra 7 giorni: Marée Noire, L’Olympia", "In 7 Tagen: Marée Noire, L’Olympia"),
'n3': ("Alice added a concert: Los Cometas", "Alice a ajouté un concert : Los Cometas", "Alice añadió un concierto: Los Cometas", "Alice ha aggiunto un concerto: Los Cometas", "Alice hat ein Konzert hinzugefügt: Los Cometas"),

'mt': ("And a few small things", "Et quelques petites choses", "Y algunas cosas pequeñas", "E qualche piccola cosa", "Und ein paar Kleinigkeiten"),
'm1': ("Five languages", "Cinq langues", "Cinco idiomas", "Cinque lingue", "Fünf Sprachen"), 'm1p': ("English, French, Spanish, Italian and German.", "Anglais, français, espagnol, italien et allemand.", "Inglés, francés, español, italiano y alemán.", "Inglese, francese, spagnolo, italiano e tedesco.", "Englisch, Französisch, Spanisch, Italienisch und Deutsch."),
'm2': ("On your home screen", "Sur ton écran d’accueil", "En tu pantalla de inicio", "Sulla schermata iniziale", "Auf deinem Startbildschirm"), 'm2p': ("Add it from your browser menu. No store, no download.", "Ajoute-la depuis le menu du navigateur. Pas de boutique, pas de téléchargement.", "Añádela desde el menú del navegador. Sin tienda, sin descargas.", "Aggiungila dal menu del browser. Nessuno store, nessun download.", "Füge sie über das Browsermenü hinzu. Kein Store, kein Download."),
'm3': ("Your list as an image", "Ta liste en image", "Tu lista como imagen", "La tua lista come immagine", "Deine Liste als Bild"), 'm3p': ("One tap captures the list you are looking at, ready to share.", "Un appui capture la liste affichée, prête à partager.", "Un toque captura la lista que ves, lista para compartir.", "Un tocco cattura l’elenco che vedi, pronto da condividere.", "Ein Tipp erfasst die angezeigte Liste, bereit zum Teilen."),
'm4': ("Band photos", "Photos des groupes", "Fotos de los grupos", "Foto dei gruppi", "Bandfotos"), 'm4p': ("Pick one from Wikipedia or Deezer, or use your own.", "Choisis-en une sur Wikipédia ou Deezer, ou utilise la tienne.", "Elige una de Wikipedia o Deezer, o usa la tuya.", "Scegline una da Wikipedia o Deezer, o usa la tua.", "Wähle eine von Wikipedia oder Deezer oder nimm deine eigene."),
'm5': ("Your own wallpaper", "Ton propre fond d’écran", "Tu propio fondo", "Il tuo sfondo", "Dein eigener Hintergrund"), 'm5p': ("Choose the picture behind your list.", "Choisis l’image derrière ta liste.", "Elige la imagen detrás de tu lista.", "Scegli l’immagine dietro la tua lista.", "Wähle das Bild hinter deiner Liste."),
'm6': ("Guest preview", "Découverte en invité", "Vista de invitado", "Anteprima ospite", "Gastansicht"), 'm6p': ("Browse the community list without an account.", "Parcours la liste de la communauté sans compte.", "Recorre la lista de la comunidad sin cuenta.", "Sfoglia l’elenco della comunità senza account.", "Stöbere ohne Konto in der Liste der Community."),
'm7': ("Idea box", "Boîte à idées", "Buzón de ideas", "Casella delle idee", "Ideenbox"), 'm7p': ("Suggest what comes next. It goes straight to the creators.", "Propose la suite. Ça arrive directement aux créateurs.", "Propón lo que viene. Llega directo a los creadores.", "Proponi cosa fare dopo. Arriva direttamente ai creatori.", "Schlage vor, was kommt. Es geht direkt an die Entwickler."),
'm8': ("What’s new", "Les nouveautés", "Novedades", "Novità", "Neuigkeiten"), 'm8p': ("After an update, see only what changed since your version.", "Après une mise à jour, vois seulement ce qui a changé depuis ta version.", "Tras una actualización, ve solo lo que cambió desde tu versión.", "Dopo un aggiornamento, vedi solo ciò che è cambiato dalla tua versione.", "Nach einem Update siehst du nur, was sich seit deiner Version geändert hat."),

'm9': ("Works offline", "Fonctionne hors connexion", "Funciona sin conexión", "Funziona offline", "Funktioniert offline"), 'm9p': ("Your list and your tickets open without a signal, even deep inside the venue.", "Ta liste et tes billets s’ouvrent sans réseau, même au fond de la salle.", "Tu lista y tus entradas se abren sin cobertura, incluso en el fondo de la sala.", "La tua lista e i tuoi biglietti si aprono senza segnale, anche in fondo alla sala.", "Deine Liste und deine Tickets öffnen sich ohne Empfang, selbst tief in der Halle."),
'm10': ("Better together", "Plus riche à plusieurs", "Mejor en comunidad", "Meglio insieme", "Gemeinsam besser"), 'm10p': ("The more people share their concerts, the richer the public list gets. You choose whether to join, anonymously.", "Plus on partage ses concerts, plus la liste publique s’enrichit. Tu choisis d’y participer, anonymement.", "Cuantos más compartan sus conciertos, más rica es la lista pública. Tú eliges si participar, de forma anónima.", "Più persone condividono i concerti, più si arricchisce l’elenco pubblico. Scegli tu se partecipare, in modo anonimo.", "Je mehr Leute ihre Konzerte teilen, desto reicher wird die öffentliche Liste. Du entscheidest, ob du anonym mitmachst."),

'm11': ("Your data stays yours", "Tes données restent les tiennes", "Tus datos siguen siendo tuyos", "I tuoi dati restano tuoi", "Deine Daten bleiben deine"), 'm11p': ("Export everything or delete your account in one tap. No ads, nothing sold.", "Exporte tout ou supprime ton compte en un geste. Pas de pub, rien n’est vendu.", "Exporta todo o elimina tu cuenta en un toque. Sin publicidad, nada se vende.", "Esporta tutto o elimina il tuo account con un tocco. Niente pubblicità, niente viene venduto.", "Exportiere alles oder lösche dein Konto mit einem Tipp. Keine Werbung, nichts wird verkauft."),
'm12': ("Optional ticket vault", "Coffre à billets facultatif", "Caja fuerte de entradas opcional", "Cassaforte dei biglietti facoltativa", "Optionaler Ticket-Tresor"), 'm12p': ("Lock your PDF tickets with a passphrase only you know. They are encrypted on your phone, so nobody else can read them. A ticket that matters more can even get its own passphrase.", "Verrouille tes billets PDF avec une phrase secrète que toi seul connais. Ils sont chiffrés sur ton téléphone : personne d’autre ne peut les lire. Un billet qui compte plus que les autres peut même avoir sa propre phrase secrète.", "Bloquea tus entradas PDF con una frase secreta que solo tú conoces. Se cifran en tu teléfono: nadie más puede leerlas. Una entrada más importante puede incluso tener su propia frase secreta.", "Proteggi i tuoi biglietti PDF con una frase segreta che conosci solo tu. Sono crittografati sul tuo telefono: nessun altro può leggerli. Un biglietto più importante può persino avere la sua frase segreta.", "Sperre deine PDF-Tickets mit einer Passphrase, die nur du kennst. Sie werden auf deinem Handy verschlüsselt, niemand sonst kann sie lesen. Ein besonders wichtiges Ticket kann sogar eine eigene Passphrase bekommen."),
'lg_t': ("Legal notice", "Mentions légales", "Aviso legal", "Note legali", "Impressum"),
'lg_priv': ("Privacy policy", "Politique de confidentialité", "Política de privacidad", "Informativa sulla privacy", "Datenschutzerklärung"),
'lg_back': ("Back to the home page", "Retour à l’accueil", "Volver al inicio", "Torna alla home", "Zurück zur Startseite"),
'lg_h1': ("Publisher", "Éditeur", "Editor", "Editore", "Herausgeber"),
# Éditeur : Zion Hut Studio. Le jour de l’immatriculation, ajouter forme juridique, SIRET et adresse — voir CLAUDE.md
'lg_p1': ("This site and the In The Pit app are published by Zion Hut Studio. Contact: {C}.", "Ce site et l’application In The Pit sont édités par Zion Hut Studio. Contact : {C}.", "Este sitio y la aplicación In The Pit están editados por Zion Hut Studio. Contacto: {C}.", "Questo sito e l’app In The Pit sono pubblicati da Zion Hut Studio. Contatto: {C}.", "Diese Website und die App In The Pit werden von Zion Hut Studio herausgegeben. Kontakt: {C}."),
'lg_h2': ("Hosting", "Hébergement", "Alojamiento", "Hosting", "Hosting"),
'lg_p2': ("This site and the app are hosted by Netlify, Inc., 101 2nd Street, San Francisco, CA 94105, USA (netlify.com). The app’s data is hosted by Supabase on servers located in Paris, France.", "Ce site et l’application sont hébergés par Netlify, Inc., 101 2nd Street, San Francisco, CA 94105, États-Unis (netlify.com). Les données de l’application sont hébergées par Supabase sur des serveurs situés à Paris, France.", "Este sitio y la aplicación están alojados por Netlify, Inc., 101 2nd Street, San Francisco, CA 94105, EE. UU. (netlify.com). Los datos de la aplicación están alojados por Supabase en servidores situados en París, Francia.", "Questo sito e l’app sono ospitati da Netlify, Inc., 101 2nd Street, San Francisco, CA 94105, USA (netlify.com). I dati dell’app sono ospitati da Supabase su server situati a Parigi, Francia.", "Diese Website und die App werden von Netlify, Inc., 101 2nd Street, San Francisco, CA 94105, USA (netlify.com) gehostet. Die Daten der App liegen bei Supabase auf Servern in Paris, Frankreich."),
'lg_h3': ("Personal data", "Données personnelles", "Datos personales", "Dati personali", "Personenbezogene Daten"),
'lg_p3': ("This site uses no cookies, no audience measurement and no forms. Like any web host, Netlify keeps technical connection logs (IP address, pages requested) for security. How the app handles your data is described in its privacy policy.", "Ce site n’utilise ni cookies, ni mesure d’audience, ni formulaire. Comme tout hébergeur, Netlify conserve des journaux techniques de connexion (adresse IP, pages demandées) à des fins de sécurité. Le traitement de vos données par l’application est décrit dans sa politique de confidentialité.", "Este sitio no utiliza cookies, medición de audiencia ni formularios. Como todo alojamiento web, Netlify conserva registros técnicos de conexión (dirección IP, páginas solicitadas) por seguridad. El tratamiento de tus datos por la aplicación se describe en su política de privacidad.", "Questo sito non usa cookie, misurazione dell’audience né moduli. Come ogni host web, Netlify conserva log tecnici di connessione (indirizzo IP, pagine richieste) per sicurezza. Il trattamento dei tuoi dati da parte dell’app è descritto nella sua informativa sulla privacy.", "Diese Website verwendet keine Cookies, keine Reichweitenmessung und keine Formulare. Wie jeder Webhoster speichert Netlify aus Sicherheitsgründen technische Verbindungsprotokolle (IP-Adresse, aufgerufene Seiten). Wie die App mit deinen Daten umgeht, steht in ihrer Datenschutzerklärung."),
'lg_h4': ("Content", "Contenus", "Contenidos", "Contenuti", "Inhalte"),
'lg_p4': ("The In The Pit name, logo, texts and screenshots belong to the publisher. The band names shown in the screenshots are fictional.", "Le nom In The Pit, le logo, les textes et les captures d’écran appartiennent à l’éditeur. Les noms de groupes visibles dans les captures sont fictifs.", "El nombre In The Pit, el logotipo, los textos y las capturas pertenecen al editor. Los nombres de grupos de las capturas son ficticios.", "Il nome In The Pit, il logo, i testi e gli screenshot appartengono all’editore. I nomi dei gruppi negli screenshot sono fittizi.", "Der Name In The Pit, das Logo, die Texte und die Screenshots gehören dem Herausgeber. Die Bandnamen in den Screenshots sind erfunden."),
'c1t': ("No PDF? Still worth it.", "Pas de PDF ? Ça vaut le coup quand même.", "¿Sin PDF? Vale la pena igual.", "Niente PDF? Ne vale comunque la pena.", "Kein PDF? Lohnt sich trotzdem."),
'c1p': ("Uploading tickets is optional. Without a single PDF, In The Pit already gives you:", "Importer ses billets est facultatif. Sans un seul PDF, In The Pit t’apporte déjà :", "Subir las entradas es opcional. Sin un solo PDF, In The Pit ya te da:", "Caricare i biglietti è facoltativo. Senza un solo PDF, In The Pit ti offre già:", "Tickets hochzuladen ist freiwillig. Ganz ohne PDF bietet dir In The Pit schon:"),
'c1a': ("your whole concert history, each show added in seconds", "tout ton historique de concerts, chaque date ajoutée en quelques secondes", "todo tu historial de conciertos, cada uno añadido en segundos", "tutta la tua storia di concerti, ognuno aggiunto in pochi secondi", "deine ganze Konzertgeschichte, jedes Konzert in Sekunden eingetragen"),
'c1b': ("filters, statistics and your favourite venues", "les filtres, les statistiques et tes salles préférées", "filtros, estadísticas y tus salas favoritas", "filtri, statistiche e i tuoi locali preferiti", "Filter, Statistiken und deine Lieblingshallen"),
'c1c': ("your friends’ concerts, and a pop-up when they add new ones", "les concerts de tes amis, et une fenêtre quand ils en ajoutent", "los conciertos de tus amigos, y un aviso cuando añaden nuevos", "i concerti dei tuoi amici, e un avviso quando ne aggiungono", "die Konzerte deiner Freunde, mit Hinweis bei neuen Einträgen"),
'c1d': ("reminders before every show, and the public list of concerts near you", "des rappels avant chaque concert, et la liste publique des concerts près de chez toi", "recordatorios antes de cada concierto, y la lista pública de conciertos cerca de ti", "promemoria prima di ogni concerto, e l’elenco pubblico dei concerti vicino a te", "Erinnerungen vor jedem Konzert und die öffentliche Liste von Konzerten in deiner Nähe"),
'c2t': ("Your tickets, under lock.", "Tes billets, sous clé.", "Tus entradas, bajo llave.", "I tuoi biglietti, sotto chiave.", "Deine Tickets, gut verschlossen."),
'c2p': ("If you do upload a PDF, you can encrypt it on your phone before it leaves. Nobody else can open it, not even us.", "Si tu importes un PDF, tu peux le chiffrer sur ton téléphone avant qu’il ne parte. Personne d’autre ne peut l’ouvrir, pas même nous.", "Si subes un PDF, puedes cifrarlo en tu teléfono antes de que salga. Nadie más puede abrirlo, ni siquiera nosotros.", "Se carichi un PDF, puoi crittografarlo sul tuo telefono prima che parta. Nessun altro può aprirlo, nemmeno noi.", "Wenn du ein PDF hochlädst, kannst du es auf deinem Handy verschlüsseln, bevor es losgeht. Niemand sonst kann es öffnen, nicht einmal wir."),
'c2a': ("One passphrase for all your tickets", "Une phrase secrète pour tous tes billets", "Una frase secreta para todas tus entradas", "Una frase segreta per tutti i tuoi biglietti", "Eine Passphrase für alle deine Tickets"),
'c2ap': ("Turn on the ticket vault once, and every new ticket is encrypted automatically.", "Active le coffre à billets une fois, et chaque nouveau billet est chiffré automatiquement.", "Activa la caja fuerte una vez y cada entrada nueva se cifra automáticamente.", "Attiva la cassaforte una volta e ogni nuovo biglietto viene crittografato automaticamente.", "Aktiviere den Ticket-Tresor einmal, und jedes neue Ticket wird automatisch verschlüsselt."),
'c2b': ("Or one passphrase for one ticket", "Ou une phrase secrète pour un seul billet", "O una frase secreta para una sola entrada", "Oppure una frase segreta per un solo biglietto", "Oder eine Passphrase für ein einziges Ticket"),
'c2bp': ("Give the ticket that matters most a passphrase of its own, separate from everything else.", "Donne au billet qui compte le plus sa propre phrase secrète, séparée de tout le reste.", "Dale a la entrada que más importa su propia frase secreta, separada de todo lo demás.", "Dai al biglietto più importante una frase segreta tutta sua, separata da tutto il resto.", "Gib dem wichtigsten Ticket eine eigene Passphrase, getrennt von allem anderen."),
'c2c': ("AES-256 encryption, done on your phone. The passphrase never leaves it.", "Chiffrement AES-256, réalisé sur ton téléphone. La phrase secrète ne le quitte jamais.", "Cifrado AES-256, hecho en tu teléfono. La frase secreta nunca sale de él.", "Crittografia AES-256, eseguita sul tuo telefono. La frase segreta non lo lascia mai.", "AES-256-Verschlüsselung direkt auf deinem Handy. Die Passphrase verlässt es nie."),
'q4': ("Do I have to upload my tickets?", "Dois-je importer mes billets ?", "¿Tengo que subir mis entradas?", "Devo caricare i miei biglietti?", "Muss ich meine Tickets hochladen?"),
'a4': ("No. Everything except the ticket screen works without them: your list, filters, statistics, friends, reminders and the public list. If you do upload one, you can encrypt it with a passphrase for all your tickets or one for that ticket only.", "Non. Tout fonctionne sans eux, sauf l’écran du billet : ta liste, les filtres, les statistiques, les amis, les rappels et la liste publique. Si tu en importes un, tu peux le chiffrer avec une phrase secrète commune à tous tes billets, ou propre à ce billet.", "No. Todo funciona sin ellas salvo la pantalla de la entrada: tu lista, filtros, estadísticas, amigos, recordatorios y la lista pública. Si subes una, puedes cifrarla con una frase secreta para todas tus entradas o solo para esa.", "No. Tutto funziona senza, tranne la schermata del biglietto: la tua lista, i filtri, le statistiche, gli amici, i promemoria e l’elenco pubblico. Se ne carichi uno, puoi crittografarlo con una frase segreta per tutti i biglietti o solo per quello.", "Nein. Alles außer dem Ticket-Bildschirm funktioniert ohne: deine Liste, Filter, Statistiken, Freunde, Erinnerungen und die öffentliche Liste. Lädst du eines hoch, kannst du es mit einer Passphrase für alle Tickets oder nur für dieses verschlüsseln."),
'm13': ("Works council refund", "Remboursement CE", "Reembolso del comité de empresa", "Rimborso CRAL", "Erstattung Betriebsrat"), 'm13p': ("Pick a period: your tickets for the concerts you attended come out as one PDF with a summary page, ready to send. Missing prices are read from the tickets.", "Choisis une période : les billets des concerts vus sortent en un seul PDF avec une page récapitulative, prêt à envoyer. Les prix manquants sont lus sur les billets.", "Elige un periodo: las entradas de los conciertos asistidos salen en un solo PDF con una página de resumen, listo para enviar. Los precios que faltan se leen en las entradas.", "Scegli un periodo: i biglietti dei concerti visti escono in un unico PDF con una pagina di riepilogo, pronto da inviare. I prezzi mancanti vengono letti sui biglietti.", "Wähle einen Zeitraum: Die Tickets der besuchten Konzerte kommen als ein PDF mit Übersichtsseite heraus, bereit zum Versenden. Fehlende Preise werden von den Tickets gelesen."),
'm14': ("Paste a link, done", "Colle un lien, c’est rempli", "Pega un enlace y listo", "Incolla un link, fatto", "Link einfügen, fertig"), 'm14p': ("Found the show on a venue or festival site? Paste the page address: artist, date, venue and city fill in by themselves.", "Tu as trouvé le concert sur le site d’une salle ou d’un festival ? Colle l’adresse de la page : artiste, date, salle et ville se remplissent tout seuls.", "¿Has encontrado el concierto en la web de una sala o un festival? Pega la dirección de la página: artista, fecha, sala y ciudad se rellenan solos.", "Hai trovato il concerto sul sito di un locale o di un festival? Incolla l’indirizzo della pagina: artista, data, locale e città si compilano da soli.", "Konzert auf der Seite einer Halle oder eines Festivals gefunden? Füge die Adresse ein: Künstler, Datum, Halle und Stadt füllen sich von selbst."),
'm15': ("Tell the night", "Raconte ta soirée", "Cuenta tu noche", "Racconta la serata", "Erzähl vom Abend"), 'm15p': ("Back from a show? Write a few words, add photos and short videos: your friends get a notification and see your story in the app.", "De retour d’un concert ? Écris quelques mots, ajoute photos et courtes vidéos : tes amis reçoivent une notification et voient ton récit dans l’appli.", "¿Vuelves de un concierto? Escribe unas palabras, añade fotos y vídeos cortos: tus amigos reciben un aviso y ven tu relato en la app.", "Di ritorno da un concerto? Scrivi qualche parola, aggiungi foto e brevi video: i tuoi amici ricevono una notifica e vedono il tuo racconto nell’app.", "Zurück von einem Konzert? Schreib ein paar Worte, füge Fotos und kurze Videos hinzu: Deine Freunde werden benachrichtigt und sehen deinen Bericht in der App."),
'm16': ("Try it, no account needed", "Essaie sans compte", "Pruébala sin cuenta", "Provala senza account", "Ohne Konto ausprobieren"), 'm16p': ("The app opens straight on the concerts shared by its members. Create an account from the menu whenever you want to keep your own.", "L’appli s’ouvre directement sur les concerts partagés par ses membres. Crée un compte depuis le menu quand tu veux tenir les tiens.", "La app se abre directamente en los conciertos compartidos por sus miembros. Crea una cuenta desde el menú cuando quieras llevar los tuyos.", "L’app si apre direttamente sui concerti condivisi dai suoi membri. Crea un account dal menu quando vuoi tenere i tuoi.", "Die App öffnet direkt die Konzerte, die ihre Mitglieder teilen. Lege im Menü ein Konto an, wenn du deine eigenen verwalten willst."),
'm17': ("The whole night at once", "Toute la soirée d’un coup", "Toda la noche de una vez", "Tutta la serata in un colpo", "Der ganze Abend auf einmal"), 'm17p': ("Headliner and opening acts in a single entry, dates in one tap, the city found from the venue: adding a concert takes a few seconds.", "Tête d’affiche et premières parties en une seule saisie, la date en un appui, la ville retrouvée depuis la salle : ajouter un concert prend quelques secondes.", "Cabeza de cartel y teloneros en una sola entrada, la fecha en un toque, la ciudad deducida de la sala: añadir un concierto lleva unos segundos.", "Headliner e gruppi d’apertura in un solo inserimento, la data in un tocco, la città ricavata dal locale: aggiungere un concerto richiede pochi secondi.", "Headliner und Vorbands in einem Eintrag, das Datum mit einem Tipp, die Stadt aus der Halle: Ein Konzert ist in Sekunden erfasst."),
'm18': ("Your genres", "Tes genres", "Tus géneros", "I tuoi generi", "Deine Genres"), 'm18p': ("Every band is linked to its genres and styles from Discogs. Pick the ones you love and the “My genres” filter keeps only those nights.", "Chaque groupe est relié à ses genres et styles Discogs. Choisis ceux que tu aimes et le filtre « Mes genres » ne garde que ces soirées-là.", "Cada grupo está vinculado a sus géneros y estilos de Discogs. Elige los que te gustan y el filtro «Mis géneros» solo deja esas noches.", "Ogni gruppo è collegato ai suoi generi e stili Discogs. Scegli quelli che ami e il filtro «I miei generi» tiene solo quelle serate.", "Jede Band ist mit ihren Genres und Stilen von Discogs verknüpft. Wähle deine Favoriten, und der Filter „Meine Genres“ zeigt nur diese Abende."),
'tk_k': ("Concert ticket", "Place de concert", "Entrada de concierto", "Biglietto concerto", "Konzertkarte"),
'tk_m': ("Membership card", "Abonnement / Adhésion", "Abono / Membresía", "Abbonamento / Tessera", "Abo / Mitgliedschaft"),

'ft': ("Free, and it stays free", "Gratuit, et ça le reste", "Gratis, y se queda gratis", "Gratis, e resta gratis", "Kostenlos, und das bleibt so"),
'fp': ("In The Pit costs nothing. Running it has fixed costs, so if you enjoy it you can chip in on Ko-fi. Accounts are approved by hand: ask for access with your email and you will hear back.", "In The Pit ne coûte rien. Le faire tourner a des coûts fixes : si tu l’apprécies, tu peux participer sur Ko-fi. Les comptes sont validés à la main : demande l’accès avec ton e-mail et tu auras une réponse.", "In The Pit no cuesta nada. Mantenerlo tiene costes fijos, así que si te gusta puedes colaborar en Ko-fi. Las cuentas se aprueban a mano: pide acceso con tu correo y recibirás respuesta.", "In The Pit non costa nulla. Mantenerlo ha costi fissi, quindi se ti piace puoi contribuire su Ko-fi. Gli account sono approvati a mano: chiedi l’accesso con la tua e-mail e riceverai una risposta.", "In The Pit kostet nichts. Der Betrieb hat Fixkosten, wenn es dir gefällt, kannst du auf Ko-fi etwas beitragen. Konten werden von Hand freigegeben: Frage den Zugang mit deiner E-Mail an, du bekommst eine Antwort."),
'bk_t': ("The books, wide open", "Les comptes, à livre ouvert", "Las cuentas, a la vista", "I conti, a carte scoperte", "Die Finanzen, offen gelegt"),
'bk_p': ("In The Pit has no ads and sells no data. Running it still costs money every month. Here is what it costs and what your donations bring in, updated live.", "In The Pit n’a pas de publicité et ne vend aucune donnée. Le faire tourner coûte pourtant de l’argent chaque mois. Voici ce que ça coûte et ce que vos dons rapportent, à jour en direct.", "In The Pit no tiene publicidad y no vende ningún dato. Aun así, mantenerlo cuesta dinero cada mes. Esto es lo que cuesta y lo que aportan vuestras donaciones, actualizado en directo.", "In The Pit non ha pubblicità e non vende alcun dato. Farlo funzionare costa comunque ogni mese. Ecco quanto costa e quanto portano le vostre donazioni, aggiornato in diretta.", "In The Pit hat keine Werbung und verkauft keine Daten. Der Betrieb kostet trotzdem jeden Monat Geld. Hier siehst du, was er kostet und was eure Spenden einbringen, live aktualisiert."),
'bk_cov': ("of monthly costs covered by donations", "des frais mensuels couverts par les dons", "de los gastos mensuales cubiertos por donaciones", "delle spese mensili coperte dalle donazioni", "der monatlichen Kosten durch Spenden gedeckt"),
'bk_fm': ("Costs per month", "Frais par mois", "Gastos al mes", "Spese al mese", "Kosten pro Monat"),
'bk_dm': ("Donations per month", "Dons par mois", "Donaciones al mes", "Donazioni al mese", "Spenden pro Monat"),
'bk_sol': ("Balance since the start", "Solde depuis le début", "Saldo desde el inicio", "Saldo dall’inizio", "Saldo seit Beginn"),
'bk_12': ("The last 12 months", "Les 12 derniers mois", "Los últimos 12 meses", "Gli ultimi 12 mesi", "Die letzten 12 Monate"),
'bk_f': ("Costs", "Frais", "Gastos", "Spese", "Kosten"),
'bk_d': ("Donations", "Dons", "Donaciones", "Donazioni", "Spenden"),
'bk_wt': ("What if donations aren’t enough?", "Et si les dons ne suffisent pas ?", "¿Y si las donaciones no bastan?", "E se le donazioni non bastano?", "Und wenn die Spenden nicht reichen?"),
'bk_wp': ("In The Pit will stay free as long as donations cover its costs. If they don’t over time, the app will have to go freemium: the essentials would stay free, and some advanced features would become paid. Every donation pushes that moment back.", "In The Pit restera gratuit tant que les dons couvrent ses frais. Si ce n’est pas le cas dans la durée, l’app devra passer en freemium : l’essentiel resterait gratuit, et certaines fonctions avancées deviendraient payantes. Chaque don repousse ce moment.", "In The Pit seguirá siendo gratuita mientras las donaciones cubran sus gastos. Si no es así con el tiempo, la app tendrá que pasar a freemium: lo esencial seguiría siendo gratuito y algunas funciones avanzadas pasarían a ser de pago. Cada donación aleja ese momento.", "In The Pit resterà gratuita finché le donazioni coprono le spese. Se a lungo andare non sarà così, l’app dovrà passare al freemium: l’essenziale resterebbe gratuito e alcune funzioni avanzate diventerebbero a pagamento. Ogni donazione allontana quel momento.", "In The Pit bleibt kostenlos, solange Spenden die Kosten decken. Wenn das auf Dauer nicht der Fall ist, muss die App auf Freemium umstellen: Das Wesentliche bliebe kostenlos, einige erweiterte Funktionen würden kostenpflichtig. Jede Spende schiebt diesen Moment hinaus."),
'bk_time': ("The time spent building and running the app isn’t counted: it’s given for free.", "Le temps passé à créer et à faire vivre l’app n’est pas compté : il est offert.", "El tiempo dedicado a crear y mantener la app no se cuenta: es un regalo.", "Il tempo speso per creare e far vivere l’app non è contato: è offerto.", "Die Zeit für Entwicklung und Betrieb der App ist nicht eingerechnet: Sie ist geschenkt."),
'bk_load': ("Loading the figures…", "Chargement des chiffres…", "Cargando las cifras…", "Caricamento dei numeri…", "Zahlen werden geladen …"),
'bk_err': ("The figures can’t be loaded right now. They are also in the app, under Finances in the menu.", "Les chiffres ne peuvent pas être chargés pour l’instant. Ils sont aussi dans l’app, menu Compta.", "Las cifras no se pueden cargar ahora. También están en la app, en el menú Cuentas.", "Al momento non è possibile caricare i numeri. Sono anche nell’app, menu Conti.", "Die Zahlen können gerade nicht geladen werden. Du findest sie auch in der App im Menü unter Finanzen."),
'bk_empty': ("The first figures will be published here very soon.", "Les premiers chiffres seront publiés ici très bientôt.", "Las primeras cifras se publicarán aquí muy pronto.", "I primi numeri saranno pubblicati qui a breve.", "Die ersten Zahlen erscheinen hier in Kürze."),
'm20': ("Venue agendas, read daily", "Les agendas des salles, lus chaque jour", "Las agendas de las salas, leídas cada día", "Le agende dei locali, lette ogni giorno", "Programme der Locations, täglich gelesen"), 'm20p': ("Every day, In The Pit reads the agendas of the venues its users go to and adds the missing concerts to the public list, with support acts, base price and sold-out shows. You get a notification when a new concert matches your tastes.", "Chaque jour, In The Pit lit l’agenda des salles fréquentées par ses utilisateurs et ajoute les concerts manquants à la liste publique, avec premières parties, prix de base et concerts complets. Une notification vous prévient quand un nouveau concert correspond à vos goûts.", "Cada día, In The Pit lee la agenda de las salas a las que van sus usuarios y añade los conciertos que faltan a la lista pública, con teloneros, precio base y conciertos agotados. Una notificación te avisa cuando un concierto nuevo coincide con tus gustos.", "Ogni giorno In The Pit legge l’agenda dei locali frequentati dai suoi utenti e aggiunge i concerti mancanti all’elenco pubblico, con gruppi di apertura, prezzo base e concerti sold out. Una notifica ti avvisa quando un nuovo concerto è in linea con i tuoi gusti.", "In The Pit liest jeden Tag die Programme der Locations, die seine Nutzer besuchen, und ergänzt fehlende Konzerte in der öffentlichen Liste, mit Vorbands, Grundpreis und ausverkauften Konzerten. Eine Benachrichtigung meldet dir neue Konzerte, die zu deinem Geschmack passen."),
'm19': ("Open books", "Comptes publics", "Cuentas públicas", "Conti pubblici", "Offene Finanzen"), 'm19p': ("The app’s costs and the donations it receives are published in the app and on this site, so everyone can see whether it pays its way.", "Les frais de l’app et les dons reçus sont publiés dans l’app et sur ce site : chacun voit si elle tient la route.", "Los gastos de la app y las donaciones recibidas se publican en la app y en este sitio: todos pueden ver si se sostiene.", "Le spese dell’app e le donazioni ricevute sono pubblicate nell’app e su questo sito: tutti possono vedere se si regge.", "Die Kosten der App und die erhaltenen Spenden werden in der App und auf dieser Website veröffentlicht, damit alle sehen, ob sie sich trägt."),
'kofi': ("Chip in on Ko-fi", "Participer sur Ko-fi", "Colaborar en Ko-fi", "Contribuisci su Ko-fi", "Auf Ko-fi unterstützen"),
'req': ("Request access", "Demander l’accès", "Pedir acceso", "Richiedi l’accesso", "Zugang anfragen"),

'qt': ("Questions", "Questions", "Preguntas", "Domande", "Fragen"),
'q1': ("Do I need to install anything?", "Faut-il installer quelque chose ?", "¿Hay que instalar algo?", "Serve installare qualcosa?", "Muss ich etwas installieren?"),
'a1': ("No. Open it in your browser. If you like, add it to your home screen from the browser menu and it behaves like an app.", "Non. Ouvre-la dans ton navigateur. Si tu veux, ajoute-la à ton écran d’accueil depuis le menu du navigateur et elle se comporte comme une app.", "No. Ábrela en tu navegador. Si quieres, añádela a tu pantalla de inicio desde el menú del navegador y se comporta como una app.", "No. Aprila nel browser. Se vuoi, aggiungila alla schermata iniziale dal menu del browser e si comporta come un’app.", "Nein. Öffne sie im Browser. Wenn du möchtest, füge sie über das Browsermenü zum Startbildschirm hinzu, dann verhält sie sich wie eine App."),
'q2': ("Who can see my concerts?", "Qui peut voir mes concerts ?", "¿Quién puede ver mis conciertos?", "Chi può vedere i miei concerti?", "Wer kann meine Konzerte sehen?"),
'a2': ("You, and the friends you share with. You can also choose to appear, anonymously, in the public guest list. It is off by default and shows no name, notes, prices or tickets.", "Toi, et les amis avec qui tu partages. Tu peux aussi choisir d’apparaître, anonymement, dans la liste publique des invités. C’est désactivé par défaut, sans nom, notes, prix ni billets.", "Tú y los amigos con quienes compartes. También puedes aparecer, de forma anónima, en la lista pública de invitados. Está desactivado por defecto y no muestra nombre, notas, precios ni entradas.", "Tu e gli amici con cui condividi. Puoi anche scegliere di comparire, in forma anonima, nell’elenco pubblico degli ospiti. È disattivato di default e non mostra nome, note, prezzi né biglietti.", "Du und die Freunde, mit denen du teilst. Du kannst auch anonym in der öffentlichen Gästeliste erscheinen. Das ist standardmäßig aus und zeigt weder Namen noch Notizen, Preise oder Tickets."),
'q3': ("What does it do with my tickets?", "Que fait-elle de mes billets ?", "¿Qué hace con mis entradas?", "Cosa fa con i miei biglietti?", "Was passiert mit meinen Tickets?"),
'a3': ("An AI reads PDF tickets to fill in artist, date, venue and price. It is told to ignore your name, address and barcodes. The QR code or barcode itself is read on your phone, not by the AI. It also reads the concert pages whose link you paste. Paper tickets are kept as photos, and you decide what to add.", "Une IA lit les billets PDF pour remplir artiste, date, salle et prix. Elle a pour consigne d’ignorer ton nom, ton adresse et les codes-barres. Le QR code ou code-barres lui-même est lu sur ton téléphone, pas par l’IA. Elle lit aussi les pages de concert dont tu colles le lien. Les billets papier sont gardés en photo, et tu choisis ce que tu ajoutes.", "Una IA lee las entradas en PDF para rellenar artista, fecha, sala y precio. Tiene la consigna de ignorar tu nombre, dirección y códigos de barras. El código QR o de barras en sí se lee en tu teléfono, no la IA. También lee las páginas de conciertos cuyo enlace pegas. Las entradas de papel se guardan como fotos y tú decides qué añadir.", "Un’IA legge i biglietti PDF per compilare artista, data, locale e prezzo. Ha l’istruzione di ignorare nome, indirizzo e codici a barre. Il codice QR o a barre vero e proprio viene letto sul tuo telefono, non dall’IA. Legge anche le pagine dei concerti di cui incolli il link. I biglietti cartacei sono salvati come foto e sei tu a decidere cosa aggiungere.", "Eine KI liest PDF-Tickets, um Künstler, Datum, Halle und Preis auszufüllen. Sie soll deinen Namen, deine Adresse und Barcodes ignorieren. Der QR-Code oder Barcode selbst wird auf deinem Handy gelesen, nicht von der KI. Sie liest auch die Konzertseiten, deren Link du einfügst. Papiertickets werden als Fotos gespeichert, und du entscheidest, was du hinzufügst."),

'cta_t': ("See you in the pit.", "On se retrouve dans la fosse.", "Nos vemos en el foso.", "Ci vediamo sotto il palco.", "Wir sehen uns im Graben."),
'foot': ("Made for people who still keep their ticket stubs.", "Fait pour ceux qui gardent encore leurs billets.", "Hecho para quienes aún guardan sus entradas.", "Fatto per chi conserva ancora i biglietti.", "Für alle, die ihre Tickets noch aufheben."),
'skip': ("Skip to content", "Aller au contenu", "Ir al contenido", "Vai al contenuto", "Zum Inhalt"),
'alt_list': ("The In The Pit concert list", "La liste de concerts d’In The Pit", "La lista de conciertos de In The Pit", "L’elenco dei concerti di In The Pit", "Die Konzertliste von In The Pit"),
'alt_filters': ("The side menu with the filters", "Le menu latéral et ses filtres", "El menú lateral con los filtros", "Il menu laterale con i filtri", "Das Seitenmenü mit den Filtern"),
'alt_stats': ("The statistics screen", "L’écran des statistiques", "La pantalla de estadísticas", "La schermata delle statistiche", "Der Statistikbildschirm"),
}
FAQ = [('q4', 'a4'), ('q1', 'a1'), ('q2', 'a2'), ('q3', 'a3')]

ICON = {
 'lk': '<rect x="4.5" y="10.5" width="15" height="10" rx="2"/><path d="M8 10.5V7.5a4 4 0 0 1 8 0v3"/><path d="M12 14.5v2.5"/>',
 'ok': '<path d="M4 12.5l5 5L20 6.5"/>',
 'ls': '<path d="M8 6h12M8 12h12M8 18h12"/><circle cx="4" cy="6" r="1"/><circle cx="4" cy="12" r="1"/><circle cx="4" cy="18" r="1"/>',
 'tk': '<path d="M3 8a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2v2a2 2 0 0 0 0 4v2a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-2a2 2 0 0 0 0-4z"/><path d="M14 6v12" stroke-dasharray="2 2.5"/>',
 'fl': '<path d="M3 5h18l-7 8v6l-4 2v-8z"/>',
 'us': '<circle cx="9" cy="8" r="3.2"/><path d="M3 20c0-3.3 2.7-5.5 6-5.5s6 2.2 6 5.5"/><circle cx="17" cy="9" r="2.4"/><path d="M17 14.3c2.4 0 4 1.7 4 4.2"/>',
 'st': '<path d="M6 20V11M12 20V4M18 20v-6"/>',
 'bl': '<path d="M6 17V11a6 6 0 0 1 12 0v6l1.5 2h-15z"/><path d="M10 21h4"/>',
 'ag': '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/><path d="M9 15l2 2 4-4"/>',
}
def icon(k): return f'<svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICON[k]}</svg>'

def qr_svg(n=25, seed=7):
    r = random.Random(seed); cells = []
    def finder(x, y):
        for i in range(7):
            for j in range(7):
                on = i in (0, 6) or j in (0, 6) or (2 <= i <= 4 and 2 <= j <= 4)
                if on: cells.append((x + i, y + j))
    finder(0, 0); finder(n - 7, 0); finder(0, n - 7)
    for i in range(n):
        for j in range(n):
            if (i < 8 and j < 8) or (i >= n - 8 and j < 8) or (i < 8 and j >= n - 8): continue
            if r.random() < .48: cells.append((i, j))
    d = ''.join(f'M{x} {y}h1v1h-1z' for x, y in cells)
    return f'<svg viewBox="-1 -1 {n+2} {n+2}" role="img" aria-hidden="true"><rect x="-1" y="-1" width="{n+2}" height="{n+2}" fill="#fff"/><path d="{d}" fill="#000"/></svg>'

CSS = r"""
:root{--ink:#0f0f10;--paper:#f4f4f2;--ticket:#f6c915;--red:#e03a2c;--grn:#22c55e;--org:#f59e0b;--vio:#8b5cf6;--pink:#e11d74;--blu:#2f6fed;--r:18px;
--f:'Archivo',system-ui,-apple-system,'Segoe UI',Roboto,sans-serif}
*{box-sizing:border-box}html{scroll-behavior:smooth}
@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}}
body{margin:0;background:var(--ink);color:var(--paper);font:400 18px/1.6 var(--f);font-stretch:100%;-webkit-text-size-adjust:100%}
img{max-width:100%;height:auto;display:block}
a{color:inherit}
:focus-visible{outline:3px solid var(--org);outline-offset:3px;border-radius:6px}
.skip{position:absolute;left:-999px;top:8px;background:var(--ticket);color:var(--ink);padding:8px 14px;border-radius:8px;z-index:9}.skip:focus{left:8px}
.wrap{width:min(1120px,100% - 40px);margin-inline:auto}
h1,h2,h3{font-stretch:68%;font-weight:900;line-height:.98;margin:0;letter-spacing:.005em}
h1{font-size:clamp(3.4rem,10.5vw,7.6rem)}
h2{font-size:clamp(2.5rem,6.2vw,4.4rem)}
h3{font-size:1.5rem;font-stretch:80%;line-height:1.1}
p{margin:0}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:10px;min-height:52px;padding:0 26px;border-radius:999px;background:var(--btn-bg,var(--ticket));color:var(--btn-fg,var(--ink));font:700 17px var(--f);text-decoration:none;border:2px solid var(--btn-bg,var(--ticket))}
.btn:hover{filter:brightness(1.08)}
.btn.ghost{background:transparent;color:inherit;border-color:currentColor}
.btns{display:flex;flex-wrap:wrap;gap:12px;margin-top:30px}
.brand{width:min(1120px,100% - 40px);margin:18px auto 0}
.brand img{width:100%;height:auto;border-radius:18px}
header.top{position:sticky;top:0;z-index:5;background:rgba(15,15,16,.94);backdrop-filter:blur(8px);border-bottom:1px solid #2a2a2d;margin-top:14px}
header.top .wrap{display:flex;align-items:center;min-height:60px}
header nav{display:flex;gap:20px;align-items:center;width:100%}
header nav .lang{flex:1;justify-content:space-around;margin-left:12px}
header nav a{text-decoration:none;font-weight:600;font-size:16px}header nav a:hover{text-decoration:underline}
.lang{display:flex;gap:2px;font-size:15px}.lang a{padding:6px 8px;border-radius:6px;text-decoration:none;color:#b9b9bd;font-weight:600}.lang a[aria-current]{color:var(--ink);background:var(--paper)}
header .btn{min-height:40px;padding:0 18px;font-size:15px}
@media(max-width:560px){header nav .l{display:none}header nav .lang{margin-left:0}}

.hero{padding:clamp(40px,7vw,92px) 0 clamp(70px,9vw,120px);overflow:hidden}
.hero .wrap{display:grid;grid-template-columns:1.15fr .85fr;gap:40px;align-items:center}
.hero p.lead{font-size:clamp(1.1rem,2vw,1.35rem);max-width:34ch;margin-top:24px;color:#d6d6d8}
.hero h1{max-width:9ch}
.phones{position:relative;min-height:560px}
.phone{position:absolute;width:min(270px,62%);border:7px solid #000;border-radius:38px;overflow:hidden;background:#000;box-shadow:0 0 0 2px #333,0 30px 60px rgba(0,0,0,.55)}
.phone img{width:100%}
.phones .p1{right:0;top:0;transform:rotate(3deg)}
.phones .p2{left:0;top:70px;transform:rotate(-4deg);z-index:-1;opacity:.95}
@media(max-width:860px){.hero .wrap{grid-template-columns:1fr}.hero h1{max-width:none}.phones{min-height:520px;max-width:420px;margin:10px auto 0;width:100%}}

.band{position:relative;padding:clamp(70px,9vw,120px) 0;background:var(--bg);color:var(--fg)}
.band::before{content:"";position:absolute;left:0;right:0;top:-12px;height:12px;background:radial-gradient(circle at 12px 12px,var(--bg) 11px,transparent 12px) 0 0/24px 12px repeat-x}
.k{--bg:var(--ink);--fg:var(--paper);--btn-bg:var(--ticket);--btn-fg:var(--ink)}
.y{--bg:var(--ticket);--fg:var(--ink);--btn-bg:var(--ink);--btn-fg:var(--ticket)}
.feat .wrap{display:grid;grid-template-columns:1fr 1fr;gap:clamp(30px,6vw,90px);align-items:center}
.feat.rev .txt{order:2}
.badge{width:64px;height:64px;border-radius:50%;display:grid;place-items:center;color:#fff;margin-bottom:22px;box-shadow:0 0 0 3px var(--bg),0 0 0 5px currentColor}
.badge svg{width:30px;height:30px}
.txt p.big{font-size:clamp(1.1rem,1.9vw,1.28rem);margin-top:20px;max-width:46ch}
ul.pts{list-style:none;padding:0;margin:26px 0 0;display:grid;gap:14px;max-width:46ch}
ul.pts li{padding-left:30px;position:relative;font-size:1rem}
ul.pts li::before{content:"";position:absolute;left:0;top:.42em;width:14px;height:14px;border-radius:50%;border:3px solid currentColor}
.vis{display:grid;place-items:center}
.vis .phone{position:relative;width:min(300px,80%);transform:rotate(-2deg)}
.feat.rev .vis .phone{transform:rotate(2deg)}
@media(max-width:860px){.feat .wrap{grid-template-columns:1fr}.feat.rev .txt{order:0}}

/* faux écrans */
.tkscr{background:#000;color:#fff;padding:22px 20px 26px;text-align:center;font-stretch:100%}
.tkscr img{width:70%;margin:0 auto 18px}
.tkscr b{display:block;font-size:1.25rem;font-stretch:80%;font-weight:800}
.tkscr small{display:block;color:#bbb;font-size:.82rem;margin:2px 0 16px}
.tkscr .qr{background:#fff;border-radius:10px;padding:8px;width:78%;margin:0 auto}
.tkscr{position:relative;padding-top:64px}
.tkscr .tb{position:absolute;top:12px;width:38px;height:38px;border:2px solid #fff;border-radius:11px;display:grid;place-items:center}
.tkscr .tb svg{width:20px;height:20px;fill:none;stroke:#fff;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}
.tkscr .tb.l{left:12px}.tkscr .tb.l2{left:58px}.tkscr .tb.r{right:12px}
.tkscr .kind{display:inline-block;border:2px solid var(--org);color:var(--org);border-radius:999px;padding:2px 14px;font-weight:700;font-size:.85rem;margin:0 0 8px}
.tkscr small{line-height:1.35}
.tkscr .val{display:block;font:normal 8px/1.2 ui-monospace,Menlo,Consolas,monospace;color:#888;margin-top:2px;word-break:break-all}
.tkscr .pdf{display:inline-block;margin-top:16px;border:2px solid #666;border-radius:8px;padding:4px 10px;font-size:.78rem;color:#ddd}
.tile{background:#222224;border:2px solid var(--org);border-radius:16px;padding:14px 16px 28px;position:relative;color:#f2f2f3;font-size:.95rem;text-align:left}
.tile small{display:block;color:#a5a5aa;font-size:.8rem}.tile .pp{display:block;font-size:.72rem;color:#c9c9ce;margin-top:2px}.tile .ags{display:flex;gap:8px;margin-top:8px}.tile .agx,.tile .agp{padding:1px 9px;border-radius:999px;font-size:.78rem;font-weight:700}.tile .agx{background:#dc2626;color:#fff}.tile .agp{background:rgba(255,255,255,.12)}
.tile b{display:block;font-size:1.2rem;font-weight:600;margin-top:4px}
.tile em{position:absolute;left:12px;bottom:6px;font-style:normal;font-size:.72rem;color:#a5a5aa}
.stack{display:grid;gap:14px;width:min(380px,100%);margin-inline:auto}
.bubble{background:#fff;color:var(--ink);border-radius:16px;padding:16px 18px;font-size:.98rem;position:relative}
.bubble small{display:block;margin-top:8px;color:#5b5b60;font-size:.78rem}
.notif{background:#fff;color:var(--ink);border-radius:18px;padding:14px 16px;display:flex;gap:12px;align-items:center;box-shadow:0 10px 24px rgba(0,0,0,.18);font-size:.95rem;line-height:1.35}
.notif img{width:38px;height:38px;border-radius:10px;flex:none}
.notif b{display:block;font-size:.8rem;color:#5b5b60;font-weight:600}
.notif:nth-child(2){margin-left:22px}.notif:nth-child(3){margin-left:6px}

.small .wrap>h2{margin-bottom:40px}
.grid{display:grid;grid-template-columns:repeat(4,1fr);gap:0;border-top:2px solid #333}
.grid div{padding:22px 22px 26px 0;border-bottom:2px solid #333}
.grid h3{margin-bottom:8px}
.grid p{font-size:.98rem;color:#cfcfd2}
@media(max-width:900px){.grid{grid-template-columns:repeat(2,1fr)}}
@media(max-width:520px){.grid{grid-template-columns:1fr}}

.claims{--bg:var(--red);--fg:#fff}
.claims .wrap{display:grid;grid-template-columns:1fr 1fr;gap:clamp(36px,6vw,90px);align-items:start}
.claims h2{font-size:clamp(2.3rem,5.4vw,4rem);line-height:.98;margin:18px 0 18px}
.claims .lead2{font-size:1.2rem;line-height:1.5;max-width:40ch;margin:0 0 20px}
.claims ul{list-style:none;margin:0;padding:0;display:grid;gap:12px}
.claims li{display:flex;gap:12px;align-items:flex-start;font-size:1.08rem;line-height:1.4}
.claims li svg{flex:none;width:22px;height:22px;margin-top:1px}
.claims .opt{display:grid;gap:12px;margin:0 0 18px}
.claims .opt>div{background:rgba(0,0,0,.22);border-radius:14px;padding:16px 18px}
.claims .opt b{display:block;font-size:1.15rem;margin-bottom:4px}
.claims .fine{font-size:.98rem;opacity:.92;display:flex;gap:10px;align-items:center}
.claims .ic{display:inline-flex;width:54px;height:54px;border-radius:14px;background:#fff;color:var(--red);align-items:center;justify-content:center}
@media(max-width:860px){.claims .wrap{grid-template-columns:1fr}}
.books .wrap{display:grid;grid-template-columns:1fr 1fr;gap:clamp(36px,6vw,90px);align-items:start}
.books h2{margin-bottom:18px}.books .lead2{font-size:1.2rem;line-height:1.5;max-width:42ch;margin:0 0 26px}
.books .warn{background:var(--ticket);color:var(--ink);border-radius:var(--r);padding:20px 22px;margin:0 0 18px}.books .warn b{display:block;font:900 1.5rem/1.1 var(--f);font-stretch:80%;margin-bottom:8px}.books .warn p{font-size:1.02rem;line-height:1.5}
.books .fine{font-size:.98rem;opacity:.75;margin:0 0 24px}
.live{--c:var(--grn)}.live.mid{--c:var(--org)}.live.low{--c:var(--red)}
.live .pc{font:900 clamp(6rem,17vw,11rem)/.82 var(--f);font-stretch:62%;color:var(--c);letter-spacing:-.01em}
.live .cov{font-size:1.15rem;margin:10px 0 14px}
.live .meter{height:14px;border-radius:7px;background:#2a2a2d;overflow:hidden}.live .meter i{display:block;height:100%;width:0;background:var(--c);border-radius:7px;transition:width 1s ease-out}
@media(prefers-reduced-motion:reduce){.live .meter i{transition:none}}
.live .kp{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin:30px 0 34px}.live .kp div{border-top:3px solid #333;padding-top:10px;min-width:0}
.live .kp b{display:block;font:900 clamp(1.5rem,3vw,2rem)/1 var(--f);font-stretch:75%;white-space:nowrap}.live .kp b.neg{color:var(--red)}.live .kp b.pos{color:var(--grn)}.live .kp span{display:block;font-size:.92rem;opacity:.75;margin-top:6px;line-height:1.3}
.live h3{font-size:1.25rem;margin:0 0 8px}.live .lg{display:flex;gap:18px;font-size:.92rem;opacity:.85;margin-bottom:10px}.live .lg span::before{content:"";display:inline-block;width:11px;height:11px;border-radius:3px;margin-right:7px;background:var(--org);vertical-align:-1px}.live .lg .d::before{background:var(--grn)}
.live .bars{display:flex;gap:6px;align-items:flex-end;height:150px}.live .bars>div{flex:1;display:flex;flex-direction:column;align-items:center;height:100%;min-width:0}.live .bars .b{flex:1;width:100%;display:flex;gap:2px;align-items:flex-end;justify-content:center}.live .bars i{flex:1;max-width:12px;min-height:2px;border-radius:3px 3px 0 0;background:var(--org)}.live .bars i.d{background:var(--grn)}.live .bars small{font-size:.8rem;opacity:.7;margin-top:6px}
.live .msg{font-size:1.1rem;opacity:.8}
@media(max-width:860px){.books .wrap{grid-template-columns:1fr}}
.free .wrap{display:grid;grid-template-columns:1.1fr .9fr;gap:40px;align-items:center}
.free p{font-size:1.2rem;margin-top:18px;max-width:48ch}
@media(max-width:860px){.free .wrap{grid-template-columns:1fr}}
.faq h2{margin-bottom:34px}
details{border-top:2px solid #333;padding:0}details:last-of-type{border-bottom:2px solid #333}
summary{cursor:pointer;list-style:none;padding:22px 0;font:800 clamp(1.3rem,2.6vw,1.7rem)/1.15 var(--f);font-stretch:80%;display:flex;justify-content:space-between;gap:20px}
summary::-webkit-details-marker{display:none}
summary::after{content:"+";font-size:1.8rem;line-height:1;color:var(--ticket)}details[open] summary::after{content:"–"}
details p{padding:0 0 24px;max-width:62ch;color:#d4d4d6}
.last{text-align:center}.last h2{max-width:11ch;margin-inline:auto;font-size:clamp(3rem,9vw,6.4rem)}
.last .btns{justify-content:center}
footer{background:var(--ink);padding:36px 0 50px;color:#a5a5aa;font-size:15px}
footer .wrap{display:flex;flex-wrap:wrap;gap:16px 30px;align-items:center;justify-content:space-between}
footer img{width:90px}
footer a{color:#d6d6d8}
"""

LAT = "U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD"
EXT = "U+0100-02BA,U+02BD-02C5,U+02C7-02CC,U+02CE-02D7,U+02DD-02FF,U+0304,U+0308,U+0329,U+1D00-1DBF,U+1E00-1E9F,U+1EF2-1EFF,U+2020,U+20A0-20AB,U+20AD-20C0,U+2113,U+2C60-2C7F,U+A720-A7FF"
# Police hébergée sur le site lui-même : aucun appel à Google Fonts (RGPD).
def fonts(base):
    return ''.join("@font-face{font-family:'Archivo';font-style:normal;font-weight:100 900;font-stretch:62%% 125%%;font-display:swap;src:url(%sfonts/%s) format('woff2');unicode-range:%s}" % (base, f, r) for f, r in (('archivo-ext.woff2', EXT), ('archivo.woff2', LAT)))

def t(k, i): return T[k][i]
def e(s): return html.escape(s, quote=True)

def page(i):
    lg = L[i]; pre = '' if lg == 'en' else f'../'  # préfixe relatif vers la racine
    base = '' if lg == 'en' else '../'
    def a(k): return e(t(k, i))
    def lhref(l):
        up = '' if lg == 'en' else '../'
        return (up or './') if l == 'en' else up + l + '/'
    langs = ''.join(f'<a href="{lhref(l)}" hreflang="{l}" lang="{l}"{" aria-current=\"page\"" if l==lg else ""}>{l.upper()}</a>' for l in L)
    alts = ''.join(f'<link rel="alternate" hreflang="{l}" href="{DOMAIN}/{"" if l=="en" else l+"/"}">' for l in L) + f'<link rel="alternate" hreflang="x-default" href="{DOMAIN}/">'
    canon = f'{DOMAIN}/{"" if lg=="en" else lg+"/"}'
    def feat(cls, rev, badge, bcol, ico, title, ptxt, pts, vis):
        li = ''.join(f'<li>{e(p)}</li>' for p in pts)
        return f'''<section class="band feat {cls}{' rev' if rev else ''}" id="{ico}"><div class="wrap"><div class="txt"><div class="badge" style="background:{bcol}">{icon(ico)}</div><h2>{e(title)}</h2><p class="big">{e(ptxt)}</p>{('<ul class="pts">'+li+'</ul>') if li else ''}</div><div class="vis">{vis}</div></div></section>'''
    ph = lambda src, alt: f'<div class="phone"><img src="{base}img/{src}" alt="{e(alt)}" width="780" height="1560" loading="lazy"></div>'
    tkvis = f'<div class="phone"><div class="tkscr"><span class="tb l" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M7 3h7l5 5v13H7z"/><path d="M9.5 13h6M9.5 17h6"/></svg></span><span class="tb l2" aria-hidden="true"><svg viewBox="0 0 24 24"><rect x="2.5" y="5" width="19" height="14" rx="2"/><circle cx="8.5" cy="11" r="2"/><path d="M5.5 16c.6-1.5 1.7-2.2 3-2.2s2.4.7 3 2.2M14.5 10h4M14.5 13.5h4"/></svg></span><span class="tb r" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M6 6l12 12M18 6L6 18"/></svg></span><img src="{base}img/logo.webp" alt="" width="900" height="300"><span class="kind">{a("tk_k")}</span><b>Velvet Static</b><small>Le Trianon, Paris<br>2026-11-28</small><div class="qr">{qr_svg()}</div><i class="val">VS-2611-A7K3-9X41-0058</i></div></div>'
    frvis = f'<div class="stack"><div class="tile"><small>2027-02-03 · Razzmatazz, Barcelona</small><b>Los Cometas</b><em>Alice</em></div><div class="tile"><small>2027-01-17 · L’Olympia, Paris</small><b>{e(t("tile_a",i))}</b><em>Bob</em></div><div class="bubble">{e(t("note",i))}<small>{e(t("note_c",i))}</small></div></div>'
    ntvis = f'<div class="stack"><div class="notif"><img src="{base}img/icon-192.png" alt="" width="38" height="38"><div><b>In The Pit</b>{e(t("n1",i))}</div></div><div class="notif"><img src="{base}img/icon-192.png" alt="" width="38" height="38"><div><b>In The Pit</b>{e(t("n2",i))}</div></div><div class="notif"><img src="{base}img/icon-192.png" alt="" width="38" height="38"><div><b>In The Pit</b>{e(t("n3",i))}</div></div></div>'
    agvis = f'<div class="stack"><div class="tile"><small>2027-03-12 · La Belle Électrique, Grenoble</small><b>Marée Noire</b><span class="ags"><span class="agx">{e(t("f6_so",i))}</span><span class="agp">32 €</span></span><em>{e(t("f6_src",i))}</em></div><div class="tile"><small>2027-04-02 · Le Transbordeur, Villeurbanne</small><b>Los Cometas</b><i class="pp">Velvet Static</i><span class="ags"><span class="agp">27 €</span></span><em>{e(t("f6_src",i))}</em></div><div class="notif"><img src="{base}img/icon-192.png" alt="" width="38" height="38"><div><b>In The Pit</b>{e(t("f6_n",i))}</div></div></div>'
    small = ''.join(f'<div><h3>{a(f"m{n}")}</h3><p>{a(f"m{n}p")}</p></div>' for n in range(1, 21) if n != 3)
    faq = ''.join(f'<details><summary>{a(q)}</summary><p>{a(an)}</p></details>' for q, an in FAQ)
    return f'''<!doctype html>
<html lang="{lg}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{a("title")}</title><meta name="description" content="{a("desc")}">
<link rel="canonical" href="{canon}">{alts}
<meta property="og:title" content="{a("title")}"><meta property="og:description" content="{a("desc")}"><meta property="og:type" content="website"><meta property="og:url" content="{canon}"><meta property="og:image" content="{DOMAIN}/img/og.png">
<meta name="twitter:card" content="summary_large_image"><meta name="theme-color" content="#0f0f10">
<link rel="icon" href="{base}img/icon-192.png"><link rel="apple-touch-icon" href="{base}img/apple-touch-icon.png">
<link rel="preload" href="{base}fonts/archivo.woff2" as="font" type="font/woff2" crossorigin>
<style>{fonts(base)}{CSS}</style></head><body>
<a class="skip" href="#main">{a("skip")}</a>
<div class="brand"><a href="{lhref(lg)}" aria-label="In The Pit"><img src="{base}img/logo.webp" alt="In The Pit" width="900" height="300"></a></div>
<header class="top"><div class="wrap"><nav><a class="l" href="#ag">{a("nav_f")}</a><a class="l" href="#faq">{a("nav_q")}</a><div class="lang" aria-label="Language">{langs}</div></nav></div></header>
<main id="main">
<section class="hero k"><div class="wrap"><div><h1>{a("h1")}</h1><p class="lead">{a("hp")}</p><div class="btns"><a class="btn" href="{APP}">{a("open")}</a><a class="btn ghost" href="#ag">{a("see")}</a></div></div>
<div class="phones" aria-hidden="false">{ph(f"s-filters-{lg}.webp",t("alt_filters",i)).replace('class="phone"','class="phone p2"')}{ph(f"s-list-{lg}.webp",t("alt_list",i)).replace('class="phone"','class="phone p1"')}</div></div></section>
{feat("y",False,"","#dc2626","ag",t("f6t",i),t("f6p",i),[t("f6a",i),t("f6b",i),t("f6c",i)],agvis)}
<section class="band claims" id="claims"><div class="wrap">
<div><span class="ic">{icon("ls")}</span><h2>{a("c1t")}</h2><p class="lead2">{a("c1p")}</p><ul>{''.join(f'<li>{icon("ok")}<span>{a(k)}</span></li>' for k in ("c1a","c1b","c1c","c1d"))}</ul></div>
<div><span class="ic">{icon("lk")}</span><h2>{a("c2t")}</h2><p class="lead2">{a("c2p")}</p><div class="opt"><div><b>{a("c2a")}</b>{a("c2ap")}</div><div><b>{a("c2b")}</b>{a("c2bp")}</div></div><p class="fine">{icon("lk")}<span>{a("c2c")}</span></p></div>
</div></section>
{feat("y",False,"","#f59e0b","tk",t("f1t",i),t("f1p",i),[t("f1a",i),t("f1b",i),t("f1c",i)],tkvis)}
{feat("k",True,"","#2f6fed","fl",t("f2t",i),t("f2p",i),[t("f2a",i),t("f2b",i),t("f2c",i),t("f2d",i)],ph(f"s-filters-{lg}.webp",t("alt_filters",i)))}
{feat("y",False,"","#e11d74","us",t("f3t",i),t("f3p",i),[t("f3a",i)],frvis)}
{feat("k",True,"","#8b5cf6","st",t("f4t",i),t("f4p",i),[],ph(f"s-stats-{lg}.webp",t("alt_stats",i)))}
{feat("y",False,"","#22c55e","bl",t("f5t",i),t("f5p",i),[],ntvis)}
<section class="band small k"><div class="wrap"><h2>{a("mt")}</h2><div class="grid">{small}</div></div></section>
<section class="band free y"><div class="wrap"><div><h2>{a("ft")}</h2><p>{a("fp")}</p></div><div class="btns" style="margin:0"><a class="btn" href="{APP}">{a("req")}</a><a class="btn ghost" href="{KOFI}" rel="noopener">{a("kofi")}</a></div></div></section>
<section class="band books k" id="books"><div class="wrap">
<div><h2>{a("bk_t")}</h2><p class="lead2">{a("bk_p")}</p><div class="warn"><b>{a("bk_wt")}</b><p>{a("bk_wp")}</p></div><p class="fine">{a("bk_time")}</p><a class="btn" href="{KOFI}" rel="noopener">{a("kofi")}</a></div>
<div class="live" id="live" data-lg="{lg}"><p class="msg" id="bk_msg">{a("bk_load")}</p><div id="bk_box" hidden><div class="pc" id="bk_pc">—</div><p class="cov">{a("bk_cov")}</p><div class="meter"><i id="bk_m"></i></div>
<div class="kp"><div><b id="bk_fm"></b><span>{a("bk_fm")}</span></div><div><b id="bk_dm"></b><span>{a("bk_dm")}</span></div><div><b id="bk_sol"></b><span>{a("bk_sol")}</span></div></div>
<h3>{a("bk_12")}</h3><div class="lg"><span class="f">{a("bk_f")}</span><span class="d">{a("bk_d")}</span></div><div class="bars" id="bk_bars"></div></div></div>
</div></section>
<script>{BKJS.replace("@ERR@",json.dumps(t("bk_err",i))).replace("@EMPTY@",json.dumps(t("bk_empty",i)))}</script>
<section class="band faq k" id="faq"><div class="wrap"><h2>{a("qt")}</h2>{faq}</div></section>
<section class="band last y"><div class="wrap"><h2>{a("cta_t")}</h2><div class="btns"><a class="btn" href="{APP}">{a("open")}</a></div></div></section>
</main>
<footer><div class="wrap"><img src="{base}img/logo.webp" alt="In The Pit" width="900" height="300"><span><a href="legal/">{a("lg_t")}</a></span><span><a href="{APP}/confidentialite.html?lang={lg}">{a("lg_priv")}</a></span><span><a href="{KOFI}" rel="noopener">Ko-fi</a></span><span>© 2026 Zion Hut Studio</span></div></footer>
</body></html>'''

BKJS = r"""(function(){var el=document.getElementById('live'),lg=el.dataset.lg,LOC={en:'en-GB',fr:'fr-FR',es:'es-ES',it:'it-IT',de:'de-DE'}[lg],msg=document.getElementById('bk_msg');
function cptCalc(rows,now){
  now=now||new Date();const mk=d=>d.getFullYear()*12+d.getMonth(),N=mk(now),pm=s=>{const [y,m]=s.split('-').map(Number);return y*12+m-1};
  const per={},cats={};let frais=0,dons=0,first=N,mens=0;
  for(const r of rows){
    const a=pm(r.debut),z=Math.min(N,r.fin?pm(r.fin):N),v=+r.montant||0,f=r.sens==='frais';if(a>N)continue;first=Math.min(first,a);
    const ms=r.periodicite==='mensuel'?Array.from({length:Math.max(0,z-a+1)},(_,i)=>a+i):r.periodicite==='annuel'?Array.from({length:Math.max(0,Math.floor((z-a)/12)+1)},(_,i)=>a+12*i):[a];
    for(const m of ms){const p=per[m]=per[m]||{f:0,d:0};if(f){p.f+=v;frais+=v}else{p.d+=v;dons+=v}}
    if(f){const on=!r.fin||pm(r.fin)>=N,cs=String(r.categorie||'autre').split(',').filter(Boolean);
      // current monthly cost: recurring lines still running, yearly ones spread over 12 months, one-off costs of the last 12 months spread too
      const mm=on&&r.periodicite==='mensuel'?v:on&&r.periodicite==='annuel'?v/12:r.periodicite==='unique'&&a>N-12?v/12:0;
      mens+=mm;cs.forEach(c=>cats[c]=(cats[c]||0)+mm/cs.length)}
  }
  const nb=Math.max(1,Math.min(12,N-first+1));let d12=0;
  const mois=Array.from({length:12},(_,i)=>{const m=N-11+i,p=per[m]||{f:0,d:0};if(m>N-nb)d12+=p.d;return{y:Math.floor(m/12),m:m%12,f:p.f,d:p.d}});
  const donsMois=d12/nb;
  return{frais,dons,solde:dons-frais,mens,donsMois,couv:mens>0?donsMois/mens:null,mois,cats,vide:!rows.length};
}
var eur=function(v){return new Intl.NumberFormat(LOC,{style:'currency',currency:'EUR',minimumFractionDigits:Math.abs(v)<100&&v%1?2:0,maximumFractionDigits:Math.abs(v)<100?2:0}).format(v)};
fetch('https://avclfmjhlmjtdcrlankq.supabase.co/rest/v1/compta?select=sens,montant,periodicite,debut,fin,categorie',{headers:{apikey:'sb_publishable_h3KHkTYHZ_fgBrqVpS0lpw_oZ04ktve'}}).then(function(r){if(!r.ok)throw 0;return r.json()}).then(function(rows){
if(!rows.length){msg.textContent=@EMPTY@;return}
var c=cptCalc(rows),pc=c.couv==null?null:Math.round(c.couv*100);el.className='live '+(pc==null||pc>=100?'ok':pc>=50?'mid':'low');
document.getElementById('bk_pc').textContent=pc==null?'—':pc+' %';
document.getElementById('bk_fm').textContent=eur(c.mens);document.getElementById('bk_dm').textContent=eur(c.donsMois);
var so=document.getElementById('bk_sol');so.textContent=(c.solde>0?'+':'')+eur(c.solde);so.className=c.solde<0?'neg':'pos';
var mx=Math.max.apply(null,[1].concat(c.mois.map(function(m){return Math.max(m.f,m.d)}))),mf=new Intl.DateTimeFormat(LOC,{month:'narrow'});
document.getElementById('bk_bars').innerHTML=c.mois.map(function(m){return '<div title="'+eur(m.f)+' / '+eur(m.d)+'"><div class="b"><i style="height:'+(m.f/mx*100)+'%"></i><i class="d" style="height:'+(m.d/mx*100)+'%"></i></div><small>'+mf.format(new Date(m.y,m.m,1))+'</small></div>'}).join('');
msg.hidden=true;document.getElementById('bk_box').hidden=false;requestAnimationFrame(function(){requestAnimationFrame(function(){document.getElementById('bk_m').style.width=Math.min(100,pc||0)+'%'})});
}).catch(function(){msg.textContent=@ERR@})})();"""

CONTACT = 'contact_I.n-T@he-P.it'
def legal(i):
    lg = L[i]; base = '../' if lg == 'en' else '../../'; home = '../'
    def a(k): return e(t(k, i)).replace('{C}', f'<a href="mailto:{CONTACT}">{CONTACT}</a>')
    secs = ''.join(f'<h2>{a(f"lg_h{n}")}</h2><p>{a(f"lg_p{n}")}</p>' for n in range(1, 5))
    return f'''<!doctype html>
<html lang="{lg}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{a("lg_t")} - In The Pit</title><meta name="robots" content="noindex"><meta name="theme-color" content="#0f0f10">
<link rel="icon" href="{base}img/icon-192.png">
<style>{fonts(base)}{CSS}.lgl{{max-width:720px;margin:0 auto;padding:40px 20px 70px}}.lgl img{{width:220px;height:auto;display:block;margin:0 0 26px}}.lgl h1{{font-size:2rem;margin:0 0 18px}}.lgl h2{{font-size:1.15rem;margin:28px 0 8px}}.lgl p{{margin:0 0 10px;line-height:1.6}}.lgl a{{color:inherit}}</style></head><body>
<main class="lgl"><a href="{home}" aria-label="In The Pit"><img src="{base}img/logo.webp" alt="In The Pit" width="900" height="300"></a>
<h1>{a("lg_t")}</h1>{secs}
<p><a href="{APP}/confidentialite.html?lang={lg}">{a("lg_priv")}</a></p>
<p><a href="{home}">‹ {a("lg_back")}</a></p><p style="margin-top:28px;opacity:.7">© 2026 Zion Hut Studio</p></main></body></html>
'''

def main():
    root = os.path.dirname(os.path.abspath(__file__))
    for i, lg in enumerate(L):
        d = root if lg == 'en' else os.path.join(root, lg)
        os.makedirs(d, exist_ok=True)
        open(os.path.join(d, 'index.html'), 'w', encoding='utf-8').write(page(i))
        os.makedirs(os.path.join(d, 'legal'), exist_ok=True)
        open(os.path.join(d, 'legal', 'index.html'), 'w', encoding='utf-8').write(legal(i))
    urls = ''.join(f'<url><loc>{DOMAIN}/{"" if l=="en" else l+"/"}</loc></url>' for l in L)
    open(os.path.join(root, 'sitemap.xml'), 'w').write(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>')
    open(os.path.join(root, 'robots.txt'), 'w').write(f'User-agent: *\nAllow: /\nSitemap: {DOMAIN}/sitemap.xml\n')
if __name__ == '__main__': main()
