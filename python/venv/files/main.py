import datetime as dt

format = '%H:%M:%S'
hoursToWork = '08:30:00'
normalExit = '17:30:00'

startTime = ''
startMealTime = ''
endMealTime = ''

beforeMealtime = ''
leftHours2Work = ''
timeendMeal = ''

# Add final zeros to the string of type HH:MM
def addfinalzeros(toadd):
    toadd += ':00'
    return toadd

# User set time of end of the meal
# Returns exit time
def substract():
    print('Enter end meal time')
    endMealTime = input()
    endMealTime = addfinalzeros(endMealTime)
    time_zero = dt.datetime.strptime('00:00:00', '%H:%M:%S')
    exitTime = (dt.datetime.strptime(endMealTime, format) - time_zero + dt.datetime.strptime(str(leftHours2Work), format)).time()
    print(f'For achive target of {hoursToWork} working, you should leave at {exitTime}')
    print(' | Press enter key for exit... |')
    input()

# Script calculates time worked between init time of work and meal start time, and suggests the meal end time
def calculateForSoonExit():
    global beforeMealtime, leftHours2Work
    beforeMealtime = dt.datetime.strptime(startMealTime, format) - dt.datetime.strptime(startTime, format)
    leftHours2Work = dt.datetime.strptime(hoursToWork, format) - dt.datetime.strptime(str(beforeMealtime), format)
    timeendlaunch = dt.datetime.strptime(normalExit, format) - dt.datetime.strptime(str(leftHours2Work), format)
    print(f'You should finish meal at {timeendlaunch} for leaving at {normalExit}')
    print('-------')
    substract()

# User enters entry time and meal start time
def setInitHours():
    global startTime, startMealTime
    print('-------')
    print('Enter entry time')
    startTime = input()
    print('Enter meal start time')
    startMealTime = input()
    startTime = addfinalzeros(startTime)
    startMealTime = addfinalzeros(startMealTime)
    calculateForSoonExit()

# Always on final
# Init method
if __name__ == '__main__':
    print('Hello Oscar! Let\'s calculate when are you leaving today...')
    print('REMEMBER!: Inputs have to be typed in format HH:MM')
    setInitHours()




