from toolkit import stopwatch, find_input_data, get_points, write_to_output


if __name__ == '__main__':
    with stopwatch(output="output.txt"):
        data = find_input_data("input.txt").split("\n")
        x_center, y_center = map(float, data[1].split())
        radius = int(data[0])

        points = get_points(x_center, y_center, radius)
        write_to_output(str(points), mode='a')
