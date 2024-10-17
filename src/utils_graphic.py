import matplotlib.pyplot as plt  # Importar o matplotlib.pyplot para usar plt.gca()

def add_mark_to_line(ax, color='blue', ha='right', va='bottom'):
    """
    Função para adicionar rótulos nos pontos de um gráfico.
    
    Parâmetros:
    - ax: O eixo (axis) onde o gráfico foi desenhado. Se None, usa o eixo atual.
    - color: Cor dos rótulos (padrão é 'blue').
    - ha: Alinhamento horizontal dos rótulos (padrão é 'right').
    - va: Alinhamento vertical dos rótulos (padrão é 'bottom').
    """
    for line in ax.lines:
        for x, y in zip(line.get_xdata(), line.get_ydata()):
            ax.text(x, y, f'{int(y):,}'.replace(',', '.'), color=color, ha=ha, va=va)
        

def add_mark_to_bar(ax, color='black'):
    """
    Função para adicionar rótulos no topo das barras de um gráfico de barras.
    
    Parâmetros:
    - ax: O eixo (axis) onde o gráfico foi desenhado.
    - data: DataFrame com os dados.
    - x_col: Nome da coluna para o eixo X.
    - y_col: Nome da coluna para o eixo Y.
    """
    for p in ax.patches:  # Itera por cada barra no gráfico
        height = p.get_height()  # Pega a altura da barra
        ax.text(p.get_x() + p.get_width() / 2., height, f'{int(height):,}'.replace(',', '.'), 
                ha='center', va='bottom', color=color)  # Adiciona o texto no topo da barra
