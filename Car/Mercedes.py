#Car need Acceleration Decceleration,Maximum mph, Tank available, Wheel Type,  Car Model, Seats_Available, Car Type, Car Model, Driver, Driver Requirements, Is Car on/off, Car Speed

# def Access_Panel(Code):
#     Cars_In_The_Nutshell = [{'Model': GL550, 
#                             'Tank_Available':300, 
#                             'Wheel_Type': "Michellin", 
#                             'Seat_Available': 7, 
#                             'Car_Type': "Mercedes" 
#                             'Car_Engine_On_Or_Off':False 
#                             'Maximum_Car_Speed' : 100
#                             'Acceleration': 100
#                             'Deceleration': 500}]
#     if Code == 12345:
#         return Cars_In_The_Nutshell
#     else:
#         return None


Car = {
    'Model': 'GL550',
    'Tank_Available': 300, 
    'Wheel_Type': 'Michellin',
    'Car_Color':'Black'
    'Seat_Available': 7,
    'Car_Engine_On_Or_Off': False,
    'Acceleration': 100
    'Minumum_Car_Speed': 0
    'Maximum_Car_Speed':260
    'Current_Car_Speed': 0
}

def Engine_On(Option):
    if Option == "On":
        Car['Car_Engine_On_Or_Off'] = True
        #True is On
    if Option == "Off":
        Car['Car_Engine_On_Or_Off'] = False
        #False is Off
    return Car['Car_Engine_On_Or_Off']

def Speeding_Up(Time):
    if Car['Car_Engine_On_Or_Off'] == True:
        Car['Current_Car_Speed'] = Car['Current_Car_Speed'] + Car['Acceleration'] * Time

        




        
