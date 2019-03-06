# Magister-naar-google-calendar-PYTHON
Met deze code zet jij jouw magister lessen in google agenda/calendar!
##### Benodigdheden:
- Ervaring met python, libraries kunnen installeren.
- Chrome
- Een python file editor
  - *Ik ga binnekort een video maken over hoe je het programma gebruikt zodat iedereen dat kan doen. Ook ga ik een video maken over de werking van de code zelf.*

## Installeren en gebruiken:
1. Download het python bestand en plaats het in een aparte map.
2. Installeer de selenium library
  - *(Selenium: https://selenium-python.readthedocs.io/)*
  - *(Standaard command voor installeren : pip install selenium)*
3. Installeer de google calendar library
   - *(Google calendar: https://developers.google.com/api-client-library/python/start/installation)*
   - *(Standaard command: pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib)*
4. Verkrijg een credentials.json file. Lees daarvoor deze uitleg: https://github.com/lesander/magister-calendar/blob/master/ENABLEAPI.md     Plaats de credentials.json file in dezelfde maps als het python bestand.
4. Open de code met een code editor. (Maakt niet uit welke, als hij maar werkt.)
5. Verander de variabelen. (In de python file zelf staat hoe dit moet)
6. Voer het bestand uit, als het goed is moet je eerst bij google inloggen. Daarna zal je rooster
worden binnengeladen en geupload naar google calendar.
7. Zodra het programma je heeft ingelogd bij magister kies je de dag waarvan je de lessen in google calendar wilt hebben. *(Je kiest door rechtsboven te klikken op weergave, en dan de datum. Je hebt hier ongeveer 4/5 seconden voor)*

©Borek Bandell 2019
