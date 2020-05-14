
// payment_info input validation
function only_num(e_id){
    var elem = document.getElementById( e_id );
    var res = elem.value;

    if (res != ""){
        if (isNaN(res)){
            elem.value = res.slice(0, -1);
            return false;
        }
    }

    if (e_id == "cc-month"){
        return check_month_input(elem);
    }
}

// no numbers in name
function no_num(e_id){
    var elem = document.getElementById( e_id );
    var res = elem.value;

    if (res != ""){
        if (res[res.length - 1] == " " || isNaN(res[res.length - 1])){
            return true;
        } else {
            elem.value = res.slice(0, -1);
            return false;
        }
    }
}

// month input check 01 <= n <= 12
function check_month_input(elem){
    var res = elem.value;

    if (res.length == 2){
        if (res < 1 || res > 12){
            elem.value = "";
            return false;
        } else {
            return true;
        }
    }
    return true;
}

function check_valid_input(){
    var pay_btn = document.getElementById("pay-btn");
    var cc_name = document.getElementById("cc-name");
    var cc_number = document.getElementById("cc-number");
    var cc_cvv = document.getElementById("cc-cvv");
    var cc_year = document.getElementById("cc-year");
    var cc_month = document.getElementById("cc-month");

    var valid_name = check_valid_name(cc_name);
    var valid_number = check_valid_number(cc_number);
    var valid_year = check_valid_year(cc_year);
    var valid_month = check_valid_month(cc_month);
    var valid_cvv = check_valid_cvv(cc_cvv);

    if (valid_name && valid_number && valid_year && valid_month && valid_cvv) {
        return pay_btn.href = "payment_review"
    }
}

function check_valid_name(cc_name){
    var name_req = document.getElementById("name-req");
    name_req.innerHTML = "";

    if (cc_name.value == ""){
        name_req.innerHTML = "Required";
        return false;
    } else {
        return true;
    }
}

function check_valid_number(cc_number){
    var number_req = document.getElementById("number-req");
    number_req.innerHTML = "";

    if (cc_number.value.length != 16){
        number_req.innerHTML = "Required (16 digits)"
        return false;
    } else {
        return true;
    }
}

function check_valid_month(cc_month){
    var month_req = document.getElementById("month-req");
    month_req.innerHTML = "";

    if (cc_month.value.length != 2){
        month_req.innerHTML = "Required";
        return false;
    } else {
        return true;
    }
}

function check_valid_year(cc_year){
    var year_req = document.getElementById("year-req");
    year_req.innerHTML = "";

    if (cc_year.value.length != 2){
        year_req.innerHTML = "Required";
        return false;
    } else {
        return true;
    }
}

function check_valid_cvv(cc_cvv){
    var cvv_req = document.getElementById("cvv-req");
    cvv_req.innerHTML = "";

    if (cc_cvv.value.length != 3){
        cvv_req.innerHTML = "Required";
        return false;
    } else {
        return true;
    }
}