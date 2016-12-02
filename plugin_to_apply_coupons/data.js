var bestbuy = ".*best.*buy.*";
var amazon = "amazon";
var gifts = "giftsforyounow";
var elves = "tipsyelves";
var barnes = "barnesandnoble";
var macys = "macys";
var url = window.location.hostname;
var i = 0;
var total = 0;
var coupons = [];
console.log('done');
function sleepFor( sleepDuration ){
    var now = new Date().getTime();
    while(new Date().getTime() < now + sleepDuration){ /* do nothing */ } 
}

function repeatCouponsElves(coupons, i){
	console.log(document.getElementsByClassName("onestepcheckout-totals")[0].innerHTML);
	document.getElementById("id_couponcode").value = coupons[i];
	console.log(coupons[i]);
	document.getElementById("onestepcheckout-coupon-add").click();

	//document.getElementById("onestepcheckout-coupon-remove").click();
	console.log(i);
}

function repeatCouponsBarnes(coupons, i){
	console.log(document.getElementById("orderSummary").innerHTML);
	console.log(document.getElementsByClassName("remove-offer"));
	if(document.getElementsByClassName("remove-offer").length)
		document.getElementsByClassName("remove-offer")[0].click();
	document.getElementById("code").value = coupons[i];
	console.log(coupons[i]);
	document.getElementsByClassName("apply-coupon-code")[0].click();
	console.log(i);
}

function repeatCouponsGifts(coupons, i){
	console.log(document.getElementById("OrderTotals").innerHTML);
	console.log(document.getElementsByClassName("appliedRemovelnk"));
	if(document.getElementsByClassName("appliedRemovelnk").length){
		for (var i = 0; i < document.getElementsByClassName("appliedRemovelnk").length; i++)
			document.getElementsByClassName("appliedRemovelnk")[i].click()
	}
	document.getElementById("couponField").value = coupons[i];
	console.log(coupons[i]);
	document.getElementById("btnAddCoupon").click();
	
	console.log(i);
}

function repeatCouponsMacys(coupons, i){
	console.log(document.getElementById("bagContainer").innerHTML);
	console.log(document.getElementsByClassName("delete-button"));
	if(document.getElementsByClassName("delete-button").length)
		document.getElementsByClassName("delete-button")[0].click();
	document.getElementById("promoCode").value = coupons[i];
	console.log(coupons[i]);
	document.getElementById("applyPromoCode").click();
	
	console.log(i);
}

//Actions for bestbuy
if (url.match(bestbuy)){
	document.getElementsByClassName("form-control")[2].value="couponcode";
	document.getElementsByClassName("btn btn-large btn-primary emphasized-copy")[1].click();
}
else if(url.match(elves)){
	console.log("elves");
	var coupons = ["4THJULY15",
"JJ",
"FALL15",
"ELVES10",
"party10",
"TCU15",
"ELVES15",
"VIP2016",
"COLLEGE",
"OOPS20",
"welcome10",
"LASTMIN15",
"FRIYAY",
"FTL",
"ILIKETOPARTY",
"SHOP15",
"MANDOWN",
"Off Topic",
"MONDAY",
"BURR",
"EEK15",
"REVIEW15"];

/*setTimeout(function(){repeatCoupons(coupons, 0)}, 2000);
setTimeout(function(){repeatCoupons(coupons, 1)}, 4000);
setTimeout(function(){repeatCoupons(coupons, 2)}, 6000);
setTimeout(function(){repeatCoupons(coupons, 3)}, 8000);
setTimeout(function(){repeatCoupons(coupons, 4)}, 10000);
setTimeout(function(){repeatCoupons(coupons, 5)}, 12000);
setTimeout(function(){repeatCoupons(coupons, 6)}, 14000);
setTimeout(function(){repeatCoupons(coupons, 7)}, 16000);
setTimeout(function(){repeatCoupons(coupons, 8)}, 18000);*/

for(var i = 0; i < coupons.length; i++)
	setTimeout(repeatCouponsElves, 4000*i, coupons, i);
	//sleepFor(15000);
	//console.log(document.getElementsByClassName("onestepcheckout-totals")[0].innerHTML);
	//sleepFor(5000);
	//console.log(document.getElementsByClassName("onestepcheckout-totals"));

}
else if(url.match(gifts)){
	console.log("gifts");
	var coupons = ["HONEY15GFY",
"SHIP50-NG",
"GFY2359",
"GFY3452",
"LSWED15",
"LSWED20",
"15MILITARYLS",
"BABYLSGFY5",
"GARDENLSGFY5",
"KIDSLSGFY5",
"BDAYLSGFY5",
"GIFTS20BAG",
"PHOTO3012",
"MMAD30BFC",
"MOMGIFT53",
"INBOXCMDP",
"TRICKMG",
"CHGFSQ",
"CS15CG",
"GFY5L",
"S141HGME",
"TREENG",
"DAYBNG",
"ART20BNG",
"mon25bng",
"GFY10HE",
"NEW29NG",
"WEDDING30LS",
"GFYMB15MG",
"SAT25GFY",
"PRE30NG",
"SUN20GFY",
"ALL35BNG",
"BIG35-NG",
"CMFS20GFY",
"MERRY40DP",
"GFY516",
"SAT25NG",
"IDFSEN",
"SUN20NG",
"MANTLENG",
"CYBERNG",
"CYBER25NG",
"SHIPMBNG",
"HOLLY15NG",
"CYBER10NG",
"FLASH29NG",
"STOCK20BMG",
"JOY25NG",
"SHIP50NG",
"SANTA20",
"ART20BMG",
"MERRYNG",
"BF35GFY"
];


for(var i = 0; i < coupons.length; i++)
	setTimeout(repeatCouponsGifts, 8000*i, coupons, i);

}


else if(url.match(barnes)){
	console.log("barnes");
	var coupons = [/*"BNCYBER16",
"DECEMBER20",
"UKTSTGZRDURTL",
"RL1QQMB78KCW1",
"9WG13QDKAJWDX",
"SLDJ4YKZSZKPA",
"NJJZ9336JAA98",
"9YEG3SN8N41YU",
"BNWHIZKID",
"F7V8H7U",
"15BNFALL",
"BNSEPT15",
"HW8VWQQ1WQ9M2",
"P4R7F8Y",
"BNSUNNY",
"BNBELLS",
"BNBFRIDAY16",
"9DAWJ1Z88Z134",
"BNLEAF30",
"CN2QAS5VJSQ54",
"SQ63RKJ3FTF48",
"25BNFRIENDS",
"BNDEC25",
"BNDEC60",
"BNDEC50",
"BNDEC16",*/
"BNGREEN",
"N7REUUYF8WXS7"
];


for(var i = 0; i < coupons.length; i++)
	setTimeout(repeatCouponsBarnes, 4000*i, coupons, i);

}
else if(url.match(macys)){
	console.log("macys");
	coupons = ["BUY2",
"FRIENDSMS",
"XPAE6P6N84AY",
"TRIAL",
"GIFT",
"xcazzlaq49mk",
"CHANEL",
"RAYBAN",
"X672FUD251",
"CYBERSMS",
"cyberple",
"OCT16",
"TRAIL",
"FRIEND",
"FRIENDS",
"CYBER"];
for(var i = 0; i < coupons.length; i++)
	setTimeout(repeatCouponsMacys, 4000*i, coupons, i);
}
