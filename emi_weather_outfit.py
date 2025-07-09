print("Emi's Weather Outfit Recommender")

print("I'm really glad that you are here today, this small prototype helps you choose great outfits based on your weather conditions and also your mood so let's get started.")

name = input("What's your name?")

print("Awesome",name ,"and by the way, what a stunning name!")

print("The goal of Emi's Weather Outfit Recommender is not only to recommend outfits to you based on the weather but also to maintain respect for different genders 😉.")

print("In this case, we only support 4 gender options (male, female, neutral, general)")

types_of_genders = [

"male",

"female",

"neutral",

"general"

  ]

while True:

question_1 = input("Write down the gender that you feel most comfortable with:").lower() .strip()

if question_1 in types_of_genders:

    break

else:

    print("This gender is not valid. Try again!")

print("Your gender is:", question_1, ".")

print("Like I mentioned before this is a really small prototype and it's limited by weather conditions. So these are the weather that we have available:")

weather_options = [

"Thunderstorm",

"Snowfall",

"Heatwave",

"Heavy Rain / Raining",

"Fog / Mist"

]

for r, wther in enumerate(weather_options, start= 1 ):

print(f"{r}. {wther}")

clothes_for_thunder = [

"CLOTHING TIPS FOR THUNDERSTORM WEATHER:",

"Waterproof jacket or raincoat",

"Waterproof boots or shoes",

"Umbrella (optional if raincoat is solid)",

"Avoid long / heavy fabric pants.",

]

female_thunder = [

"FINAL OUTFIT FOR YOU QUEEN!",

"Waterproof trench coat.",

"High-rise jeans.",

"Waterproof boots.",

"Tied-up hair."

]

male_thunder = [

"FINAL OUTFIT FOR YOU DUDE!",

"Hooded rain jacket.",

"Joggers.",

"Waterproof sneakers."

]

neutral_thunder = [

"10/10 WOULD RECOMMEND!",

"Windbreaker.",

"Cropped utility pants.",

"Slip-resistant boots."

]

clothes_for_snowfall = [

"CLOTHING TIPS FOR SNOWFALL WEATHER:",

"Insulated coat.",

"Thermal layers (underwear, tops).",

"Gloves, scarf, hat / beanie.",

"Waterproof boots with grip."

]

female_snowfall = [

"FINAL OUTFIT FOR YOU QUEEN!",

"Puffer coat.",

"Fleece-lined.",

"Leggings.",

"Snow boots.",

"Knit scarf & beanie."

]

male_snowfall = [

"FINAL OUTFIT FOR YOU DUDE!", 

"Parka.",

"Thermals.",

"Wool pants.",

"Waterproof boots."

]

neutral_snowfall = [

"10/10 WOULD RECOMMEND!",

"Layered thermal hoodie under a long coat.",

"Snow boots.",

"Warm gloves."

]

clothes_for_heatwave = [

"CLOTHING TIPS FOR HEATWAVE WEATHER:",

"Light-colored.",

"Breathable fabrics (cotton, linen).",

"Sleeveless or short-sleeved tops.",

"Sandals or breathable sneakers.",

"Sunglasses & hat."

]

female_heatwave = [

"FINAL OUTFIT FOR YOU QUEEN!",

"Linen dress.",

"Sandals or breathable sneakers.",

]

male_heatwave = [

"FINAL OUTFIT FOR YOU DUDE!",

"Cotton t-shirt.",

"Shorts.",

"Canvas sneakers."

]

neutral_heatwave = [

"10/10 WOULD RECOMMEND!",

"Loose tank.",

"Breathable tank or shorts.",

"Sun visor."

]

clothes_for_rain = [

"CLOTHING TIPS FOR HEAVY RAIN:",

"Raincoat or poncho.",

"Quick-drying fabrics.",

"Closed waterproof shoes.",

"Avoid denim (takes long to dry)."

]

female_rain = [

"FINAL OUTFIT FOR YOU QUEEN!",

"Hooded poncho.",

"Capri pants.",

"Waterproof sneakers."

]

male_rain = [

"FINAL OUTFIT FOR YOU DUDE!",

"Raincoat.",

"Track pants.",

"Rain boots."

]

neutral_rain = [

"10/10 WOULD RECOMMEND!",

"Oversized rain jacket.",

"Breathable joggers.",

"Waterproof sneakers."

]

clothes_for_mist = [

"CLOTHING TIPS FOR FOG OR MIST WEATHER:",

"Layered clothing (slightly cool / damp).",

"Light jacket or hoodie.",

"Reflective items (if walking outdoors).",

"Moisture-wicking layers."

]

