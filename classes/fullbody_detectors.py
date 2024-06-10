# Libs
import cv2

class FullBodyDetector:
    def __init__(self, image_path, cascade_path):
        self.image = cv2.imread(image_path)
        self.image_gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.cascade = cv2.CascadeClassifier(cascade_path)

    def __detect__(self):
        faces = self.cascade.detectMultiScale(self.image_gray, 
                                              scaleFactor=1.1, 
                                              #minNeighbors=5, 
                                              minSize=(50, 50))
        return faces
    
    def draw(self):
        for (x, y, w, h) in self.__detect__():
            cv2.rectangle(self.image, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.imshow("Imagem", self.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()