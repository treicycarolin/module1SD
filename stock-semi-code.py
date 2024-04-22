def calculate_pe_ratio(price, earnings_per_share):
  if earnings_per_share == 0:
      return "N/A"
  return price / earnings_per_share

def main():
  # Get prices of stocks
  qualcomm_price = float(input("Enter the price of Qualcomm stock: $"))
  nvidia_price = float(input("Enter the price of Nvidia stock: $"))
  taiwan_semiconductor_price = float(input("Enter the price of Taiwan Semiconductor stock: $"))

  # Assumed earnings per share for demonstration
  qualcomm_eps = 2.46
  nvidia_eps = 0.82
  taiwan_semiconductor_eps = 6.25

  # Calculate PE ratio for each stock
  qualcomm_pe_ratio = calculate_pe_ratio(qualcomm_price, qualcomm_eps)
  nvidia_pe_ratio = calculate_pe_ratio(nvidia_price, nvidia_eps)
  taiwan_semiconductor_pe_ratio = calculate_pe_ratio(taiwan_semiconductor_price, taiwan_semiconductor_eps)

  # Display results
  print("\nStock Prices and PE Ratios:")
  print(f"Qualcomm Price: ${qualcomm_price}, PE Ratio: {qualcomm_pe_ratio}")
  print(f"Nvidia Price: ${nvidia_price}, PE Ratio: {nvidia_pe_ratio}")
  print(f"Taiwan Semiconductor Price: ${taiwan_semiconductor_price}, PE Ratio: {taiwan_semiconductor_pe_ratio}")

if __name__ == "__main__":
  main()
