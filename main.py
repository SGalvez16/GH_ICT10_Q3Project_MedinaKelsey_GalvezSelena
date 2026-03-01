from pyscript import document, display

def password_authenticator(e):
    password = document.getElementById('input2').value
    output = document.getElementById("output")

    output.innerHTML = ""

    count = 0
    for char in password:
        count += 1

    if not password.isalpha():
        if password.isdigit():
            display("Must contain at least one letter", target="output")
        else:
            if count < 10:
                display("Must be 10 characters long", target="output")
            else:
                display("Thank you for submitting!", target="output")
    else:
        display("Must contain at least one number", target="output")

def intrams_qualifications(e):
    document.getElementById('output').innerHTML = ''
    reg_cleared = document.getElementById('body1').checked
    reg_notcleared = document.getElementById('body2').checked

    med_cleared = document.getElementById('body3').checked
    med_notcleared = document.getElementById('body4').checked

    section = document.getElementById("section").value

    if reg_cleared and med_cleared:
        display(f'Congratulations! Are you ready to rumble with {teams.get(section, "your team")}?', target='output')

    elif reg_notcleared:
        display('Unfortunately, you are not fit to play.', target='output')

    elif med_notcleared:
        display('Unfortunately, you are not fit to play.', target='output')

    else:
        display('Invalid Input', target='output')


# ---------- Intramurals Team Information ----------

teams = {
    "Sapphire": "Yellow Tigers",
    "Ruby": "Red Bulldogs",
    "Emerald": "Blue Bears",
    "Topaz": "Green Hornets"
}

def show_team_info(event):
    level = document.getElementById("level").value
    section = document.getElementById("section").value

    if not level or not section:
        document.getElementById("output").innerText = "Please select both grade and section."
        return

    if section not in clubs:
        document.getElementById("output").innerText = "Invalid section selected."
        return

    team = clubs[section]

    document.getElementById("output").innerText = (
        f"Congratulations! You are part of the {team}"
    )

players = [
    "Dela Cruz", "Garcia", "Reyes", "Ramos", "Mendoza",
    "Santos", "Gonzales", "Bautista", "Villanueva", "Cruz",
    "Torres", "Aquino", "Flores", "Rivera", "Lopez",
    "Perez", "Castillo", "Morales", "Rodriguez", "Fernandez",
    "Diaz"
]

def show_players(event):
    document.getElementById("output").innerHTML = ""
    
    for i in range(len(players)):
        display(str(i + 1) + ". " + players[i], target="output")
