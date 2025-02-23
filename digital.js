function updateClock() {
    const now = new Date();
    const hours = now.getHours().toString().padStart(2, '0');
    const minutes = now.getMinutes().toString().padStart(2, '0');
    const seconds = now.getSeconds().toString().padStart(2, '0');
    
    const daysOfWeek = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
    const dayName = daysOfWeek[now.getDay()];
    
    const day = now.getDate().toString().padStart(2, '0');
    const month = (now.getMonth() + 1).toString().padStart(2, '0');
    const year = now.getFullYear();
    
    const timeString = `${hours}:${minutes}:${seconds}`;
    const dayString = dayName;
    const dateString = `${day}/${month}/${year}`;
    
    document.getElementById('time').textContent = timeString;
    document.getElementById('day').textContent = dayString;
    document.getElementById('date').textContent = dateString;
}

setInterval(updateClock, 1000);
updateClock();
