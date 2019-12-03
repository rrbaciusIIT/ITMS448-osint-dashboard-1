import fetchHelper from "helpers/fetchHelper";
import { thunk, action, actionOn, thunkOn, computed, debug } from "easy-peasy";
import { tableHeaderNames } from "variables/general";

const postsModel = {
  headers: [],
  data: [],
  boards: {},
  threads: {},
  postAnaylzed: 0,
  terroismFlagCount: 0,
  nsaPrismFlagCount: 0,
  nsaEchelonFlagCount: 0,
  hateSpeechFlagCount: 0,
  conspiracyFlagCount: 0,
  noContentFlagCount: 0,
  racismFlagCount: 0,
  dataType: "",
  fetchData: thunk(async (actions, payload) => {
    let data = await fetchHelper(payload);
    const { responseType: dataType } = payload;

    if (dataType === "json") {
      data = await { ...data };
    }

    // headers[headers.length - 1] = await headers[headers.length - 1].replace("\r", "");
    await actions.setDataType({ dataType });
    await actions.setPosts({ ...data }); // 👈 dispatch local actions to update state
    actions.analyzeThreadIds({ ...data }); // 👈 dispatch local actions to update state
    actions.analyzeBoards({ ...data }); // 👈 dispatch local actions to update state
    actions.analyzeTerroismFlag({ ...data });
    actions.analyzeNsaPrismFlag({ ...data });
    actions.analyzeNsaEchelonFlag({ ...data });
    actions.analyzeHateSpeechFlag({ ...data });
    actions.analyzeRacismFlag({ ...data });
    actions.analyzeConspiracyFlag({ ...data });
    actions.analyzeNoContent({ ...data });
    if (dataType === "json") {
      // actions.analyzeNsaPrismFlag({ ...data });
    }
  }),
  setDataType: action((state, payload) => {
    const { dataType } = payload;
    state.dataType = dataType;
  }),
  setPosts: action((state, payload) => {
    var postAnaylzed = 0;
    var formatteddata = [];
    var headers = [];

    if (state.dataType === "csv") {
      const { data, headers: incomingHeaders } = payload;

      formatteddata = data;
      headers = incomingHeaders;
      postAnaylzed = data.length;
    }

    // json request
    if (state.dataType === "json") {
      console.log("PAYLOAD", payload);
      let data = [];
      postAnaylzed = Object.keys(payload.board).length;
      // const { data, headers } = payload;

      for (let index = 0; index < postAnaylzed; index++) {
        let obj = {};

        obj[tableHeaderNames.NoContent] = payload[tableHeaderNames.NoContent][index];
        if (payload[tableHeaderNames.ContentFlaggerNsaEchelon]) {
          obj[tableHeaderNames.ContentFlaggerNsaEchelon] =
            payload[tableHeaderNames.ContentFlaggerNsaEchelon][index];
        }
        if (payload[tableHeaderNames.ContentFlaggerHateSpeech]) {
          obj[tableHeaderNames.ContentFlaggerHateSpeech] =
            payload[tableHeaderNames.ContentFlaggerHateSpeech][index];
        }
        if (payload[tableHeaderNames.ContentFlaggerNsaPrism]) {
          obj[tableHeaderNames.ContentFlaggerNsaPrism] =
            payload[tableHeaderNames.ContentFlaggerNsaPrism][index];
        }
        if (payload[tableHeaderNames.ContentFlaggerRacism]) {
          obj[tableHeaderNames.ContentFlaggerRacism] =
            payload[tableHeaderNames.ContentFlaggerRacism][index];
        }
        if (payload[tableHeaderNames.ContentFlaggerConspiracy]) {
          obj[tableHeaderNames.ContentFlaggerConspiracy] =
            payload[tableHeaderNames.ContentFlaggerConspiracy][index];
        }
        if (payload[tableHeaderNames.ContentFlaggerTerroism]) {
          obj[tableHeaderNames.ContentFlaggerTerroism] =
            payload[tableHeaderNames.ContentFlaggerTerroism][index];
        }

        obj.board = payload.board[index];
        obj.country_code = payload.country_code[index];
        obj.full_comment = payload.full_comment[index];
        obj.op = payload.op[index];
        obj.post_api_url = payload.post_api_url[index];
        obj.post_id = payload.post_id[index];
        obj.post_url = payload.post_url[index];
        obj.thread_api_url = payload.thread_api_url[index];
        obj.thread_id = payload.thread_id[index];
        obj.thread_url = payload.thread_url[index];
        obj.timestamp_ISO8601 = payload.timestamp_ISO8601[index];
        obj.timestamp_epoch = payload.timestamp_epoch[index];
        data.push(obj);
      }

      formatteddata = data;
      headers = Object.keys(payload);
      postAnaylzed = postAnaylzed;
    }

    state.postAnaylzed = postAnaylzed;
    state.data = formatteddata;
    state.headers = headers;
  }),

  analyzeThreadIds: action((state, payload) => {
    let threads = {};

    state.data.forEach(post => {
      const { thread_id } = post;
      threads[thread_id] = threads[thread_id] + 1 || 1;
    });

    state.threads = threads;
    state.threads.count = Object.keys(threads).length;
  }),
  analyzeBoards: action((state, payload) => {
    let boards = {};

    state.data.forEach(post => {
      const { board } = post;
      boards[board] = boards[board] + 1 || 1;
    });

    state.boards = boards;
    state.boards.count = Object.keys(boards).length;
  }),
  analyzeTerroismFlag: action((state, payload) => {
    let count = 0;
    let feild = "";

    if (
      typeof state.data[0][tableHeaderNames.ContentFlaggerTerroism] === "boolean" ||
      typeof state.data[0][tableHeaderNames.ContentFlaggerTerroism] === "string"
    ) {
      feild = tableHeaderNames.ContentFlaggerTerroism;
    } else if (
      typeof state.data[0][tableHeaderNames.ContentFlaggerTerroism + "\r"] === "boolean" ||
      typeof state.data[0][tableHeaderNames.ContentFlaggerTerroism + "\r"] === "string"
    ) {
      feild = tableHeaderNames.ContentFlaggerTerroism + "\r";
    }

    if (feild) {
      state.data.forEach((post, index) => {
        if (state.dataType === "csv") {
          if (post[feild].includes("True")) {
            count = count + 1 || 1;
          }
        }

        if (state.dataType === "json") {
          if (post[feild] == true) {
            count = count + 1 || 1;
            state.data[index][feild] = "True";
          } else {
            state.data[index][feild] = "False";
          }
        }
      });
    }

    state.terroismFlagCount = count;
  }),
  analyzeNsaPrismFlag: action((state, payload) => {
    let count = 0;
    let feild = "";

    if (
      typeof state.data[0][tableHeaderNames.ContentFlaggerNsaPrism] === "boolean" ||
      typeof state.data[0][tableHeaderNames.ContentFlaggerNsaPrism] === "string"
    ) {
      feild = tableHeaderNames.ContentFlaggerNsaPrism;
    } else if (
      typeof state.data[0][tableHeaderNames.ContentFlaggerNsaPrism + "\r"] === "boolean" ||
      typeof state.data[0][tableHeaderNames.ContentFlaggerNsaPrism + "\r"] === "string"
    ) {
      feild = tableHeaderNames.ContentFlaggerNsaPrism + "\r";
    }

    if (feild) {
      state.data.forEach((post, index) => {
        if (state.dataType === "csv") {
          if (post[feild].includes("True")) {
            count = count + 1 || 1;
          }
        }

        if (state.dataType === "json") {
          if (post[feild] == true) {
            count = count + 1 || 1;
            state.data[index][feild] = "True";
          } else {
            state.data[index][feild] = "False";
          }
        }
      });

      state.nsaPrismFlagCount = count;
    }
  }),
  analyzeNsaEchelonFlag: action((state, payload) => {
    let count = 0;
    let feild = "";

    if (
      typeof state.data[0][tableHeaderNames.ContentFlaggerNsaEchelon] === "boolean" ||
      typeof state.data[0][tableHeaderNames.ContentFlaggerNsaEchelon] === "string"
    ) {
      feild = tableHeaderNames.ContentFlaggerNsaEchelon;
    } else if (
      typeof state.data[0][tableHeaderNames.ContentFlaggerNsaEchelon + "\r"] === "boolean" ||
      typeof state.data[0][tableHeaderNames.ContentFlaggerNsaEchelon + "\r"] === "string"
    ) {
      feild = tableHeaderNames.ContentFlaggerNsaEchelon + "\r";
    }

    if (feild) {
      state.data.forEach((post, index) => {
        if (state.dataType === "csv") {
          if (post[feild].includes("True")) {
            count = count + 1 || 1;
          }
        }

        if (state.dataType === "json") {
          if (post[feild] == true) {
            count = count + 1 || 1;
            state.data[index][feild] = "True";
          } else {
            state.data[index][feild] = "False";
          }
        }
      });

      state.nsaEchelonFlagCount = count;
    }
  }),
  analyzeHateSpeechFlag: action((state, payload) => {
    let count = 0;
    let feild = "";

    if (
      typeof state.data[0][tableHeaderNames.ContentFlaggerHateSpeech] === "boolean" ||
      typeof state.data[0][tableHeaderNames.ContentFlaggerHateSpeech] === "string"
    ) {
      feild = tableHeaderNames.ContentFlaggerHateSpeech;
    } else if (
      typeof state.data[0][tableHeaderNames.ContentFlaggerHateSpeech + "\r"] === "boolean" ||
      typeof state.data[0][tableHeaderNames.ContentFlaggerHateSpeech + "\r"] === "string"
    ) {
      feild = tableHeaderNames.ContentFlaggerHateSpeech + "\r";
    }

    if (feild) {
      state.data.forEach((post, index) => {
        if (state.dataType === "csv") {
          if (post[feild].includes("True")) {
            count = count + 1 || 1;
          }
        }

        if (state.dataType === "json") {
          if (post[feild] == true) {
            count = count + 1 || 1;
            state.data[index][feild] = "True";
          } else {
            state.data[index][feild] = "False";
          }
        }
      });

      state.hateSpeechFlagCount = count;
    }
  }),
  analyzeRacismFlag: action((state, payload) => {
    let count = 0;
    let feild = "";

    if (
      typeof state.data[0][tableHeaderNames.ContentFlaggerRacism] === "boolean" ||
      typeof state.data[0][tableHeaderNames.ContentFlaggerRacism] === "string"
    ) {
      feild = tableHeaderNames.ContentFlaggerRacism;
    } else if (
      typeof state.data[0][tableHeaderNames.ContentFlaggerRacism + "\r"] === "boolean" ||
      typeof state.data[0][tableHeaderNames.ContentFlaggerRacism + "\r"] === "string"
    ) {
      feild = tableHeaderNames.ContentFlaggerRacism + "\r";
    }

    if (feild) {
      state.data.forEach((post, index) => {
        if (state.dataType === "csv") {
          if (post[feild].includes("True")) {
            count = count + 1 || 1;
          }
        }

        if (state.dataType === "json") {
          if (post[feild] == true) {
            count = count + 1 || 1;
            state.data[index][feild] = "True";
          } else {
            state.data[index][feild] = "False";
          }
        }
      });

      state.racismFlagCount = count;
    }
  }),
  analyzeConspiracyFlag: action((state, payload) => {
    let count = 0;
    let feild = "";

    if (
      typeof state.data[0][tableHeaderNames.ContentFlaggerConspiracy] === "boolean" ||
      typeof state.data[0][tableHeaderNames.ContentFlaggerConspiracy] === "string"
    ) {
      feild = tableHeaderNames.ContentFlaggerConspiracy;
    } else if (
      typeof state.data[0][tableHeaderNames.ContentFlaggerConspiracy + "\r"] === "boolean" ||
      typeof state.data[0][tableHeaderNames.ContentFlaggerConspiracy + "\r"] === "string"
    ) {
      feild = tableHeaderNames.ContentFlaggerConspiracy + "\r";
    }

    if (feild) {
      state.data.forEach((post, index) => {
        if (state.dataType === "csv") {
          if (post[feild].includes("True")) {
            count = count + 1 || 1;
          }
        }

        if (state.dataType === "json") {
          if (post[feild] == true) {
            count = count + 1 || 1;
            state.data[index][feild] = "True";
          } else {
            state.data[index][feild] = "False";
          }
        }
      });

      state.conspiracyFlagCount = count;
    }
  }),
  analyzeNoContent: action((state, payload) => {
    let count = 0;
    let feild = "";

    if (
      typeof state.data[0][tableHeaderNames.NoContent] === "boolean" ||
      typeof state.data[0][tableHeaderNames.NoContent] === "string"
    ) {
      feild = tableHeaderNames.NoContent;
    } else if (
      typeof state.data[0][tableHeaderNames.NoContent + "\r"] === "boolean" ||
      typeof state.data[0][tableHeaderNames.NoContent + "\r"] === "string"
    ) {
      feild = tableHeaderNames.NoContent + "\r";
    }

    if (feild) {
      state.data.forEach((post, index) => {
        if (state.dataType === "csv") {
          if (post[feild].includes("True")) {
            count = count + 1 || 1;
          }
        }

        if (state.dataType === "json") {
          if (post[feild] == true) {
            count = count + 1 || 1;
            state.data[index][feild] = "True";
          } else {
            state.data[index][feild] = "False";
          }
        }
      });

      state.noContentFlagCount = count;
    }
  })
};

export default postsModel;
