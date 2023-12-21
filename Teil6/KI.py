print("                                                        ")
print("--------------------------------------------------------")
print("Programmstart (Module laden)")
print("--------------------------------------------------------")

# ------------ 1. Module importieren
from tensorflow import keras

#import keras
from keras.models import Sequential
from keras.layers import Dense
from matplotlib import pyplot as plt
import numpy as np

# ------------ 2. Trainigsdaten & Testdaten laden
#x_train    - Trainigsbilder,   y_train    - Trainigszahlen
#x_test     - Testbilder,       y_test     - Testzahlen
mnist = keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

#Ausgabe der Trainigsbilder (1-10)
for i in range(0,10):
    plt.subplot(2,5,i+1)
    plt.imshow(x_train[i])
    plt.title("TrainData")
    plt.xticks([])
    plt.yticks([])
plt.show()

#Ausgabe der Trainigszahlen (1-10)
print("                                                        ")
print("--------------------------------------------------------")
result = ""
for i in range(0,10):
    result = result + " " + str(y_train[i])
print("Trainingsdaten:\t" + result)
print("--------------------------------------------------------")

#Ausgabe der Testbilder (1-10)
for i in range(0,10):
    plt.subplot(2,5,i+1)
    plt.imshow(x_test[i])
    plt.title("TestData")
    plt.xticks([])
    plt.yticks([])
plt.show()

#Ausgabe der Testzahlen (1-10)
print("                                                        ")
print("--------------------------------------------------------")
result = ""
for i in range(0,10):
    result = result + " " + str(y_test[i])
print("Testdaten:\t\t" + result)
print("--------------------------------------------------------")

#Normalisierung der Daten
x_train     = keras.utils.normalize(x_train, axis=1)
x_test      = keras.utils.normalize(x_test, axis=1)


# ------------ 3. Erstellung und Training des Neuronalen Netzes
model       = Sequential()
model.add(Dense(128, activation='relu'))    # Hidden Layer 1
model.add(Dense(128, activation='relu'))    # Hidden Layer 2
model.add(Dense(10, activation='softmax'))  # Output Layer
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
print("                                                        ")
print("--------------------------------------------------------")
print("Training")
print("--------------------------------------------------------")
model.fit(x_train.reshape(60000, 784), y_train, epochs=3)
print("--------------------------------------------------------")

# ------------ 4. Ermittlung der Genauigkeiten des Neuronalen Netzes
print("                                                        ")
print("--------------------------------------------------------")
print("Genauigkeit")
print("--------------------------------------------------------")
value_loss, value_acc = model.evaluate(x_test.reshape(-1, 784), y_test)
print("                                                        ")
print("Die Genauigkeit der erkannten Bilder:\t%2.4f" % (value_acc))
print("Die Ungenauigkeit der erkannten Bilder:\t%2.4f" % (value_loss))
print("--------------------------------------------------------")


# ------------ 5. Validierung des Ergebnisses des Neuronalen Netzes
print("                                                        ")
print("--------------------------------------------------------")
print("Wahrscheinlichkeiten")
print("--------------------------------------------------------")
predictions = model.predict(x_test.reshape(-1, 784))

#Die Nummer des Testbildes (Anfang bei 0)
verify_number = 8

P1,P2,P3,P4,P5,P6,P7,P8,P9,P10 = predictions[verify_number]
print("Die Wahrscheinlichkeit fuer die Zahl 0 lautet: %2.2f" % (P1*100))
print("Die Wahrscheinlichkeit fuer die Zahl 1 lautet: %2.2f" % (P2*100))
print("Die Wahrscheinlichkeit fuer die Zahl 2 lautet: %2.2f" % (P3*100))
print("Die Wahrscheinlichkeit fuer die Zahl 3 lautet: %2.2f" % (P4*100))
print("Die Wahrscheinlichkeit fuer die Zahl 4 lautet: %2.2f" % (P5*100))
print("Die Wahrscheinlichkeit fuer die Zahl 5 lautet: %2.2f" % (P6*100))
print("Die Wahrscheinlichkeit fuer die Zahl 6 lautet: %2.2f" % (P7*100))
print("Die Wahrscheinlichkeit fuer die Zahl 7 lautet: %2.2f" % (P8*100))
print("Die Wahrscheinlichkeit fuer die Zahl 8 lautet: %2.2f" % (P9*100))
print("Die Wahrscheinlichkeit fuer die Zahl 9 lautet: %2.2f" % (P10*100))
print("--------------------------------------------------------")
#print(predictions[verify_number])

print("                                                        ")
print("--------------------------------------------------------")
print("Das Ergebnis:")
print("--------------------------------------------------------")

pred_list   = predictions[verify_number]

max_value   = np.argmax(pred_list)
print("Die gefundene Zahl lautet: " + str(max_value)+ " (siehe Bild)")
plt.imshow(x_test[verify_number])
plt.show()
plt.title("ausgewaehltes Bild")
print("--------------------------------------------------------")

print("                                                        ")
print("--------------------------------------------------------")
print("Programmende")
print("--------------------------------------------------------")
