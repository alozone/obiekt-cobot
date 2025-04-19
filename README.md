# Aplikacja Detekcji Obiektów z YOLOv8

Prosta aplikacja do detekcji obiektów w czasie rzeczywistym wykorzystująca kamerę oraz model YOLOv8. Aplikacja wyświetla obraz z kamery i zaznacza wykryte obiekty wraz z ich klasami i środkiem obiektu. Posiada także plik z koordynatami, które są dostosowane pod Cobota.

## Wymagania systemowe

- Windows 10 lub nowszy
- Python 3.8 lub nowszy
- Kamera USB (wbudowana lub zewnętrzna)

## Instalacja
1. Przygotowanie środowiska
Otwórz wiersz poleceń (cmd) lub PowerShell jako administrator i wykonaj następujące kroki:
### Utwórz folder dla projektu
mkdir DetektorObiektow
cd DetektorObiektow

### Utwórz wirtualne środowisko Python
python -m venv venv

### Aktywuj wirtualne środowisko
venv\Scripts\activate
2. Instalacja wymaganych bibliotek

- Aktywuj wirtualne środowisko (jeśli jeszcze nie jest aktywne):

```PowerShell
  venv\Scripts\activate
```
- Pobierz wymagane biblioteki
```python
pip install -r requirments.txt
```

*** Instalacja może trochę zająć, ponieważ model yolov8 jest spory, ale posiada wszystkie potrzebne rzeczy. ***

3. Uruchom aplikację:
python main.py

Aplikacja powinna uruchomić się w nowym oknie, wyświetlając obraz z kamery z wykrytymi obiektami.
Aby zakończyć działanie aplikacji, naciśnij klawisz q.

## Ustawianie źródła obrazu
1. W pliku main.py jest ustawione źródło kamery. Jeżeli występuję błąd, należy 
sprawdzić jakie źródło mogłobyć poprawne. (1,2,3)
```python
cap = cv2.videoCapture(source)
```
