
const product_name = document.getElementById("product_name");
const product_price = document.getElementById("product_price");
const cart = document.getElementById("cart_items");
const payment_btn = document.getElementById("payment-btn");

$("#add_to_cart").click(function(){
    const name = product_name.innerHTML;
    const price = product_price.innerHTML;
    localStorage.setItem(name, price);
    location.reload();
})

$("#clear_cart").click(function(){
    localStorage.clear();
})

// type is either review or cart. Display remove buttons if type is cart
function populate_cart(type){
    cart.innerHTML = "";
    var total_price = 0;

    for (let i = 0; i < localStorage.length; i++) {
        const name = localStorage.key(i);
        const price = localStorage.getItem(name);
        total_price += parseFloat(price.slice(1));
        if (type == "cart"){
            cart.innerHTML += `<p class="padding-l-20 font-weight-bold">${name}:</p>
                                <button id="${name}" type="button" class="btn btn-secondary btn-sm float-right margin-r-20" onclick="remove_from_cart(id);">Remove</button>
                                <p class="padding-l-20">${price}</p>                               
                                <br>`;
        } else {
            cart.innerHTML += `<p class="padding-l-20 font-weight-bold">${name}:</p>
                                <p class="padding-l-20">${price}</p><br>`;
        }
    }
    cart.innerHTML += `<div class="card-footer text-muted"> Total price: &emsp;` + "$" + `${total_price.toFixed(2)}</div>`;

    if (total_price){
        payment_btn.style.display = "inline";
    } else {
        payment_btn.style.display = "none";
    }
}

function remove_from_cart(key){
    localStorage.removeItem(key);
    populate_cart("cart");
}