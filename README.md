# raspi-pir-binary-counter
School project made with a Raspberry Pi for detecting movements from a PIR sensor and showing the amount of movements on connected LEDs in a binary pattern.  

Connect LEDs to GPIO pins: 7, 8, 25, 24, 23, 18, 15, 14.  
Connect PIR sensor to GPIO pin 17.  

Run the following script in projet folder and wave your hand in front of the PIR sensor to see the LEDs change.  
```
python3 main.py
```

Working example:  
![](pir.gif)
