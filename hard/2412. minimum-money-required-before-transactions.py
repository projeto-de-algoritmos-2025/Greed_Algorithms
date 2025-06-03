class Solution:
    def minimumMoney(self, transactions: List[List[int]]) -> int:
        # total_loss: acumula a soma das perdas com custo > cashback
        total_loss = 0
        # max_cashback_loss: rastreia maior perda com transações custo > cashback
        max_cashback_loss = 0
        # max_cost_gain: rastreia maior perda com transaçoes cashback > custo
        max_cost_gain = 0
        
        for cost, cashback in transactions:
            if cost > cashback:
                # perda total
                total_loss += cost - cashback
                # atualiza o maior cashback encontrado nas transações com perda de dinheiro
                if cashback > max_cashback_loss:
                    max_cashback_loss = cashback
            else:
                if cost > max_cost_gain:
                    max_cost_gain = cost
        # calculo:
        # 1. perda total acumulada das transações com perda (total_loss)
        # 2. o maior valor entre:
        #    - maior cashback das transações (max_cashback_loss)
        #    - Mmior custo das transações (max_cost_gain)
        return total_loss + max(max_cashback_loss, max_cost_gain)