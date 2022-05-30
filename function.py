def multiply_and_greet(*args,**kwargs):
    keys=kwargs.keys()
    x=1
    for num in args:
        x*=num
    print(x)
    if  "country" in keys:
        print(f"hello {kwargs['name']} from the beautiful Country {kwargs['country']}")
    elif "age" in keys:
        year=2022-kwargs["age"] 
        print( f"{kwargs['name']} you were born in {year}")
    elif "color" in keys:
        print(f"I am {kwargs['name']} and I like {kwargs['color']} jackets")
    elif "name" in keys:
        print(f"hello {kwargs['name']}")
    else:
        return f"hello you"
