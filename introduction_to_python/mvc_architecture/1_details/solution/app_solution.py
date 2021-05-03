import view_solution as view
import model_solution as model

name = view.capture_name()
age =  view.capture_age()
model.store(name,age)

info = view.display(name,age)
print(info)