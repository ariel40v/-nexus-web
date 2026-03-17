import ccxt
import time
import os

def run_trading_bot(symbol='BTC/USDT'):
    # Inicializamos el exchange (usamos Binance por defecto para data publica)
    exchange = ccxt.binance()
    
    print(f"--- BOT DE TRADING INICIADO ---")
    print(f"Monitoreando: {symbol}")
    print(f"Presiona Ctrl+C para detener.")
    print("-" * 30)

    # Variables para una estrategia simple (Simulación)
    buying_price = None
    balance_usd = 1000  # Empezamos con 1000 USD ficticios
    balance_crypto = 0

    try:
        while True:
            # 1. Obtener datos actuales del mercado
            ticker = exchange.fetch_ticker(symbol)
            current_price = ticker['last']
            bid_price = ticker['bid'] # El mejor precio de compra actual
            ask_price = ticker['ask'] # El mejor precio de venta actual

            # 2. Mostrar estado en consola
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"--- NEXUS TRADING BOT (MOCK MODE) ---")
            print(f"Símbolo: {symbol} | Precio Actual: ${current_price:,.2f}")
            print(f"Bid: ${bid_price:,.2f} | Ask: ${ask_price:,.2f}")
            print(f"Balance Mock: ${balance_usd:,.2f} USDT | {balance_crypto:.6f} {symbol.split('/')[0]}")
            print("-" * 40)
            
            # 3. Lógica de Estrategia Muy Básica (Ejemplo de Cruce de Precios)
            # Aquí es donde pondríamos los indicadores reales (RSI, Medias Móviles, etc)
            
            # Simulación: Si baja un 2%, compramos. Si sube un 5%, vendemos.
            if balance_usd > 10 and (buying_price is None or current_price < buying_price * 0.98):
                # ESTRATEGIA: COMPRA
                buying_price = current_price
                balance_crypto = balance_usd / current_price
                balance_usd = 0
                print(f"⚡ ORDEN DE COMPRA (Simulada): {balance_crypto:.6f} a ${current_price:,.2f}")
            
            elif balance_crypto > 0 and current_price > buying_price * 1.05:
                # ESTRATEGIA: VENTA
                balance_usd = balance_crypto * current_price
                profit = balance_usd - 1000 # Profit relativo al inicio
                print(f"💰 ORDEN DE VENTA (Simulada): Ganancia de ${profit:,.2f}")
                balance_crypto = 0
                buying_price = None

            # Esperar 10 segundos antes de la siguiente actualización
            time.sleep(10)

    except KeyboardInterrupt:
        print("\nBot detenido por el usuario.")
    except Exception as e:
        print(f"\nError ocurrido: {e}")

if __name__ == "__main__":
    run_trading_bot('BTC/USDT') # Puedes cambiarlo a 'ETH/USDT', 'SOL/USDT', etc.
