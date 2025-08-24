import typer

def hello(name):
    print(f'hello {name}')
    
if __name__ == '__main__':
    typer.run(hello)