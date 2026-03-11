import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

def draw_chart(df, symbol, entry, sl, tp1, tp2, tp3):
    plt.style.use('seaborn-darkgrid')
    fig, ax = plt.subplots(figsize=(12,6))
    
    df = df[-50:]  # show last 50 candles
    df['index'] = np.arange(len(df))
    
    # Candlesticks
    for idx, row in df.iterrows():
        color = 'green' if row['close'] >= row['open'] else 'red'
        ax.plot([row['index'], row['index']], [row['low'], row['high']], color='black')
        ax.add_patch(plt.Rectangle((row['index']-0.3, row['open']), 0.6, row['close']-row['open'], color=color))
    
    # Entry / SL / TP lines
    ax.hlines([entry, sl, tp1, tp2, tp3], xmin=df['index'].min(), xmax=df['index'].max(),
              colors=['blue','red','lime','limegreen','darkgreen'], linestyles='dashed')
    
    ax.set_title(f"{symbol} - Signal Chart", fontsize=14)
    ax.set_xlabel("Candles")
    ax.set_ylabel("Price")
    
    # Save chart to PNG
    filename = f"{symbol}.png"
    plt.savefig(filename)
    plt.close(fig)
    return filename
