import json

company_dict = {}
average_profit = 0
profit_companies = 0

with open("text7.txt", encoding="utf-8") as f_obj:
    for line in f_obj:
        split_line = line.split()
        profit = int(split_line[2]) - int(split_line[3])
        company_dict.update({split_line[0]: profit})
        if profit > 0:
            average_profit += profit
            profit_companies += 1

company_list = [company_dict, {"average_profit": average_profit / profit_companies}]

with open("text7.json", "w", encoding="utf8") as json_file:
    json.dump(company_list, json_file, ensure_ascii=False, sort_keys=True, indent=4)
