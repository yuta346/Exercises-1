
import view_solution as view
import model_solution as model

movie_list = model.get_list()
del_key = view.delete_key()
model.del_list_key(del_key)
final_list = model.get_list()
view.display(final_list)
