
const product_name = document.getElementById("product_name");
const product_price = document.getElementById("product_price");
const cart = document.getElementById("cart_items");
//const product_image = document.getElementById("product_img").innerHTML;
//const btn_add_to_cart = document.getElementById("add_to_cart");
//const btn_open_cart = document.getElementById("open_cart");

$("#add_to_cart").click(function(){
    console.log("hello")
    const name = product_name.innerHTML;
    const price = product_price.innerHTML;
    localStorage.setItem(name, price);
    location.reload()
})

function populate_cart(){
    cart.innerHTML = ""
    for (let i = 0; i < localStorage.length; i++) {
        const name = localStorage.key(i);
        const price = localStorage.getItem(name);
        cart.innerHTML += `<button id="${name}" type="button" class="btn btn-secondary btn-sm" onclick="remove_from_cart(id);">Remove</button> ${name}:&emsp; ${price} <br />`;
    }
}

function remove_from_cart(key){
    localStorage.removeItem(key);
    populate_cart();
}


