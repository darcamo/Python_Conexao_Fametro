from random import choice
times = ["Time {0}".format(i) for i in "ABCDEF"]  # Sou preguiçoso
vitorias = {time:0 for time in times}
for time1 in times:
    for time2 in times:
        if time1!=time2:
            print("{0} x {1}".format(time1.upper(), time2))
            ganhador = choice([time1, time2])
            vitorias[ganhador] += 1
            print("{0} ganhou!".format(ganhador))

for time, num_vitorias in vitorias.items():
    print("{0} ganhou {1} vezes".format(time, num_vitorias))
