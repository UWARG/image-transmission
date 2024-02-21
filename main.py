"""
Entry point for LTE Communication.
"""
import time

from modules.common.mavlink.modules import flight_controller


MISSION_PLANNER_ADDRESS = "tcp:127.0.0.1:14550"
DELAY_TIME = 1.0  # seconds


def main() -> int:
    """
    Main function for LTE Communication code. Assumes that a mission has already been uploaded to 
    the drone at MISSION_PLANNER_ADDRESS.
    """
    result, controller = flight_controller.FlightController.create(MISSION_PLANNER_ADDRESS)
    if not result:
        print("Failed to create flight controller.")
        return -1

    print("Entering polling loop for drone end of mission.")

    while True:
        result, is_mission_end = controller.is_drone_destination_final_waypoint()

        if not result:
            print("Failed to poll flight controller.")
            continue

        if is_mission_end:
            print("Exiting polling loop.")
            break

        print("Drone's destination is not final waypoint.")

        time.sleep(DELAY_TIME)

    return 0


if __name__ == "__main__":
    result_main = main()
    if result_main < 0:
        print(f"ERROR: Status code: {result_main}")

    print("Done!")
