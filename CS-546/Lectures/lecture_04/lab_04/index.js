const animals = require("./data/animals");
const connection = require("./data/connection");

async function main() {
    const sasha = await animals.create("Sasha", "Dog");
    console.log(sasha);

    const lucy = await animals.create("Lucy", "Dog");
    console.log(lucy)

    const allAnimals = await animals.getAll();
    console.log(allAnimals)

    const duke = await animals.create("Duke", "Walrus");
    console.log(duke)

    sashita = await animals.rename(sasha._id, "Sashita");
    console.log(sashita)

    await animals.remove(lucy._id)
    
    console.log(await animals.getAll());

  const db = await connection();
  await db.serverConfig.close();
}

main();