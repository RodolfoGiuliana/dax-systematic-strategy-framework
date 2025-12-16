# Calcolo range giornaliero: Massimi - Minimi
data_dax['Daily_Range'] = data_dax['High'] - data_dax['Low']

plt.figure(figsize=(14, 7))

# Plotting del Range Giornaliero
plt.plot(
    data_dax.index, 
    data_dax['Daily_Range'], 
    label='Escursione Giornaliera (High - Low)', 
    color='orange',
    linewidth=1.5
)

# Personal.
plt.title('Escursione di Prezzo Giornaliera del DAX (^GDAXI)', fontsize=16)
plt.xlabel('Data', fontsize=12)
plt.ylabel('Differenza di Prezzo', fontsize=12)
plt.legend(loc='upper left', fontsize=10)
plt.grid(True, linestyle=':', alpha=0.6)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

print("\nStatistiche del Range Giornaliero:")
print(data_dax['Daily_Range'].describe())
