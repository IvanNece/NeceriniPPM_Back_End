function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');


let btns = document.querySelectorAll(".addToCartContainer button");

btns.forEach(btn => {
    btn.addEventListener("click", addToCart);
});

function addToCart(e) {
    let item_id = e.target.value;
    let url = "/addToCart/";

    let data = { id: item_id };
    
    fetch(url, {
        method: "POST",
        headers: { "Content-Type": "application/json", 'X-CSRFToken': csrftoken,},
        body: JSON.stringify(data),
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("numOfItems").innerHTML = data;
        console.log(data);
    })
    .catch(err => { console.log(err); })
}



// Aggiungi il seguente codice per associare il gestore di eventi al pulsante del cestino
let removeBtns = document.querySelectorAll("button[data-item-id]");

removeBtns.forEach(btn => {
    btn.addEventListener("click", removeFromCart);
});


function removeFromCart(e) {
    let item_id = e.currentTarget.getAttribute('data-item-id');
    let url = "/removeFromCart/";

    let data = { id: item_id };

    fetch(url, {
        method: "POST",
        headers: { "Content-Type": "application/json", 'X-CSRFToken': csrftoken },
        body: JSON.stringify(data),
    })
    .then(response => {
        if (response.ok) {
            return response.json();
        } else {
            throw new Error('Error: ' + response.status);
        }
    })
    .then(data => {
        document.getElementById("numOfItems").innerHTML = data;
        console.log(data);
    })
    .catch(err => { console.log(err); });
}
