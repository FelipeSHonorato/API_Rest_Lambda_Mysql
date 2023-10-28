from chalice import Chalice
from chalicelib.controllers.view_tasks import ViewTasks
from chalicelib.controllers.view_task import ViewTask
from chalicelib.controllers.insert_task import InsertTask
from chalicelib.controllers.edit_task import EditTask
from chalicelib.controllers.delete_task import DeleteTask

# Instanciando a classe do framework Chalice para gerenciar o aplicativo
app = Chalice(app_name='apitodo')

# Disponibilizando rota para editar tarefa - método PUT
@app.route('/tasks/{id_task}', methods=['PUT'])
def custom_edit(id_task):
    data = app.current_request
    task = EditTask()
    result = task.edit_task(id_task, data)
    return result

# Disponibilizando rota para criar tarefa - método POST
@app.route('/tasks', methods=['POST'])
def custom_insert():
    data = app.current_request
    task = InsertTask()
    result = task.insert_task(data)
    return result

# Disponibilizando rota para visualizar tarefas - método GET
@app.route('/tasks', methods=['GET'])
def custom_get():
    tasks = ViewTasks()
    result = tasks.view_tasks()
    return result

# Disponibilizando rota para visualizar tarefa - método GET
@app.route('/tasks/{id_task}', methods=['GET'])
def custom_get_id(id_task):
    task = ViewTask()
    result = task.view_task(id_task)
    return result

# Disponibilizando rota para deletar tarefa - método DELETE
@app.route('/tasks/{id_task}', methods=['DELETE'])
def custom_delete(id_task):
    task = DeleteTask()
    result = task.delete_task(id_task)
    return result