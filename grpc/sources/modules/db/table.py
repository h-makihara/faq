import prettytable

def tableCreate(result):
    print("in table create")
    table = prettytable.PrettyTable(["Name", "Value", "type"])

    for index in range(len(result)):
        # for logs to prettytable
        table.add_row(
                [
                    "QID",
                    int(result[index].get('QID')),
                    type(int(result[index].get('QID')))
                    ]
                )
        table.add_row(
                [
                    "category",
                    result[index].get('category'),
                    type(result[index].get('category'))
                    ]
                )
        table.add_row(
                [
                    "scope",
                    result[index].get('scope'),
                    type(result[index].get('scope'))
                    ]
                )
        table.add_row(
                [
                    "service_name",
                    result[index].get('service'),
                    type(result[index].get('service'))
                    ]
                )
        table.add_row(
                [
                    "question",
                    result[index].get('question'),
                    type(result[index].get('question'))
                    ]
                )
        table.add_row(
                [
                    "answer",
                    result[index].get('answer'),
                    type(result[index].get('answer'))
                    ]
                )
        for tagNum in range(len(result[index].get('tag'))):
            table.add_row(
                    [
                        "tag",
                        result[index].get('tag')[tagNum],
                        type(result[index].get('tag')[tagNum])
                        ]
                    )

    print("response data\n%s" % table)
