elif tipo == "3" or tipo.lower() == "Villano":
    situacion = input(f"""Que sucede en saltadilla? (1-4)
                        1. La ciudad se encuentra muy tranquila
                        2. Las personas estan felices en un parque
                        3. Un transporte de colegio va muy tranquilo
                        4. Un puente se encuentra estable
                      """)
    if situacion == "1":
        if estado == "1" or estado.lower() == "melo":
            print("Estas habilitado para quitar la tranquilidad de la ciudad ")
        elif estado == "2" or estado.lower() == "cansado":
            solo = input(f"""Estas solo o acompañado?
                            1. Solo
                            2. Acompañado  
                          """)
            if solo == "1" or solo.lower() == "solo":
                print("Igual puedes destrozar la ciudad")
            elif solo == "2" or solo.lower() == "acompañado":
                print("Mucho mejor, se puede quitar la tranquilidad y la paz de la ciudad")
            else:
                print("Explicate mejor ombee ")
        elif estado == "3" or estado.lower() == "inconciente":
            print("Incapacitado, gano el heroe")
        elif estado == "4" or estado.lower() == "Herido":
            dolor = input("""Que tan grave: (1-3)
                            1. Dolor de cabeza
                            2. Demasiado
                            3. Poco
                          """)
            if dolor == "1":
                print("Tomate alguito como un dolex y melo")
            elif dolor == "2":
                print("Primero curate, luego destrozamos la ciudad")
            elif dolor == "3":
                print("Buena suerte en la pelea, puedes quitar la paz en la ciudad")
            else:
                print("Estas muerto")
    elif situacion == "2":
        if estado == "2" or estado.lower() == "melo":
            print("Estas habilitado para quitar la felicidad del parque, con todaa ")
        elif estado == "2" or estado.lower() == "cansado":
            solo = input(f"""Estas solo o acompañado?
                            1. Solo
                            2. Acompañado  
                          """)
            if solo == "1" or solo.lower() == "solo":
                print("Igual dale, el mal que triunfe")
            elif solo == "2" or solo.lower() == "acompañado":
                print("Que chimbx, dale con toda")
            else:
                print("Explicate mejor ombee")
        elif estado == "3" or estado.lower() == "inconciente":
            print("Incapacitado, gano el heroe")
        elif estado == "4" or estado.lower() == "Herido":
            dolor = input("""Que tan grave: (1-3)
                            1. Dolor de cabeza
                            2. Demasiado
                            3. Poco
                          """)
            if dolor == "1":
                print("Tomate alguito como un dolex y melo")
            elif dolor == "2":
                print("Primero curate, luego quitamos la felicidad del parque")
            elif dolor == "3":
                print("Buena suerte en la pelea, puedes quitar la felicidad del parque")
            else:
                print("Estas muerto")
 elif situacion == "3":
        if estado == "2" or estado.lower() == "melo":
            print("Estas habilitado para quitar la tranquilidad del transporte del colegio ")
        elif estado == "2" or estado.lower() == "cansado":
            solo = input(f"""Estas solo o acompañado?
                            1. Solo
                            2. Acompañado  
                          """)
            if solo == "1" or solo.lower() == "solo":
                print("Igual dale, el mal que triunfe")
            elif solo == "2" or solo.lower() == "acompañado":
                print("Que chimbx, dale con toda")
            else:
                print("Explicate mejor ombee")
        elif estado == "3" or estado.lower() == "inconciente":
            print("Incapacitado, gano el heroe y la tranquilidad")
        elif estado == "4" or estado.lower() == "Herido":
            dolor = input("""Que tan grave: (1-3)
                            1. Dolor de cabeza
                            2. Demasiado
                            3. Poco
                          """)
            if dolor == "1":
                print("Tomate alguito como un dolex y melo")
            elif dolor == "2":
                print("Primero curate, luego quitamos la tranquilidad del transporte del colegio")
            elif dolor == "3":
                print("Buena suerte en la pelea, puedes quitar la quitar la tranquilidad del transporte del colegio")
            else:
                print("Estas muerto")
elif situacion == "4":
        if estado == "2" or estado.lower() == "melo":
            print("Estas habilitado para quitar la estabilidad del puente ")
        elif estado == "2" or estado.lower() == "cansado":
            solo = input(f"""Estas solo o acompañado?
                            1. Solo
                            2. Acompañado  
                          """)
            if solo == "1" or solo.lower() == "solo":
                print("Igual dale, el mal que triunfe")
            elif solo == "2" or solo.lower() == "acompañado":
                print("Que chimbx, dale con toda")
            else:
                print("Explicate mejor ombee")
        elif estado == "3" or estado.lower() == "inconciente":
            print("Incapacitado, gano el heroe y la estabilidad del puente")
        elif estado == "4" or estado.lower() == "Herido":
            dolor = input("""Que tan grave: (1-3)
                            1. Dolor de cabeza
                            2. Demasiado
                            3. Poco
                          """)
            if dolor == "1":
                print("Tomate alguito como un dolex y melo")
            elif dolor == "2":
                print("Primero curate, luego quitamos la estabilidad del")
            elif dolor == "3":
                print("Buena suerte en la pelea, puedes quitar la estabilidad del puente")
            else:
                print("Estas muerto")