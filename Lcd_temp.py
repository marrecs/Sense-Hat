from sense_hat import SenseHat

sense = SenseHat()

sense.show_message("Edu a vestir-te")



temperature = sense.temperature
sense.show_message("Temperature is %d" % temperature)
sense.show_message("One small step for Pi!", text_colour=[255, 0, 0])

