dateId = document.getElementById("date")

function displayDateTime() {
    let currentDate = new Date();
    // let year = currentDate.getFullYear();
    // let month = currentDate.getMonth() + 1;
    // let day = currentDate.getDate();
    // let hours = currentDate.getHours();
    // let minutes = currentDate.getMinutes();
    // let seconds = currentDate.getSeconds();
    // let formattedDate = `${month}/${day}/${year} ${hours}:${minutes}:${seconds}`;
    let formattedDate = currentDate.toLocaleString();
    // dateId.innerText = formattedDate;
    
    dateId.innerText = formattedDate;

}
displayDateTime();