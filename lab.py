class BMI:
    def __init__(self, weight, height):
        self._weight = weight
        self._height = height
    
    @property
    def weight(self):
        return self._weight
    
    @property
    def height(self):
        return self._height
    
    def BMI_Value(self):
        return self._weight / (self._height ** 2)
    
    def __eq__(self, other):
        if isinstance(other, BMI):
            return self._weight == other.weight and self._height == other.height
        return False
# Creating BMI objects
person1 = BMI(70, 1.75)  # weight in kilograms, height in meters
person2 = BMI(65, 1.70)

# Getting BMI values
bmi1 = person1.BMI_Value()
bmi2 = person2.BMI_Value()

print("BMI of person 1:", bmi1)
print("BMI of person 2:", bmi2)

# Comparing two BMI objects
print("Are the two persons equal in weight and height?", person1 == person2)
