# Beveiligingsbeleid

Deze repository is het openbare GitHub-profiel van Life Outdoor Living. Ze bevat tekst, één
workflow en het script dat die draait, en geen data of credentials. Ze is **openbaar**: alles wat
hier staat, ook in een issue, een pull request of de wiki, kan iedereen lezen. Elke andere
repository van de organisatie is privé en heeft een eigen `SECURITY.md` met de details voor die
repository; dit bestand voegt daar niets aan toe.

## Wat telt als een beveiligingsprobleem

- **Een credential waar hij niet hoort.** Een wachtwoord, token, sleutel of certificaat in een
  commit, een branch, een issue, een pull request, een reactie of de wiki van een repository van
  Life Outdoor Living. Gedeeltelijk, onleesbaar gemaakt of "alleen de client-id" telt ook.
- **Iets dat niet openbaar hoort te zijn** en hier of in de wiki staat: een persoonsgegeven, een
  interne naam of adres, of een beschrijving van hoe een systeem van binnen werkt.
- **Een kwetsbaarheid** in een systeem, website of koppeling van Life Outdoor Living.

## Hoe je het meldt

**Niet in een issue, een pull request of een reactie.** Die zijn hier voor iedereen leesbaar, en
een geplakte waarde is niet terug te halen: GitHub bewaart de bewerkingsgeschiedenis, en meldingen
zijn dan al per mail verstuurd.

Meld het rechtstreeks bij de beheerders van de organisatie. Ben je lid, dan vind je in de
`SECURITY.md` van elke repository wie dat zijn en hoe je ze bereikt. Zeg:

1. wat het is en waar het staat, zonder de waarde zelf over te nemen;
2. wanneer je het zag;
3. of het er nog staat.

## Wat er dan gebeurt

1. **Een gelekte credential wordt vervangen**, niet alleen uit de geschiedenis gehaald: wie hem
   uitgaf, trekt hem in en geeft een nieuwe uit, en de nieuwe waarde gaat in de digitale kluis.
2. **Wat niet openbaar hoort te zijn, gaat eruit** met een pull request, en de oorzaak krijgt
   waar dat kan een controle die het de volgende keer tegenhoudt.
3. **Een datalek** volgt de stappen van de AVG (artikel 33 en 34), zoals de `SECURITY.md` van de
   repository waar het speelt die beschrijft.
