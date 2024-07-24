def transition_function(turing_machine, cadena, tape_symbols, final_state, initial_state=0):
    tape = cadena
    tape_print_before = ""
    # guarda el estado previo de la cinta, evita impresion repetida
    
    state_before = -1
    # lo mismo pero con el estado, siendo -1 en la primera vez 
    
    direction = {"D": 1, "I": -1, "S": 0}
    # establecemos numericamente como nos movemos por la cadena
    
    state = initial_state
    # estado inicial de la maquina de turing
    
    pointer = 0
    # posicion del cabezal sobre la cinta

    accept_transition = False
    # seteamos en falso por default que se acepta la transicion

    while True:
        transition = list(turing_machine[state])
        # obtenemos en una lista la función de transición en el estado actual de la mt

        if pointer == -1:
            tape = "~" + tape
            pointer += 1
        # si el cabezal esta antes del inicio de la cinta añadimos blanco al inicio de la cinta e inrementamos la posicion del cabezal sobre la cinta

        if pointer >= len(tape):
            tape = tape + "~"
        # si el cabezal apunta más allá del final de la cinta añadimos blanco al final de la misma

        for O, F, L, E, D in transition:
            # vamos a recorrer la lista del estado actual de la maquina de turing

            if tape[pointer] == L:
            
                if E in tape_symbols:
                    tape = tape[:pointer] + E + tape[pointer + 1:]
                    pointer += direction[D]
                    accept_transition = True 
                    tape_print = sides_without(tape.strip())
            # si el simbolo que apunta el cabezal es el mismo que el simbolo de la funcion de transicion y el simbolo para escribir en la cinta está en los simbolos de cinta que recibe la función, se escribe el símbolo en la cinta y se avanza el cabezal, se acepta la transición y se eliminan los rellenos y espacios

                    if tape_print_before != tape_print or state_before != state:
                        print(tape_print)
                    # se imprime la cinta si se cambió respecto a como se tenía originalmente
                    
                    state_before = state
                    # se situa el estado previo como el estado que estamos actualmente, en la primera vez es el estado inicial
                    
                    state = F
                    # se actualiza el estado actual al estado señalado por F en nuestra cadena

                    tape_print_before = tape_print
                    # guardamos el string como teníamos anteriormente en tape_print_before, para compararlo nuevamente en el futuro
                    break
        
        if not accept_transition and state == final_state:
            return True
         # si llegamos al estado final se acepta la cadena
        if not accept_transition:
            return False
        accept_transition = False
        # reseteamos el flag de aceptar la transicion para la proxima iteracion

def sides_without(tape, character="~"):
    while tape.startswith(character) or tape.endswith(character):
        if tape.startswith(character):
            tape = tape[1:]
        if tape.endswith(character):
            tape = tape[:-1]
        # remueve el primer o segundo caracter si son blanco
    if tape == "":
        tape += "~"
    # si la cinta queda vacía se agrega un blanco
    return tape
# funcion que remueve caracteres de relleno (por defecto "~" blanco) de los extremos de la cinta.

casos = int(input())
# introducimos los casos de entrada

for case in range(casos):
    N, T = map(int, input().strip().split(" "))
    # Lee el número de estados y transiciones

    estado_final = N - 1
    # El estado final es el último estado

    simbolos_cinta = input().replace(" ", "") + "~"
    # Lee los símbolos de la cinta y añade el relleno

    maquina_turing = dict()
    # Diccionario para almacenar las transiciones

    for _ in range(T):
        transition = input().strip().split(" ")
        #lee una transicion

        O = int(transition[0])
        #estado origen

        F = int(transition[1])
        #estado destino
        
        L, E, D = transition[2], transition[3], transition[4]
        # Símbolo leído, simbolo escrito, dirección de la transicion

        if O in maquina_turing:
            maquina_turing[O].append((O, F, L, E, D))
            # Añade la transición a la maquina de turing si el estado O pertenece a la maquina
        else:
            maquina_turing[O] = [(O, F, L, E, D)]
            # Crea una nueva lista de transiciones para el estado si este no se encontraba en la maquina
    
    for vertice in range(N):
        if vertice not in maquina_turing:
            maquina_turing[vertice] = list()
            # Asegura que todos los estados tengan una lista de transiciones, es decir se asegura de que se incluya un estado aunque no haya sido declarado antes en las funciones de transicion
    
    cadena_entrada = input()
    # recibimos la cadena

    print(f"caso {case + 1}:")
    print(cadena_entrada)
    # imprimimos el caso y la cadena recibida

    result = transition_function(maquina_turing, cadena_entrada, simbolos_cinta, estado_final)
    # nuestro resultado es un booleano que viene dado por la funcion transition_function
    if result:
        print("Aceptada")
    else:
        print("Rechazada")
    
    if case != casos - 1:
        print("")
    # imprimimos los resultados de cada cadena si fue aceptada o rechazada y un espacio entre ellos mientras no hayamos terminado