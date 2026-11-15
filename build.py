#!/usr/bin/env python3
"""Génère le site (5 langues) : python3 build.py   →  index.html (en), fr/, es/, it/, de/ + sitemap.xml
Variable d'environnement DOMAIN pour les URL absolues (défaut https://in-the-pit.com)."""
import os, random, html
DOMAIN = os.environ.get('DOMAIN', 'https://in-the-pit.com').rstrip('/')
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
'f1p': ("Drop in the PDF you received. In The Pit reads the artist, date, venue and price for you. At the entrance, one tap opens a black screen with only the QR code, big and sharp. The PDF stays one icon away for the staff.", "Dépose le PDF reçu. In The Pit lit l’artiste, la date, la salle et le prix à ta place. À l’entrée, un appui ouvre un écran noir avec le seul QR code, grand et net. Le PDF reste à une icône de distance pour le personnel.", "Sube el PDF que recibiste. In The Pit lee el artista, la fecha, la sala y el precio por ti. En la entrada, un toque abre una pantalla negra solo con el código QR, grande y nítido. El PDF queda a un icono de distancia para el personal.", "Carica il PDF ricevuto. In The Pit legge artista, data, locale e prezzo al posto tuo. All’ingresso, un tocco apre uno schermo nero con il solo codice QR, grande e nitido. Il PDF resta a un’icona di distanza per il personale.", "Lade das erhaltene PDF hoch. In The Pit liest Künstler, Datum, Halle und Preis für dich aus. Am Einlass öffnet ein Fingertipp einen schwarzen Bildschirm nur mit dem QR-Code, groß und scharf. Das PDF ist für das Personal ein Symbol entfernt."),
'f1a': ("Paper ticket? Photograph it. It is straightened, cropped and stored as a very light image.", "Un billet papier ? Photographie-le. Il est redressé, recadré et gardé en image très légère.", "¿Entrada de papel? Fotografíala. Se endereza, se recorta y se guarda como una imagen muy ligera.", "Biglietto cartaceo? Fotografalo. Viene raddrizzato, ritagliato e salvato come immagine leggerissima.", "Papierticket? Fotografiere es. Es wird begradigt, zugeschnitten und als sehr leichtes Bild gespeichert."),
'f1b': ("Add a note to the photo. Friends read it translated into their own language.", "Ajoute une note à la photo. Tes amis la lisent traduite dans leur langue.", "Añade una nota a la foto. Tus amigos la leen traducida a su idioma.", "Aggiungi una nota alla foto. Gli amici la leggono tradotta nella loro lingua.", "Füge der Foto eine Notiz hinzu. Freunde lesen sie in ihre Sprache übersetzt."),
'f1c': ("Venue membership cards go in too, with an icon on your upcoming concerts there.", "Les cartes d’abonnement aux salles aussi, avec une icône sur tes concerts à venir dans ces salles.", "Las tarjetas de socio de las salas también, con un icono en tus próximos conciertos allí.", "Anche le tessere di abbonamento ai locali, con un’icona sui tuoi prossimi concerti lì.", "Auch Mitgliedskarten von Hallen, mit einem Symbol bei deinen kommenden Konzerten dort."),

