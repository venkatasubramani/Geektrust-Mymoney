import pandas as pd


class Mymoney:
    def __init__(self, equity, debt, gold):
        # print('inside constructor')
        self.equity = equity
        self.debt = debt
        self.gold = gold
        self.sip_equity = 0
        self.sip_debt = 0
        self.sip_gold = 0
        self.equity_alloc = equity * 100 / (equity + debt + gold)
        self.debt_alloc = debt * 100 / (equity + debt + gold)
        self.gold_alloc = gold * 100 / (equity + debt + gold)
        self.money_df = pd.DataFrame(columns=['equity', 'debt', 'gold', 'month', 'total'])

    def sip(self, sip_equity, sip_debt, sip_gold):
        # print('inside sip')
        self.sip_equity = sip_equity
        self.sip_debt = sip_debt
        self.sip_gold = sip_gold

    def change(self, equity_percent, debt_percent, gold_percent, month, month_count):
        # print('inside change')
        if month_count == 0:
            self.equity = int(self.equity * (1 + equity_percent/100))
            self.debt = int(self.debt * (1 + debt_percent / 100))
            self.gold = int(self.gold * (1 + gold_percent/100))
        else:
            self.equity = int((self.equity + self.sip_equity) * (1 + equity_percent/100))
            self.debt = int((self.debt + self.sip_debt) * (1 + debt_percent/100))
            self.gold = int((self.gold + self.sip_gold) * (1 + gold_percent/100))
        total = self.equity + self.debt + self.gold
        self.money_df = self.money_df.append(pd.DataFrame([[self.equity, self.debt, self.gold, month, total]],
                                                          columns=['equity', 'debt', 'gold', 'month', 'total']))
        if month == "JUNE\n" or month == "DECEMBER\n":
            self.money_df = self.money_df.append(pd.DataFrame([[int(self.equity_alloc * total / 100),
                                                                int(self.debt_alloc * total / 100),
                                                                int(self.gold_alloc * total / 100),
                                                                'REBALANCE', total]],
                                                              columns=['equity', 'debt', 'gold', 'month', 'total']))

        # print(self.money_df)

    def balance(self, month):
        res = self.money_df[self.money_df['month'] == month].tail(1)
        result = res['equity'].astype(str)[0] + ' ' + res['debt'].astype(str)[0] + ' '+ res['gold'].astype(str)[0]
        print(result)

    def rebalance(self):
        results = self.money_df[self.money_df['month'] == "REBALANCE"].copy(deep=True)
        if len(results)>0:
            results['output'] = results['equity'].astype(str) + ' ' + results['debt'].astype(str) + ' ' + results['gold'].astype(str)
            res = results['output'].to_list()
            for r in res:
                print(r)
        else:
            print('CANNOT_REBALANCE')
