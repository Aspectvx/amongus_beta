import random

# =========================
# GAME SETUP
# =========================

rooms = [
    "Cafeteria",
    "Electrical",
    "Navigation",
    "Reactor",
    "MedBay",
    "Security",
    "Admin"
]

bots = [
    "Red", "Blue", "Green", "Yellow",
    "Pink", "Orange", "White", "Black",
    "Purple", "Cyan"
]

all_players = ["You"] + bots
impostor = random.choice(all_players)

player_room = "Cafeteria"
alive = all_players.copy()
tasks_done = 0
max_tasks = 5

# =========================
# START MESSAGE
# =========================

print("🚀 AMONG US TERMINAL 🚀")
print(f"👥 Players: {', '.join(all_players)}")

if impostor == "You":
    print("😈 YOU ARE THE IMPOSTOR!")
else:
    print("🧑‍🚀 You are a CREWMATE.")

# =========================
# MAIN GAME LOOP
# =========================

while True:

    print(f"\n📍 Current room: {player_room}")
    print(f"🔧 Tasks: {tasks_done}/{max_tasks}")
    print(f"❤️ Alive players: {', '.join(alive)}")

    print("\nActions:")
    print("1. Move to another room")
    print("2. Do a task")
    print("3. Check who is in the room")
    print("4. Call an emergency meeting")

    if impostor == "You":
        print("5. 💀 Kill a player")

    choice = input("👉 Choose an action: ")

    # =====================
    # MOVE
    # =====================

    if choice == "1":
        print("\nAvailable rooms:")

        for i, room in enumerate(rooms):
            print(f"{i+1}. {room}")

        try:
            n = int(input("Room number: ")) - 1
            player_room = rooms[n]
            print(f"➡️ You moved to {player_room}.")
        except:
            print("❌ Invalid room!")

    # =====================
    # DO TASK
    # =====================

    elif choice == "2":

        if impostor == "You":
            print("😈 Impostors fake tasks...")
        else:
            tasks_done += 1
            print("🔧 Task completed!")

            if tasks_done >= max_tasks:
                print("\n🏆 ALL TASKS COMPLETED!")
                print("🧑‍🚀 Crewmates win!")
                break

    # =====================
    # CHECK ROOM
    # =====================

    elif choice == "3":

        present = random.sample(
            alive,
            random.randint(1, min(4, len(alive)))
        )

        print(f"👀 Players in {player_room}: {', '.join(present)}")

    # =====================
    # EMERGENCY MEETING
    # =====================

    elif choice == "4":

        print("\n📢 EMERGENCY MEETING!")

        suspect = random.choice([p for p in alive if p != "You"])

        print(f"🤖 Red: 'I think {suspect} is suspicious.'")
        print(f"🤖 Blue: 'I saw them near Electrical.'")
        print(f"🤖 Green: 'Where was everyone?'")

        vote = input("🗳️ Who do you want to eject? ")

        if vote not in alive:
            print("❌ That player is not alive or does not exist.")
        else:
            alive.remove(vote)

            print(f"🚀 {vote} was ejected.")

            if vote == impostor:
                print(f"🎉 {vote} was THE IMPOSTOR!")

                if impostor == "You":
                    print("💀 You lost!")
                else:
                    print("🏆 Crewmates win!")

                break

            else:
                print(f"😬 {vote} was not the impostor.")

    # =====================
    # KILL (IMPOSTOR ONLY)
    # =====================

    elif choice == "5" and impostor == "You":

        victims = [p for p in alive if p != "You"]

        if not victims:
            print("😈 No one left to kill.")
            continue

        print("\nPossible victims:")

        for v in victims:
            print("-", v)

        target = input("💀 Choose a victim: ")

        if target in victims:
            alive.remove(target)

            print(f"🔪 {target} was eliminated in {player_room}!")

            if len(alive) <= 2:
                print("\n😈 Impostors have taken control of the ship!")
                print("🏆 YOU WIN!")
                break

        else:
            print("❌ Invalid target.")

    else:
        print("❌ Invalid choice.")

    # =====================
    # RANDOM BODY DISCOVERY
    # =====================

    if (
        random.random() < 0.25 and
        impostor != "You" and
        len(alive) > 3
    ):

        victims = [p for p in alive if p != impostor]

        if victims:
            victim = random.choice(victims)
            alive.remove(victim)

            print(f"\n💀 A body has been reported: {victim}!")
            print(f"📍 The body was found in {random.choice(rooms)}.")
            print("🤔 Someone is lying...")