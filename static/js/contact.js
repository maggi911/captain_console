
function check_contact_input(){
    var name = document.getElementById("contact-name");
    var address = document.getElementById("contact-address");
    var city = document.getElementById("contact-city");
    var payment_btn = document.getElementById("go-to-payment");

    var valid_name = check_name(name);
    var valid_address = check_address(address);
    var valid_city = check_city(city);

    if (valid_name && valid_address && valid_city){
        return payment_btn.href = "payment_info"
    }
}

function check_name(name){
    var name_req = document.getElementById("cn-req");
    name_req.innerHTML = "";

    if (name.value.length == 0){
        name_req.innerHTML = "Required"
        return false;
    } else {
        return true;
    }
}

function check_address(address){
    var address_req = document.getElementById("ca-req")
    address_req.innerHTML = ""

    if (address.value.length == 0){
        address_req.innerHTML = "Required"
        return false;
    } else {
        return true;
    }
}

function check_city(city){
    var city_req = document.getElementById("ccity-req");
    city_req.innerHTML = "";

    if (city.value.length == 0){
        city_req.innerHTML = "Required"
        return false;
    } else {
        return true;
    }
}