female_mist = [

"FINAL OUTFIT FOR YOU QUEEN!",

"Light bomber jacket.",

"Jeans.",

"Sneakers."

]

male_mist = [

"FINAL OUTFIT FOR YOU DUDE!",

"Hoodie under light windbreaker.",

"Chinos.",

"Low-top shoes."

]

neutral_mist = [

"10/10 WOULD RECOMMEND!",

"Sweatshirt.",

"Tech pants.",

"Reflective sneakers or vest."

]

weather = int(input("How's the weather today where you live? (Choose a number.):"))

Outfits for the thunder

if question_1 == "male" and weather == 1:

print("Here are my recommendations for you buddy:")

for w, me in enumerate(male_thunder, start = 1 ):

    print(f"{w}. {me}")



elif question_1 == "female" and weather == 1:

print("Here are some of my recommendations for you queen:")

for q, fe in enumerate(female_thunder, start = 1 ):

    print(f"{q}. {fe}")



elif question_1 == "neutral" and weather == 1:

print("Here are some of my recommendations for you:")

for e, ne in enumerate(neutral_thunder, start = 1 ):

    print(f"{e}. {ne}")



elif question_1 == "general" and weather == 1:

print("Here are some general options for your closet:")

for a, thun in enumerate(clothes_for_thunder, start = 1 ):

    print(f"{a}. {thun}")

Outfits for the snowfall

elif question_1 == "male" and weather == 2:

print("Here are my recommendations for you buddy:")

for u, fa in enumerate(male_snowfall, start = 1 ):

    print(f"{u}. {fa}")



elif question_1 == "female" and weather == 2:

print("Here are some of my recommendations for you queen:")

for e, m in enumerate(female_snowfall, start = 1 ):

    print(f"{e}. {m}")



elif question_1 == "neutral" and weather == 2:

print("Here are some of my recommendations for you:")

for i, ll in enumerate(neutral_snowfall, start = 1 ):

    print(f"{i}. {ll}")



elif question_1 == "general" and weather == 2:

print("Here are some general options for your closet:")

for t, sn in enumerate(clothes_for_snowfall, start = 1 ):

    print(f"{t}. {sn}")

Outfits for heatwave

elif question_1 == "male" and weather == 3:

print("Here are my recommendations for you buddy:")

for s, wa in enumerate(male_heatwave, start = 1 ):

    print(f"{s}. {wa}")



elif question_1 == "female" and weather == 3:

print("Here are some of my recommendations for you queen:")

for p, at in enumerate(female_heatwave, start = 1 ):

    print(f"{p}. {at}")



elif question_1 == "neutral" and weather == 3:

print("Here are some of my recommendations for you:")

for d, ve in enumerate(neutral_heatwave, start = 1 ):

    print(f"{d}. {ve}")



elif question_1 == "general" and weather == 3:

print("Here are some general options for your closet:")

for o, he in enumerate(clothes_for_heatwave, start = 1 ):

    print(f"{o}. {he}")

#Outfits for rain

elif question_1 == "male" and weather == 4:

print("Here are my recommendations for you buddy:")

for h, raa in enumerate(male_rain, start = 1 ):

    print(f"{h}. {raa}")



elif question_1 == "female" and weather == 4:

print("Here are some of my recommendations for you queen:")

for g, ing in enumerate(female_rain, start = 1 ):

    print(f"{g}. {ing}")



elif question_1 == "neutral" and weather == 4:

print("Here are some of my recommendations for you:")

for j, vvv in enumerate(neutral_rain, start = 1 ):

    print(f"{j}. {vvv}")



elif question_1 == "general" and weather == 4:

print("Here are some general options for your closet:")

for f, ra in enumerate(clothes_for_rain, start = 1 ):

    print(f"{f}. {ra}")

Outfits for mist or fog

elif question_1 == "male" and weather == 5:

print("Here are my recommendations for you buddy:")

for z, mi in enumerate(male_mist, start = 1 ):

    print(f"{z}. {mi}")



elif question_1 == "female" and weather == 5:

print("Here are some of my recommendations for you queen:")

for l, g in enumerate(female_mist, start=1 ):

    print(f"{l}. {g}")



elif question_1 == "neutral" and weather == 5:

print("Here are some of my recommendations for you:")

for x, st in enumerate(neutral_mist, start = 1 ):

    print(f"{x}. {st}")



elif question_1 == "general" and weather == 5:

print("Here are some general options for your closet:")

for k, fo in enumerate(clothes_for_mist, start = 1 ):

    print(f"{k}. {fo}")

else:

print("NOT AVAILABLE")

Done

