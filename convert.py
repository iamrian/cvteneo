import pandas as pd

# Ganti ini dengan nama file Excel kamu
df = pd.read_excel("data.xlsx")

# Simpan hasil ke file .txt
with open("output.txt", "w", encoding="utf-8") as f:
    for _, row in df.iterrows():
        line = f"{row['Email']}|{row['Password']}"
        f.write(line + "\n")

print("✅ Sukses convert ke 'output.txt'!")
