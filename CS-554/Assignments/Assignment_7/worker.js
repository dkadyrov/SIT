const redisConnection = require("./redis-connection");
const axios = require("axios");
const api = require("./api_key.json")
const search_query = require("query-string");

async function main()  {
    redisConnection.on("research:request:*", async (message, channel) => {
        let id = message.requestId;
        let eventName = message.eventName;

        let query = message.data.query;

        let successEvent = `${eventName}:success:${id}`;
        let failedEvent = `${eventName}:failed:${id}`;

        let params = {
            key: api.pixabay,
            q: query,
            image_type: "photo"
        }

        let search = search_query.stringify(params);
        try {
            let res = await axios.get("https://pixabay.com/api/?" + search);

            redisConnection.emit(successEvent, {
                id,
                eventName,
                data: {
                    results: res.data.hits
                }
            })
        } catch (e) {
            redisConnection.emit(failedEvent, {
                id,
                eventName,
                data: {
                    message: "No Results from Pixabay"
                }
            })
        }
    })
}

main();