# Site vitrine In The Pit

Site statique généré par `build.py` (5 langues), dépôt `madc-ccc/in-the-pit-site`, publié par Netlify à chaque push sur `main` (https://site.i.n-t.he-p.it). Régénérer avec `DOMAIN=https://site.i.n-t.he-p.it python3 build.py`.

- Commits : auteur `madc-ccc <34864328+madc-ccc@users.noreply.github.com>`.
- Polices hébergées dans `fonts/` (aucun appel à Google Fonts, pour le RGPD).
- Mentions légales générées dans `legal/` (clés `lg_*` de `build.py`).

## Éditeur : Zion Hut Studio

- **Nom** : éviter autant que possible le nom du fondateur ; partout (site, app, code, commits, documentation, communication) seul « Zion Hut Studio » est utilisé. Exception : là où la loi l’exige (mentions légales, CGV, factures, contrats), écrire « [prénom nom] EI – Zion Hut Studio » avec le SIRET, et nulle part ailleurs.

In The Pit et son site vitrine sont présentés comme édités par **Zion Hut Studio** (mentions légales, politique de confidentialité et copyright « © 2026 Zion Hut Studio » dans le pied de page du site, les mentions légales, la politique de confidentialité et la fenêtre « À propos » de l’app).

Le jour de l’immatriculation de Zion Hut Studio, mettre à jour (5 langues à chaque fois) :

- `concert-manager/confidentialite.html` : section « Qui est responsable » (forme juridique, SIRET, adresse) et date de mise à jour ; revoir les bases légales si l’activité devient commerciale.
- `in-the-pit-site/build.py` : mentions légales `lg_p1` (forme juridique, SIRET, adresse, directeur de la publication), puis régénérer le site.
- Comptes des prestataires à transférer au nom de la société, et accords de traitement des données (DPA) à réaccepter : Supabase, Netlify, Resend, Anthropic, Cloudflare ; titulaire du domaine he-p.it (OVH) ; Ko-fi ; dépôts GitHub.
- Nom d’expéditeur des e-mails (secret `MAIL_FROM` des Edge Functions) et adresse de contact si elle change.
- Comptes développeur Google Play / App Store au nom de Zion Hut Studio le jour d’une publication en magasin.
- `historique.json` : une ligne si le changement est visible des utilisateurs.
