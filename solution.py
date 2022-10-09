def log(line, info: str):
    with open("trace.txt", "a") as f:
        f.write(f"line {line} {info}\n");f.close() #3
#constants declarations
FOOTBALL_PRICE = 120 * 0.9
BASKETBALL_PRICE = 200 * 0.9
NETBALL_PRICE = 225 * 0.9
HOCKEY_PRICE = 275 * 0.9
SWIMMING_PRICE = 300 * 0.9
SPORTS = ["football", "basketball", "netball", "hockey", "swimming"]

#Global list of campers playing each sport
football_players = []
basketball_players = []
netball_players = []
hockey_players = []
swimming_players = []

#Global list of campers
campers = []


class Camper:
    #Member declarations
    name: str
    sports: list[str]
    total_fee: float

    def __init__(self, camper_name, camper_sports) -> None:
        """
        Creates a camper object from the camper's name and the sports they registered for.
        The total fee after discount will also be calculated according to the sports registered for.

        The camper's name will be stored in the respective global list of campers for each sport.
        """
        self.name = camper_name
        self.sports = camper_sports

        self.total_fee = 0
        for sport in self.sports:
            match sport:
                case "football":
                    football_players.append(camper_name)
                    self.total_fee += FOOTBALL_PRICE
                case "basketball":
                    basketball_players.append(camper_name)
                    self.total_fee += BASKETBALL_PRICE
                case "netball":
                    netball_players.append(camper_name)
                    self.total_fee += NETBALL_PRICE
                case "hockey":
                    hockey_players.append(camper_name)
                    self.total_fee += HOCKEY_PRICE
                case "swimming":
                    swimming_players.append(camper_name)
                    self.total_fee += SWIMMING_PRICE
  


    def __repr__(self) -> str:
        """
        Formats camper's name, sports played and fee into one string for outputting data neatly
        """
        return f"{self.name:<20}{', '.join(self.sports):<40}${self.total_fee:.2f}"


taking_input = True; log(64, f"taking_input = {taking_input}")

while taking_input:
    """
    The following variables are used to initialize current_camper
    """
    current_camper_name = input("Enter the name of the camper:\n");log(70, f"OUTPUT: Enter the name of the camper:");log(70, f"current_camper_name = {current_camper_name}")
    current_camper_sports = [];log(71, f"current_camper_sports = {current_camper_sports}")

    for sport in SPORTS:
        log(73, f"sport = {sport}") #4
        """
        Will keep asking for a y or n
        If y is inputted the value of sport in the current iteration will be added to the sports of the current camper
        """
        while True:
            is_playing_sport = input(f"Will {current_camper_name} be playing {sport}? Enter y for yes and n for no.\n").strip().lower();log(79, f"OUTPUT: Will {current_camper_name} be playing {sport}? Enter y for yes and n for no.");log(79, f"is_playing_sport = {is_playing_sport}")
            if is_playing_sport == "y":
                log(81, f"(is_playing_sport == 'y') = true") #5
                current_camper_sports.append(sport);log(81, f"current_camper_sports = {current_camper_sports}")
                break
            elif is_playing_sport == "n":
                log(83, f"(is_playing_sport == 'n') = true") #6
                break
            else:
                print(f"'{is_playing_sport}' is not a valid option, please enter y or n")
                continue

    """
    A camper object is created and added to the list of campers
    The program then outputs the current camper's name, lists the sports the current camper registered for and outputs the camper's total fee after discount
    """
    current_camper = Camper(current_camper_name, current_camper_sports);log(93, f"football_players = {football_players}");log(93, f"basketball_players = {basketball_players}");log(93, f"netball_players = {netball_players}");log(93, f"hockey_players = {hockey_players}");log(93, f"swimming_players = {swimming_players}")
    campers.append(current_camper);log(94, f"campers = {[camper.name for camper in campers]}")
    print(f"{current_camper.name} registered for {', '.join(current_camper.sports) if current_camper.sports else 'no sports'}, total fee is ${current_camper.total_fee:.2f} after discount\n");log(95, f"OUTPUT: {current_camper.name} registered for {', '.join(current_camper.sports)}, total fee is ${current_camper.total_fee:.2f} after discount")

    """
    Will keep asking for a y or n until one is provided
    If y is inputted the program will ask for another camper's data
    If n is inputted taking_input will be set to false and the program will stop asking for new camper's data
    """
    while True:
        inputting_more = input("Enter y to continue adding campers or n to stop\n").lower();log(103, "OUTPUT: Enter y to continue adding campers or n to stop"); log(103, f"inputting_more = {inputting_more}")
        if inputting_more == "y":
            log(111-6, f"(inputting_more == 'y') = true") #7
            break
        elif inputting_more == "n":
            log(114 - 7, f"inputting_more == 'n') = true") #8
            taking_input = False; log(107, f"taking_input = {taking_input}")
            break
        else:
            print(f"'{inputting_more}' is not a valid option, please enter y or n")

    

"""
Each camper's name, sports and total fee is outputted in a table with a blank line after
"""
print("\nList of campers")
print(f"{'Name':<20}{'Sports played':<40}{'Total fee':<10}")
print(*campers, sep="\n",end="\n\n")

"""
Outputs the amount of campers registered and total money earned in each sport 
"""
print(f"{'Sport':<20}{'Amount of Campers registered':<40}{'Total paid in sport':<20}")
print(f"{'Football':<20}{len(football_players):<40}${len(football_players) * FOOTBALL_PRICE:.2f}")
print(f"{'Basketball':<20}{len(basketball_players):<40}${len(basketball_players) * BASKETBALL_PRICE:.2f}")
print(f"{'Netball':<20}{len(netball_players):<40}${len(netball_players) * NETBALL_PRICE:.2f}")
print(f"{'Hockey':<20}{len(hockey_players):<40}${len(hockey_players) * HOCKEY_PRICE:.2f}")
print(f"{'Swimming':<20}{len(swimming_players):<40}${len(swimming_players) * SWIMMING_PRICE:.2f}")


