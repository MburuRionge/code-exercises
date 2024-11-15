const request = require('request');

function fetchCharacters(movieId) {
    const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

    // fetch movie data
    request(url, { json: true }, (error, response, body) => {
        if (error) {
            console.error(`Error fetching movie data: ${error}`);
            return;
        }
        if (response.statusCode !== 200) {
            console.error(`Failed to fetch movie. Status code: ${response.statusCode}`);
            return;
        }

        // Display movie title
        const movieTitle = body.title || "Unknown Movie";
        console.log(`Characters in '${movieTitle}:`);

        //fetch each character in the List and print their names in order
        const characters = body.characters || [];
        characters.forEach((characterUrl) => {
            request(characterUrl,{ json: true }, (charError, charResponse, charBody) => {
                if (charError) {
                    console.error(`Error fetching character data: ${charError}`);
                    return;
                }
                if (charResponse.statusCode == 200) {
                    console.log(charBody.name);
                } else {
                    console.error(`Failed to fetch character. Status code: ${charResponse.statuscode}`);
                }
            });
        });
    });
}

//run the script
const movieId = process.argv[2];
if (!movieId) {
    console.log("Usage: node script.js <Movie ID>");
} else {
    fetchCharacters(vovieId);
}