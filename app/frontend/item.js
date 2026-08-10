const parametros = new URLSearchParams(window.location.search);
const itemId = parametros.get("id");

async function carregarItem(){
    const resposta = await fetch(`http://127.0.0.1:8000/guide-items/${itemId}`);
    const item = await resposta.json();
    let classe = "";
    switch(item.game_nome){
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
    document.body.className = `tema-${classe}`;
    document.getElementById("header-item").innerHTML = `
    <h1>${item.titulo}</h1>
    `;
    document.getElementById("informacoes-item").className = `informacoes-item ${classe}`;
    document.getElementById("informacoes-item").innerHTML = `
    <h2>${item.titulo}</h2>
    <p><strong>Tipo:</strong> ${item.tipo}</p>
    <p>${item.descricao}</p>
    `;
    let video = item.video_url;
    if (video.includes("watch?v=")){
        video = video.replace("watch?v=", "embed/");
    }
    document.getElementById("video-item").innerHTML = `
    <h2>Vídeo</h2>
    <iframe width="100%" height="500" src="${video}" title="Tutorial" frameborder="0" allowfullscreen></iframe>
    `;
}
carregarItem();