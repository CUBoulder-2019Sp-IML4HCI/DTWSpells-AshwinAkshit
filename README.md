# DTWSpells-AshwinAkshit 
Harry Potter Spells 🧙🏼‍ 🎩

## Ashwin Sankaralingam, Akshit Arora
---

### Sensors used : Two microbits 
- Wand Microbit : 
    * Send accelerometer reading via bluetooth.
    * Display the icon on LED based on received signals.
- Laptop Microbit : 
    * Send received signals via serial port to Wekinator (pyscript).
    * Send classified prediction (spell) to display in wand.


### Feature Extraction: 
Just stream accelerometer readings speedup using Ben's hack.
#### Feature Engineering: Using totally varied gestures (❤️,🐍,💀)

### ML block:
We used DTW for training our examples over three classes. In order to avoid confusion, all the three gestures have a varied start point, involves different motion and direction.

### Experiments:
We tested out two versions of DTW:
1) Matches computed only after running stops :  Even though this method did really well, it was painful to stop and start the running everytime at the end of the spell. 
2) Matches computed continuously while running: This started to working better when we started to play with the thresholds and find optimal values through stochastic testing.

### Improvements we could have made:
1) Insted of sending x,y,z (accelerometer) reading continuously, we could have done something like dx,dy,dz and found some interesting patterns.


### Github link : https://github.com/CUBoulder-2019Sp-IML4HCI/DTWSpells-AshwinAkshit


### Youtube link : https://www.youtube.com/watch?v=sT3Nnmz4WO4&feature=youtu.be
