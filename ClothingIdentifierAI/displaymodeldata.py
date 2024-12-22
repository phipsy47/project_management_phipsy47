import numpy as np
import matplotlib.pyplot as plt

def plot_image(mod, i, predictions_array, true_label, img):
    true_label, img = true_label[i], img[i]
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])

    plt.imshow(img, cmap=plt.cm.binary)

    predicted_label = np.argmax(predictions_array)
    if predicted_label == true_label:
        color = 'blue'
    else:
        color = 'red'

    plt.xlabel("{} {:2.0f}% ({})".format(mod.class_names[predicted_label],
                                100*np.max(predictions_array),
                                mod.class_names[true_label]),
                                color=color)

def plot_value_array(i, predictions_array, true_label):
    true_label = true_label[i]
    plt.grid(False)
    plt.xticks(range(10))
    plt.yticks([])
    thisplot = plt.bar(range(10), predictions_array, color="#777777")
    plt.ylim([0, 1])
    predicted_label = np.argmax(predictions_array)

    thisplot[predicted_label].set_color('red')
    thisplot[true_label].set_color('blue')
 
def visualizeExamples(mod):   
    i = 0
    plt.figure(figsize=(6,3))
    plt.subplot(1,2,1)
    plot_image(mod, i, mod.predictions[i], mod.test_labels, mod.test_images)
    plt.subplot(1,2,2)
    plot_value_array(i, mod.predictions[i],  mod.test_labels)
    plt.show()

    i = 12
    plt.figure(figsize=(6,3))
    plt.subplot(1,2,1)
    plot_image(mod, i, mod.predictions[i], mod.test_labels, mod.test_images)
    plt.subplot(1,2,2)
    plot_value_array(i, mod.predictions[i],  mod.test_labels)
    plt.show()

    num_rows = 5
    num_cols = 3
    num_images = num_rows*num_cols
    plt.figure(figsize=(2*2*num_cols, 2*num_rows))
    for i in range(num_images):
        plt.subplot(num_rows, 2*num_cols, 2*i+1)
        plot_image(mod, i, mod.predictions[i], mod.test_labels, mod.test_images)
        plt.subplot(num_rows, 2*num_cols, 2*i+2)
        plot_value_array(i, mod.predictions[i], mod.test_labels)
    plt.tight_layout()
    plt.show()