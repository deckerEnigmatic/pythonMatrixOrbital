# pythonMatrixOrbital
Python I2C driver for Matrix Orbital VK204-25 LCD displays
<h2>Usage examples:</h2>
Turning on the display:
  orbitalWrite.on_display(busAddr)
  <br>
Turning off the display:
  orbitalWrite.off_display(busAddr)
Display word or words on display:
  orbitalWrite.write_display(busAddr,wordDisp)
  
busAddr is the I2C address of the LCD module
wordDisp can be a single word or several

write_display will iterate over each character specified in wordDisp including spaces and send to the LCD to be displayed
