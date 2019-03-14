""" 字典取值 """
# -*- coding:utf-8 -*-


def res(d, code):
    result = []
    """
    d.keys表示字典d中所有的项；d.values表示字典d中所有项的值例如
    d={"OrderCode": "1002", "ShipperCode": "SF", "LogisticCode": "118652124588863"}
    d.keys = (['OrderCode', 'ShipperCode', 'LogisticCode'])
    d.values = (['1002', 'SF', '118652124588863'])
    """
    if isinstance(d, dict) and code in d.keys():   # isinstance(d, dict)判断d的类型是否值dict
        value = d[code]
        result.append(value)
        return result
    elif isinstance(d, (list, tuple)):
        for item in d:
            value = res(item, code)
            if value == "None" or value is None:
                pass
            elif len(value) == 0:
                pass
            else:
                result.append(value)
        return result
    else:
        if isinstance(d, dict):
            for k in d:
                value = res(d[k], code)
                if value == "None" or value is None:
                    pass
                elif len(value) == 0:
                    pass
                else:
                    for item in value:
                        result.append(item)
            return result
