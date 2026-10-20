# .github

De openbare repository van de GitHub-organisatie van Life Outdoor Living. GitHub toont
[`profile/README.md`](profile/README.md) bovenaan de pagina van de organisatie; dat is het profiel.

De repositories van de organisatie zelf zijn privé en alleen toegankelijk voor leden. Deze is
openbaar, omdat GitHub het profiel alleen uit een openbare repository toont. Alles wat hier staat,
ook in de wiki, een issue of een pull request, kan dus iedereen lezen.

## Wat hier staat

- [`profile/README.md`](profile/README.md): het profiel van de organisatie.
- [`CONTRIBUTING.md`](CONTRIBUTING.md): hoe je een wijziging voorstelt, en een overzicht van elk
  bestand en elke workflow.
- [`SECURITY.md`](SECURITY.md): hoe je een beveiligingsprobleem meldt.
- [`LICENSE`](LICENSE): alles hier is eigendom van Life Outdoor Living International B.V.; er wordt
  geen licentie verleend.
- [`docs/wiki/`](docs/wiki/): de bron van de wiki. De workflow
  [`wiki`](.github/workflows/wiki.yml) zet de wiki na elke push naar `main` gelijk aan die map.
- [`.github/about.yml`](.github/about.yml): wat GitHub onder *About* toont. Dezelfde workflow
  vergelijkt het met GitHub, met [`.github/scripts/check_about.py`](.github/scripts/check_about.py).
