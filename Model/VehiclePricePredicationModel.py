import pandas as pd
import pickle
from sklearn.ensemble import RandomForestRegressor

vehicle_data = pd.read_csv('vehicleDatasetFinal.csv')

# Remove the rows that contain missing values
vehicle_data = vehicle_data.dropna(how='any', axis=0)

# Dependant variables
features = ['Make', 'Model', 'Year', 'Transmission', 'FuelType', 'EngineCapacity', 'Mileage']
X = vehicle_data[features]

# Target variable
y = vehicle_data.Price


# Converting categorical to numerical data
def encode_make(make):
    make_dict = {
        "Audi": 1,
        "Austin": 2,
        "BMW": 3,
        "Chery": 4,
        "Chevrolet": 5,
        "Chrysler": 6,
        "Daihatsu": 7,
        "Datsun": 8,
        "DFSK": 9,
        "Ford": 10,
        "Honda": 11,
        "Hyundai": 12,
        "Isuzu": 13,
        "Jaguar": 14,
        "Kia": 15,
        "Land Rover": 16,
        "Mahindra": 17,
        "Maruti Suzuki": 18,
        "Mazda": 19,
        "Mercedes Benz": 20,
        "MG": 21,
        "Micro": 22,
        "Mini": 23,
        "Mitsubishi": 24,
        "Morris": 25,
        "Nissan": 26,
        "Perodua": 27,
        "Peugeot": 28,
        "Renault": 29,
        "Ssang Yong": 30,
        "Subaru": 31,
        "Suzuki": 32,
        "Tata": 33,
        "Toyota": 34,
        "Volkswagen": 35,
        "Zotye": 36
    }
    return make_dict[make]


def encode_model(model_name):
    model_dict = {
        "3": 1,
        "300": 2,
        "406": 3,
        "800": 4,
        "318i": 5,
        "320d": 6,
        "4DR": 7,
        "520d": 8,
        "740Le": 9,
        "A-Star": 10,
        "A1": 11,
        "A3": 12,
        "A4": 13,
        "A6": 14,
        "Accent": 15,
        "Accord": 16,
        "Actyon": 17,
        "AD Wagon": 18,
        "Allion": 19,
        "Alto": 20,
        "Aqua": 21,
        "Avanza": 22,
        "Axela": 23,
        "Axia": 24,
        "Axio": 25,
        "BAIC": 26,
        "Baleno": 27,
        "Beetle": 28,
        "Belta": 29,
        "Bezza": 30,
        "Bighorn": 31,
        "Bluebird": 32,
        "Bolero": 33,
        "C180": 34,
        "C200": 35,
        "Camry": 36,
        "Carina": 37,
        "Cefiro": 38,
        "Celerio": 39,
        "Charade": 40,
        "CHR": 41,
        "City": 42,
        "Civic": 43,
        "CLA 180": 44,
        "Cooper": 45,
        "Copen": 46,
        "Corolla": 47,
        "Corona": 48,
        "Corsa": 49,
        "Crown": 50,
        "Cruze": 51,
        "CRV": 52,
        "CRZ": 53,
        "Dayz": 54,
        "Defender": 55,
        "Demio": 56,
        "Discovery": 57,
        "Dutsun": 58,
        "E200": 59,
        "E220": 60,
        "E300": 61,
        "E350": 62,
        "Elantra": 63,
        "Eon": 64,
        "Escudo": 65,
        "Esquire": 66,
        "Estilo": 67,
        "Familia": 68,
        "Fit": 69,
        "Fit Aria": 70,
        "Fit Shuttle": 71,
        "Flair": 72,
        "Fortuner": 73,
        "Freed": 74,
        "Freelander": 75,
        "Geely": 76,
        "Gemini": 77,
        "Glory": 78,
        "Grace": 79,
        "Grand Vitara": 80,
        "Harrier": 81,
        "Hilux": 82,
        "Hustler": 83,
        "Indica": 84,
        "Indigo": 85,
        "Insight": 86,
        "IST": 87,
        "Kelisa": 88,
        "KWID": 89,
        "Kyron": 90,
        "L200": 91,
        "Lancer": 92,
        "Land Cruiser Prado": 93,
        "Land Cruiser Sahara": 94,
        "Laser": 95,
        "March": 96,
        "Mark": 97,
        "Maruti": 98,
        "Mini Cooper": 99,
        "Minor": 100,
        "Mira": 101,
        "Montero": 102,
        "MX 7": 103,
        "N-WGN": 104,
        "Nano": 105,
        "Navara": 106,
        "Nomad": 107,
        "Outlander": 108,
        "Pajero": 109,
        "Panda": 110,
        "Panda Cross": 111,
        "Passo": 112,
        "Patrol": 113,
        "Picanto": 114,
        "Premio": 115,
        "Presea": 116,
        "Primera": 117,
        "Prius": 118,
        "Pulsar": 119,
        "Q2": 120,
        "Q7": 121,
        "QQ": 122,
        "Range Rover": 123,
        "Range Rover Sport": 124,
        "RAV4": 125,
        "Redi Go": 126,
        "Rexton": 127,
        "Rio": 128,
        "Rush": 129,
        "RX": 130,
        "S300": 131,
        "SAI": 132,
        "Santa Fe": 133,
        "Soluna": 134,
        "Sonata": 135,
        "Sorento": 136,
        "Spacia": 137,
        "Sportage": 138,
        "Sprinter": 139,
        "Starlet": 140,
        "Sunny": 141,
        "Swift": 142,
        "Sylphy": 143,
        "Tank": 144,
        "Tercel": 145,
        "Terios": 146,
        "Tiida": 147,
        "Tivoli": 148,
        "Trend": 149,
        "Tucson": 150,
        "Vezel": 151,
        "Vios": 152,
        "Vitz": 153,
        "Viva Elite": 154,
        "Wagon R": 155,
        "Wagon R FX": 156,
        "Wagon R FZ": 157,
        "Wagon R Stingray": 158,
        "Wigo": 159,
        "Wingroad": 160,
        "X-Trail": 161,
        "X-Type": 162,
        "X1": 163,
        "X3": 164,
        "Xenon": 165,
        "XV": 166,
        "Yaris": 167,
        "Zen": 168,
        "ZS": 169
    }

    return model_dict[model_name]


def encode_transmission(transmission):
    transmission_dict = {
        'Automatic': 1, 'Manual': 2
    }
    return transmission_dict[transmission]


def encode_fuel_type(fuel_type):
    fuel_type_dict = {
        "Petrol": 1,
        "Diesel": 2
    }
    return fuel_type_dict[fuel_type]


X['Make'] = X['Make'].apply(lambda x: encode_make(x))
X['Model'] = X['Model'].apply(lambda x: encode_model(x))
X['Transmission'] = X['Transmission'].apply(lambda x: encode_transmission(x))
X['FuelType'] = X['FuelType'].apply(lambda x: encode_fuel_type(x))

print(X)

rf_model = RandomForestRegressor(max_depth=7, random_state=1)
rf_model.fit(X, y)

pickle.dump(rf_model, open('model.pkl', 'wb'))
model = pickle.load(open('model.pkl', 'rb'))


print(model.predict([[25, 141, 1984, 1, 7, 1400, 100000]]))
