import requests

API_URL = "http://localhost:8000"

def fetch_sensor_data():
    print(f"Відправка запиту до {API_URL}...\n")
    try:
        response = requests.get(API_URL)
        response.raise_for_status() 
        data = response.json()
        
        print("=== Дані систем автоматизації ===")
        print(f"{'Тег':<10} | {'Тип':<30} | {'Значення':<15} | {'Статус'}")
        print("-" * 75)
        
        for item in data:
            val_str = f"{item['value']} {item['unit']}"
            print(f"{item['tag']:<10} | {item['type']:<30} | {val_str:<15} | {item['status']}")
            
    except requests.exceptions.RequestException as e:
        print(f"Помилка з'єднання з API: {e}")
    except ValueError:
        print("Помилка обробки JSON-відповіді.")

if __name__ == "__main__":
    fetch_sensor_data()