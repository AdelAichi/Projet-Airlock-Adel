from bleak import BleakClient

def envoyer_message_bluetooth(message):
    try:
        address = "XX:XX:XX:XX:XX:XX"  # Adresse MAC du périphérique Bluetooth
        async with BleakClient(address) as client:
            await client.write_gatt_char("UUID_CHARACTERISTIC", message.encode())
        print(f"Message envoyé via Bluetooth : {message}")
    except Exception as e:
        print(f"Erreur lors de la communication Bluetooth : {e}")
