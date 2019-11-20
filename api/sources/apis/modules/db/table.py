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
                    "share",
                    int(result[index].get('share')),
                    type(int(result[index].get('share')))
                    ]
                )
        table.add_row(
                [
                    "s_name",
                    result[index].get('service'),
                    type(result[index].get('service'))
                    ]
                )
        table.add_row(
                [
                    "lang",
                    result[index].get('lang'),
                    type(result[index].get('lang'))
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
    print("response data\n%s" % table)
