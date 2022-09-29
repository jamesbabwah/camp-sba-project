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
        return f"Name: {self.name}, Sports played: {', '.join(self.sports)}, Total Fee: ${self.discounted_fee}"

   
        
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
    

print("List of campers:")
print(*campers, sep="\n")



