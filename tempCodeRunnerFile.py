        next(iterdata)
        for (columnName, columnData) in iterdata:
            key = "ln" + str(item)
            data[key].append(float(columnData[count]))
            lines[key].set_data(xdata, data[key])
            item+=1

        count+=1