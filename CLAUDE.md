# Site vitrine In The Pit

Site statique généré par `build.py` (5 langues), dépôt `madc-ccc/in-the-pit-site`, publié par Netlify à chaque push sur `main` (https://site.i.n-t.he-p.it). Régénérer avec `DOMAIN=https://site.i.n-t.he-p.it python3 build.py`.

- Commits : auteur `madc-ccc <34864328+madc-ccc@users.noreply.github.com>`.
- Polices hébergées dans `fonts/` (aucun appel à Google Fonts, pour le RGPD).
- Mentions légales générées dans `legal/` (clés `lg_*` de `build.py`).

## Éditeur : passage de Pascal Berne à Zion Hut Studio (à faire)

Aujourd’hui, In The Pit et son site vitrine sont édités par **Pascal Berne, à titre personnel** (particulier, non commercial). À terme, l’éditeur doit devenir **Zion Hut Studio**, la société de Pascal dédiée à ses applis. Le jour du changement, mettre à jour tous les points suivants (5 langues à chaque fois) :

- `concert-manager/confidentialite.html` : section « Qui est responsable » (nom de la société, forme juridique, SIRET, adresse, contact) et date de mise à jour ; revoir les bases légales si l’activité devient commerciale.
- `in-the-pit-site/build.py` : mentions légales `lg_p1` (raison sociale, forme juridique, SIRET, adresse, directeur de la publication ; retirer « à titre non commercial »), puis régénérer le site.
- Copyright : déjà au nom de Zion Hut Studio (« © 2026 Zion Hut Studio » dans le pied de page du site vitrine, les mentions légales, la politique de confidentialité et la fenêtre « À propos » de l’app) ; mettre l’année à jour si besoin.
- Comptes des prestataires à transférer au nom de la société, et accords de traitement des données (DPA) à réaccepter : Supabase, Netlify, Resend, Anthropic, Cloudflare ; titulaire du domaine he-p.it (OVH) ; Ko-fi ; dépôts GitHub.
- Nom d’expéditeur des e-mails (secret `MAIL_FROM` des Edge Functions) et adresse de contact si elle change.
- Comptes développeur Google Play / App Store au nom de Zion Hut Studio le jour d’une publication en magasin.
- `historique.json` : une ligne pour annoncer le changement d’éditeur.
