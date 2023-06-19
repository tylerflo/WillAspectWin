import math

maps = {
    "Ambrose Island": .79,
    "Bangkok": .75,
    "Berlin": .93,
    "Chongqing": .93,
    "Colorado": .63,
    "Dartmoor": .76,
    "Dubai": .81,
    "Hokkaido": .65,
    "Haven Island": .72,
    "Isle of Sgail": .69,
    "Marrakesh": .54,
    "Mendoza": .88,
    "Miami": .88,
    "Mumbai": .80,
    "New York": .75,
    "Paris": .61,
    "Santa Fortuna": .72,
    "Sapienza": .79,
    "Whittleton Creek": .74
}

times = {
    "Ambrose Island": 60+43,
    "Bangkok": 60+32,
    "Berlin": 60+48,
    "Chongqing": 120+4,
    "Colorado": 60+17,
    "Dartmoor": 60+50,
    "Dubai": 60+35,
    "Hokkaido": 60+28,
    "Haven Island": 60+9,
    "Isle of Sgail": 120+16,
    "Marrakesh": 60+45,
    "Mendoza": 60+27,
    "Miami": 120+21,
    "Mumbai": 120+11,
    "New York": 60+34,
    "Paris": 60+46,
    "Santa Fortuna": 180+7,
    "Sapienza": 120+1,
    "Whittleton Creek": 60+1
}

def syndicate_calc():
    list_maps = []
    num_maps = int(input('Which syndicate is Aspect on? '))
    num_maps += 2
    print('Enter the names of each map in the syndicate')
    for x in range(0, num_maps):
        map = str(input())
        list_maps.append(map)
    total_one = 0
    total_two = 0
    for y in list_maps:
        total_one += maps[y]
        total_two += times[y]
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