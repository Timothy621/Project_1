from controllers import creation_controler, aproval_controler, employee_controler


def route(app):
    # Call remaining controllers
    creation_controler.route(app)
    aproval_controler.route(app)
    employee_controler.route(app)
