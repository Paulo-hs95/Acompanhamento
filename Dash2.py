import zipfile
import plotly.express as px
import pandas as pd
import numpy as np
import streamlit as st
import plotly.figure_factory as ff
import time
import calendar
from datetime import datetime
from calendar import monthrange
from collections import defaultdict
from collections import Counter
import string


today = datetime.now()
current_date_str = today.strftime("%d/%m/%Y")
st.title(f"Produtividade")
st.set_page_config(layout="wide")
st.sidebar.header("Filtros")
year = today.strftime("%Y")
year=int(year)


#df = pd.read_csv(f'Historico.csv')
df = pd.read_csv('Historico.csv', compression='zip')

rt_ag = rt_ag2 = sorted(set({x for x in df['Agência'] if x == x}))
rt_ag2.append("Supervisão ou outros técnicos")
rt_ag2.append("Todas")
rt_rp = sorted(set({x for x in df['Responsavel'] if x == x}))
rt_rp2 = [string.capwords(s) for s in rt_rp if isinstance(s, str)]
rt_rp2.append("Todos")
rt_tp = rt_tp2 = sorted(set({x for x in df['Tipo'] if x == x}))
rt_tp.append("Todas")
# In[5]:




filtro_resp = df[df['Responsavel'] == rt_rp[1]]

filtro_ag = df[df['Agência'] == rt_ag[4]]

filtro_tp = df[df['Tipo'] == rt_tp[1]]

filtro = df[(df['Responsavel'] == rt_rp[1]) & (df['Agência'] == rt_ag[4]) & (df['Tipo'] == rt_tp[1])]

st.set_page_config(layout="wide")
col1, col2 = st.columns(2) # Primeira linha com duas colunas
col3, col4 = st.columns(2) # Segunda linha com três colunas
col5, col6 = st.columns(2)
col7, col8 = st.columns(2)
col9, col10 = st.columns(2)
col11, col12 = st.columns(2)







st.markdown(
        """
        <style>
        [data-testid="stSidebarContent"] {
            background-color: #6785b5; /* Replace with your desired color */
        }
        </style>
        """,
        unsafe_allow_html=True
    )



#rp2 = pd.DataFrame(rt_rp2, columns=['rp'])
#rp3 = rp2[rp2['rp'] == rt_rp2[3]]
#rtp = pd.DataFrame(rt_tp, columns=['rp'])
#rtp3 = rp2[rp2['rp'] == rt_rp2[3]]

grafico_tipo = st.sidebar.selectbox("Tipo de atividade:", rt_tp)

#grafico_tipo2 = st.sidebar.selectbox("Técnico:", rt_rp2)
#grafico_tipo3 = st.sidebar.selectbox("Agência:", rt_ag2)
for jk in rt_tp:
	if grafico_tipo == jk:
		jlk1=df[df['Tipo'] == jk]
		rt_rpx = sorted(set({x for x in jlk1['Responsavel'] if x == x}))
		rt_rpx2 = [string.capwords(s) for s in rt_rpx if isinstance(s, str)]
		rt_rpx2.append("Todos")
		if grafico_tipo == "Todas":
			grafico_tipo2 = st.sidebar.selectbox("Técnico:", rt_rp2)
			for js in rt_rp2:
				if grafico_tipo2 == js:
					jlk3=df[df['Responsavel'] == js.upper()]
					rt_agx = sorted(set({x for x in jlk3['Agência'] if x == x}))
					if (grafico_tipo2 == "Todos") & (grafico_tipo != "Todas"):
						grafico_tipo3 = st.sidebar.selectbox("Agência:", rt_agx)
						break
					elif (rt_agx==[]) & (grafico_tipo != "Todas"):
						rt_agx.append("Supervisão ou outros técnicos")
						grafico_tipo3 = st.sidebar.selectbox("Agência:", rt_agx)

					elif (rt_agx==[]) & (grafico_tipo == "Todas") & (grafico_tipo2 == "Todos"):
						grafico_tipo3 = st.sidebar.selectbox("Agência:", rt_ag2)
					elif (rt_agx==[]) & (grafico_tipo == "Todas"):
						rt_agx.append("Supervisão ou outros técnicos")
						grafico_tipo3 = st.sidebar.selectbox("Agência:", rt_agx)
					else:
						grafico_tipo3 = st.sidebar.selectbox("Agência:", rt_agx)
			
			break
		grafico_tipo2 = st.sidebar.selectbox("Técnico:", rt_rpx2)
