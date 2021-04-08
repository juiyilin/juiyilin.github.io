// function
async function fetchData(fetchfunc) {
    let data = await fetchfunc;
    let textdata = data.json();
    return textdata
}

function deleteText(blockNum) { //第n個.form-text
    let htmlId = document.getElementById('message' + blockNum);
    // 刪除上一筆查詢的結果文字
    if (htmlId != null) {
        content[blockNum - 1].removeChild(htmlId);
    }
}

function appendText(blockNum, text) {
    let tag = document.createElement('p');
    tag.className = 'result-text';
    tag.id = 'message' + blockNum;
    let result = document.createTextNode(text);
    //console.log(result);

    tag.appendChild(result);
    content[blockNum - 1].appendChild(tag);
}

let content = document.querySelectorAll('.form-text');

// 查詢
let btn = document.getElementById('search');
btn.addEventListener('click', function () {
    let name = document.getElementById('input-username').value;
    let url = '/api/users?username=' + name;

    let getData = fetchData(fetch(url)); // promise
    getData.then(function (jsonData) {

        let text;
        // 資料庫有資料
        if (jsonData.data != null) {
            let name = jsonData.data.name;
            let username = jsonData.data.username;
            //console.log(name, username);
            text = `${name} (${username})`;

        } else {
            text = '查無資料';
        }

        //刪除上一筆查詢的結果文字，num=message${num}
        deleteText(1);

        // 新增結果文字
        appendText(1, text);
    })
})

// 清除查詢
let clean = document.getElementById('clean');

clean.addEventListener('click', function () {
    console.log('clean search');
    let name = document.getElementById('input-username');
    name.value = '';

    // 刪除上一筆查詢的結果文字
    deleteText(1)
})

// 更新
let updateBtn = document.getElementById('update');
const postUrl = '/api/user';

updateBtn.addEventListener('click', function () {
    let updateInput = document.getElementById('update-username');
    //console.log(updateInput.value);
    let updateName = updateInput.value;
    updateInput.value = '';
    //console.log('after:', updateInput.value)

    let postData = fetchData(fetch(postUrl, {
        method: 'post',
        body: JSON.stringify({
            name: updateName
        }),
        headers: {
            'content-type': 'application/json'
        }
    }))
    postData.then(jsonData => {
        // 刪除上一次的結果文字
        deleteText(2)

        let text;
        if (jsonData.ok) {
            text = '成功更新為' + updateName;
            //更改畫面上方姓名文字
            let spanName = document.querySelector('span');
            spanName.textContent = updateName;
        } else {
            text = '發生不明錯誤';
        }

        // 新增結果文字
        appendText(2, text);
    })
})