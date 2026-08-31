def generator_demo():
    yield "first statement"
    yield "second statement"
    yield "third statement"

gen=generator_demo()
for i