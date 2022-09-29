#constants
FOOTBALL_PRICE = 120
BASKETBALL_PRICE = 200
NETBALL_PRICE = 225
HOCKEY_PRICE = 275
SWIMMING_PRICE = 300

football_players = []
basketball_players = []
netball_players = []
hockey_players = []
swimming_players = []

campers = []

class Camper:
    name: str
    sports: list[str]

    def __init__(self, camper_name, sports) -> None:
        self.name = camper_name
        self.sports = sports   

        total_fee = 0
        for sport in self.sports:
            match sport:
                case "football":
                    football_players.append(camper_name)
                    total_fee += FOOTBALL_PRICE
                case "basketball":
                    basketball_players.append(camper_name)
                    total_fee += BASKETBALL_PRICE
                case "netball":
                    netball_players.append(camper_name)
                    total_fee += NETBALL_PRICE
                case "hockey":
                    hockey_players.append(camper_name)
                    total_fee += HOCKEY_PRICE
                case "swimming":
                    swimming_players.append(camper_name)
                    total_fee += SWIMMING_PRICE
        self.discounted_fee = total_fee * 0.9

        campers.append(self)

    def __repr__(self) -> str:
        return f"{self.name:<20}{', '.join(self.sports):<40}{self.discounted_fee:<10}"

   
        
taking_input = True
counter = 0

while taking_input:
    current_camper_name = input("Enter the name of the camper:\n")
    current_camper_sports = [sport.strip() for sport in input("Enter the sports the camper registered for separated by a comma:\n").split(",")]
    Camper(current_camper_name, current_camper_sports)

    counter+=1
    if counter >= 5:
        if input("Enter y to continue adding campers or n to stop\n") == "n":
            taking_input = False

    

print("\nList of campers")
print(f"{'Name':<20}{'Sports played':<40}{'Total fee':<10}")
print(*campers, sep="\n",end="\n\n")

print(f"{'Sport':<20}{'Amount of Campers registered':<40}{'Total paid in sport':<20}")
print(f"{'Football':<20}{len(football_players):<40}${len(football_players) * FOOTBALL_PRICE * 0.9:.2f}")
print(f"{'Basketball':<20}{len(basketball_players):<40}${len(basketball_players) * BASKETBALL_PRICE * 0.9:.2f}")
print(f"{'Netball':<20}{len(netball_players):<40}${len(netball_players) * NETBALL_PRICE * 0.9:.2f}")
print(f"{'Hockey':<20}{len(hockey_players):<40}${len(hockey_players) * HOCKEY_PRICE * 0.9:.2f}")
print(f"{'Swimming':<20}{len(swimming_players):<40}${len(swimming_players) * SWIMMING_PRICE * 0.9:.2f}")



