async function carregarGames() {
    const resposta = await fetch("http://127.0.0.1:8000/games");
    const games = await resposta.json();
    const lista = document.getElementById("lista-games");

    lista.innerHTML = "";
    games.forEach(game => {

        let classe = "";

        switch(game.nome) {
            case "Red Dead Redemption 2":
                classe = "rdr2";
                break;
            case "The Last of Us Part II":
                classe = "tlou2";
                break;
            case "Cyberpunk 2077":
                classe = "cyberpunk2077";
                break;
            case "Shadow of the Colossus":
                classe = "sotc";
                break;
            case "Death Stranding":
                classe = "deathstranding";
                break;
            case "Grand Theft Auto VI":
                classe = "gtavi";
                break;
        }

        lista.innerHTML += `
        <div class="card-game ${classe}" onclick="abrirJogo(${game.id})">

        <img src="${capas[game.nome]}"
        alt="${game.nome}"
        class="capa-game"

        >

        <h3>${game.nome}</h3>

        <p><strong>Desenvolvedora:</strong> ${game.desenvolvedora}</p>
        <p><strong>Ano:</strong> ${game.ano}</p>
        <p>${game.descricao}</p>

        </div>
    `;

    });
}

const capas = {
    "Red Dead Redemption 2": "imagens/rdr2.jpg",
    "The Last of Us Part II": "imagens/tlou2.jpeg",
    "Cyberpunk 2077": "imagens/cyberpunk2077.jpg",
    "Shadow of the Colossus": "imagens/sotc.jpg",
    "Death Stranding": "imagens/deathstranding.jpg",
    "Grand Theft Auto VI": "imagens/gtavi.jpg"
};

carregarGames();

async function carregarGuides(gameId){
    const resposta = await fetch(`http://127.0.0.1:8000/games/${gameId}/guides`);
    const guides = await resposta.json();
    const lista = document.getElementById("lista-guides");
    lista.innerHTML = "";
    if (guides.length === 0) {
        lista.innerHTML = "<p>Este jogo ainda não possui guias cadastrados.</p>";
        return;
    }

    guides.forEach(guide => { 
        lista.innerHTML += `
        <div class="card-guide">

        <h3>${guide.titulo}</h3>

        <p><strong>Categoria:</strong> ${guide.categoria}</p>

        <p>${guide.conteudo}</p>

        </div>
        `;
    });
}

function abrirJogo(id){
    window.location.href = `jogo.html?id=${id}`;
}