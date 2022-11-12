import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(page_title="Stock/Price Analysis and Prediction", page_icon="chart_with_upwards_trend",
                    layout="centered", initial_sidebar_state="auto")

st.title("Stock Market Price Prediction")
@st.cache
def get_data():
    path = 'stock.csv'
    return pd.read_csv(path, low_memory=False)

df = get_data()
df = df.drop_duplicates(subset="Name", keep="first")
stocks = df['Name']
selected_stock = st.selectbox("Select Stock ", stocks)

index = df[df["Name"]==selected_stock].index.values[0]
symbol = df["Symbol"][index]
START = st.date_input("Enter Start Date").strftime("%Y-%m-%d")
TODAY = st.date_input("Enter end date").strftime("%Y-%m-%d")

interval_option = st.selectbox(
        'Time Interval',
        ('Day', 'Week', 'Month'))

if interval_option == "Week":
    interval_option = "1wk"
if interval_option == "Month":
    interval_option = "1mo"
else:
    interval_option = "1d"

algo = st.selectbox("Choose an algorithm that predict your price:", ("Prophet", "SRIMAX"))
start = st.button("choose algorithm")
if start:
    if algo == "Prophet":
        import streamlit as st
        import yfinance as yf
        from plotly import graph_objs as go
        import pandas as pd
        from prophet import Prophet
        from prophet.plot import plot_plotly
        st.write("###")


        period = 1 * 365

        @st.cache
        def load_data(ticker):
            data = yf.download(ticker, START, TODAY)
            data.reset_index(inplace=True)
            return data

        data_load_state = st.text("Load data ...")
        data = load_data(symbol)
        data_load_state.text("Loading data ... Done!")

        st.write("###")

        st.subheader("Raw data")
        st.write(data.tail())

        def plot_raw_data():
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name='stock_open'))
            fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name='stock_close'))
            fig.layout.update(title_text = "Time Series Data", xaxis_rangeslider_visible = True)
            st.plotly_chart(fig)

        plot_raw_data()
        #Forecasting
        df_train = data[['Date', 'Close']]
        df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

        m = Prophet()
        m.fit(df_train)

        future = m.make_future_dataframe(periods=period)
        forecast = m.predict(future)

        st.write("***")
        st.write("###")

        st.subheader("Forecast data")
        st.write(forecast.tail())

        fig1 = plot_plotly(m, forecast)
        st.plotly_chart(fig1)

        st.subheader("Forecast Components")
        fig2 = m.plot_components(forecast)
        st.write(fig2)

    else:
        import streamlit as st
        import yahoo_fin.stock_info as si
        from sklearn.metrics import classification_report
        from yahoo_fin.stock_info import get_data
        import yfinance as yf
        import datetime
        import pandas as pd

        ticker_details = get_data(symbol, start_date=START, end_date=TODAY, interval=interval_option
        )
        df = ticker_details
        df['daily_pc_returns'] = (df['close'] / df['close'].shift(1) - 1) * 100
        if (len(ticker_details) > 0):
            st.subheader(f'{symbol} Stock Data')
            st.dataframe(df.tail(), 1500, 210)
            st.line_chart(df.daily_pc_returns)
        else:
            st.write("No Data Found!")

        import matplotlib.pyplot as plt
        from statsmodels.tsa.statespace.sarimax import SARIMAX
        import warnings

        warnings.filterwarnings("ignore")

        data = df[['close']]

        if (len(data) > 31):
            data = data.tail(30)
        model = SARIMAX(data['close'])
        result = model.fit()
    # Train the model on the full dataset
        model = SARIMAX(data['close'],
                    order=(0, 1, 1),
                    seasonal_order=(2, 1, [], 12))
        result = model.fit()

    # Forecast for the next 30 days
        forecast = result.predict(start=(len(data) - 1),
                            end=(len(data) - 1) + 30,
                            typ='levels').rename('Forecast')


    # Forecast for the next 30 days
        title_col1, title_col2, title_col3 = st.columns([2, 2, 5])
        with title_col1:
            st.dataframe(data.tail())
        with title_col2:
            st.dataframe(forecast.head())
        with title_col3:
            tkr = yf.Ticker(symbol)
            ticker_info = tkr.info
            st.write("Sector : ", ticker_info['sector'], '-', ticker_info['symbol'], " - ", ticker_info['shortName'])
        # st.image(ticker_info['logo_url'])
        # st.write("Sector : ", ticker_info['sector'])
            st.write("52Week High-Low : ", ticker_info['fiftyTwoWeekHigh'], '-', ticker_info['fiftyTwoWeekLow'])
            st.write("day High-Low : ", ticker_info['dayHigh'], '-', ticker_info['dayLow'])
            st.write("Current Price : ", ticker_info['currentPrice'], " ", ticker_info['financialCurrency'])
            st.write("marketCap : ", ticker_info['marketCap'])

    # Plot the forecast values
        fig = plt.figure()
        data['close'].plot(figsize=(20, 5), legend=True)
        forecast.plot(legend=True)
        st.pyplot(fig)

