def table(rows, cols):
    print("<table>")
    counter = 1
    for i in range(rows):
        print(f"<tr> linha: {i}")

        for _ in range(cols):
            print(f"<td> {counter} </td>")
            counter += 1
        print("</tr>")
    print("</table>")

table(2, 2)
