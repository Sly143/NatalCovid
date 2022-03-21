# =============================================================
# Criado por Paulo H. Lopes 2020
# =============================================================

pajucara = {
	# =============================================================
	# Dados Demográficos
	'regiao': 'norte',					# Zona ao qual o bairro pertence
	'tamPop': 75008,					# Tamanho da população
	'tamFisico': 766.1,					# Área do bairro em Hectare
	'densidadeDemografica': 97.91,		# Densidade demografica (Hab/km²)
	'numDomicilio': 16693,				# Numero de domicilios
	'domicilio': {'casa': 95.51, 'apartamento': 0.18, 'comodo':0.02, 'casa de vila ou condominio': 3.29,  'outro': 0},
	'idade': [8883, 13206, 14887, 10568, 14428, 7427, 3233, 1414, 961],  # Vetor de dados, cada posição é referente a um tipo de dado ->['0-9','10-19','20-29','30-39','40-49','50-59','60-69','70-79','80-']
	'renda': [2.2, 8.32, 25.02, 35.11, 20.11, 4.06, 1.92, 0.54, 0.06, 2.66, 0], # Vetor de dados, cada posição é referente a um tipo de dado ->[Até 1/8 de SM, Mais de 1/8 a 1/4 de SM, Mais de 1/4 a 1/2 SM, Mais de 1/2 a 1 SM, Mais de 1 a 2 SM, Mais de 2 a 3 SM, Mais de 3 a 5 SM, Mais de 5 a 10 SM, Mais de 10 SM, Sem rendimento, Sem declaração]
	'esgoto': {'existe': 29.57, 'naoExiste': 70.43},	# Porcentagem de esgoto a céu aberto
	
	# =============================================================
	# Dados Hospitalares
	'hospitais': 'vazio',		# Numero de Hospitais, Unidade de pronto atendimento e Unidade básica de saude
	'leitos': 'vazio',			# Numero de leitos dos hospitais
	'uti': 'vazio',				# Número de UTIS do bairro
	'doencasCronicas': 'vazio',	# Numero de pessoas com doenças cronicas
	
	# =============================================================
	# Dados Escolares
	'escolas': {'municipal':12, 'estadual': 1, 'particular': 15},	# Número de escolas
	'mediaFuncEscola': 'vazio',		# Média de funcionários das escolas
	'mediaAlunosEscola': {'municipal':4689, 'estadual': 1295, 'particular': 5173},	# Número de escolas	# Média de Alunos por escolas
}
