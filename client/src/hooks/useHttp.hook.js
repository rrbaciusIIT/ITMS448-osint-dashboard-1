// url http://192.168.2.11:1839/generate/csv?boards=x,pol&flaggers=NSA_PRISM,TERRORISM&start_page=1&stop_page=2/

import { useState, useEffect } from "react";

const useHttp = ({
  url,
  method = "GET",
  body = undefined,
  mode = "cors",
  responseType = "json"
}) => {
  const [isLoading, setIsLoading] = useState(false);
  const [fetchData, setFetchData] = useState(null);

  useEffect(() => {
    async function fetchData() {
      let data;
      setIsLoading(true);
      try {
        const response = await fetch(url, { method, body, mode });

        if (responseType === "csv") {
          data = await response.text();
          console.log(data);
          data = await csvJSON(data);
        }

        if (responseType === "json") {
          data = await response.json();
        }

        if (!response.ok) {
          throw new Error("Could not fetch person!");
        }

        setFetchData(data);
        setIsLoading(false);
      } catch (error) {
        console.log(error);
      }
    }
    fetchData();
  }, [url]);

  return [isLoading, fetchData];
};

export default useHttp;

function csvJSON(csv) {
  const rows = csv.split("\n");

  const result = [];

  const headers = rows[0].split(",");

  for (let col = 1; col < rows.length; col++) {
    const obj = {};
    const currentline = rows[col].split(",");

    for (let j = 0; j < headers.length; j++) {
      obj[headers[j]] = currentline[j];
    }

    result.push(obj);
  }

  //return result; //JavaScript object
  return JSON.parse(JSON.stringify(result));
}
