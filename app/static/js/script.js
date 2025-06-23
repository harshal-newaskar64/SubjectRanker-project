
let progress = document.querySelector(".Progress")

async function fetchMatch() {
    let response = await fetch("/match");
    if (!response.ok) {
        throw new Error(`Server error: ${response.status} ${response.statusText}`);
    }
    const data = await response.json();
    return data.pair;
}



function updateButtons(subjectA, subjectB) {
    const sub1 = document.querySelector("#S1");
    const sub2 = document.querySelector("#S2");

    sub1.innerText = subjectA.name;
    sub1.dataset.subjectId = subjectA.id;

    sub2.innerText = subjectB.name;
    sub2.dataset.subjectId = subjectB.id;
}


async function postVote(winnerID, loserID) {
    const res = await fetch("/vote", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            winner_id: +winnerID,
            loser_id: +loserID
        })
    });
    if (!res.ok) {
        throw new Error(`Vote failed: ${res.status} ${res.statusText}`);
    }
    return res.json();
}


function endSession() {

    document.querySelector('.subjects').style.display = 'none';
    document.getElementById('message').innerText = "Thank you for voting. Session complete!";
    progress.style.display = 'none';


    const revoteBtn = document.createElement('button');
    revoteBtn.innerText = 'Revote';
    revoteBtn.onclick = () => location.reload();

    const seeRankingsBtn = document.createElement('button');
    seeRankingsBtn.innerText = 'See Rankings';
    seeRankingsBtn.onclick = () => window.location.href = '/rankings';

    const buttonRow = document.createElement('div');
    buttonRow.className = 'button-row';

    const container = document.querySelector('.container');
    buttonRow.appendChild(revoteBtn);
    buttonRow.appendChild(seeRankingsBtn);

    container.appendChild(buttonRow);

}


let round = 1;
const maxRounds = 10;


async function nextRound() {
    if (round > maxRounds) {
        endSession();
        return;
    }
    progress.innerText = `${round}/${maxRounds}`;

    const [left, right] = await fetchMatch();

    updateButtons(left, right);

    document.getElementById("S1").onclick = async () => {
        await postVote(left.id, right.id);
        round++;
        nextRound();
    };
    document.getElementById("S2").onclick = async () => {
        await postVote(right.id, left.id);
        round++;
        
        nextRound();
    };

}

nextRound();