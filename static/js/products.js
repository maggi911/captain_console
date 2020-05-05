$(document).ready(function() {
    $("#search-btn").on("click", function(e) {
        e.preventDefault();
        var searchText = $("#search-box").val();
        $.ajax({
            url: "/products?search_filter=" + searchText,
            type: "GET",
            success: function(resp) {
                var newHtml = resp.data.map(d => {
                    return  `<div class="card card-body bg-light product">
                                <a href="/products/${d.id}">
                                    <img class="product-img" src="${d.image}" />
                                    <h4>${d.name}</h4>
                                    <p>${d.description}</p>
                                </a>
                            </div>`
                });
                $(".products").html(newHtml.join(""));
                $("#search-box").val( "");
            },
            error: function(xhr, status, error){
                console.error(error);
            }
        });
    });
});

