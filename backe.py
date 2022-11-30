
filename='data.txt'
def todo_open(filename ='data.txt'):
    """This function is open a file and
      read it contents to a list"""
    with open(filename,'r') as file:
        todos = file.readlines()
        return todos
#print(help(todo_open()))            #prints the doc string
def todo_write(todos):
    with open('data.txt', 'w') as file:
        file.writelines(todos)


if __name__=='__main__':

   print('this is a function page')
