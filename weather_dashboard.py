{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "db02a8b9-5678-4ab1-967b-af344193901b",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "59caeba9-3151-463f-a91a-aaa3e6db3c05",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-04-07 12:37:52.457 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\SUYASH\\anaconda3\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import requests\n",
    "import pandas as pd\n",
    "import plotly.express as px\n",
    "from datetime import datetime\n",
    "\n",
    "API_KEY = \"b76ab9b14abba7b3a9a6f86d5c021414\"\n",
    "CITY = \"Dublin\"\n",
    "FORECAST_URL = f\"https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric\"\n",
    "\n",
    "st.title(\"🇮🇪 Irish Weather Forecast App\")\n",
    "\n",
    "# Input\n",
    "city = st.selectbox(\"Select a City\", [\"Dublin\", \"Cork\", \"Galway\", \"Limerick\"])\n",
    "days = st.slider(\"Forecast Days\", 1, 7, 3)\n",
    "\n",
    "# API Call\n",
    "params = {'q': city, 'appid': API_KEY, 'units': 'metric'}\n",
    "res = requests.get(FORECAST_URL)\n",
    "data = res.json()\n",
    "\n",
    "# Process Forecast\n",
    "forecast = []\n",
    "for entry in data[\"list\"]:\n",
    "    dt = datetime.fromtimestamp(entry[\"dt\"])\n",
    "    forecast.append({\n",
    "        \"Date\": dt.date(),\n",
    "        \"Hour\": dt.hour,\n",
    "        \"Temp (°C)\": entry[\"main\"][\"temp\"]\n",
    "    })\n",
    "\n",
    "df = pd.DataFrame(forecast)\n",
    "df = df[df[\"Hour\"] == 12].head(days)  # Midday forecast\n",
    "\n",
    "# Display\n",
    "st.write(f\"### {days}-Day Forecast for {city}\")\n",
    "fig = px.line(df, x=\"Date\", y=\"Temp (°C)\", title=\"Temperature Forecast\")\n",
    "st.plotly_chart(fig)\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
