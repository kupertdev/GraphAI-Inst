from objects.interpreter import Interpreter

script = """
makebox Box1; 50; 50; Create Easy Graph
makebox Box2; Box1.x + 10; Box1.y + 100; With
makebox Box3; Box2.x + 10; Box2.y + 130; Small Graph Language
makearrow Box1; Box2
makearrow Box2; Box3
"""

interpreter = Interpreter()
interpreter.execute_gai(script)

graph = interpreter.get_graph()
graph.create_image()
graph.show_image()