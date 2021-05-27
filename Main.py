from threading import Thread
import inputs
import calculation
import motor

dire, dist = inputs.input_()

M1 = Thread(target=motor.motorR(calculation.distance(dist), calculation.direction(dire)))
M2 = Thread(target=motor.motorR(calculation.distance(dist), calculation.direction(dire)))

M1.start()
M2.start()
