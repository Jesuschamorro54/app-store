"use strict";

$(document).ready(function () {
    $("#submit-button").click(function () {
        // Obtener los datos del formulario
        var formData = $("#create-article-form").serialize();
        const data = decodeBinaryData(formData);
        http.post('/distributors/2/articles', data).then(response => {
            console.log(response)
        })
    });
});

function decodeBinaryData(formData) {

    let data = {}

    const isNumberField = (field) => {
        const fields = ['sale', 'price']
        return Boolean(fields.includes(field))
    }

    decodeURIComponent(formData).split("&").forEach((item) => {
        const [field, value] = item.split("=")
        if (value && field != "provider") data[field] = isNumberField(field) ? parseFloat(value) : value
    })

    return data
}

// document.addEventListener("submit", postArticle)