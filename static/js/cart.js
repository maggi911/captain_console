
const product_name = document.getElementById("product_name");
const product_price = document.getElementById("product_price");
const cart = document.getElementById("cart_items");
//const product_image = document.getElementById("product_img").innerHTML;

$("#add_to_cart").click(function(){
    const name = product_name.innerHTML;
    const price = product_price.innerHTML;
    localStorage.setItem(name, price);
    location.reload()
})

// type: review or cart
function populate_cart(type){
    cart.innerHTML = ""
    //cart_review.innerHTML = ""
    var total_price = 0
    for (let i = 0; i < localStorage.length; i++) {
        const name = localStorage.key(i);
        const price = localStorage.getItem(name);
        console.log(price.slice(1))
        total_price += parseFloat(price.slice(1));
        if (type == "cart"){
            cart.innerHTML += `<p style="padding-left: 20px; font-weight: bold">${name}:</p>
                                <button id="${name}" type="button" class="btn btn-secondary btn-sm float-right" style="margin-right: 20px" onclick="remove_from_cart(id);">Remove</button>
                                <p style="padding-left: 20px;">${price}</p>                               
                                <br>`;
        } else {
            cart.innerHTML += `<p style="padding-left: 20px; font-weight: bold">${name}:</p>
                                <p style="padding-left: 20px;">${price}</p><br>`;
        }
    }
    console.log(total_price)
    cart.innerHTML += `<div class="card-footer text-muted"> Total price: &emsp;` + "$" + `${total_price.toFixed(2)}</div>`;
}

function remove_from_cart(key){
    localStorage.removeItem(key);
    populate_cart("cart");
}

