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
        console.log(data);
    })
    .catch(err => {console.log(error);})
}
