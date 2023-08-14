"use strict";

$(document).ready(function() {
    $("#submit-button").click(function() {
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
        const fields =  ['sales', 'price']
        return Boolean(fields.includes(field))
    }

    decodeURIComponent(formData).split("&").forEach((item) => {
        const [field, value ] = item.split("=")
        if (value) data[field] = isNumberField(value) ? parseFloat(value) : value
    })

    return JSON.stringify(data)
}

// document.addEventListener("submit", postArticle)