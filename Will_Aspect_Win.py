import math

maps = {
    "Ambrose Island": .833,
    "Bangkok": .786,
    "Berlin": .927,
    "Chongqing": .889,
    "Colorado": .529,
    "Dartmoor": .73,
    "Dubai": .855,
    "Hokkaido": .608,
    "Haven Island": .708,
    "Isle of Sgail": .583,
    "Marrakesh": .579,
    "Mendoza": .896,
    "Miami": .778,
    "Mumbai": .864,
    "New York": .786,
    "Paris": .64,
    "Santa Fortuna": .545,
    "Sapienza": .75,
    "Whittleton Creek": .72
}

times = {
    "Ambrose Island": 60+52,
    "Bangkok": 60+23,
    "Berlin": 60+41,
    "Chongqing": 60+58,
    "Colorado": 60+14,
    "Dartmoor": 60+38,
    "Dubai": 60+38,
    "Hokkaido": 60+26,
    "Haven Island": 60+3,
    "Isle of Sgail": 120+6,
    "Marrakesh": 60+37,
    "Mendoza": 60+36,
    "Miami": 60+52,
    "Mumbai": 120+11,
    "New York": 60+32,
    "Paris": 60+36,
    "Santa Fortuna": 120+20,
    "Sapienza": 60+40,
    "Whittleton Creek": 54
}

showdowns = {
    "Dubai": 1,
    "Hokkaido": 0,
    "Haven Island": .6,
    "Mendoza": .727,
    "New York": 0,
    "Whittleton Creek": .703
}

showdown_times = {
    "Dubai": 60+38,
    "Hokkaido": 60+26,
    "Haven Island": 48,
    "Mendoza": 58,
    "New York": 60+32,
    "Whittleton Creek": 53
}

def syndicate_calc():
    list_maps = []
    num_maps = int(input('Which syndicate is Aspect on? '))
    num_maps += 2
    print('Enter the names of each map in the syndicate (besides the showdown)')
    for x in range(0, num_maps-1):
        map = str(input())
        list_maps.append(map)
    print('Enter the map where the showdown takes place')
    showdown_map = str(input())
    total_one = 0
    total_two = 0
    for y in list_maps:
        total_one += maps[y]
        total_two += times[y]
    total_one += showdowns[showdown_map]
    total_two += showdown_times[showdown_map]
    chance_of_success = total_one/num_maps * 100
    gamba_threshold = (.65 + (.05 * (num_maps-2))) * 100
    seconds = math.ceil((total_two/60 % 1) * 60)
    if seconds < 10:
        seconds = '0' + str(seconds)
    total_time = str(math.floor(total_two/60)) + ':' + str(seconds)
    print('Chance of Success:', "{:.2f}%".format(chance_of_success),  '\n'
          'Estimated Time: ' + total_time)
    if chance_of_success > gamba_threshold:
        print('You should BELIEVE in the GAMBA')
    else:
        print('You should DOUBT in the GAMBA')

if __name__ == "__main__":
    # This uses data collected by Tyler James Hurson on the HITMAN Freelancer Hardcore Speedruns document, thanks!
    # Link to the document -> https://docs.google.com/spreadsheets/d/1tK9DuUMCHDy28IFWSwj5oUBiyk6WAPhu8K_MSSMeSlE/edit#gid=0
    # Note, this is more than likely inaccurate as it doesn't take into account user error or any other potential variables, this
    # is just a silly little goof :)
    syndicate_calc()
    val = str(input('Would you like to continue? Y/N: '))
    while val == 'y' or val == 'Y':
        syndicate_calc()
        val = str(input('Would you like to continue? Y/N: '))
