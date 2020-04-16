import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.colors import ListedColormap

class PSA_WBO:
    def __init__(self, sheet, cat):
        self.df = pd.read_excel(sheet)
        if cat != 'alle_functiegroepen':
            self.df = self.df.loc[self.df[self.df.columns[1]] == cat]
        self.df = self.df.drop(self.df.columns[[0, 1]], axis=1)
        self.questions = self.df.columns
        matplotlib.rc('xtick', labelsize=15)
        matplotlib.rc('ytick', labelsize=15)
        self.cmap = ListedColormap(["maroon", "red", "yellow", "lightgreen", "darkgreen", "lightblue"])
        self.cmap2 = ListedColormap(["red", "lightgreen", "lightblue"])
        self.cmap3 = ListedColormap(["red", "yellow", "lightgreen", "lightblue"])

    def get_plot_data(self, questions, options, dataframe):
        data = pd.DataFrame(index=questions, columns=options)  # create dataframe
        for option in options:
            data[option] = [sum(dataframe[question] == option) for question in
                            questions]  # fill in dataframe with right amounts of antwoordmogelijkheden
        data = 100 * data[options].div(data.sum(axis=1), axis=0)  # divide to get the percentage
        data = data.reindex(index=data.index[::-1])
        new = self.get_count(data.index)
        data = data.set_index(new)
        return data

    def get_count(self, lst):
        questions = []
        for i in range(len(lst)):
            q = lst[i]
            count = (sum(self.df[q].notnull()))
            questions.append(lst[i] + f' n={count}')
        return pd.Index(questions)

    def get_PSA_plots(self, year, func):
        # antwoordopties
        o_a = ['Zeer oneens', 'Oneens', 'Neutraal', 'Eens', 'Zeer eens', 'Geen mening']  # als input antwoordmogelijkheden
        o_b = ['Ja', 'Nee', 'Weet niet']
        o_c = ['Nee, ik zou graag meer uren willen werken', 'Nee, ik zou graag minder uren willen werken',
               'Ja, ik ben tevreden over het aantal uren dat ik werk', 'Geen mening']
        # vragen behorend tot antwoordopties
        q_a = self.questions[[0, 1] + list(range(3, 16))]
        q_b = self.questions[list(range(16, len(self.questions)))]
        q_c = [self.questions[2]]
        # verkrijg data
        data_a = self.get_plot_data(q_a, o_a, self.df)
        data_b = self.get_plot_data(q_b, o_b, self.df)
        data_c = self.get_plot_data(q_c, o_c, self.df)
        # verkrijg en toon figuren
        PSA_WBO.get_figures(data_a, (20, 10), self.cmap, f"PSA_plots/PSA_{year}_{func}_1_uit_3.png")
        PSA_WBO.get_figures(data_b, (20, 6), self.cmap2, f"PSA_plots/PSA_{year}_{func}_2_uit_3.png")
        PSA_WBO.get_figures(data_c, (20, 1.7), self.cmap3, f"PSA_plots/PSA_{year}_{func}_3_uit_3.png")
        # sla ruwe data op in een excel sheet
        with pd.ExcelWriter(f'PSA_plots_data/PSA_{year}_{func}.xlsx') as writer:
            data_a.to_excel(writer, sheet_name='1')
            data_b.to_excel(writer, sheet_name='2')
            data_c.to_excel(writer, sheet_name='3')
        return

    def get_WBO_plots(self, year, func):
        # antwoordopties
        o_a = ['Zeer oneens', 'Oneens', 'Neutraal', 'Eens', 'Zeer eens',
               'Geen mening']
        o_b = ['Te hoog', 'Hoog', 'Passend', 'Laag', 'Te laag', 'Geen mening']
        o_c = ['Ja', 'Nee', 'Weet niet']
        o_d = list(range(1, 11))
        # vragen behorend tot antwoordopties
        q_a = self.questions[[0] + list(range(2, 21))]
        q_b = self.questions[[1]]
        q_c = self.questions[[23]]
        q_d = self.questions[[26]]
        # verkrijg data
        data_a = self.get_plot_data(q_a, o_a, self.df)
        data_b = self.get_plot_data(q_b, o_b, self.df)
        data_c = self.get_plot_data(q_c, o_c, self.df)
        data_d = self.get_plot_data(q_d, o_d, self.df)
        # verkrijg en toon plots
        PSA_WBO.get_figures(data_a, (20, 13), self.cmap, f"WBO_plots/WBO_{year}_{func}_1_uit_4.png")
        PSA_WBO.get_figures(data_b, (20, 1.8), self.cmap, f"WBO_plots/WBO_{year}_{func}_2_uit_4.png")
        PSA_WBO.get_figures(data_c, (20, 1.5), self.cmap3, f"WBO_plots/WBO_{year}_{func}_3_uit_4.png")
        PSA_WBO.get_figures(data_d, (20, 2.4), plt.get_cmap('RdYlGn'), f"WBO_plots/WBO_{year}_{func}_4_uit_4.png")
        # sla ruwe data op in excel sheet
        with pd.ExcelWriter(f'WBO_plots_data/WBO_{year}_{func}.xlsx') as writer:
            data_a.to_excel(writer, sheet_name='1')
            data_b.to_excel(writer, sheet_name='2')
            data_c.to_excel(writer, sheet_name='3')
            data_d.to_excel(writer, sheet_name='4')

    @staticmethod
    def get_figures(data, figuresize, colormap, outputname):
        def add_text(df):

            for n in df:
                for i, (cs, ab, pc) in enumerate(zip(df.iloc[:, :].cumsum(1)[n], df[n], df[n])):
                    if int(pc) != 0:
                        plt.text(cs - ab / 2, i, str(np.round(pc, 1)) + '%', va='center', ha='center', weight='bold', size='small', stretch='ultra-condensed')
            return
        data.plot(kind='barh', stacked=True, figsize=figuresize, colormap=colormap)
        plt.legend(bbox_to_anchor=(0, 1.02, 1, 0.2), loc="lower left", mode="expand", borderaxespad=0, ncol=3,
                   fontsize=15)
        add_text(data)
        fig1 = plt.gcf()
        fig1.tight_layout()
        fig1.savefig(outputname)
        return

    @staticmethod
    def psa_or_wbo():
        psa_or_wbo = input('\nPSA of WBO?\n')
        if psa_or_wbo.upper() == 'PSA':
            return 'PSA'
        elif psa_or_wbo.upper() == 'WBO':
            return 'WBO'
        else:
            print('Ongeldige input, type PSA of WBO')
            return PSA_WBO.psa_or_wbo()

    @staticmethod
    def open_sheet():
        spreadsheet = input('\nType hier de bestandsnaam van de spreadsheet die u wilt analyseren:\n')
        try:
            f = open(spreadsheet)
            f.close()
            return spreadsheet
        except OSError as err:
            print(str(err) + '\nOngeldige input, check de spelling en/of aanwezigheid van het bestand in de map.')
            return PSA_WBO.open_sheet()

    @staticmethod
    def get_functiegroep():

        def open_functiegroepen():
            try:
                df = pd.read_excel('functiegroepen.xlsx')
                groepen = df[df.columns[0]].tolist()
                anw = list(range(len(groepen)))
                cat = ''
                for number, functie in enumerate(groepen):
                    cat += f"Type '{number}' voor de resultaten van functiegroep {functie}\n"
                return cat, anw, groepen
            except OSError as err:
                print(str(
                    err) + '\nDe excelsheet "functiegroepen.xlsx" is niet aanwezig in de map. Zorg ervoor dat deze '
                           'aanwezig is en deze naam draagt en probeer het programma opnieuw uit te voeren')
                return

        functiekeuze, antwoordmogelijkheden, functiegroepen = open_functiegroepen()
        category = input(f"\nVan welke functiegroep wilt u de {psa_wbo}-resultaten van {jaar} hebben?\n"
                         f"Type 'alle' voor de resultaten van alle functiegroepen\n"+functiekeuze)
        if category.isnumeric():
            if int(category) in antwoordmogelijkheden:
                return functiegroepen[int(category)]
        elif category.lower() == 'alle':
            return 'alle_functiegroepen'

        print('Ongeldige input, probeer opnieuw')
        return PSA_WBO.get_functiegroep()


