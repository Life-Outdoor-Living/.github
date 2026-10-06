# Life Outdoor Living

Dit is de GitHub-organisatie van Life Outdoor Living: de code achter onze data, onze rapportages
en de manier waarop we met AI werken. Deze pagina is alleen zichtbaar voor leden van de organisatie.

## De repositories

| repository | wat het is | voor wie |
| --- | --- | --- |
| [`lakehouse`](https://github.com/Life-Outdoor-Living/lakehouse) | De Databricks-werkruimte als code: de bronnen (SAP, de webshop, de kassa's, betalingen, marketing en meer) van landing via bronze naar silver en gold, met de regels voor toegang, maskering en datakwaliteit. Alles wat in Databricks staat, staat hier in een bestand. | data-team |
| [`life-outdoor-living-analytics`](https://github.com/Life-Outdoor-Living/life-outdoor-living-analytics) | De eerste pilot: acht systemen in een lakehouse, en twee rapportages als Databricks App (E-Commerce Performance en Kassa Reconciliatie). | data-team |
| [`skills`](https://github.com/Life-Outdoor-Living/skills) | De skills die iedereen in Claude gebruikt, in Chat, Cowork en Claude Code, als plugin-marketplace. Bijvoorbeeld `issue-melden` om een probleem met de data te melden. | iedereen |
| [`finance-plugin`](https://github.com/Life-Outdoor-Living/finance-plugin) | De Finance-plugin voor Claude. Wijzigingen gaan via een pull request, en na de merge synct claude.ai hem naar de organisatie. | Finance & Control |
| [`ai-knowledge-base`](https://github.com/Life-Outdoor-Living/ai-knowledge-base) | Een portaal voor collega's die met AI werken: artikelen, podcasts en prompts. | iedereen |

## Een probleem met de data?

Gebruik de skill **`issue-melden`** in Claude. Je melding komt dan als issue in `lakehouse` terecht
met het label `melding`, en je hoort terug wat ermee gebeurt. Een melding sluit pas als jij antwoord
hebt gehad.

**Een beveiligingsprobleem meld je niet in een issue**, maar rechtstreeks bij Nino of Nicky. Denk
aan een wachtwoord of sleutel op een plek waar hij niet hoort, data die iemand kan zien die hem niet
hoort te zien, of een koppeling met meer dan leesrechten. Hoe dat verder gaat staat in
[`SECURITY.md`](https://github.com/Life-Outdoor-Living/lakehouse/blob/main/SECURITY.md) van
`lakehouse`.

## Hoe we werken

- **Wat niet in een bestand staat, bestaat niet.** De Databricks-werkruimte, de skills en de
  plugins worden uit deze repositories gezet; met de hand in een UI iets maken doen we niet.
- **Een wijziging is een pull request.** Hij gaat open als draft zodra de branch er is, en wordt
  gemerged op de dag dat hij groen is.
- **Koppelingen lezen alleen.** Elke koppeling met een extern systeem krijgt uitsluitend
  leesrechten. Uitzonderingen worden per systeem vastgelegd door een Owner. Wij schrijven nooit
  terug naar een bronsysteem.
- **Een wachtwoord of sleutel staat nooit in een repository**, een issue of een pull request. Niet
  gedeeltelijk en niet afgeschermd. Sleutels staan in de kluis, en in Databricks als secret van
  hun bron.
- **Persoonsgegevens worden gemaskeerd**, en wie een kolom meet rapporteert aantallen en nooit
  waarden.
- **Claude werkt mee**, binnen vastgelegde grenzen. In `lakehouse` houdt een hook die grenzen vast:
  geen secrets en niets wat niet terug te draaien is. Naar productie gaat alleen wat via een merge
  komt.

## Wie

- **Nino** (data) en **Nicky** beheren de organisatie, de koppelingen en de sleutels.
- Toegang tot een repository of tot Databricks vraag je bij een van hen aan.