for js in rt_rpx2:
	if grafico_tipo2 == js:
		jlk2=jlk1[jlk1['Responsavel'] == js.upper()]
		rt_agx = sorted(set({x for x in jlk2['Agência'] if x == x}))
		if (grafico_tipo2 == "Todos") & (grafico_tipo != "Todas"):
			grafico_tipo3 = st.sidebar.selectbox("Agência:", rt_ag2)
			break
		elif (rt_agx==[]) & (grafico_tipo != "Todas"):
			rt_agx.append("Supervisão ou outros técnicos")
		if (grafico_tipo2 != "Todos") & (grafico_tipo != "Todas"):
			grafico_tipo3 = st.sidebar.selectbox("Agência:", rt_agx)
		elif (grafico_tipo2 == "Todos") & (grafico_tipo != "Todas"):
			grafico_tipo3 = st.sidebar.selectbox("Agência:", rt_agx)

		rt_agx.append("Todos")
grafico = st.sidebar.write(f"Data: {current_date_str}")
#for g1 in rt_tp
#	if grafico_tipo == st.sidebar.selectbox("Técnico:", rt_tp)
#		grafico_tipo2 = st.sidebar.selectbox("Técnico:", rt_rp2)



#rp2 = pd.DataFrame(rt_rp2, columns=['rp'])
#rp23 = rp2[rp2['rp'] == rt_rp2[3]]
#st.text(rp23)

m = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]

x=['Domingo','Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta','Sábado']
y=['Semana 5', 'Semana 4', 'Semana 3', 'Semana 2', 'Semana 1']
y1=['', 'Semana 4', 'Semana 3', 'Semana 2', 'Semana 1']


t=0

