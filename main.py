from code.algoritmes import random
from code.algoritmes import greedy
from code.klassen import district
from code.visualisatie import smartgrid

def run_printer(x):
    print(f'run: {x}', end='\r', flush=True)

if __name__ == "__main__":

    wijk_kiezen = input('Kies wijk 1, 2 of 3: ')
    algoritme_kiezen = input('Kies uit algoritme (R)andom, (G)reedy: ')
    
    
    run_succesvol = False
    succesvolle_runs = {}
    mislukte_runs = 0
    

    if algoritme_kiezen == 'R' or algoritme_kiezen == "Random":
        aantal_runs = int(input('geef aantal runs: '))
        for x in range (0, aantal_runs):
            wijk = district.District(wijk_kiezen, x)
            run_succesvol = random.random_alg(wijk)
            run_printer(x)
            if run_succesvol:
                succesvolle_runs[wijk] = wijk.kosten_berekening()
            else: 
                mislukte_runs += 1
                
    elif algoritme_kiezen == 'G' or algoritme_kiezen == "Greedy":
        aantal_runs = 1
        wijk = district.District(wijk_kiezen, aantal_runs)
        run = greedy.greedy_alg(wijk)
        succesvolle_runs[wijk] = wijk.kosten_berekening()   
        
    else: 
        print('Invalid Argument')
    
    if len(succesvolle_runs) > 0:
        goedkoopste_run = min(succesvolle_runs, key= lambda x: succesvolle_runs[x])
        gemiddelde_prijs = int(sum(succesvolle_runs.values()) / len(succesvolle_runs))
        
        print('')
        print('Resultaten: ')
        print(f'Succesvolle runs:   {len(succesvolle_runs)}')
        print(f'Mislukte_runs:      {mislukte_runs}')
        print(f'goedkoopste run:    {goedkoopste_run.id} | {succesvolle_runs[goedkoopste_run]}')
        print(f'gemiddelde:         {gemiddelde_prijs}')
        smartgrid.visualise(wijk_kiezen, goedkoopste_run)
        
    else:
        print('Geen succesvolle runs!')


    