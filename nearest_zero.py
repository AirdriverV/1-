def nearest_zero(List_Number_home):
    array_Number_home = List_Number_home.split(" ") #преобразуем списка в массив
    array_distance = [0] * len(array_Number_home) #устанавливаем длинну массива расстояний от пустого участка до дома
        
    for number in range(len(array_Number_home)): #перебираем все участки с домами по порядку
        if int(array_Number_home[number]) == 0: #Если номер дома 0 (свободный участок)                   
            array_distance[number] = 0 	#То записываем растояние 0
            step = 0 #обнуляем счетчик расстояния        
            step_back = 0 #обнуляем счетчик обратного расстояния
            for number_back in range(number,0,-1): #заполняем расстояние от 0 в обратном порядке
                step_back += 1                
                if array_distance[number_back-1] > step_back: #если растояние от 0 меньше, чем ранее записанное
                    array_distance[number_back-1] = step_back #то переписываем значение на меньшее
                else:
                    break #если расстояние равно или больше предыдущего завершаем цикл      
                
        else: #если участок не свободен
            step += 1 #увеличиваем расстояние от 0 на 1 шаг
            array_distance[number] = step #записываем расстояние от 0 в массив
            
     
    List_distance = ' '.join(map(str, array_distance))  # преобразуем массив с расстояниями до домов в сторку через пробел
    return List_distance

List_Number_home = "0 55 55 33 55 22 33 33 0 44 55 44 0 44 55 44 33 66 66 0 0 55 33" #список номеров домов
print("Вход: \n", List_Number_home) # выводим списк номеров домов
print ("Выход: \n", nearest_zero (List_Number_home)) #выводим расстояния от свободных участков до домов
