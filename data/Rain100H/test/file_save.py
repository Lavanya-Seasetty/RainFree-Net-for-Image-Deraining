import os 

# Define directories
data_dir = r"C:\Users\nandi\Downloads\DSDNet-main\DSDNet-main\data\Rain100H\test"
rain_dir = os.path.join(data_dir, "rain")
norain_dir = os.path.join(data_dir, "norain")

# Define text file paths
train_rain_txt = os.path.join(data_dir, "test_rain.txt")  # Updated variable name
train_norain_txt = os.path.join(data_dir, "test_norain.txt")  # Updated variable name

# Function to save only filenames in text file
def save_filenames(folder_path, txt_path):
    filenames = sorted(f for f in os.listdir(folder_path) if f.endswith(".png"))
    with open(txt_path, "w") as f:
        for filename in filenames:
            f.write(f"{filename}\n")

# Generate lists
save_filenames(rain_dir, train_rain_txt)
save_filenames(norain_dir, train_norain_txt)

print("test_rain.txt and test_norain.txt updated successfully!")
