print("==============spisok============")
b = [1,"True",2]
print(b)


print("===========pop==============")
b = [1,"True",2]
test_pop = b.pop(2) #Поп удалит элемент списка под номером 2 и вернет результат в виде того что удалил
print(b)
print(test_pop)

print("===============remove==============")
b = [1,"True",2]
b.remove("True") #Удаляет элемент из списка по значению. В данном случае удалит "True"
print(b)

print("==================del===============")
b = [1,"True",2]
del b[1] #Удаляет элемент из списка по номеру. Так то может удалить что угодно. В данном случае удалить "True"
print(b)

print("================append==============")
b = [1,"True",2]
b.append("False") #Добавляет элемент в конец списка (нужно указать)
print(b)

print("=================perebor============")
b = [1,"True",2]
for test_perebor in b:
    print(test_perebor)#Перебирает весь список (не одним принтом)

print("=================len(length)============")
b = [1,"True",2]
test_len = len(b) # Говорит длину списка
print(test_len)

print("===============red_el_spiska============")
b = [1,"True",2]
b[2] = 1 # Меняет выбранный элемент списка на выбранное значение
print(b)

print("================our_task=============")#<<<<------ ТЕБЕ СЮДА
b = [4,2,56,5,9]
tot = len(b)
for tot_for_range in range(0,tot):
    print(tot_for_range,b[tot_for_range])
    b[tot_for_range]+=1 #<<<<------ ТЕБЕ СЮДА
print(b)