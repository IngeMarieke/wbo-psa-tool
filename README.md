# wbo-psa-tool
Om gebruik te maken van deze WBO- & PSA-visualisatie tool, is zult u de volgende stappen moeten doorlopen:


1) Installeren van Miniconda (alleen bij eerste gebruik, in de afwezigheid van een versie van Anaconda of Miniconda op uw computer)
	- Installeren in een Windows omgeving: https://docs.conda.io/projects/conda/en/latest/user-guide/install/windows.html
	- Installeren in een Mac omgeving: https://docs.conda.io/projects/conda/en/latest/user-guide/install/macos.html
	- Installeren in een Linux omgeving: https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html
	
	
2) Het creëren van een virtuele omgeving met Miniconda/ Anaconda (alleen bij eerste gebruik)
	- Open prompt/terminal:
	
		- Voor Windows gebruikers: open de Anaconda prompt
		
		- Voor Mac/ Linux gebruikers: open de Terminal
	- Navigeer volgens vanuit de prompt of terminal, naar de map "WBO_PSA_visualisatie_tool"
	- Vanuit deze map, type de volgende command:
		
			conda env create -f environment.yml
	
	Als het goed is heeft u nu een virtuele omgeving en bent u nu klaar om de tool te gebruiken!


3) De virtuele omgeving activeren (bij ieder gebruik)
	- Zorg dat u vanuit de Anaconda prompt of de Terminal in de map "WBO_PSA_visualisatie_tool" bent.
	- Type de volgende command:
		
			conda activate wbo_psa_omgeving


4) Het programma testen (optioneel)
	Als u de vorige stappen zonder problemen heeft doorlopen, kunnen we testen of de tool naar behoren functioneert. Dit kunt u doen door de volgende stappen te doorlopen:
	- Het programma opstarten
		
		Dit doet u door de volgende command te typen:
		
			python main.py
	- Vervolgens vraagt de tool om een spreadsheet. 
	
		- Om PSA te testen typt u hier het volgende:
		
			test/psa.xlsx
		
		- Om WBO te testen, typt u hier het volgende:
		
			test/wbo.xlsx
	
	De vervolgstappen spreken voor zich


5) Uw eigen data (enquete-reacties) verwerken
	- Zorg dat uw data zich in de map "WBO_PSA_visualisatie_tool" bevindt. 
		
		Uw data moet een excel spreadsheet zijn, met een .xlsx-extensie, bijvoorbeeld: PSA_2020.xlsx. Kopieer of verplaats uw spreadsheet naar de genoemde map.
	- Start het programma op door het volgende te typen: 
		
			python main.py
	- Het programma vraagt vervolgens om uw spreadsheet, in het geval van hetzelfde voorbeeld, typt u bij deze stap dus:
		
			PSA_2020.xlsx
		
		Let op: dit werkt alleen wanneer de spreadsheet zich in de map "WBO_PSA_visualisatie_tool" bevindt.
	
	Het programma vraagt na deze stap om nog een paar input-parameters, deze spreken in principe voor zich
	- Uw visualisaties bekijken
		
		Uw visualisaties verschijnen als .png bestanden in de map "PSA_plots" of in de map "WBO_plots" afhankelijk voor welk van de twee u heeft gekozen
	- De data bij de plots bekijken
		
		De data die geplot is in de .png bestanden kunt u terugvinden in een spreadsheet in de map "PSA_plots_data" of "WBO_plots_data" afhankelijk voor welk van de twee u gekozen heeft.