'f2t': ("Find any concert in seconds", "Retrouve n’importe quel concert en quelques secondes", "Encuentra cualquier concierto en segundos", "Trova qualsiasi concerto in pochi secondi", "Finde jedes Konzert in Sekunden"),
'f2p': ("Switches for your concerts, your friends’ concerts, past, upcoming, opening acts and not seen yet. Sort by date either way, and combine two keywords with and / or.", "Des interrupteurs pour tes concerts, ceux de tes amis, passés, à venir, premières parties et pas encore vus. Tri par date dans les deux sens, et deux mots-clés combinés par et / ou.", "Interruptores para tus conciertos, los de tus amigos, pasados, próximos, teloneros y aún no vistos. Orden por fecha en ambos sentidos y dos palabras clave combinadas con y / o.", "Interruttori per i tuoi concerti, quelli degli amici, passati, futuri, gruppi spalla e non ancora visti. Ordine per data in entrambi i sensi e due parole chiave combinate con e / o.", "Schalter für deine Konzerte, die deiner Freunde, vergangene, kommende, Vorbands und noch nicht gesehene. Sortierung nach Datum in beide Richtungen, zwei Stichwörter mit und / oder."),
'f2a': ("A slider keeps only what is within reach of home, and the distance shows on every concert.", "Un curseur ne garde que ce qui est à portée de chez toi, et la distance s’affiche sur chaque concert.", "Un control deslizante deja solo lo que está cerca de casa, y la distancia aparece en cada concierto.", "Un cursore tiene solo ciò che è vicino a casa, e la distanza compare su ogni concerto.", "Ein Schieberegler zeigt nur, was von zu Hause erreichbar ist, und die Entfernung steht bei jedem Konzert."),
'f2b': ("Your filters are remembered, and one blue button resets them all.", "Tes filtres sont mémorisés, et un bouton bleu les remet tous à zéro.", "Tus filtros se recuerdan y un botón azul los reinicia todos.", "I filtri vengono ricordati e un pulsante blu li azzera tutti.", "Deine Filter werden gemerkt, und ein blauer Knopf setzt alle zurück."),
'f2c': ("The search also finds friends, by name or email.", "La recherche trouve aussi les amis, par nom ou e-mail.", "La búsqueda también encuentra amigos, por nombre o correo.", "La ricerca trova anche gli amici, per nome o e-mail.", "Die Suche findet auch Freunde, nach Name oder E-Mail."),

'f3t': ("Concerts are better with friends", "Les concerts, c’est mieux entre amis", "Los conciertos son mejores con amigos", "I concerti sono più belli con gli amici", "Konzerte sind mit Freunden besser"),
'f3p': ("Share your list by email. Your friends’ concerts appear in yours, tagged with their name, and you can rename them however you like. You get a notification when a friend adds a concert.", "Partage ta liste par e-mail. Les concerts de tes amis apparaissent dans la tienne, avec leur nom, et tu peux les renommer comme tu veux. Tu es prévenu quand un ami ajoute un concert.", "Comparte tu lista por correo. Los conciertos de tus amigos aparecen en la tuya, con su nombre, y puedes renombrarlos como quieras. Recibes un aviso cuando un amigo añade un concierto.", "Condividi la tua lista via e-mail. I concerti degli amici compaiono nella tua, con il loro nome, e puoi rinominarli come preferisci. Ricevi una notifica quando un amico aggiunge un concerto.", "Teile deine Liste per E-Mail. Die Konzerte deiner Freunde erscheinen in deiner, mit ihrem Namen, und du kannst sie beliebig umbenennen. Du wirst benachrichtigt, wenn ein Freund ein Konzert hinzufügt."),
'f3a': ("Your venue memberships stay private. Only photos and notes of old tickets are shown to your friends.", "Tes abonnements restent privés. Seules les photos et notes de vieux billets sont montrées à tes amis.", "Tus abonos siguen siendo privados. Solo se muestran a tus amigos las fotos y notas de entradas antiguas.", "I tuoi abbonamenti restano privati. Solo foto e note dei vecchi biglietti sono mostrate agli amici.", "Deine Mitgliedschaften bleiben privat. Nur Fotos und Notizen alter Tickets sehen deine Freunde."),
'tile_a': ("Marée Noire", "Marée Noire", "Marée Noire", "Marée Noire", "Marée Noire"),
'note': ("“Front row, Hellfest 2009. Still the loudest night of my life.”", "« Premier rang, Hellfest 2009. La nuit la plus bruyante de ma vie. »", "«Primera fila, Hellfest 2009. La noche más ruidosa de mi vida.»", "«Prima fila, Hellfest 2009. La notte più rumorosa della mia vita.»", "„Erste Reihe, Hellfest 2009. Die lauteste Nacht meines Lebens.“"),
'note_c': ("Translated automatically from Spanish", "Traduit automatiquement de l’espagnol", "Traducido automáticamente del italiano", "Tradotto automaticamente dallo spagnolo", "Automatisch aus dem Spanischen übersetzt"),

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
'm7': ("Idea box", "Boîte à idées", "Buzón de ideas", "Casella delle idee", "Ideenbox"), 'm7p': ("Suggest what comes next. It goes straight to the creator.", "Propose la suite. Ça arrive directement au créateur.", "Propón lo que viene. Llega directo al creador.", "Proponi cosa fare dopo. Arriva direttamente al creatore.", "Schlage vor, was kommt. Es geht direkt an den Entwickler."),
'm8': ("What’s new", "Les nouveautés", "Novedades", "Novità", "Neuigkeiten"), 'm8p': ("After an update, see only what changed since your version.", "Après une mise à jour, vois seulement ce qui a changé depuis ta version.", "Tras una actualización, ve solo lo que cambió desde tu versión.", "Dopo un aggiornamento, vedi solo ciò che è cambiato dalla tua versione.", "Nach einem Update siehst du nur, was sich seit deiner Version geändert hat."),

