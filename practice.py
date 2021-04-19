def maskify(cc):
    str_length = len(str)
    masked = str_length - 4
    cc = str[masked:]
    print("#" * masked + cc)


maskify(123213123)
