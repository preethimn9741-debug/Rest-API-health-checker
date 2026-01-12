function loadItems() {
    fetch("/items")
        .then(res => res.json())
        .then(data => {
            const list = document.getElementById("items");
            list.innerHTML = "";
            data.forEach(item => {
                const li = document.createElement("li");
                li.innerText = item.name;
                li.onclick = () => deleteItem(item.id);
                list.appendChild(li);
            });
        });
}

function addItem() {
    const name = document.getElementById("itemName").value;
    fetch("/items", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({name})
    }).then(() => loadItems());
}

function deleteItem(id) {
    fetch(`/items/${id}`, {method: "DELETE"})
        .then(() => loadItems());
}

loadItems();
