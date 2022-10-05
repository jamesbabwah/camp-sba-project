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

    def __init__(self, name, sports) -> None:
        """
        Creates a camper object from the camper's name and the sports they registered for.
        The total fee after discount will also be calculated according to the sports registered for.

        The camper's name will be stored in the respective global list of campers for each sport.
        """
        self.name = name
        self.sports = sports

        total_fee = 0
        for sport in self.sports:
            match sport:
                case "football":
                    football_players.append(name)
                    total_fee += FOOTBALL_PRICE
                case "basketball":
                    basketball_players.append(name)
                    total_fee += BASKETBALL_PRICE
                case "netball":
                    netball_players.append(name)
                    total_fee += NETBALL_PRICE
                case "hockey":
                    hockey_players.append(name)
                    total_fee += HOCKEY_PRICE
                case "swimming":
                    swimming_players.append(name)
                    total_fee += SWIMMING_PRICE
        self.total_fee = total_fee


    def __repr__(self) -> str:
        """
        Formats camper's name, sports played and fee into one string for outputting data neatly
        """
        return f"{self.name:<20}{', '.join(self.sports):<40}${self.total_fee:.2f}"


taking_input = True

while taking_input:
    current_camper_name = input("Enter the name of the camper:\n")
    current_camper_sports = []

    for sport in SPORTS:
        while True:
            is_playing_sport = input(f"Will {current_camper_name} be playing {sport}? Enter y for yes and n for no.\n").strip().lower()
            if is_playing_sport == "y":
                current_camper_sports.append(sport)
                break
            elif is_playing_sport == "n":
                break
            else: 
                print(f"'{is_playing_sport}' is not a valid option, please enter y or n")
                continue

    
    current_camper = Camper(current_camper_name, current_camper_sports)
    campers.append(current_camper)
    print(f"{current_camper.name} registered for {', '.join(current_camper.sports)}, total fee is ${current_camper.total_fee:.2f} after discount\n")
    
    while True:
        inputting_more = input("Enter y to continue adding campers or n to stop\n")
        if inputting_more == "y":
            break
        elif inputting_more == "n":
            taking_input = False
            break
        else:
            print(f"'{inputting_more}' is not a valid option, please enter y or n")

    

#Outputs all the information in a table
print("\nList of campers")
print(f"{'Name':<20}{'Sports played':<40}{'Total fee':<10}")
print(*campers, sep="\n",end="\n\n")

print(f"{'Sport':<20}{'Amount of Campers registered':<40}{'Total paid in sport':<20}")
print(f"{'Football':<20}{len(football_players):<40}${len(football_players) * FOOTBALL_PRICE:.2f}")
print(f"{'Basketball':<20}{len(basketball_players):<40}${len(basketball_players) * BASKETBALL_PRICE:.2f}")
print(f"{'Netball':<20}{len(netball_players):<40}${len(netball_players) * NETBALL_PRICE:.2f}")
print(f"{'Hockey':<20}{len(hockey_players):<40}${len(hockey_players) * HOCKEY_PRICE:.2f}")
print(f"{'Swimming':<20}{len(swimming_players):<40}${len(swimming_players) * SWIMMING_PRICE:.2f}")


