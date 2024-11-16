from objects.interpreter import Interpreter

file = input("Enter path to GAI file: ")
interpreter = Interpreter()

script = open(file, "r").read()

interpreter.execute_gai(script)

graph = interpreter.get_graph()
graph.create_image()
graph.show_image()