if __name__ == "__main__":
    print('\nWBO/PSA VISUALISATIE TOOL\n'
          'April 2020 \nontwikkeld door Ingmar Visser in opdracht van Jelle Visser\n\n'
          'Deze tool is ontwikkeld om de data van PSA en WBO enquetes te verwerken en te visualiseren. Na het \n'
          'doorlopen van de stappen kunt u de PSA visualisaties in de map "PSA_plots" vinden en de WBO visualisaties \n'
          'in de map "WBO_plots. Ook de verwerkte data wordt opgeslagen, deze kunt u terugvinden in de mappen \n'
          '"PSA_plots_data" en WBO_plots_data".\n')
    sheet = PSA_WBO.open_sheet()
    psa_wbo = PSA_WBO.psa_or_wbo()
    jaar = input('\nVan welk jaar?\n')
    functiegroep = PSA_WBO.get_functiegroep()

    # sheet = 'test/EXCEL WBO.xlsx'
    # psa_wbo = 'WBO'
    # jaar = '2020'
    # functiegroep = 0
    #
    # sheet = 'test/PILOT PSA.xlsx'
    # psa_wbo = 'PSA'
    # jaar = '2020'
    # functiegroep = 0

    cls = PSA_WBO(sheet, functiegroep)
    if psa_wbo.upper() == 'PSA':
        cls.get_PSA_plots(jaar, functiegroep)
    elif psa_wbo.upper() == 'WBO':
        cls.get_WBO_plots(jaar, functiegroep)

    print(f'\nGelukt!\n'
          f'De visualisaties kunnen als .png-bestanden gevonden worden in de map "{psa_wbo}_plots".\n'
          f'Het excel-bestand met de gevisualiseerde percentages kan worden gevonden in de map "{psa_wbo}_plots_data."')
