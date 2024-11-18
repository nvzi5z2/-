import pandas as pd
import os

def load_fund_data(folder_path, funds):
    """
    从文件夹中加载指定的基金数据。

    参数:
    - folder_path: 包含Excel文件的文件夹路径。
    - funds: 要加载的基金名称列表。

    返回:
    - fund_navs: 包含DataFrame的字典，每个DataFrame都有日期索引和'nav'列。
    """
    fund_navs = {}
    for fund in funds:
        file_path = os.path.join(folder_path, f"{fund}.xlsx")
        if os.path.exists(file_path):
            df = pd.read_excel(file_path, header=0, parse_dates=[0], names=['date', 'nav'])
            df = df[pd.to_numeric(df['nav'], errors='coerce').notnull()]  # 过滤掉非数值数据
            df['nav'] = df['nav'].astype(float)
            df.set_index('date', inplace=True)
            fund_navs[fund] = df
        else:
            print(f"警告: {fund}.xlsx 不存在于文件夹中。")
    return fund_navs

def calculate_portfolio_value(fund_navs, weights, full_dates, initial_investment):
    """
    计算组合净值。

    参数:
    - fund_navs: 包含DataFrame的字典，每个DataFrame都有日期索引和'nav'列。
    - weights: 每个基金的权重字典。
    - full_dates: 基金的完整日期范围。
    - initial_investment: 初始投资金额。
    
    返回:
    - portfolio_values: 包含'portfolio_value'列的DataFrame。
    """
    portfolio_values = pd.DataFrame(index=full_dates, columns=['portfolio_value'])
    portfolio_values['portfolio_value'] = 0.0

    for fund, nav_df in fund_navs.items():
        # 获取基金的初始净值和起始日期
        initial_nav = nav_df.iloc[0]['nav']
        initial_date = nav_df.index[0]
        shares = (initial_investment * weights[fund]) / initial_nav
        
        # 计算每个基金的净值，并对没有数据的日期视为现金
        nav_df = nav_df.reindex(full_dates, method='ffill').fillna(0)
        nav_df.loc[:initial_date, 'nav'] = initial_nav  # 在初始日期之前的净值为初始净值
        portfolio_values['portfolio_value'] += shares * nav_df['nav']
    
    total_weight = sum(weights.values())
    if total_weight < 1:
        cash_weight = 1 - total_weight
        portfolio_values['portfolio_value'] += initial_investment * cash_weight

    portfolio_values['portfolio_value'] /= initial_investment
    return portfolio_values.rename(columns={'portfolio_value': 'portfolio_nav'})

def backtest_portfolio(fund_navs, weights, start_date, end_date, initial_investment=10000000):
    """
    基于基金净值和权重回测组合。

    参数:
    - fund_navs: 包含DataFrame的字典，每个DataFrame都有日期索引和'nav'列。
    - weights: 每个基金的权重字典。
    - start_date: 回测的开始日期（格式为'YYYY-MM-DD'）。
    - end_date: 回测的结束日期（格式为'YYYY-MM-DD'）。
    - initial_investment: 初始投资金额
    
    返回:
    - portfolio_nav: 以日期为索引，包含'portfolio_nav'列的DataFrame。
    """
    # 获取所有基金的日期，并生成完整日期范围
    all_dates = pd.date_range(start=start_date, end=end_date, freq='B')  # 仅包含工作日
    return calculate_portfolio_value(fund_navs, weights, all_dates, initial_investment)

# 定义文件夹路径和权重
folder_path = r'D:\量化交易构建\私募基金研究\基金表现预警程序\清洗后持仓基金净值（观察池）'
funds = ['博润易量稳健1号私募证券投资基金','量派对冲9号私募证券投资基金',
'量派CTA七号私募证券投资基金','千衍九凌1号私募证券投资基金','东恺祖率中性2号私募证券投资基金A',
'交叉智能-量化增强2号私募证券投资基金','宏翼高频1号私募证券投资基金']
weights = {
    '博润易量稳健1号私募证券投资基金': 0.14,
    '量派对冲9号私募证券投资基金': 0.14,
    '量派CTA七号私募证券投资基金':0.15,
    '千衍九凌1号私募证券投资基金':0.15,
    '东恺祖率中性2号私募证券投资基金A':0.14,
    '交叉智能-量化增强2号私募证券投资基金':0.14,
    '宏翼高频1号私募证券投资基金':0.14
}

# 加载基金数据
fund_navs = load_fund_data(folder_path, funds)

# 定义回测的开始和结束日期
start_date = '2022-10-01'
end_date = '2024-07-10'

# 执行回测
portfolio_nav = backtest_portfolio(fund_navs, weights, start_date, end_date)
print(portfolio_nav)


os.chdir(r'D:\量化交易构建\私募基金研究\基金表现预警程序')
portfolio_nav.to_excel('组合回测.xlsx')