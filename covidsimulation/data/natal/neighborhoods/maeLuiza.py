# =============================================================
# Criado por Paulo H. Lopes 2020
# =============================================================

maeLuiza = {
	# =============================================================
	# Dados Demográficos
	'regiao': 'leste',					# Zona ao qual o bairro pertence
	'tamPop': 14191,					# Tamanho da população
	'tamFisico': 95.69,					# Área do bairro em Hectare
	'densidadeDemografica': 149.04,		# Densidade demografica (Hab/km²)
	'numDomicilio': 4070,				# Numero de domicilios
	'domicilio': {'casa': 91.03, 'apartamento': 1.94, 'comodo': 0.39, 'casa de vila ou condominio': 6.6,  'outro': 0},
	'idade': [1743, 2396, 2874, 2111, 2257, 1148, 893, 520, 247],  # Vetor de dados, cada posição é referente a um tipo de dado ->['0-9','10-19','20-29','30-39','40-49','50-59','60-69','70-79','80-']
	'renda': [3.1, 11.23, 28.18, 35.48, 13.1, 2.19, 1.03, 0.69, 0.84, 4.18, 0], # Vetor de dados, cada posição é referente a um tipo de dado ->[Até 1/8 de SM, Mais de 1/8 a 1/4 de SM, Mais de 1/4 a 1/2 SM, Mais de 1/2 a 1 SM, Mais de 1 a 2 SM, Mais de 2 a 3 SM, Mais de 3 a 5 SM, Mais de 5 a 10 SM, Mais de 10 SM, Sem rendimento, Sem declaração]
	'esgoto': {'existe': 31.26, 'naoExiste': 68.74},	# Porcentagem de esgoto a céu aberto
	
	# =============================================================
	# Dados Hospitalares Públicos
	'hospitais': 'vazio',				# Numero de Hospitais, Unidade de pronto atendimento e Unidade básica de saude
	'leitos': 'vazio',			# Numero de leitos dos hospitais
	'uti': 'vazio',				# Número de UTIS do bairro
	'doencasCronicas': 'vazio',	# Numero de pessoas com doenças cronicas
	
	# =============================================================
	# Dados Escolares
	'escolas': {'municipal':4, 'estadual': 4, 'federal': 0,'particular': 2},	# Número de escolas
	'mediaFuncEscola': 'vazio',		# Média de funcionários das escolas
	'mediaAlunosEscola': {'municipal':823, 'estadual': 1116, 'federal': 0,'particular': 366},	# Número de escolas	# Média de Alunos por escolas
}
