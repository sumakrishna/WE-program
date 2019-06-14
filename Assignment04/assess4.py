def terminus(start_point, steps) -> (int, int):
    x_cordi, y_cordi = start_point
    #operations_dict = {"N" : y_cordi + i[0] ,"NE": handle_NE() ,"S": 1,"E": 1, "W": 1,"NW": 1,"SE": 1,"SW": 1}
    for i in steps:
        #operations_dict = {"N" : y_cordi + int(i[0]) ,"NE": (y_cordi + int(i[0]),x_cordi + int(i[0])) ,"S": y_cordi - int(i[0]),"E": x_cordi + int(i[0]), "W": x_cordi - int(i[0]),
                           #"NW": (y_cordi + int(i[0]),x_cordi - int(i[0])),"SE": (y_cordi - int(i[0]),x_cordi + int(i[0])),"SW": (y_cordi - int(i[0]), x_cordi - int(i[0]))}
        #operations_dict[i[1:]]
        if i[1:] == "N":
            y_cordi += int(i[0])
        if i[1:] == "S":
            y_cordi -= int(i[0])
        if i[1:] == "NE":
            y_cordi += int(i[0])
            x_cordi += int(i[0])
        if i[1:] == "NW":
            y_cordi += int(i[0])
            x_cordi -= int(i[0])
        if i[1:] == "E":
            x_cordi += int(i[0])
        if i[1:] == "W":
            x_cordi -= int(i[0])
        if i[1:] == "SE":
            y_cordi -= int(i[0])
            x_cordi += int(i[0])
        if i[1:] == "SW":
            y_cordi -= int(i[0])
            x_cordi -= int(i[0])
            
    return (x_cordi, y_cordi)


print(terminus((1,1), ["1N", "3NW"]))
             
