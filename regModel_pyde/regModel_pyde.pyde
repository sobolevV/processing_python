import random, math

class regModel:
    def __init__(self, canvas_size):
        self.w = 0.0
        self.b = 0.5
        self.canvas_size = canvas_size
        self.lr = 0.2
    
    
    def predict(self, x_points):
        """
        Predict 1d array of points (x_i)
        Returns: 1d array (y^)
        """
        predictions = []
        for point_ in x_points:
            predictions.append(self.w*float(point_) + self.b)
        return predictions
    
    
    def predict_one(self, x_point):
        return self.w*float(x_point) + self.b
    
    
    def draw_line(self):
        x1 = 0
        y1 = x1 * self.w + ((1-self.b) * self.canvas_size)
        
        x2 = self.canvas_size
        y2 = x2 * (-self.w) + ((1-self.b) * self.canvas_size)
        stroke(200)
        strokeWeight(3)
        line(x1, y1, x2, y2)
        
    
    def fit(self, x_vals, y_vals):
        common_err = 0
        for i in range(len(x_vals)):
            y_pred = self.predict_one(x_vals[i])
            # err = y_true - y_predicted
            error = y_vals[i] - y_pred
            common_err += abs(error)
            # gradients
            self.w += self.lr*error*(x_vals[i])
            self.b += self.lr*error
        
        print("Error", str(common_err/len(x_vals))[:5])
        
        
    @classmethod
    def mse(cls, y_pred, y_true):
        error = 0
        for i in range(len(y_pred)):
            error += (y_true[i] - y_pred[i])**2
        error /= len(y_pred)
        return error
    
    
    def __str__(self):
        return str(self.w)[:5] + "*X + " + str(self.b)[:5]


# global variables
height = 500
width = 500
x_vals = []
y_vals = []
model = regModel(height)
frame_i = 0

def setup():
    size(height, width)
    frameRate(10)
    
def draw():
    global frame_i
    background(50)
    draw_points(x_vals, y_vals)
    
    # fit model
    if len(x_vals) > 0:
        model.fit(x_vals, y_vals)
    # update model line
    model.draw_line()
    
    
    # saveFrame("frames\\frame_{}.png".format(frame_i))    
    # frame_i += 1
    
def draw_points(x_vals, y_vals):
    for i in range(len(x_vals)):
        fill(200, 0, 250)
        strokeWeight(1)
        circle(int(x_vals[i]*width), int((1 - y_vals[i])*height), 8)

# set point in canvas
def mouseClicked():
    fill(200, 0, 250)
    circle(mouseX, mouseY, 8)
    x_vals.append(float(mouseX)/width)
    y_vals.append(1 - float(mouseY)/height)