'ft': ("Free, and it stays free", "Gratuit, et ça le reste", "Gratis, y se queda gratis", "Gratis, e resta gratis", "Kostenlos, und das bleibt so"),
'fp': ("In The Pit costs nothing. Running it has fixed costs, so if you enjoy it you can chip in on Ko-fi. Accounts are approved by hand: ask for access with your email and you will hear back.", "In The Pit ne coûte rien. Le faire tourner a des coûts fixes : si tu l’apprécies, tu peux participer sur Ko-fi. Les comptes sont validés à la main : demande l’accès avec ton e-mail et tu auras une réponse.", "In The Pit no cuesta nada. Mantenerlo tiene costes fijos, así que si te gusta puedes colaborar en Ko-fi. Las cuentas se aprueban a mano: pide acceso con tu correo y recibirás respuesta.", "In The Pit non costa nulla. Mantenerlo ha costi fissi, quindi se ti piace puoi contribuire su Ko-fi. Gli account sono approvati a mano: chiedi l’accesso con la tua e-mail e riceverai una risposta.", "In The Pit kostet nichts. Der Betrieb hat Fixkosten, wenn es dir gefällt, kannst du auf Ko-fi etwas beitragen. Konten werden von Hand freigegeben: Frage den Zugang mit deiner E-Mail an, du bekommst eine Antwort."),
'kofi': ("Chip in on Ko-fi", "Participer sur Ko-fi", "Colaborar en Ko-fi", "Contribuisci su Ko-fi", "Auf Ko-fi unterstützen"),
'req': ("Request access", "Demander l’accès", "Pedir acceso", "Richiedi l’accesso", "Zugang anfragen"),

