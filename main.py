from pyscript import display
from js import document

# club information ( Dictionary, by pair)
clubs = {            #format of club details
    "Marching Band": {
        "description": "A performance club for students who play instruments.",
        "schedule": "Tuesday and Wednesday 03:00-4:30 PM",
        "adviser": "Mr. Emilio Alumno",
        "venue": "Band Room"
    },
    "Glee Club": {
        "description": "A singing club for students who love music.",
        "schedule": "Monday 03:00- 05:00 PM",
        "adviser": "Mr. Denver Martin",
        "venue": "High School Music Room"
    },
    "Dance Club": {
        "description": "A club for students who enjoy dancing.",
        "schedule": "Tuesday 03:00 - 05:00 PM",
        "adviser": "Mr. Alfred Cases",
        "venue": "Theathro Preciosa"
    },
    "Math Club": {
        "description": "A club focused on math activities and competitions.",
        "schedule": "Monday 02:00 - 3:00PM",
        "adviser": "Mr. Nicole Gabuya",
        "venue": "Room 404",
        "number of members": "20",
        "category": "Academic"
    },
    "Science Club": {
        "description": "A club focused on science activities and experiments.",
        "schedule": "Tuesday 03:00 - 04:00 PM",
        "adviser": "Ms. Jameelyn Maramag",
        "venue": "Room 404",
        "number of members": "17",
        "category": "Academic"
    },

    "Communications Arts Club": {
         "description": "A club for students interested in communication and media.",
         "schedule": "Wednesday 03:00 - 04:00 PM, Friday 03:00 - 04:00 PM",
         "adviser": "Ms. Yannis Fernandez",
         "venue": "Room 406",
         "number of members": "20",
        "category": "Academic"
    },

    "COCC": {
         "description": "A leadership and discipline training program for students.",
          "schedule": "Wednesday 02:30 - 04:30 PM",
          "adviser": "SSgt. Jemima David PA (Res)",
          "venue": "Quadrangle / Teatro Preciosa",
          "number of members": "25",
          "category": "Academic"
     },

     "Social Science Club": {
          "description": "A club that focuses on social studies and related topics.",
          "schedule": "Tuesday 03:00 - 04:00 PM",
          "adviser": "Mr. Roberto Lim",
          "venue": "Room 409"
       },

    "Volleyball Varsity": {
          "description": "A varsity team for students who play volleyball.",
          "schedule": "Wednesday 03:00 - 04:00 PM",
          "adviser": "Mr. Adrian Ruiz",
          "venue": "Quadrangle",
          "number of members": "20",
          "category": "Sports"
      },

   "Basketball Varsity": {
          "description": "A varsity team for students who play basketball.",
          "schedule": "Monday 03:00 - 04:00 PM",
          "adviser": "Mr. Adrian Ruiz",
          "venue": "Quadrangle",
          "number of members": "20",
          "category": "Sports"
      } }

def submit_club(event):     #to be able to show details of club
    selected_club = document.getElementById("clubs").value
    document.getElementById("output").innerHTML = "" #this part is needed so that the details won't stack up

    if selected_club == "Choose":   #this specifies the club you are choosing
        display("Please select a club.", target="output")
    else:
        info = clubs[selected_club]

    # displaying club details
    display(f"Club Name: {selected_club}", target="output")
    display(f"Description: {info['description']}", target="output")
    display(f"Schedule: {info['schedule']}", target="output")
    display(f"Adviser: {info['adviser']}", target="output")
    display(f"Venue: {info['venue']}", target="output")