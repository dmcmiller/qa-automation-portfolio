#Exceptions

# number = 10
# if number > 5:
#     raise Exception(f"The number should not exceed 5. ({number=})")
# print(number)

# Assert

# number = 10
# assert (number < 5), f"The number should not exceed 5. ({number=})"
# print(number)

# try and except block

def linux_interaction():
    import sys
    if "linux" not in sys.platform:
        raise RuntimeError("Function can only run on Linux Systems.")
    print("Doing linux stuff.")

# try:
#     linux_interaction()
# except RuntimeError as error:
#     print(error)
#     print("Linux function wasn't executed")

# ## Another try except example

# try:
#     with open("file.log") as file:
#         read_data = file.read()
# except FileNotFoundError as fnf_error:
#     print(fnf_error)
# ...

# ...


# Use finally clause to run whatever is in its block
try:
    linux_interaction()
except RuntimeError as error:
    print(error)
else:
    try:
        with open("file.log") as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)
finally:
    print("Cleaning up, irrespective of any exceptions.")