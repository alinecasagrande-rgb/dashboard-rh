document.addEventListener('DOMContentLoaded', function () {
    // Função para carregar dados - tenta fetch primeiro, se falhar tenta carregar inline
    function carregarDados() {
        // Tenta carregar via fetch (funciona com servidor HTTP)
        fetch('dados.json')
            .then(response => {
                if (!response.ok) {
                    throw new Error(`Erro HTTP: ${response.status}`);
                }
                return response.json();
            })
            .then(data => {
                inicializarDashboard(data);
            })
            .catch(error => {
                console.warn("Erro ao carregar via fetch, tentando carregar dados inline...", error);
                // Se falhar, tenta carregar dados inline do script tag
                if (window.dadosDashboard) {
                    inicializarDashboard(window.dadosDashboard);
                } else {
                    // Última tentativa: carregar do arquivo usando XMLHttpRequest (funciona com file://)
                    carregarDadosXMLHttp();
                }
            });
    }
    
    // Função alternativa usando XMLHttpRequest (funciona melhor com file://)
    function carregarDadosXMLHttp() {
        const xhr = new XMLHttpRequest();
        xhr.open('GET', 'dados.json', true);
        xhr.onreadystatechange = function() {
            if (xhr.readyState === 4) {
                if (xhr.status === 200 || xhr.status === 0) { // 0 para file://
                    try {
                        const data = JSON.parse(xhr.responseText);
                        inicializarDashboard(data);
                    } catch (e) {
                        mostrarErro('Erro ao processar dados JSON: ' + e.message);
                    }
                } else {
                    mostrarErro('Erro ao carregar dados.json. Certifique-se de que o arquivo está na mesma pasta.');
                }
            }
        };
        xhr.onerror = function() {
            mostrarErro('Erro de rede ao carregar dados.json. Verifique se o arquivo existe na mesma pasta que index.html');
        };
        xhr.send(null);
    }
    
    function inicializarDashboard(data) {
        // Esconde mensagem de carregamento e mostra conteúdo
        document.getElementById('loading-message').classList.add('hidden');
        document.getElementById('content-visao-geral').classList.remove('hidden');
        
        // Inicializa o dashboard com os dados carregados
        initializeDashboard(data);
    }
    
    function mostrarErro(mensagem) {
        console.error("Erro ao carregar dados:", mensagem);
        document.getElementById('loading-message').classList.add('hidden');
        document.getElementById('error-message').classList.remove('hidden');
        document.getElementById('error-text').textContent = mensagem;
    }
    
    // Inicia o carregamento
    carregarDados();

    const chartColors = {
        primary: '#1e3a8a', // Azul Escuro
        primaryLight: 'rgba(30, 58, 138, 0.1)',
        secondary: '#1d4ed8', // Azul Médio
        secondaryLight: 'rgba(29, 78, 216, 0.1)',
        green: '#059669',
        greenLight: 'rgba(5, 150, 105, 0.1)',
        red: '#dc2626',
        redLight: 'rgba(220, 38, 38, 0.1)',
    };
    
    // Opções padrão para gráficos
    const defaultChartOptions = {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
            legend: { position: 'bottom', labels: { usePointStyle: true, padding: 20 } },
            tooltip: { 
                backgroundColor: '#fff', 
                titleColor: '#1f2937', 
                bodyColor: '#4b5563', 
                borderColor: '#e5e7eb', 
                borderWidth: 1, 
                padding: 10, 
                cornerRadius: 4,
                displayColors: true,
                boxPadding: 4
            }
        },
        scales: {
            x: { grid: { display: false } },
            y: { grid: { color: '#f3f4f6' }, beginAtZero: true }
        }
    };
    
    // Opções para gráficos de barras horizontais
    const horizontalBarOptions = {
        ...defaultChartOptions,
        indexAxis: 'y',
        scales: {
            x: { grid: { color: '#f3f4f6' }, beginAtZero: true },
            y: { grid: { display: false } }
        }
    };

    function initializeDashboard(data) {
        const ultimoIndice = data.labels.length - 1;
        const ultimoMes = data.labels[ultimoIndice];
        const ultimoMesCapitalized = ultimoMes.charAt(0).toUpperCase() + ultimoMes.slice(1);
        const ano = new Date().getFullYear();

        function updateTitles() {
            document.getElementById('kpi-competencia').textContent = `${ultimoMesCapitalized} de ${ano}`;
            document.getElementById('estabelecimento-chart-title').textContent = `Colaboradores por Estabelecimento (${ultimoMesCapitalized})`;
            document.getElementById('pcd-card-title').textContent = `Total de Colaboradores PCD (${ultimoMesCapitalized})`;
            document.getElementById('aprendiz-card-title').textContent = `Total de Aprendizes (${ultimoMesCapitalized})`;
            document.getElementById('turnover-chart-title').textContent = `Turnover por Estabelecimento (%) - ${ultimoMesCapitalized}`;
            document.getElementById('turnover-table-title').textContent = `Dados de Turnover - ${ultimoMesCapitalized}`;
        }

        function initKPIs() {
            document.getElementById('kpi-total-colaboradores').textContent = Math.round(data.colaboradores.totais[ultimoIndice]);
            document.getElementById('kpi-total-admissoes').textContent = Math.round(data.admitidos.totais[ultimoIndice]);
            document.getElementById('kpi-total-desligamentos').textContent = Math.round(data.desligados.totais[ultimoIndice]);
            document.getElementById('kpi-total-pcd').textContent = Math.round(data.pcd.totais[ultimoIndice]);
            document.getElementById('kpi-total-aprendizes').textContent = Math.round(data.aprendizes.totais[ultimoIndice]);
        }
        
        // --- FUNÇÕES DE CRIAÇÃO DE GRÁFICOS ---
        
        function createAdmissoesDesligamentosChart() {
            const ctx = document.getElementById('admissoesDesligamentosChart').getContext('2d');
            new Chart(ctx, { 
                type: 'line', 
                data: { 
                    labels: data.labels, 
                    datasets: [
                        { label: 'Admissões', data: data.admitidos.totais, borderColor: chartColors.green, backgroundColor: chartColors.greenLight, fill: true, tension: 0.3, pointBackgroundColor: chartColors.green }, 
                        { label: 'Desligamentos', data: data.desligados.totais, borderColor: chartColors.red, backgroundColor: chartColors.redLight, fill: true, tension: 0.3, pointBackgroundColor: chartColors.red }
                    ] 
                }, 
                options: defaultChartOptions 
            });
        }
        
        function createColaboradoresEstabelecimentoChart() {
            const dadosUltimoMes = data.colaboradores.dados.map(d => d[ultimoIndice]);
            const ctx = document.getElementById('colaboradoresEstabelecimentoChart').getContext('2d');
            new Chart(ctx, { 
                type: 'bar', 
                data: { 
                    labels: data.colaboradores.estabelecimentos, 
                    datasets: [{ 
                        label: `Colaboradores em ${ultimoMesCapitalized}`, 
                        data: dadosUltimoMes, 
                        backgroundColor: chartColors.secondaryLight, 
                        borderColor: chartColors.secondary, 
                        borderWidth: 1 
                    }] 
                }, 
                options: {...defaultChartOptions, plugins: { ...defaultChartOptions.plugins, legend: { display: false } }} 
            });
        }
        
        function createGenderDistributionChart() {
            const ctx = document.getElementById('genderDistributionChart').getContext('2d');
            if (!data.demographics.gender || data.demographics.gender.labels.length === 0) {
                ctx.canvas.parentNode.innerHTML = '<p class="text-center text-gray-500">Dados de "Funcionários por gênero" não encontrados.</p>';
                return;
            }
            new Chart(ctx, { 
                type: 'doughnut', 
                data: { 
                    labels: data.demographics.gender.labels, 
                    datasets: [{ 
                        label: 'Gênero', 
                        data: data.demographics.gender.data, 
                        backgroundColor: [chartColors.primary, chartColors.secondary], 
                        hoverOffset: 4,
                        borderWidth: 0
                    }] 
                }, 
                options: {...defaultChartOptions, scales: { x: { display: false }, y: { display: false } } } 
            });
        }
        
        function createAgeDistributionChart() {
            const ctx = document.getElementById('ageDistributionChart').getContext('2d');
             if (!data.demographics.ageRange || data.demographics.ageRange.labels.length === 0) {
                ctx.canvas.parentNode.innerHTML = '<p class="text-center text-gray-500">Dados de "Funcionários por Faixa Etária" não encontrados.</p>';
                return;
            }
            new Chart(ctx, { 
                type: 'bar', 
                data: { 
                    labels: data.demographics.ageRange.labels, 
                    datasets: [{ 
                        label: 'Nº de Colaboradores', 
                        data: data.demographics.ageRange.data, 
                        backgroundColor: chartColors.primaryLight, 
                        borderColor: chartColors.primary, 
                        borderWidth: 1 
                    }] 
                }, 
                options: { ...horizontalBarOptions, plugins: { ...horizontalBarOptions.plugins, legend: { display: false } } } 
            });
        }

        function createSimpleLineChart(canvasId, datasetLabel, datasetData, color) {
             const ctx = document.getElementById(canvasId).getContext('2d');
             new Chart(ctx, { 
                 type: 'line', 
                 data: { 
                     labels: data.labels, 
                     datasets: [{ 
                         label: datasetLabel, 
                         data: datasetData, 
                         borderColor: color.primary, 
                         backgroundColor: color.primaryLight, 
                         fill: true, 
                         tension: 0.3,
                         pointBackgroundColor: color.primary
                     }] 
                 }, 
                 options: defaultChartOptions 
             });
        }
        
        function createSimpleBarChart(canvasId, datasetLabel, datasetData, color) {
            const ctx = document.getElementById(canvasId).getContext('2d');
             new Chart(ctx, { 
                 type: 'bar', 
                 data: { 
                     labels: data.labels, 
                     datasets: [{ 
                         label: datasetLabel, 
                         data: datasetData, 
                         backgroundColor: color.light, 
                         borderColor: color.dark, 
                         borderWidth: 1 
                     }] 
                 }, 
                 options: defaultChartOptions 
             });
        }

        // --- FUNÇÕES DE CRIAÇÃO DE TABELAS ---

        function createTable(container, headers, rows, title) {
            let tableHTML = `<table class="w-full">`;
            tableHTML += '<thead><tr>';
            headers.forEach(h => { tableHTML += `<th scope="col" class="px-4 py-3 text-left">${h}</th>`; });
            tableHTML += '</tr></thead>';
            
            tableHTML += '<tbody>';
            rows.forEach(row => {
                tableHTML += `<tr>`;
                row.forEach((cell, index) => {
                    const cellClass = index === 0 ? 'px-4 py-2 font-medium text-gray-900 whitespace-nowrap' : 'px-4 py-2 text-center';
                    tableHTML += `<td class="${cellClass}">${cell}</td>`;
                });
                tableHTML += `</tr>`;
            });
            tableHTML += '</tbody></table>';

            if (title) {
                // Cria um novo elemento div para cada tabela (evita duplicação)
                const tableDiv = document.createElement('div');
                tableDiv.className = 'segment-table';
                tableDiv.innerHTML = `<h3 class="text-lg font-semibold text-gray-800 mb-3">${title}</h3>${tableHTML}`;
                container.appendChild(tableDiv);
            } else {
                container.innerHTML = tableHTML;
            }
        }

        function createColaboradoresEstabelecimentoTable() {
            const headers = ["Estab.", ...data.labels.map(l => l.substring(0,3))];
            const rows = data.colaboradores.estabelecimentos.map((label, index) => {
                return [label, ...data.colaboradores.dados[index].map(val => Math.round(val))];
            });
            rows.push(["Total", ...data.colaboradores.totais.map(val => `<strong class="text-gray-900">${Math.round(val)}</strong>`)]);
            createTable(document.getElementById('colaboradoresEstabelecimentoTable'), headers, rows);
        }

        function createEvolutionTable() {
            const container = document.getElementById('evolutionTable');
            container.innerHTML = ''; // Limpa a tabela
            
            const headers = ["Métrica", ...data.labels.map(l => l.substring(0,3))];
            let tableHTML = `<thead><tr>`;
            headers.forEach(h => { tableHTML += `<th scope="col" class="px-4 py-3 text-left">${h}</th>`; });
            tableHTML += `</tr></thead><tbody>`;

            const allData = [
                { title: 'COLABORADORES', metric: 'colaboradores' }, 
                { title: 'ADMISSÕES', metric: 'admitidos' }, 
                { title: 'DESLIGAMENTOS', metric: 'desligados' }
            ];

            allData.forEach(item => {
                tableHTML += `<tr class="header-row"><th colspan="${headers.length}">${item.title}</th></tr>`;
                const metricData = data[item.metric];
                const estabelecimentos = metricData.estabelecimentos || data.colaboradores.estabelecimentos;
                estabelecimentos.forEach((label, i) => {
                    const rowData = metricData.dados[i] || [];
                    tableHTML += `<tr><td class="px-4 py-2 font-medium text-gray-900 whitespace-nowrap">Est. ${label}</td>`;
                    data.labels.forEach((_, j) => {
                        tableHTML += `<td class="px-4 py-2 text-center">${rowData[j] ? Math.round(rowData[j]) : 0}</td>`;
                    });
                    tableHTML += `</tr>`;
                });
                tableHTML += `<tr class="total-row"><td class="px-4 py-2 font-bold">Total ${item.title}</td>`;
                metricData.totais.forEach(v => { tableHTML += `<td class="px-4 py-2 text-center font-bold">${v ? Math.round(v) : 0}</td>`; });
                tableHTML += `</tr>`;
            });
            
            tableHTML += `</tbody>`;
            container.innerHTML = tableHTML;
        }
        
        function createDynamicEvolutionTable(container, title, metricData) {
            if (!metricData || !metricData.labels || metricData.labels.length === 0) {
                container.innerHTML += `<div class="segment-table"><h3 class="text-lg font-semibold text-gray-800 mb-3">${title}</h3><p class="text-gray-500">Dados não encontrados no arquivo.</p></div>`;
                return;
            }
            const headers = [title.includes('Gerente') ? 'Gerente' : 'Centro de Custo', ...data.labels.map(l => l.substring(0,3))];
            const rows = metricData.labels.map((label, index) => {
                return [label, ...metricData.dados[index].map(val => Math.round(val))];
            });
            createTable(container, headers, rows, title);
        }

        function createGerentesEvolutionTable() {
            const container = document.getElementById('gerentesEvolutionTable');
            container.innerHTML = '';
            createDynamicEvolutionTable(container, 'Total de Colaboradores por Gerente', data.porGerenteEvolucao.colaboradores);
            createDynamicEvolutionTable(container, 'Admissões por Gerente', data.porGerenteEvolucao.admissoes);
            createDynamicEvolutionTable(container, 'Demissões por Gerente', data.porGerenteEvolucao.demissoes);
        }

        function createSegmentoEvolutionTable() {
            const container = document.getElementById('segmentoEvolutionTable');
            container.innerHTML = '';
            createDynamicEvolutionTable(container, 'Total de Colaboradores por Segmento', data.porSegmentoEvolucao.colaboradores);
        }

        function createTurnoverSection() {
            const ctx = document.getElementById('turnoverChart').getContext('2d');
            new Chart(ctx, { 
                type: 'bar', 
                data: { 
                    labels: data.turnover.labels, 
                    datasets: [{ 
                        label: `Turnover em ${ultimoMesCapitalized}`, 
                        data: data.turnover.rates, 
                        backgroundColor: chartColors.primaryLight, 
                        borderColor: chartColors.primary, 
                        borderWidth: 1 
                    }] 
                },
                options: { 
                    ...defaultChartOptions, 
                    plugins: { 
                        ...defaultChartOptions.plugins, 
                        legend: { display: false },
                        tooltip: { 
                            ...defaultChartOptions.plugins.tooltip,
                            callbacks: { label: (context) => `${context.dataset.label || ''}: ${context.parsed.y.toFixed(2)}%` } 
                        } 
                    }, 
                    scales: { 
                        ...defaultChartOptions.scales, 
                        y: { ...defaultChartOptions.scales.y, ticks: { callback: (value) => `${value}%` } } 
                    } 
                }
            });

            const container = document.getElementById('turnoverTable');
            const headers = ["Estabelecimento/Total", "Turnover (%)"];
            const rows = data.turnover.labels.map((label, index) => {
                const cellValue = data.turnover.rates[index].toFixed(2) + '%';
                return label === 'TOTAL' ? [`<strong>${label}</strong>`, `<strong>${cellValue}</strong>`] : [label, cellValue];
            });
            createTable(container, headers, rows);
        }

        // --- NAVEGAÇÃO ---
        const navLinks = document.querySelectorAll('.nav-link');
        const contentSections = document.querySelectorAll('.content-section');
        navLinks.forEach(link => {
            link.addEventListener('click', (e) => {
                e.preventDefault();
                navLinks.forEach(l => l.classList.remove('active'));
                link.classList.add('active');
                // Remove o prefixo 'nav-' do ID do link para construir o targetId correto
                const sectionName = link.id.replace('nav-', '');
                const targetId = 'content-' + sectionName;
                contentSections.forEach(section => { 
                    section.id === targetId ? section.classList.remove('hidden') : section.classList.add('hidden'); 
                });
                window.scrollTo(0, 0); // Rola para o topo ao trocar de aba
            });
        });

        // --- CHAMADAS DE INICIALIZAÇÃO ---
        updateTitles();
        initKPIs();
        createAdmissoesDesligamentosChart();
        createGenderDistributionChart();
        createAgeDistributionChart();
        createColaboradoresEstabelecimentoChart();
        createSimpleLineChart('totalColaboradoresChart', 'Total de Colaboradores', data.colaboradores.totais, {primary: chartColors.primary, primaryLight: chartColors.primaryLight});
        createColaboradoresEstabelecimentoTable();
        createSimpleBarChart('admissoesChart', 'Admissões', data.admitidos.totais, {dark: chartColors.green, light: chartColors.greenLight});
        createSimpleBarChart('desligamentosChart', 'Desligamentos', data.desligados.totais, {dark: chartColors.red, light: chartColors.redLight});
        createEvolutionTable();
        createGerentesEvolutionTable();
        createSegmentoEvolutionTable();
        createTurnoverSection();
    }
});

