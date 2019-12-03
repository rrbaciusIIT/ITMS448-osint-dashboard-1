// url http://192.168.2.11:1839/generate/csv?boards=x,pol&flaggers=NSA_PRISM,TERRORISM&start_page=1&stop_page=2/
const fetchHelper = async ({
  url,
  method = "GET",
  body = undefined,
  mode = "cors",
  responseType = "json"
}) => {
  let data;

  try {
    const response = await fetch(url, { method, body, mode });

    if (responseType === "csv") {
      data = await response.text();
      data = await csvJSON(data);
    }

    if (responseType === "json") {
      data = await response.json();
    }

    if (!response.ok) {
      throw new Error("Could not fetch item!");
    }
  } catch (error) {
    console.error(error);
  }

  return data;
};

function csvJSON(csv) {
  const rows = csv.split("\n");

  const result = [];

  const headers = rows[0].split(",");

  for (let col = 1; col < rows.length; col++) {
    const obj = {};
    const currentRow = rows[col].split(",");

    for (let j = 0; j < headers.length; j++) {
      obj[headers[j]] = currentRow[j];
    }

    if (obj.board) {
      result.push(obj);
    }
  }

  //return result; //JavaScript object
  const data = JSON.parse(JSON.stringify(result));
  return { data, headers };
}

export default fetchHelper;