'qt': ("Questions", "Questions", "Preguntas", "Domande", "Fragen"),
'q1': ("Do I need to install anything?", "Faut-il installer quelque chose ?", "¿Hay que instalar algo?", "Serve installare qualcosa?", "Muss ich etwas installieren?"),
'a1': ("No. Open it in your browser. If you like, add it to your home screen from the browser menu and it behaves like an app.", "Non. Ouvre-la dans ton navigateur. Si tu veux, ajoute-la à ton écran d’accueil depuis le menu du navigateur et elle se comporte comme une app.", "No. Ábrela en tu navegador. Si quieres, añádela a tu pantalla de inicio desde el menú del navegador y se comporta como una app.", "No. Aprila nel browser. Se vuoi, aggiungila alla schermata iniziale dal menu del browser e si comporta come un’app.", "Nein. Öffne sie im Browser. Wenn du möchtest, füge sie über das Browsermenü zum Startbildschirm hinzu, dann verhält sie sich wie eine App."),
'q2': ("Who can see my concerts?", "Qui peut voir mes concerts ?", "¿Quién puede ver mis conciertos?", "Chi può vedere i miei concerti?", "Wer kann meine Konzerte sehen?"),
'a2': ("You, and the friends you share with. You can also choose to appear, anonymously, in the public guest list. It is off by default and shows no name, notes, prices or tickets.", "Toi, et les amis avec qui tu partages. Tu peux aussi choisir d’apparaître, anonymement, dans la liste publique des invités. C’est désactivé par défaut, sans nom, notes, prix ni billets.", "Tú y los amigos con quienes compartes. También puedes aparecer, de forma anónima, en la lista pública de invitados. Está desactivado por defecto y no muestra nombre, notas, precios ni entradas.", "Tu e gli amici con cui condividi. Puoi anche scegliere di comparire, in forma anonima, nell’elenco pubblico degli ospiti. È disattivato di default e non mostra nome, note, prezzi né biglietti.", "Du und die Freunde, mit denen du teilst. Du kannst auch anonym in der öffentlichen Gästeliste erscheinen. Das ist standardmäßig aus und zeigt weder Namen noch Notizen, Preise oder Tickets."),
'q3': ("What does it do with my tickets?", "Que fait-elle de mes billets ?", "¿Qué hace con mis entradas?", "Cosa fa con i miei biglietti?", "Was passiert mit meinen Tickets?"),
'a3': ("An AI reads PDF tickets to fill in artist, date, venue and price. It is told to ignore your name, address and barcodes. Paper tickets are kept as photos, and you decide what to add.", "Une IA lit les billets PDF pour remplir artiste, date, salle et prix. Elle a pour consigne d’ignorer ton nom, ton adresse et les codes-barres. Les billets papier sont gardés en photo, et tu choisis ce que tu ajoutes.", "Una IA lee las entradas en PDF para rellenar artista, fecha, sala y precio. Tiene la consigna de ignorar tu nombre, dirección y códigos de barras. Las entradas de papel se guardan como fotos y tú decides qué añadir.", "Un’IA legge i biglietti PDF per compilare artista, data, locale e prezzo. Ha l’istruzione di ignorare nome, indirizzo e codici a barre. I biglietti cartacei sono salvati come foto e sei tu a decidere cosa aggiungere.", "Eine KI liest PDF-Tickets, um Künstler, Datum, Halle und Preis auszufüllen. Sie soll deinen Namen, deine Adresse und Barcodes ignorieren. Papiertickets werden als Fotos gespeichert, und du entscheidest, was du hinzufügst."),

'cta_t': ("See you in the pit.", "On se retrouve dans la fosse.", "Nos vemos en el foso.", "Ci vediamo sotto il palco.", "Wir sehen uns im Graben."),
'foot': ("Made for people who still keep their ticket stubs.", "Fait pour ceux qui gardent encore leurs billets.", "Hecho para quienes aún guardan sus entradas.", "Fatto per chi conserva ancora i biglietti.", "Für alle, die ihre Tickets noch aufheben."),
'skip': ("Skip to content", "Aller au contenu", "Ir al contenido", "Vai al contenuto", "Zum Inhalt"),
'alt_list': ("The In The Pit concert list", "La liste de concerts d’In The Pit", "La lista de conciertos de In The Pit", "L’elenco dei concerti di In The Pit", "Die Konzertliste von In The Pit"),
'alt_filters': ("The filters panel", "Le panneau de filtres", "El panel de filtros", "Il pannello dei filtri", "Das Filterpanel"),
'alt_stats': ("The statistics screen", "L’écran des statistiques", "La pantalla de estadísticas", "La schermata delle statistiche", "Der Statistikbildschirm"),
}
FAQ = [('q1', 'a1'), ('q2', 'a2'), ('q3', 'a3')]

