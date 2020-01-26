function delivery(value, id) {
    document.getElementById("form_delivery").value = parseInt(value).toFixed(2);
    var summary = document.getElementById("purchaseSummary");
    var delivery_option = document.getElementById("DeliveryOption");
    var subtotal = document.getElementById("subtotal").innerHTML;
    var total_price = document.getElementById("TotalPrice");
    summary.style.display = "";
    delivery_option.innerHTML = "&pound;" + parseInt(value).toFixed(2);
    var new_price = parseInt(value) + parseFloat(subtotal);
    total_price.innerHTML = "&pound;" + new_price.toFixed(2);
    if (id != "collect") {
        document.getElementById("cashButton").style.display = "none";
        document.getElementById("Howtopay").style.display = "none";
        document.getElementById("proceedToPayment").style.display = "";

    } else {
        document.getElementById("cashButton").style.display = "";
        document.getElementById("Howtopay").style.display = "";
        document.getElementById("proceedToPayment").style.display = "none";
    }
    document.getElementById("paymentDetails").style.display = "none";

}

function cardFunction() {
		var x = document.getElementById("paymentDetails");
		if (x.style.display === "none") {
			x.style.display = "block";
		}
	}


function cashFunction() {
	var x = document.getElementById("paymentDetails");
		if (x.style.display === "block") {
			x.style.display = "none";
		}

}

function enablepay() {
    var cardNumber = document.getElementById("cardNumber").value;
    var expiryDate = document.getElementById("expirydate").value;
    var cvv = document.getElementById("cvv").value;
    var str = expiryDate.split("/");
    document.getElementById("confirm-purchase").disabled = true;

    if (cardNumber.length == 16) {
        if (Number.isInteger(Number(cardNumber)) == true) {
            if (str.length == 2) {
        var mm = Number(str[0]);
        var yyyy = Number(str[1]);
        if ((Number.isInteger(mm) == true) && (Number.isInteger(yyyy) == true)) {
            if ((mm > 0) && (mm < 13) && (yyyy > 2019) && (yyyy < 2040)) {
                if (cvv.length == 3) {
            if (Number.isInteger(Number(cvv)) == true) {
                document.getElementById("confirm-purchase").disabled = false;
            }
        }
            }
        }
    }
        }

    }
}

function invalid(x) {
    var cardNumber = document.getElementById("cardNumber").value;
    var expiryDate = document.getElementById("expirydate").value;
    var cvv = document.getElementById("cvv").value;
    var str = expiryDate.split("/");

    if (x == 1) {
        if (cardNumber.length == 16) {
            if (Number.isInteger(Number(cardNumber)) == true) {
                document.getElementById("invalid_card_number").style.display = "none";
            }
        } else {
            document.getElementById("invalid_card_number").style.display = "";
        }
    } else if (x == 2) {
        if (str.length == 2) {
            var mm = Number(str[0]);
            var yyyy = Number(str[1]);
            if ((Number.isInteger(mm) == true) && (Number.isInteger(yyyy) == true)) {
                if ((mm > 0) && (mm < 13) && (yyyy > 2019) && (yyyy < 2040)) {
                    document.getElementById("invalid_expiry_date").style.display = "none";
                } else {
                    document.getElementById("invalid_expiry_date").style.display = "";
                }
            } else {
                document.getElementById("invalid_expiry_date").style.display = "";
            }
        } else {
            document.getElementById("invalid_expiry_date").style.display = "";
        }
    } else if (x == 3) {
        if (cvv.length == 3) {
            if (Number.isInteger(Number(cvv)) == true) {
                document.getElementById("invalid_cvv").style.display = "none";
            }
        } else {
            document.getElementById("invalid_cvv").style.display = "";
        }
    }


}