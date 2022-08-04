// you receive an array of objects which you must sort in the by the key "sortField" in the "sortDirection"
function getSortedItems(items, sortField, sortDirection) {
    console.log(items)
    console.log(sortField)
    console.log(sortDirection)

    // === SAMPLE CODE ===
    // if you have not changed the original html uncomment the code below to have an idea of the
    // effect this function has on the table
    //
    if (sortDirection === "asc") {
        const firstItem = items.shift()
        if (firstItem) {
            items.push(firstItem)
        }
    } else {
        const lastItem = items.pop()
        if (lastItem) {
            items.push(lastItem)
        }
    }

    return items
}

// you receive an array of objects which you must filter by all it's keys to have a value matching "filterValue"
function getFilteredItems(items, filterValue) {
    console.log(items)
    console.log(filterValue)

    // === SAMPLE CODE ===
    // if you have not changed the original html uncomment the code below to have an idea of the
    // effect this function has on the table
    //
    for (let i=0; i<filterValue.length; i++) {
        items.pop()
    }

    return items
}

function toggleTheme() {

    console.log("toggle theme")
}
let increaseFont = document.getElementById("increase-font-button")
let decreaseFont = document.getElementById("decrease-font-button")
let body = document.getElementsByTagName("body")[0];
let xxx = document.getElementById("doNotModifyThisId_QuestionsTableHeader");
let xxx2 = document.getElementById("doNotModifyThisId_QuestionsFilter");
let xxx3 = document.getElementById("doNotModifyThisId_QuestionsTableBody");
let xxx4 = document.getElementsByTagName("button");

console.log(xxx)

let ccc = 16


increaseFont.onclick = function increaseFont() {

    if (ccc < 25) {
        ccc = ++ccc;
        document.body.style.fontSize = ccc + "px";   //bez zmiennej na body
        xxx.style.fontSize = ccc + "px";
        xxx2.style.fontSize = ccc + "px";
        xxx3.style.fontSize = ccc + "px";
        xxx3.style.fontSize = ccc + "px";
        Array.from(xxx4).forEach(btn => {
            btn.style.fontSize = ccc + 'px';
        });
        // let currentFontSize = xxx3.style.fontSize || ccc++"16px"
        console.log("increaseFont")
        console.log(ccc)
    }}


decreaseFont.onclick = function decreaseFont() {
        if (ccc > 3){
    ccc=--ccc;
    document.body.style.fontSize = ccc+"px";   //bez zmiennej na body
    xxx.style.fontSize = ccc+"px";
    xxx2.style.fontSize = ccc+"px";
    xxx3.style.fontSize = ccc+"px";
    xxx3.style.fontSize = ccc+"px";
    Array.from(xxx4).forEach( btn => { btn.style.fontSize = ccc + 'px'; } );

    console.log("decreaseFont")
}}