const parametros = new URLSearchParams(window.location.search);
const gameId = parametros.get("id");

const capas = {
    "Red Dead Redemption 2": "imagens/rdr2.jpg",
    "The Last of Us Part II": "imagens/tlou2.jpeg",
    "Cyberpunk 2077": "imagens/cyberpunk2077.jpg",
    "Shadow of the Colossus": "imagens/sotc.jpg",
    "Death Stranding": "imagens/deathstranding.jpg"
};

const iconesCategorias = {
    "Troféus": "🏆",
    "Missões": "📖",
    "Animais": "🦌",
    "Infectados": "🧟",
    "Colecionáveis": "🗺️",
    "Finais": "🔚",
    "Colossos": "🗿",
    "Time Attack": "⏱️",
    "Estruturas": "🏗️"
};

async function carregarJogo() {
    const resposta = await fetch(`http://127.0.0.1:8000/games/${gameId}`);
    const game = await resposta.json();
    document.body.className = "";
    switch (game.nome) {
        case "Red Dead Redemption 2":
            document.body.classList.add("tema-rdr2");
            break;
        case "The Last of Us Part II":
            document.body.classList.add("tema-tlou2");
            break;
        case "Cyberpunk 2077":
            document.body.classList.add("tema-cyberpunk2077");
            break;
        case "Shadow of the Colossus":
            document.body.classList.add("tema-sotc");
            break;
        case "Death Stranding":
            document.body.classList.add("tema-deathstranding");
            break;
    }
    document.getElementById("header-jogo").innerHTML = `

    <h1>${game.nome}</h1>

    `;

    document.getElementById("informacoes-jogo").innerHTML = `

    <img src="${capas[game.nome]}" class="capa-game">

    <h2>${game.nome}</h2>

    <p><strong>Desenvolvedora:</strong> ${game.desenvolvedora}</p>
    <p><strong>Ano:</strong> ${game.ano}</p>
    <p>${game.descricao}</p>

    `;
}

async function carregarGuides() {
    const resposta = await fetch (`http://127.0.0.1:8000/games/${gameId}/guides`);
    const guides = await resposta.json();
    const lista = document.getElementById("lista-guides");

    lista.innerHTML = "";

    if (guides.length === 0) {
        lista.innerHTML = "<p>Este jogo ainda não possui guias.</p>";
        return;
    }

    guides.forEach(guide => {
        lista.innerHTML += `
        <div class="card-guide"
        onclick="carregarItensGuia(${guide.id})">

        <h3>${guide.titulo}</h3>

        <p><strong>Categoria:</strong> ${guide.categoria}</p>
        <p>${guide.conteudo}</p>

        </div>

        `;
    });
}

async function carregarCategoria(categoria) {
    const resposta = await fetch(`http://127.0.0.1:8000/games/${gameId}/guides/${categoria}`);

    const guides = await resposta.json();
    const lista = document.getElementById("lista-guides");

    lista.innerHTML = "";

    if (guides.length === 0){
        lista.innerHTML = "<p>Nenhum guia encontrado nesta categoria.</p>";
        return;
    }

    guides.forEach(guide => {
        lista.innerHTML += `
        <div class="card-guide"
        onclick="carregarItensGuia(${guide.id})">

        <h3>${guide.titulo}</h3>

        <p><strong>Categoria:</strong> ${guide.categoria}</p>
        <p>${guide.conteudo}</p>

        </div>
        `;
    })
}

async function carregarCategorias() {
    const resposta = await fetch(`http://127.0.0.1:8000/games/${gameId}/categorias`);
    const categorias = await resposta.json();
    const menu = document.getElementById("menu-guias");
    menu.innerHTML = "";
    categorias.forEach(categoria => {
        const botao = document.createElement("button");
        const icone = iconesCategorias[categoria] || "🎮";
        botao.innerHTML = `${icone} ${categoria}`;
        botao.onclick = () => carregarCategoria(categoria);
        menu.appendChild(botao);
    });
}

carregarJogo();
carregarCategorias();
carregarGuides();

async function carregarItensGuia(guideId) {
    const resposta = await fetch(`http://127.0.0.1:8000/guides/${guideId}/items`);
    const itens = await resposta.json();
    const lista = document.getElementById("lista-guides");

    lista.innerHTML = "";
    itens.forEach(item => {
        lista.innerHTML += `
        <div class="card-guide" onclick="abrirItem(${item.id})">
        <h3>${item.titulo}</h3>
        <p>${item.tipo}</p>
        <p>${item.descricao}</p>

        </div>
        `;
    });

}

function abrirItem(itemId){
    window.location.href = `item.html?id=${id}`;
}