def error_msg(s):
    print("error: " + s)
    exit()
kata = (0, 4, 132.42222, 10000, 12345.67)


if __name__ == "__main__":
    if (type(kata) != tuple):
        error_msg("argument error")

    if (len(kata) != 5):
        error_msg("too much params in tuple")

    if (type(kata[0]) != int or type(kata[1]) != int):
        error_msg("first arguments arent integers")
    if (len(str(kata[0])) > 2 or len(str(kata[1])) > 2):
         error_msg("first arguments must have 1 or 2 digits at max")
    if (type(kata[2]) != float):
        error_msg("3rd argument isnt a float")
    if (type(kata[3]) != int):
        error_msg("4th argument isnt a int")
    if (type(kata[4]) != float):
        error_msg("5th argument isnt a float")

    s = "module_{:02d}, ex{:02d} : {:.2f}, {:.2E}, {:.2E}".format(kata[0], kata[1], kata[2], kata[3], kata[4])
    print(s)
