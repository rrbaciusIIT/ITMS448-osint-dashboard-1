import fetchHelper from "helpers/fetchHelper";
import { thunk, action, actionOn, thunkOn, computed, debug } from "easy-peasy";
import { tableHeaderNames } from "variables/general";

const postsModel = {
  headers: [],
  data: [],
  threads: [],
  postAnaylzed: 0,
  dataType: "",
  fetchData: thunk(async (actions, payload) => {
    let data = await fetchHelper(payload);
    const { responseType: dataType } = payload;

    if (dataType === "json") {
      data = await { ...data };
    }

    await actions.setDataType({ dataType });
    await actions.setPosts({ ...data }); // 👈 dispatch local actions to update state
  }),
  setDataType: action((state, payload) => {
    const { dataType } = payload;
    state.dataType = dataType;
  }),
  setPosts: action((state, payload) => {
    var postAnaylzed = 0;
    var formatteddata = [];

    // json request
    if (state.dataType === "json") {
      payload.subreddit_response.data.children.forEach(post => {
        const { data } = post;
        let { author, media_only, created, over_18, selftext, title, url, ups, downs } = data;

        if (over_18) {
          over_18 = "True";
        } else {
          over_18 = "False";
        }

        if (media_only) {
          media_only = "True";
        } else {
          media_only = "False";
        }

        let obj = {};

        obj.author = author;
        obj.media_only = media_only;
        obj.created = created;
        obj.over_18 = over_18;
        obj.selftext = selftext;
        obj.title = title;
        obj.url = url;
        obj.ups = ups;
        obj.downs = downs;

        formatteddata.push(obj);
        postAnaylzed++;
      });
    }

    state.headers = Object.keys(formatteddata[0]);
    state.data = formatteddata;
    state.threads = payload.thread_list;
  })
};

export default postsModel;
