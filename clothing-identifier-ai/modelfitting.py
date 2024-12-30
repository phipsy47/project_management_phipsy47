import tensorflow as tf

class modelfitter:
    def __init__(self):
        self.class_names = None
        self.predictions = None
        self.test_loss = None
        self.test_labels = None
        self.test_images = None
        self.train_labels = None
        self.train_images = None
        self.probability_model = None
        
    def initFit(self):
        self.class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
        fashion_mnist = tf.keras.datasets.fashion_mnist

        (self.train_images, self.train_labels), (self.test_images, self.test_labels) = fashion_mnist.load_data()

        self.train_images = self.train_images / 255.0
        self.test_images = self.test_images / 255.0   
        
        model = tf.keras.Sequential()
        model.add(tf.keras.layers.Flatten(input_shape=(28, 28)))
        model.add(tf.keras.layers.Dense(128, activation='relu'))
        model.add(tf.keras.layers.Dense(10))

        model.compile(optimizer='adam',
                loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
                metrics=['accuracy'])

        model.fit(self.train_images, self.train_labels, epochs=10)

        self.test_loss, test_acc = model.evaluate(self.test_images,  self.test_labels, verbose=2)

        print('\nTest accuracy:', test_acc)

        self.probability_model = tf.keras.Sequential([model, 
                                            tf.keras.layers.Softmax()])

        self.predictions = self.probability_model.predict(self.test_images)
        