{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "55de3e7c-2e06-47d2-9d09-f3bfde661018",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "File saved as CSV at: E:\\final_project\\streamlite\\Suppliers_fainal_edit.csv\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import os\n",
    "\n",
    "# Define the path to the Excel file\n",
    "excel_file_path = r\"E:\\final_project\\streamlite\\Suppliers_fainal_edit.xlsx\"  # Update this to your actual file path\n",
    "\n",
    "# Define the folder where CSV should be saved\n",
    "folder_path = r\"E:\\final_project\\streamlite\"  # Ensure this path is correct for your system\n",
    "\n",
    "# Load the Excel file\n",
    "df = pd.read_excel(excel_file_path)  # Correct path for the Excel file\n",
    "\n",
    "# Define the CSV file name (same as Excel, but with .csv extension)\n",
    "csv_file_name = \"Suppliers_fainal_edit.csv\"\n",
    "\n",
    "# Create the folder if it doesn't exist\n",
    "if not os.path.exists(folder_path):\n",
    "    os.makedirs(folder_path)\n",
    "\n",
    "# Save the file as CSV in the specified folder\n",
    "csv_file_path = os.path.join(folder_path, csv_file_name)\n",
    "df.to_csv(csv_file_path, index=False)\n",
    "\n",
    "print(f\"File saved as CSV at: {csv_file_path}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "75133fef-4dab-4071-9fce-d649c35867e9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: streamlit in c:\\users\\lenovo\\appdata\\local\\programs\\python\\python311\\lib\\site-packages (1.39.0)Note: you may need to restart the kernel to use updated packages.\n",
      "\n",
      "Requirement already satisfied: altair<6,>=4.0 in c:\\users\\lenovo\\appdata\\local\\programs\\python\\python311\\lib\\site-packages (from streamlit) (5.4.1)\n",
      "Requirement already satisfied: blinker<2,>=1.0.0 in c:\\users\\lenovo\\appdata\\local\\programs\\python\\python311\\lib\\site-packages (from streamlit) (1.8.2)\n",
      "Requirement already satisfied: cachetools<6,>=4.0 in c:\\users\\lenovo\\appdata\\local\\programs\\python\\python311\\lib\\site-packages (from streamlit) (5.5.0)\n",
      "Requirement already satisfied: click<9,>=7.0 in c:\\users\\lenovo\\appdata\\local\\programs\\python\\python311\\lib\\site-packages (from streamlit) (8.1.7)\n",
      "Requirement already satisfied: numpy<3,>=1.20 in c:\\users\\lenovo\\appdata\\local\\programs\\python\\python311\\lib\\site-packages (from streamlit) (1.26.4)\n",
      "Requirement already satisfied: packaging<25,>=20 in c:\\users\\lenovo\\appdata\\local\\programs\\python\\python311\\lib\\site-packages (from streamlit) (23.2)\n",
      "Requirement already satisfied: pandas<3,>=1.4.0 in c:\\users\\lenovo\\appdata\\local\\programs\\python\\python311\\lib\\site-packages (from streamlit) (2.2.2)\n",
      "Requirement already satisfied: pillow<11,>=7.1.0 in c:\\users\\lenovo\\appdata\\local\\programs\\python\\python311\\lib\\site-packages (from streamlit) (10.3.0)\n",
      "Requirement already satisfied: protobuf<6,>=3.20 in c:\\users\\lenovo\\appdata\\local\\programs\\python\\python311\\lib\\site-packages (from streamlit) (5.28.2)\n",
      "Requirement already satisfied: pyarrow>=7.0 in c:\\users\\lenovo\\appdata\\local\\programs\\python\\python311\\lib\\site-packages (from streamlit) (17.0.0)\n",
      "Requirement already satisfied: requests<3,>=2.27 in c:\\users\\lenovo\\appdata\\local\\programs\\python\\python311\\lib\\site-packages (from streamlit) (2.31.0)\n",
      "Requirement already satisfied: rich<14,>=10.14.0 in c:\\users\\lenovo\\appdata\\local\\programs\\python\\python311\\lib\\site-packages (from streamlit) (13.9.2)\n",
      "Requirement already satisfied: tenacity<10,>=8.1.0 in c:\\users\\lenovo\\appdata\\local\\programs\\python\\python311\\lib\\site-packages (from streamlit) (9.0.0)\n",
      "Requirement already satisfied: toml<2,>=0.10.1 in c:\\users\\lenovo\\appdata\\local\\programs\\python\\python311\\lib\\site-packages (from streamlit) (0.10.2)\n",
      "Requirement already satisfied: typing-extensions<5,>=4.3.0 in c:\\users\\lenovo\\appdata\\local\\programs\\python\\python311\\lib\\site-packages (from streamlit) (4.12.2)\n",
      "Requirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in c:\\users\\lenovo\\appdata\\local\\programs\\python\\python311\\lib\\site-packages (from streamlit) (3.1.43)\n",
      "Requirement already satisfied: pydeck<1,>=0.8.0b4 in c:\\users\\lenovo\\appdata\\local\\programs\\python\\python311\\lib\\site-packages (from streamlit) (0.9.1)\n",
      "Requirement already satisfied: tornado<7,>=6.0.3 in c:\\users\\lenovo\\appdata\\local\\programs\\python\\python311\\lib\\site-packages (from streamlit) (6.4)\n",
      "Requirement already satisfied: watchdog<6,>=2.1.5 in c:\\users\\lenovo\\appdata\\local\\programs\\python\\python311\\lib\\site-packages (from streamlit) (5.0.3)\n",
      "Requirement already satisfied: jinja2 in c:\\users\\lenovo\\appdata\\local\\programs\\python\\python311\\lib\\site-packages (from altair<6,>=4.0->streamlit) (3.1.3)\n",
      "Requirement already satisfied: jsonschema>=3.0 in c:\\users\\lenovo\\appdata\\local\\programs\\python\\python311\\lib\\site-packages (from altair<6,>=4.0->streamlit) (4.21.1)\n",
      "Requirement already satisfied: narwhals>=1.5.2 in c:\\users\\lenovo\\appdata\\local\\programs\\python\\python311\\lib\\site-packages (from altair<6,>=4.0->streamlit) (1.9.1)\n",
      "Requirement already satisfied: colorama in c:\\users\\lenovo\\appdata\\local\\programs\\python\\python311\\lib\\site-packages (from click<9,>=7.0->streamlit) (0.4.6)\n",
      "Requirement already satisfied: gitdb<5,>=4.0.1 in c:\\users\\lenovo\\appdata\\local\\programs\\python\\python311\\lib\\site-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.11)\n",
      "Requirement already satisfied: python-dateutil>=2.8.2 in c:\\users\\lenovo\\appdata\\local\\programs\\python\\python311\\lib\\site-packages (from pandas<3,>=1.4.0->streamlit) (2.9.0.post0)\n",
      "Requirement already satisfied: pytz>=2020.1 in c:\\users\\lenovo\\appdata\\local\\programs\\python\\python311\\lib\\site-packages (from pandas<3,>=1.4.0->streamlit) (2024.1)\n",
      "Requirement already satisfied: tzdata>=2022.7 in c:\\users\\lenovo\\appdata\\local\\programs\\python\\python311\\lib\\site-packages (from pandas<3,>=1.4.0->streamlit) (2024.1)\n",
      "Requirement already satisfied: charset-normalizer<4,>=2 in c:\\users\\lenovo\\appdata\\local\\programs\\python\\python311\\lib\\site-packages (from requests<3,>=2.27->streamlit) (3.3.2)\n",
      "Requirement already satisfied: idna<4,>=2.5 in c:\\users\\lenovo\\appdata\\local\\programs\\python\\python311\\lib\\site-packages (from requests<3,>=2.27->streamlit) (3.6)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in c:\\users\\lenovo\\appdata\\local\\programs\\python\\python311\\lib\\site-packages (from requests<3,>=2.27->streamlit) (2.2.1)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\lenovo\\appdata\\local\\programs\\python\\python311\\lib\\site-packages (from requests<3,>=2.27->streamlit) (2024.2.2)\n",
      "Requirement already satisfied: markdown-it-py>=2.2.0 in c:\\users\\lenovo\\appdata\\local\\programs\\python\\python311\\lib\\site-packages (from rich<14,>=10.14.0->streamlit) (3.0.0)\n",
      "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in c:\\users\\lenovo\\appdata\\local\\programs\\python\\python311\\lib\\site-packages (from rich<14,>=10.14.0->streamlit) (2.17.2)\n",
      "Requirement already satisfied: smmap<6,>=3.0.1 in c:\\users\\lenovo\\appdata\\local\\programs\\python\\python311\\lib\\site-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (5.0.1)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in c:\\users\\lenovo\\appdata\\local\\programs\\python\\python311\\lib\\site-packages (from jinja2->altair<6,>=4.0->streamlit) (2.1.5)\n",
      "Requirement already satisfied: attrs>=22.2.0 in c:\\users\\lenovo\\appdata\\local\\programs\\python\\python311\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (23.2.0)\n",
      "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in c:\\users\\lenovo\\appdata\\local\\programs\\python\\python311\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (2023.12.1)\n",
      "Requirement already satisfied: referencing>=0.28.4 in c:\\users\\lenovo\\appdata\\local\\programs\\python\\python311\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.33.0)\n",
      "Requirement already satisfied: rpds-py>=0.7.1 in c:\\users\\lenovo\\appdata\\local\\programs\\python\\python311\\lib\\site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.18.0)\n",
      "Requirement already satisfied: mdurl~=0.1 in c:\\users\\lenovo\\appdata\\local\\programs\\python\\python311\\lib\\site-packages (from markdown-it-py>=2.2.0->rich<14,>=10.14.0->streamlit) (0.1.2)\n",
      "Requirement already satisfied: six>=1.5 in c:\\users\\lenovo\\appdata\\local\\programs\\python\\python311\\lib\\site-packages (from python-dateutil>=2.8.2->pandas<3,>=1.4.0->streamlit) (1.16.0)\n"
     ]
    }
   ],
   "source": [
    "pip install streamlit"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "63c51fa2-f909-4f53-b48c-08b4d59ed939",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2024-10-05 21:27:16.469 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-10-05 21:27:16.472 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-10-05 21:27:19.335 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\LENOVO\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n",
      "2024-10-05 21:27:19.336 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-10-05 21:27:19.339 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-10-05 21:27:19.341 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-10-05 21:27:19.343 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-10-05 21:27:19.345 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-10-05 21:27:19.346 Session state does not function when running a script without `streamlit run`\n",
      "2024-10-05 21:27:19.348 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-10-05 21:27:19.351 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import os\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "\n",
    "# Set the page config\n",
    "st.set_page_config(page_title='Data Visualizer',\n",
    "                   layout='centered',\n",
    "                   page_icon='📊')\n",
    "\n",
    "# Title\n",
    "st.title('📊  Data Visualizer')\n",
    "\n",
    "# Specify the folder where your CSV files are located\n",
    "folder_path = r\"E:\\final_project\\streamlite\"  # Update this to your folder path\n",
    "\n",
    "# List all files in the folder\n",
    "files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]\n",
    "\n",
    "# Dropdown to select a file\n",
    "selected_file = st.selectbox('Select a file', files, index=None)\n",
    "\n",
    "if selected_file:\n",
    "    # Construct the full path to the file\n",
    "    file_path = os.path.join(folder_path, selected_file)\n",
    "\n",
    "    # Read the selected CSV file\n",
    "    df = pd.read_csv(file_path)\n",
    "\n",
    "    col1, col2 = st.columns(2)\n",
    "\n",
    "    columns = df.columns.tolist()\n",
    "\n",
    "    with col1:\n",
    "        st.write(\"\")\n",
    "        st.write(df.head())\n",
    "\n",
    "    with col2:\n",
    "        # Allow the user to select columns for plotting\n",
    "        x_axis = st.selectbox('Select the X-axis', options=columns+[\"None\"])\n",
    "        y_axis = st.selectbox('Select the Y-axis', options=columns+[\"None\"])\n",
    "\n",
    "        plot_list = ['Line Plot', 'Bar Chart', 'Scatter Plot', 'Distribution Plot', 'Count Plot']\n",
    "        # Allow the user to select the type of plot\n",
    "        plot_type = st.selectbox('Select the type of plot', options=plot_list)\n",
    "\n",
    "    # Generate the plot based on user selection\n",
    "    if st.button('Generate Plot'):\n",
    "\n",
    "        fig, ax = plt.subplots(figsize=(6, 4))\n",
    "\n",
    "        if plot_type == 'Line Plot':\n",
    "            sns.lineplot(x=df[x_axis], y=df[y_axis], ax=ax)\n",
    "        elif plot_type == 'Bar Chart':\n",
    "            sns.barplot(x=df[x_axis], y=df[y_axis], ax=ax)\n",
    "        elif plot_type == 'Scatter Plot':\n",
    "            sns.scatterplot(x=df[x_axis], y=df[y_axis], ax=ax)\n",
    "        elif plot_type == 'Distribution Plot':\n",
    "            sns.histplot(df[x_axis], kde=True, ax=ax)\n",
    "            y_axis = 'Density'\n",
    "        elif plot_type == 'Count Plot':\n",
    "            sns.countplot(x=df[x_axis], ax=ax)\n",
    "            y_axis = 'Count'\n",
    "\n",
    "        # Adjust label sizes\n",
    "        ax.tick_params(axis='x', labelsize=10)  # Adjust x-axis label size\n",
    "        ax.tick_params(axis='y', labelsize=10)  # Adjust y-axis label size\n",
    "\n",
    "        # Adjust title and axis labels with a smaller font size\n",
    "        plt.title(f'{plot_type} of {y_axis} vs {x_axis}', fontsize=12)\n",
    "        plt.xlabel(x_axis, fontsize=10)\n",
    "        plt.ylabel(y_axis, fontsize=10)\n",
    "\n",
    "        # Show the results\n",
    "        st.pyplot(fig)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "1545ddb3-f2f6-4eba-a30a-80e5f3fb595a",
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.11.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
