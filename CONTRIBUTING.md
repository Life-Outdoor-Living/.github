# Een wijziging voorstellen

Deze repository is het openbare GitHub-profiel van Life Outdoor Living. Wat op `main` staat,
toont GitHub op de pagina van de organisatie, voor iedereen.

## Wat hier staat

| bestand | wat het is |
| --- | --- |
| [`profile/README.md`](profile/README.md) | het profiel dat GitHub op de pagina van de organisatie toont |
| [`README.md`](README.md) | wat deze repository is |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | dit bestand |
| [`SECURITY.md`](SECURITY.md) | hoe je een beveiligingsprobleem meldt |
| [`LICENSE`](LICENSE) | eigendom van Life Outdoor Living International B.V.; geen licentie |
| [`docs/wiki/`](docs/wiki/) | de bron van de wiki van deze repository |
| [`.github/about.yml`](.github/about.yml) | wat GitHub onder *About* toont |
| [`.github/CODEOWNERS`](.github/CODEOWNERS) | wie GitHub om een review vraagt op elke pull request: het team Admins |
| [`.github/pull_request_template.md`](.github/pull_request_template.md) | de tekst waarmee elke nieuwe pull request begint |
| [`.github/dependabot.yml`](.github/dependabot.yml) | laat Dependabot eens per maand de GitHub Actions in de workflows bijwerken |
| [`.github/workflows/wiki.yml`](.github/workflows/wiki.yml) | zet de wiki gelijk aan `docs/wiki/` en vergelijkt *About* met `about.yml` |
| [`.github/scripts/check_about.py`](.github/scripts/check_about.py) | de vergelijking van *About* |

## Hoe een wijziging gaat

1. Maak een branch van `main`.
2. Wijzig de bestanden. **Alles hier is openbaar**: geen namen van klanten, leveranciers, collega's
   of interne systemen, geen adressen, en nooit een wachtwoord of sleutel.
3. Open een pull request naar `main` en zeg wat er verandert en waarom.
4. Een beheerder van de organisatie bekijkt hem en merget.

De wiki en *About* zijn een weergave van bestanden hier. Wijzig `docs/wiki/` of
`.github/about.yml` in een pull request; wat iemand in de wiki zelf typt, wordt bij de volgende
push naar `main` overschreven.

Een beveiligingsprobleem meld je niet in een pull request: zie [`SECURITY.md`](SECURITY.md).
