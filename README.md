# pythonMatrixOrbital
Python I2C driver for Matrix Orbital VK204-25 LCD displays
<h2>Usage examples:</h2>
Turning on the display:
  <b>orbitalWrite.on_display(busAddr)</b>
  <br>
Turning off the display:
  <b>orbitalWrite.off_display(busAddr)</b>
  <br>
Display word or words on display:
  <b>orbitalWrite.write_display(busAddr,wordDisp)</b>
  <br>
  <br>
busAddr is the I2C address of the LCD module
wordDisp can be a single word or several

write_display will iterate over each character specified in wordDisp including spaces and send to the LCD to be displayed
