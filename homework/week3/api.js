let url = 'https://padax.github.io/taipei-day-trip-resources/taipei-attractions.json';
let count = 1;


function showdata(data, cur, ct) {
    let content = document.querySelector('.content');
    for (let spot of data.result.results.slice(cur, 8 * ct)) {

        //.card
        let cardClass = document.createElement('div');
        cardClass.className = 'card';

        //處理圖片網址
        let imgUrl = spot.file.split('http');
        imgUrl = 'http' + imgUrl[1];

        // .card>.img>img src
        let imgClass = document.createElement('div');
        imgClass.className = 'img';
        let imgTag = document.createElement('img');
        imgTag.src = imgUrl;

        imgClass.appendChild(imgTag);

        // .card>.img>img src+.card-text
        let cardText = document.createElement('div');
        cardText.className = 'card-text';
        let text = document.createTextNode(spot.stitle);

        cardText.appendChild(text);
        cardClass.appendChild(imgClass).appendChild(cardText);
        content.appendChild(cardClass);

    };
}



async function fetchdata(url) {
    let response = await fetch(url);
    return response.json();

};
let jsondata = fetchdata(url)
//console.log(jsondata); 
//後續用.then()取得PromiseResult的值

window.addEventListener('load', function () {
    jsondata.then(function (data) {
        showdata(data, 0, count);
    });
});

let btn = document.getElementById('btn');
btn.addEventListener('click', function () {
    jsondata.then(function (data) {
        //取得網頁目前的資料筆數
        let curCount = document.getElementsByClassName('card').length;
        //console.log('.card:', curCount);
        count += 1;
        showdata(data, curCount, count);

    });
})