from flask import render_template
from app import app
from models.order_details import orders


@app.route('/')
def app_index():
    return '<p>This is the index, go to <a href="orders">Tasks</p>'


@app.route('/orders/')
def task_index():
    return render_template('index.html', title="Order list", orders=orders)

# /tasks url
# list of tasks
# list of tasks with clickable links
# links route to /task/1


@app.route('/orders/<order_id>/', methods=['GET'])
def order_detail(order_id):
    for order in orders:
        if order_id == order.order_id:
            chosen_order = order
    return render_template('order.html', title="Order Details", order=chosen_order)
