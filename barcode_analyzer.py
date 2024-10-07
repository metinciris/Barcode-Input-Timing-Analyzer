from pynput import keyboard
import time
import pyautogui
import pyperclip  # Kopyalama için eklenen modül

last_time = time.time()
time_differences = []
barcode_chars = []
all_results = []
threshold = 0.05  # 50ms'den kısa aralıklı girişler barkod olarak kabul edilir
timeout = 1  # 1 saniye boyunca giriş olmazsa aralık değerlendirilmez

def on_press(key):
    global last_time, time_differences, barcode_chars, all_results

    current_time = time.time()
    time_difference = current_time - last_time
    last_time = current_time

    # ESC tuşuna basılınca sonuçları göster
    if key == keyboard.Key.esc:
        if all_results:
            result_summary = "\n".join(all_results) + "\nSonuçlar tamamlandı."
            pyperclip.copy(result_summary)
            pyautogui.hotkey('ctrl', 'v')  # Ctrl+V ile yapıştır
            all_results.clear()
        return False  # Dinlemeyi durdur

    # Zaman farkı threshold altında ve timeout süresi içinde ise barkod girişi kabul et
    if time_difference < timeout:
        try:
            barcode_chars.append(key.char)  # Karakteri ekle
            time_differences.append(round(time_difference * 1000, 2))  # Zaman farkını ms cinsinden ekle
        except AttributeError:
            pass
    else:
        if barcode_chars:  # Barkod tamamlandıysa
            # İstatistikler hesapla
            num_chars = len(barcode_chars)
            if time_differences:
                min_diff = min(time_differences)
                max_diff = max(time_differences)
                avg_diff = round(sum(time_differences) / len(time_differences), 2)
            else:
                min_diff = max_diff = avg_diff = 0

            # Barkod karakterlerini ve zaman farklarını kaydet
            result = f"{num_chars} karakter: " + ' '.join(map(str, time_differences)) + f" ms | Min: {min_diff} ms, Max: {max_diff} ms, Ortalama: {avg_diff} ms"
            all_results.append(result)  # Sonucu kaydet
            
            # Listeyi temizle
            barcode_chars.clear()
            time_differences.clear()

# Tuş basışlarını dinlemek için listener başlat
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
