from flask import render_template
from app import app
from models.order_details import orders


@app.route('/')
def app_index():
    return '<p>This is the index, go to <a href="orders">Tasks</p>'


@app.route('/orders/')
def task_index():
    return render_template('index.html', title="Todo list", orders=orders)

# /tasks url
# list of tasks
# list of tasks with clickable links
# links route to /task/1


@app.route('/orders/<int:index>/', methods=['GET'])
def order_detail(index):
    order = orders[index]
    return render_template('order.html', title="Task", order=order)


#app.add_url_rule('/tasks/<int:id>', 'task_index', task_index)
