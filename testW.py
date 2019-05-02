import asyncio
import spheropy

async def main():
    sphero = spheropy.Sphero()
    await sphero.connect(num_retry_attempts=3, use_ble=True)

    original_bluetooth_info = await sphero.get_bluetooth_info()

    print("Original Bluetooth Info:")
    print("Name: {}".format(original_bluetooth_info.name))
    print("Bluetooth Address: {}".format(
        original_bluetooth_info.bluetooth_address))
    print("ID Colors: {}".format(original_bluetooth_info.id_colors))
    print("")

    original_bluetooth_info = await sphero.get_bluetooth_info()

    print("Original Bluetooth Info:")
    print("Name: {}".format(original_bluetooth_info.name))
    print("Bluetooth Address: {}".format(
        original_bluetooth_info.bluetooth_address))
    print("ID Colors: {}".format(original_bluetooth_info.id_colors))
    print("")

    await sphero.roll(127, 0, wait_for_response=False)
    time.sleep(0.5)
    await sphero.roll(127, 90)
    time.sleep(0.5)
    await sphero.roll(127, 180)
    time.sleep(0.5)
    await sphero.roll(127, 270)
    time.sleep(0.5)

    await sphero.roll(16, 0)
    time.sleep(0.5)
    await sphero.roll(255, 180)
    time.sleep(0.5)
    await sphero.roll(0, 0)

if __name__ == "__main__":
  main_loop = asyncio.get_event_loop()
  main_loop.run_until_complete(main())