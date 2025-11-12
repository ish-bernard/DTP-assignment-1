is_raining = True
has_umbrella = True

if not is_raining:
    print("It's not raining, you don't need an umbrella.")  
elif is_raining and has_umbrella:
    print("It's raining, but you have an umbrella, you can go out.")
else:
    print("Better stay inside, it's raining and you don't have an umbrella.")