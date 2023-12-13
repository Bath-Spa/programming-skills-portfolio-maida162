respnose_code=201
match response_code:
    case 200:
        print("Ok")
    case 201:
        print("Created")
    case 300:
        print("Multiple choices")
