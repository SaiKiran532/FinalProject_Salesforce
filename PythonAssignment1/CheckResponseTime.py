import time


def time_simulation():
    time.sleep(5)


def check_response_time():
    execution_start_time = time.time()
    time_simulation()
    execution_end_time = time.time()

    overall_execution_time = execution_end_time - execution_start_time
    print(f"Overall Execution Time: {overall_execution_time} seconds")

    if overall_execution_time <= 4:
        print("Function executed within the performance requirement.")
    else:
        print("Function exceeded the performance requirement.")


check_response_time()
