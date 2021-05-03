
import model_solution as model
import view_solution as view

fruits = model.get_store()
show = view.show_fruits(fruits)
print(show)
fruit = view.ask_fruits()
model.update_fruits(fruit)
data = view.show_fruits(fruits)
print(data)