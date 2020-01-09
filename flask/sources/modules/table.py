import prettytable

# client側では、既にgRPCを通ったあとの class だからデータのとり方が違う
def tableCreate(result, num):
    table = prettytable.PrettyTable(["Name", "Value", "type"])

    # for logs to prettytable
    table.add_row(
            [
                "QID",
                int(result.QID),
                type(int(result.QID))
                ]
            )
    table.add_row(
            [
                "category",
                result.category,
                type(result.category)
                ]
            )
    table.add_row(
            [
                "scope",
                result.scope,
                type(result.scope)
                ]
            )
    table.add_row(
            [
                "service_name",
                result.service_name,
                type(result.service_name)
                ]
            )
    table.add_row(
            [
                "question",
                result.question,
                type(result.question)
                ]
            )
    table.add_row(
            [
                "answer",
                result.answer,
                type(result.answer)
                ]
            )
    for tagNum in range(len(result.tag)):
        table.add_row(
                [
                    "tag",
                    result.tag[tagNum],
                    type(result.tag[tagNum])
                    ]
                )
    print("number : %d FAQ\n%s" % (num,table) )
