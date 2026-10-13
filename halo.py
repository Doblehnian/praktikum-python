from colorama import Fore, Style, init

# Inisialisasi colorama
init(autoreset=True)


def main():
  print(Fore.CYAN + "========================================")
  print(Fore.CYAN + "   PROGRAM PERKIRAAN USIA - PYTHON")
  print(Fore.CYAN + "========================================")

  nama = input("Masukkan nama Anda: ")
  print(f"Halo, {nama}!")

  # Tantangan: try/except untuk input bukan angka
  while True:
    try:
      tahun_lahir = int(
          input(Fore.YELLOW + "Masukkan tahun lahir Anda (contoh: 2005): ")
      )
      tahun_sekarang = 2026  # Tahun saat ini

      if tahun_lahir > tahun_sekarang or tahun_lahir < 1900:
        print(Fore.RED + "Tahun lahir tidak valid. Silakan masukkan dengan benar.")
        continue

      usia = tahun_sekarang - tahun_lahir
      print(
          Fore.GREEN
          + f"Berhasil! Halo {nama}, perkiraan usia Anda adalah {usia} tahun"
          f" pada tahun 2026."
      )
      break
    except ValueError:
      print(
          Fore.RED
          + "Error: Input yang Anda masukkan bukan angka! Harap masukkan tahun"
          " dalam format angka."
      )


if __name__ == "__main__":
  main()