for v1 in rt_tp:
	for v2 in rt_rp2:
		for v3 in rt_ag2:
			if grafico_tipo == v1 and grafico_tipo2 == v2 and grafico_tipo3 == v3:
				if (grafico_tipo == "Todas") & (grafico_tipo2 != "Todos") & (grafico_tipo3 != "Todas") & (grafico_tipo3 != "Supervisão ou outros técnicos"):
					filtro = df[(df['Responsavel'] == v2.upper()) & (df['Agência'] == v3)]
				elif (grafico_tipo != "Todas") & (grafico_tipo2 == "Todos") & (grafico_tipo3 != "Todas") & (grafico_tipo3 != "Supervisão ou outros técnicos"):
					filtro = df[(df['Agência'] == v3) & (df['Tipo'] == v1)]
				elif (grafico_tipo != "Todas") & (grafico_tipo2 != "Todos") & (grafico_tipo3 == "Todas"):
					filtro = df[(df['Responsavel'] == v2.upper()) & (df['Tipo'] == v1)]
				elif (grafico_tipo == "Todas") & (grafico_tipo2 == "Todos") & (grafico_tipo3 != "Todas") & (grafico_tipo3 != "Supervisão ou outros técnicos"):
					filtro = df[df['Agência'] == v3]	
				elif (grafico_tipo != "Todas") & (grafico_tipo2 == "Todos") & (grafico_tipo3 == "Todas"):
					filtro = df[df['Tipo'] == v1]		
				elif (grafico_tipo == "Todas") & (grafico_tipo2 == "Todos") & (grafico_tipo3 == "Todas"):
					filtro = df
				elif (grafico_tipo3 == "Supervisão ou outros técnicos") & (grafico_tipo != "Todas") & (grafico_tipo2 == "Todos"):
					filtro = df[(df['Agência'].isnull()) & (df['Tipo'] == v1)]
				elif (grafico_tipo3 == "Supervisão ou outros técnicos") & (grafico_tipo == "Todas") & (grafico_tipo2 == "Todos"):
					filtro = df[df['Agência'].isnull()]				
				elif (grafico_tipo3 == "Supervisão ou outros técnicos") & (grafico_tipo == "Todas") & (grafico_tipo2 != "Todos"):
					filtro = df[df['Responsavel'] == v2.upper()]
				elif (grafico_tipo3 == "Supervisão ou outros técnicos") & (grafico_tipo != "Todas") & (grafico_tipo2 == v2):
					filtro = df[(df['Responsavel'] == v2.upper()) & (df['Tipo'] == v1)]				
				else:
					filtro = df[(df['Responsavel'] == v2.upper()) & (df['Agência'] == v3) & (df['Tipo'] == v1)]

				for month in range(12):

				    if calendar.monthrange(year, month+1)[1] == 28:
				        
				        z_text28 = [['', '', '', '', '', '', ''],
				              ['22', '23', '24', '25', '26', '27', '28'],
				              ['15', '16', '17', '18', '19', '20', '21'],
				              ['8', '9', '10', '11', '12', '13', '14'],
				              ['1', '2', '3', '4', '5', '6', '7']]


				        a = [0.0] * 36
				        max=0
				        dd=0
				        h1=0
				        for i in range(28):
				        	t=t+1
				        	dd=dd+1
				        	dia=f"{month+1}/{dd}/{year}"
				        	a[i+1] = len(filtro[filtro['DataAlteração'].str.contains(dia)])
				        	if a[i+1]>0:
				        		h1=1
				        if h1==1:
				        	colorscale=[[0.0, 'rgb(255,255,255)'], [.01, 'rgb(255, 255, 153)'],
            							[.4, 'rgb(153, 255, 204)'], [.6, 'rgb(179, 217, 255)'],
            							[.8, 'rgb(240, 179, 255)'],[1.0, 'rgb(255, 77, 148)']]			        		
				        else:
				        	colorscale=[[0.0, 'rgb(255,255,255)'], [1.0, 'rgb(255,255,255)']]



				        z = np.array ([[a[29], a[30], a[31], a[32], a[33], a[34], a[35]], 
				           [a[22], a[23], a[24], a[25], a[26], a[27], a[28]], 
				           [a[15], a[16], a[17], a[18], a[19], a[20], a[21]], 
				           [a[8], a[9], a[10], a[11], a[12], a[13], a[14]], 
				           [a[1], a[2], a[3], a[4], a[5], a[6], a[7]]])

				        g=0
				        hover_text = []
				        for i in range(z.shape[0]):
				        	row = []
				        	for j in range(z.shape[1]):
				        		if g<8:
				        			row.append([])
				        		else:
				        			row.append(f"{z[i, j]:.0f}")
				        		g=g+1
				        	hover_text.append(row)

				        exec(f'fig{month+1} = ff.create_annotated_heatmap(z, x=x, y=y1, annotation_text=z_text28, colorscale=colorscale, text=hover_text, hoverinfo="text")')
				        exec(f'fig{month+1}.update_layout(title_text = f"Produtividade mês de {m[month]}")')



				        #exec(f'fig{month+1}.update_traces(hovertemplate=("%{x}<br>%{y1}<br><b>correlation: %{z_text28}</b><extra></extra>"))')
				        
				        
				    elif calendar.monthrange(year, month+1)[1] == 29:
				        
				        z_text29 = [['29', '', '', '', '', '', ''],
				              ['22', '23', '24', '25', '26', '27', '28'],
				              ['15', '16', '17', '18', '19', '20', '21'],
				              ['8', '9', '10', '11', '12', '13', '14'],
				              ['1', '2', '3', '4', '5', '6', '7']]

				        a = [0.0] * 36
				        max=0
				        dd=0
				        h1=0
				        for i in range(29):
				        	t=t+1
				        	dd=dd+1
				        	dia=f"{month+1}/{dd}/{year}"
				        	a[i+1] = len(filtro[filtro['DataAlteração'].str.contains(dia)])
				        	if a[i+1]>max:
				        		max=a[i+1]
				        	if a[i+1]>0.01:
				        		h1=1

				        if h1==1:
				        	colorscale=[[0.0, 'rgb(255,255,255)'], [.01, 'rgb(255, 255, 153)'],
            							[.4, 'rgb(153, 255, 204)'], [.6, 'rgb(179, 217, 255)'],
            							[.8, 'rgb(240, 179, 255)'],[1.0, 'rgb(255, 77, 148)']]				        		
				        else:
				        	colorscale=[[0.0, 'rgb(255,255,255)'], [1.0, 'rgb(255,255,255)']]

				        z = np.array ([[a[29], a[30], a[31], a[32], a[33], a[34], a[35]], 
				           [a[22], a[23], a[24], a[25], a[26], a[27], a[28]], 
				           [a[15], a[16], a[17], a[18], a[19], a[20], a[21]], 
				           [a[8], a[9], a[10], a[11], a[12], a[13], a[14]], 
				           [a[1], a[2], a[3], a[4], a[5], a[6], a[7]]])

				        g=0
				        hover_text = []
				        for i in range(z.shape[0]):
				        	row = []
				        	for j in range(z.shape[1]):
				        		if g<7:
				        			row.append([])
				        		else:
				        			row.append(f"{z[i, j]:.0f}")
				        		g=g+1
				        	hover_text.append(row)

				        exec(f'fig{month+1} = ff.create_annotated_heatmap(z, x=x, y=y, annotation_text=z_text29, colorscale=colorscale, text=hover_text, hoverinfo="text")')
				        exec(f'fig{month+1}.update_layout(title_text = f"Produtividade mês de {m[month]}")')
				        
				    elif calendar.monthrange(year, month+1)[1] == 30:
				        
				        z_text30 = [['29', '30', '', '', '', '', ''],
				              ['22', '23', '24', '25', '26', '27', '28'],
				              ['15', '16', '17', '18', '19', '20', '21'],
				              ['8', '9', '10', '11', '12', '13', '14'],
				              ['1', '2', '3', '4', '5', '6', '7']]

				        a = [0.0] * 36
				        max=0
				        dd=0
				        h1=0
				        for i in range(30):
				        	t=t+1
				        	dd=dd+1
				        	dia=f"{month+1}/{dd}/{year}"
				        	a[i+1] = len(filtro[filtro['DataAlteração'].str.contains(dia)])
				        	if a[i+1]>max:
				        		max=a[i+1]
				        	if a[i+1]>0.01:
				        		h1=1

				        if h1==1:
				        	colorscale=[[0.0, 'rgb(255,255,255)'], [.01, 'rgb(255, 255, 153)'],
            							[.4, 'rgb(153, 255, 204)'], [.6, 'rgb(179, 217, 255)'],
            							[.8, 'rgb(240, 179, 255)'],[1.0, 'rgb(255, 77, 148)']]				        		
				        else:
				        	colorscale=[[0.0, 'rgb(255,255,255)'], [1.0, 'rgb(255,255,255)']]

				        z = np.array ([[a[29], a[30], a[31], a[32], a[33], a[34], a[35]], 
				           [a[22], a[23], a[24], a[25], a[26], a[27], a[28]], 
				           [a[15], a[16], a[17], a[18], a[19], a[20], a[21]], 
				           [a[8], a[9], a[10], a[11], a[12], a[13], a[14]], 
				           [a[1], a[2], a[3], a[4], a[5], a[6], a[7]]])

				        g=0
				        hover_text = []
				        for i in range(z.shape[0]):
				        	row = []
				        	for j in range(z.shape[1]):
				        		if 1<g<7:
				        			row.append([])
				        		else:
				        			row.append(f"{z[i, j]:.0f}")
				        		g=g+1
				        	hover_text.append(row)


				        exec(f'fig{month+1} = ff.create_annotated_heatmap(z, x=x, y=y, annotation_text=z_text30, colorscale=colorscale, text=hover_text, hoverinfo="text")')
				        exec(f'fig{month+1}.update_layout(title_text = f"Produtividade mês de {m[month]}")')
				        
				    elif calendar.monthrange(year, month+1)[1] == 31:
				        
				        z_text31 = [['29', '30', '31', '', '', '', ''],
				              ['22', '23', '24', '25', '26', '27', '28'],
				              ['15', '16', '17', '18', '19', '20', '21'],
				              ['8', '9', '10', '11', '12', '13', '14'],
				              ['1', '2', '3', '4', '5', '6', '7']]

				        a = [0.0] * 36
				        max=0
				        dd=0
				        h1=0
				        for i in range(31):
				        	t=t+1
				        	dd=dd+1
				        	dia=f"{month+1}/{dd}/{year}"
				        	a[i+1] = len(filtro[filtro['DataAlteração'].str.contains(dia)])
				        	if a[i+1]>0.01:
				        		h1=1
				        if h1==1:
				        	colorscale=[[0.0, 'rgb(255,255,255)'], [.01, 'rgb(255, 255, 153)'],
            							[.4, 'rgb(153, 255, 204)'], [.6, 'rgb(179, 217, 255)'],
            							[.8, 'rgb(240, 179, 255)'],[1.0, 'rgb(255, 77, 148)']]				        		
				        else:
				        	colorscale=[[0.0, 'rgb(255,255,255)'], [1.0, 'rgb(255,255,255)']]

				        z = np.array ([[a[29], a[30], a[31], a[32], a[33], a[34], a[35]], 
				           [a[22], a[23], a[24], a[25], a[26], a[27], a[28]], 
				           [a[15], a[16], a[17], a[18], a[19], a[20], a[21]], 
				           [a[8], a[9], a[10], a[11], a[12], a[13], a[14]], 
				           [a[1], a[2], a[3], a[4], a[5], a[6], a[7]]])	

				        g=0
				        hover_text = []
				        for i in range(z.shape[0]):
				        	row = []
				        	for j in range(z.shape[1]):
				        		if 2<g<7:
				        			row.append([])
				        		else:
				        			row.append(f"{z[i, j]:.0f}")
				        		g=g+1
				        	hover_text.append(row)	

				        exec(f'fig{month+1} = ff.create_annotated_heatmap(z, x=x, y=y, annotation_text=z_text31, colorscale=colorscale, text=hover_text, hoverinfo="text")')
				        exec(f'fig{month+1}.update_layout(title_text = f"Produtividade mês de {m[month]}")')

st.text(f'Total de dias no ano: {t}')


col1.plotly_chart(fig1)
col2.plotly_chart(fig2)
col3.plotly_chart(fig3)
col4.plotly_chart(fig4)
col5.plotly_chart(fig5)
col6.plotly_chart(fig6)
col7.plotly_chart(fig7)
col8.plotly_chart(fig8)
col9.plotly_chart(fig9)
col10.plotly_chart(fig10)
col11.plotly_chart(fig11)
col12.plotly_chart(fig12)




















