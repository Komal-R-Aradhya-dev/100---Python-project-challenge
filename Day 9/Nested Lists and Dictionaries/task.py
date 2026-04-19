travel_logs = {
    "Karnataka" : {
        "places_visited": ["sira","tumkur","banglore"],
        "num_of_visits": 100,
        "fav_place": {"sira": ["prseidency school","temple","my home"],
                      "tumkur": ["my home","all places","my room"],
                      "banglore": ["my military yard","army arena"]},

    "India" : ["Rajasthan", "Andhra Pradesh","Karnataka"]}
}
#print(travel_logs["Karnataka"][1])
#print(travel_logs["India"][2])
#nested_lists = ["arena","area",["komal","shiv",["komal1","komal2"]]]
#print(nested_lists[2][2][1])
print(travel_logs["Karnataka"]["fav_place"]["sira"][1])
