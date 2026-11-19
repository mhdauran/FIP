from datetime import datetime
import logging

logging.basicConfig(
    filename="tasks.log",
    level=logging.INFO
)

#logging.info(f"program started: {datetime.now()}")
while True:
    task = input("\nEnter task (or exit): ")

    if task.lower() == "exit":
        break

#for i in range(3):
   # task = input("Enter task: ")
    logging.info(f"{task} - {datetime.now()}")

#print("Task saved!")
print("Tasks saved successfully!")