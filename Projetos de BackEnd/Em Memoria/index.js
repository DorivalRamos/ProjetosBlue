const express = require("express");
const app = express();

app.use(express.json());

const port = 3000;

const listJogos = [
    {
        nome: "God of War 4",
        imagem : "https://cdn.awsli.com.br/600x700/1610/1610163/produto/62283088/5a770f7cc2.jpg",
        id : 1
    },
    {
        nome: "Persona 5",
        imagem : "https://image.api.playstation.com/vulcan/img/cfn/113073qYZHyiDU5-4vu9krqfIPdGCvcGob0VpazrmfyUEbn4qZ64XBJfRKHvwa_tStB4nMD3UDv4Cb9V3iTH6cJymhQ1sJiU.png",
        id: 2
    },
    {
        nome: "Destiny 2",
        imagem: "http://guiadecompras.casasbahia.com.br/imagens/2017/12/Destiny-2-Official-Reveal-Art.jpg",
        id: 3
    },
    {
        nome : "Doom Eternal",
        imagem: "https://xboxplay.games/uploadStream/11781.jpg",
        id: 4
    },
    {
        nome : "Days Gone",
        imagem: "https://image.api.playstation.com/vulcan/ap/rnd/202011/0921/B7jV8ThPs8eqDz8NRRllf7g6.jpg",
        id: 5
    },
    {
        nome: "BoodBorn",
        imagem : "https://image.api.playstation.com/cdn/UP9000/CUSA00900_00/b5uuNMulpxnRpWZDG7lPexwMY7i9Pns7.png",
        id: 6
    }

];

const getJogosValidos = () => listaJogos.filter(Boolean);

const getJogosById = id => getJogosValidos.find(a => a.id === a.id);

const getJogosIndexById = id => getJogosValidos.findIndex(a => a.id === id);

//Rota Get / - home
app.get("/", (req,res)=>{
    res.status(200).send("Hollo World");
});



app.get('/jogos',  (req, res) => {
    res.send({listaJogos: listJogos  })
  });

app.get("/jogos/:id", (req,res)=>{
    const id = +req.params.id;
    const jogos =getJogosById(id);
    !jogos ? res.status(404).send({error : 'Jogo não existe'}) : res.json({jogos})
});


app.post("/jogos", (req,res)=>{
    const jogo = req.body;

    if(!jogo || !jogo.nome || !jogo.imagem){
        res.status(404).send({error : 'Jogo Invalido'})
    };

    const lastJogo = listJogos[listJogos.length - 1]

    if (listJogos.length){
        jogo.id = lastJogo.id +1;
        listJogos.push(jogo)       
    } else {
        jogo.id = 1,
        listJogos.push(jogo)
    };
    res.status(201).send({res : "Jogo inserido com sucesso!"})
});

app.put("/jogos/:id", (req,res)=>{
    const id = +req.params.id;
    const jogoIndex = getJogosIndexById(id); 
    
    if (jogoIndex < 0) {
        res.status(404).send({error : "Jogo não encontrado"});
        return;    
    }
    
    const novoJogo = req.body;
    if(!jogo || !jogo.nome || !jogo.imagem){
        res.status(404).send({error : 'Jogo Invalido'})
    };

    
    const jogo = getJogosById(id);

    novoJogo.id = jogo.id;

    listaJogos[jogoIndex] = novoJogo;

    res.status(200).send({status : 'Jogo alterado com sucesso!!'})
});

app.delete("/jogos/:id",(req,res)=>{
    const id = +req.params.id;
    
    const jogoIndex = getJogosIndexById(id);
    
    if (jogoIndex < 0 ){
        res.status(404).send({error : "Jogo não encontrado"});
        return;
    }

    listaJogos.splice(jogoIndex, 1);
    
    res.send({message : 'Jogo deletado com sucesso!!'})
});

app.listen(port, () =>{
    console.log(`Servidor rodando no localhost:${port}`)
})