ICON = {
 'tk': '<path d="M3 8a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2v2a2 2 0 0 0 0 4v2a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-2a2 2 0 0 0 0-4z"/><path d="M14 6v12" stroke-dasharray="2 2.5"/>',
 'fl': '<path d="M3 5h18l-7 8v6l-4 2v-8z"/>',
 'us': '<circle cx="9" cy="8" r="3.2"/><path d="M3 20c0-3.3 2.7-5.5 6-5.5s6 2.2 6 5.5"/><circle cx="17" cy="9" r="2.4"/><path d="M17 14.3c2.4 0 4 1.7 4 4.2"/>',
 'st': '<path d="M6 20V11M12 20V4M18 20v-6"/>',
 'bl': '<path d="M6 17V11a6 6 0 0 1 12 0v6l1.5 2h-15z"/><path d="M10 21h4"/>',
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
header.top{position:sticky;top:0;z-index:5;background:rgba(15,15,16,.92);backdrop-filter:blur(8px);border-bottom:1px solid #2a2a2d}
header.top .wrap{display:flex;align-items:center;gap:18px;min-height:68px}
header.top img{width:104px;height:auto}
header nav{display:flex;gap:20px;margin-left:auto;align-items:center}
header nav a{text-decoration:none;font-weight:600;font-size:16px}header nav a:hover{text-decoration:underline}
.lang{display:flex;gap:2px;font-size:14px}.lang a{padding:6px 7px;border-radius:6px;text-decoration:none;color:#b9b9bd;font-weight:600}.lang a[aria-current]{color:var(--ink);background:var(--paper)}
header .btn{min-height:42px;padding:0 18px;font-size:15px}
@media(max-width:820px){header nav .l{display:none}header.top .wrap{gap:10px}.lang a{padding:6px 5px}header .btn{padding:0 14px}}
@media(max-width:520px){header.top img{width:84px}header .btn{display:none}}

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
.tkscr .pdf{display:inline-block;margin-top:16px;border:2px solid #666;border-radius:8px;padding:4px 10px;font-size:.78rem;color:#ddd}
.tile{background:#222224;border:2px solid var(--org);border-radius:16px;padding:14px 16px 28px;position:relative;color:#f2f2f3;font-size:.95rem;text-align:left}
.tile small{display:block;color:#a5a5aa;font-size:.8rem}
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
    tkvis = f'<div class="phone"><div class="tkscr"><img src="{base}img/logo.webp" alt="" width="900" height="300"><b>Velvet Static</b><small>2026-11-28 · Le Trianon, Paris</small><div class="qr">{qr_svg()}</div><span class="pdf">PDF</span></div></div>'
    frvis = f'<div class="stack"><div class="tile"><small>2027-02-03 · Razzmatazz, Barcelona</small><b>Los Cometas</b><em>Alice</em></div><div class="tile"><small>2027-01-17 · L’Olympia, Paris</small><b>{e(t("tile_a",i))}</b><em>Bob</em></div><div class="bubble">{e(t("note",i))}<small>{e(t("note_c",i))}</small></div></div>'
    ntvis = f'<div class="stack"><div class="notif"><img src="{base}img/icon-192.png" alt="" width="38" height="38"><div><b>In The Pit</b>{e(t("n1",i))}</div></div><div class="notif"><img src="{base}img/icon-192.png" alt="" width="38" height="38"><div><b>In The Pit</b>{e(t("n2",i))}</div></div><div class="notif"><img src="{base}img/icon-192.png" alt="" width="38" height="38"><div><b>In The Pit</b>{e(t("n3",i))}</div></div></div>'
    small = ''.join(f'<div><h3>{a(f"m{n}")}</h3><p>{a(f"m{n}p")}</p></div>' for n in range(1, 9))
    faq = ''.join(f'<details><summary>{a(q)}</summary><p>{a(an)}</p></details>' for q, an in FAQ)
    return f'''<!doctype html>
<html lang="{lg}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{a("title")}</title><meta name="description" content="{a("desc")}">
<link rel="canonical" href="{canon}">{alts}
<meta property="og:title" content="{a("title")}"><meta property="og:description" content="{a("desc")}"><meta property="og:type" content="website"><meta property="og:url" content="{canon}"><meta property="og:image" content="{DOMAIN}/img/og.png">
<meta name="twitter:card" content="summary_large_image"><meta name="theme-color" content="#0f0f10">
<link rel="icon" href="{base}img/icon-192.png"><link rel="apple-touch-icon" href="{base}img/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,100..900&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body>
<a class="skip" href="#main">{a("skip")}</a>
<header class="top"><div class="wrap"><a href="{lhref(lg)}" aria-label="In The Pit"><img src="{base}img/logo.webp" alt="In The Pit" width="900" height="300"></a>
<nav><a class="l" href="#tk">{a("nav_f")}</a><a class="l" href="#faq">{a("nav_q")}</a><div class="lang" aria-label="Language">{langs}</div><a class="btn" href="{APP}">{a("open")}</a></nav></div></header>
<main id="main">
<section class="hero k"><div class="wrap"><div><h1>{a("h1")}</h1><p class="lead">{a("hp")}</p><div class="btns"><a class="btn" href="{APP}">{a("open")}</a><a class="btn ghost" href="#tk">{a("see")}</a></div></div>
<div class="phones" aria-hidden="false">{ph("s-filters.webp",t("alt_filters",i)).replace('class="phone"','class="phone p2"')}{ph("s-list.webp",t("alt_list",i)).replace('class="phone"','class="phone p1"')}</div></div></section>
{feat("y",False,"","#f59e0b","tk",t("f1t",i),t("f1p",i),[t("f1a",i),t("f1b",i),t("f1c",i)],tkvis)}
{feat("k",True,"","#2f6fed","fl",t("f2t",i),t("f2p",i),[t("f2a",i),t("f2b",i),t("f2c",i)],ph("s-filters.webp",t("alt_filters",i)))}
{feat("y",False,"","#e11d74","us",t("f3t",i),t("f3p",i),[t("f3a",i)],frvis)}
{feat("k",True,"","#8b5cf6","st",t("f4t",i),t("f4p",i),[],ph("s-stats.webp",t("alt_stats",i)))}
{feat("y",False,"","#22c55e","bl",t("f5t",i),t("f5p",i),[],ntvis)}
<section class="band small k"><div class="wrap"><h2>{a("mt")}</h2><div class="grid">{small}</div></div></section>
<section class="band free y"><div class="wrap"><div><h2>{a("ft")}</h2><p>{a("fp")}</p></div><div class="btns" style="margin:0"><a class="btn" href="{APP}">{a("req")}</a><a class="btn ghost" href="{KOFI}" rel="noopener">{a("kofi")}</a></div></div></section>
<section class="band faq k" id="faq"><div class="wrap"><h2>{a("qt")}</h2>{faq}</div></section>
<section class="band last y"><div class="wrap"><h2>{a("cta_t")}</h2><div class="btns"><a class="btn" href="{APP}">{a("open")}</a></div></div></section>
</main>
<footer><div class="wrap"><img src="{base}img/logo.webp" alt="In The Pit" width="900" height="300"><span>{a("foot")}</span><span><a href="{KOFI}" rel="noopener">Ko-fi</a></span></div></footer>
</body></html>'''

def main():
    root = os.path.dirname(os.path.abspath(__file__))
    for i, lg in enumerate(L):
        d = root if lg == 'en' else os.path.join(root, lg)
        os.makedirs(d, exist_ok=True)
        open(os.path.join(d, 'index.html'), 'w', encoding='utf-8').write(page(i))
    urls = ''.join(f'<url><loc>{DOMAIN}/{"" if l=="en" else l+"/"}</loc></url>' for l in L)
    open(os.path.join(root, 'sitemap.xml'), 'w').write(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>')
    open(os.path.join(root, 'robots.txt'), 'w').write(f'User-agent: *\nAllow: /\nSitemap: {DOMAIN}/sitemap.xml\n')
if __name__ == '__main__': main()
