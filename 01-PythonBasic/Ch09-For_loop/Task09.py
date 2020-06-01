from datetime import date


def get_constellation(birthday: date):
    """
    根據使用者給的生日，回傳對應的星座。
    ex get_constellation(date(month=10,day=20)) "天秤座"
    """

    return ""


def get_constellations(birthdays: list) -> []:
    """
    傳入一組生日清單，每個生日都是date 物件。
    ex [date(2000, 10, 20), date(2000, 3, 20)]
    要回傳多個對應的星座 ex ["天秤座", "雙魚座"]
    Hint:試著先用 for-loop印出每個生日
    """
    result = ["天秤座", "雙魚座"]
    return result
