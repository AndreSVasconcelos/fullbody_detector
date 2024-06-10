from classes.fullbody_detectors import FullBodyDetector

image_path = './images/pessoas.jpg'
cascade_path = './cascades/fullbody.xml'

fullbody_detector = FullBodyDetector(image_path, cascade_path)
fullbody_detector.draw()