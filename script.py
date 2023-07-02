destinations = ['Paris, France', 'Shanghai, China', 'Los Angeles, USA', 'São Paulo, Brazil', 'Cairo, Egypt']

test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

def get_destination_index(destination):
    return destinations.index(destination)

def get_traveler_location(traveler):
    traveler_destination = traveler[1]
    traveler_destination_index = get_destination_index(traveler_destination)
    return traveler_destination_index

attractions = [[] for destination in destinations]

def add_attraction(destination, attraction):
    destination_index = get_destination_index(destination)
    attractions_for_destination = attractions[destination_index]
    attractions_for_destination.append(attraction)
    return

# Adding all attractions

add_attraction('Los Angeles, USA', ['Venice Beach', ['beach']])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

def find_attractions(destination, interests):
    destination_index = get_destination_index(destination)
    attractions_in_city = attractions[destination_index]
    attractions_with_interest = []
    for attraction in attractions_in_city:
        possible_attraction = attraction[0]
        attraction_tags = attraction[1]
        for interest in interests:
            if interest in attraction_tags:
                attractions_with_interest.append(possible_attraction)
    return attractions_with_interest

def get_attractions_for_traveller(traveler):
    traveler_destination = traveler[1]
    traveler_interests = traveler[2]
    traveler_attractions = find_attractions(traveler_destination, traveler_interests)
    interests_string = "Hi " + traveler[0] + ", we think you'll like these places around " + traveler_destination + ': '
    traveler_attractions_length = len(traveler_attractions)
    index = 0
    for attraction in traveler_attractions:
        index += 1
        if index < traveler_attractions_length:
            interests_string += attraction + ', '
        else:
            interests_string += attraction + '.'
    return interests_string

print(get_attractions_for_traveller(['Dereck Smill', 'Paris, France', ['monument']]))



# print(find_attractions("Los Angeles, USA", ['art']))

# print(attractions)

# print(get_destination_index('Paris, F'))

# test_destination_index = get_traveler_location(test_traveler)

# print(test_destination_index)


