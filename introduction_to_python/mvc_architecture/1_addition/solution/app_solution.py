import view_solution as view
import  model_solution as model

number_1 = int(input('input1'))
number_2 = int(input('input2'))
result = number_1+number_2
view.display(result)
model.store([number_1,number_2,result])