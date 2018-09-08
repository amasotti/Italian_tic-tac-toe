import repertoire as rp
#import main

rp.benvenuto()

interuttore = True
while interuttore == True:
    # Settaggio dei parametri
    griglia_partenza = [ '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ' ]
    marker1, marker2 = rp.player_input()
    a_chi_tocca = rp.inizia_per_primo()
    if a_chi_tocca == 'Giocatore 1':
        print('Inizia per primo il ', a_chi_tocca, ' con la ', marker1)
    else:
        print('Inizia per primo il ', a_chi_tocca, ' con la ', marker2)

    # Inizio
    inizio = input('Pronti ad iniziare? (y/n) ')

    if inizio.lower().startswith("y"):
        partita = True
    else:
        partita = False

    while partita:
    # turno del giocatore 1
        if a_chi_tocca == 'Giocatore 1':
            rp.mostra_griglia(griglia_partenza)
            pos = rp.scelta(griglia_partenza)
            rp.posiziona_marker(griglia_partenza,marker1,pos)
            rp.mostra_griglia(griglia_partenza)
            if rp.controlla_vincitore(griglia_partenza,marker1):
                print('Complimenti', a_chi_tocca, '!!! Hai vinto!!!')
                partita = False
            else:
                if rp.controllo_saturazione(griglia_partenza):
                    rp.mostra_griglia(griglia_partenza)
                    print("Pareggio!")
                    partita = False
                else:
                    a_chi_tocca = 'Giocatore 2'
    # turno del giocatore 2
        else:
            rp.mostra_griglia(griglia_partenza)
            pos = rp.scelta(griglia_partenza)
            rp.posiziona_marker(griglia_partenza, marker2, pos)
            rp.mostra_griglia(griglia_partenza)
            if rp.controlla_vincitore(griglia_partenza, marker2):
                print('Complimenti', a_chi_tocca, '!!! Hai vinto!!!')
                partita = False
            else:
                if rp.controllo_saturazione(griglia_partenza):
                    rp.mostra_griglia(griglia_partenza)
                    print("Pareggio!")
                    partita = False
                else:
                    a_chi_tocca = 'Giocatore 1'


    # chiedi per continuare, altrimenti interrompi il loop principale
    if not rp.rivincita():
        interuttore = False







