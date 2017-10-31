import graphene
import requests


class TodoItem(graphene.ObjectType):
    id = graphene.Int()
    description = graphene.String(required=True)
    status_done = graphene.Boolean()
    todoId = graphene.Int()
    todo = graphene.Field(lambda: Todo)

    def resolve_todo(self, info):
        """Resolve function to get all todo"""
        response = requests.get('http://localhost:3000/todos/%i' % self.todoId).json()
        data = Todo(id=response['id'], name=response['name'])
        return data


class Todo(graphene.ObjectType):
    id = graphene.Int()
    name = graphene.String(required=True)
    todo_items = graphene.List(lambda: TodoItem)

    def resolve_todo_items(self, info):
        """Resolve function to get todo items for a particular todolist"""
        response = requests.get('http://localhost:3000/todos/%i/todoitems' % self.id)
        data = [TodoItem(id=todo['id'], description=todo['description'], status_done=todo['status_done']) for todo in
                response.json()]
        return data


class Query(graphene.ObjectType):
    todos = graphene.List(Todo)
    todo_items = graphene.List(TodoItem)
    todo = graphene.Field(Todo, id=graphene.Int())
    todo_item = graphene.Field(TodoItem, id=graphene.Int())

    def resolve_todos(self, info):
        """Resolve function to get all todo lists available"""
        response = requests.get('http://localhost:3000/todos').json()
        data = [Todo(id=todo['id'], name=todo['name']) for todo in response]
        return data


    def resolve_todo_items(self, info):
        """Resolve function to get all todo items available"""
        response = requests.get('http://localhost:3000/todoitems').json()
        data = [TodoItem(id=todo['id'], description=todo['description'], todoId=todo['todoId'],
                         status_done=todo['status_done']) for todo in response]
        return data


    def resolve_todo(self, info, id):
        """Resolve function to get a particular todo"""
        response = requests.get('http://localhost:3000/todos/%i' % id).json()
        data = Todo(id=response['id'], name=response['name'])
        return data


    def resolve_todo_item(self, info, id):
        """Resolve function to get a todo item"""
        response = requests.get('http://localhost:3000/todoitems/%i' % id).json()
        data = TodoItem(id=response['id'], description=response['description'], status_done=response['status_done'],
                        todoId=response['todoId'])
        return data


schema = graphene.Schema(query=Query)
