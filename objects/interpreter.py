import re
from objects.graph import Graph

class Interpreter:
    def __init__(self):
        self.graph = Graph()
        self.objects = {}

    def interpret(self, command: str, *args):
        if command == "makebox":
            if len(args) != 4:
                raise ValueError("Passed invalid number of arguments for makebox command")
            obj, x, y, text = args

            x = self.evaluate_expression(x)
            y = self.evaluate_expression(y)

            self.graph.add_box(obj, x, y, text)
            self.objects[obj] = self.graph.boxes[-1]
        elif command == "makearrow":
            box1, box2 = args
            box1 = self.objects[box1] if isinstance(box1, str) else box1
            box2 = self.objects[box2] if isinstance(box2, str) else box2

            self.graph.add_arrow(box1, box2)

    def evaluate_expression(self, expression):
        if isinstance(expression, (int, float)):
            return expression
        elif isinstance(expression, str):
            for name, obj in self.objects.items():
                expression = re.sub(rf"\b{name}\.x\b", str(obj.x), expression)
                expression = re.sub(rf"\b{name}\.y\b", str(obj.y), expression)

            return eval(expression)
        else:
            raise ValueError(f"Invalid expression: {expression}")

    def execute_gai(self, script: str):
        lines = script.splitlines()
        for line in lines:
            line = line.strip()
            if line.startswith("makebox"):
                _, args = line.split(" ", 1)
                args = [arg.strip() for arg in args.split(";")]
                self.interpret("makebox", *args)
            elif line.startswith("makearrow"):
                _, args = line.split(" ", 1)
                args = [arg.strip() for arg in args.split(";")]
                self.interpret("makearrow", *args)

    def get_graph(self):
        return self.graph
