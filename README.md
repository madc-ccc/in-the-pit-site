# Site vitrine In The Pit

Site statique, 5 langues (en à la racine, puis /fr/ /es/ /it/ /de/). Aucun framework, aucun JavaScript.

- Textes et mise en page : `build.py` (tous les textes sont dans le dictionnaire `T`, 5 langues alignées).
- Régénérer : `DOMAIN=https://site.i.n-t.he-p.it python3 build.py`
- Images : `img/` (captures de l'app avec des groupes fictifs).
- Déploiement : un nouveau site Netlify (dépôt Git distinct de l'app), puis domaine personnalisé dans Netlify > Domain management.
- Captures : `img/s-<écran>-<langue>.webp`, générées depuis l’app (données fictives) dans chaque langue ; pour les refaire, refaire les captures puis les convertir en WebP.
