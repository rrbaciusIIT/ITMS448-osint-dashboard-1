import fetchHelper from "helpers/fetchHelper";
import { thunk, action, actionOn, thunkOn, computed } from "easy-peasy";

const postsModel = {
  headers: [],
  data: [],
  boards: {},
  threads: {},
  postAnaylzed: 0,
  terroismFlagCount: 0,
  nsaFlagCount: 0,
  fetchData: thunk(async (actions, payload) => {
    const data = await fetchHelper(payload);
    console.log(data);

    actions.setPosts({ ...data }); // 👈 dispatch local actions to update state
    actions.analyzeThreadIds({ ...data }); // 👈 dispatch local actions to update state
    actions.analyzeBoards({ ...data }); // 👈 dispatch local actions to update state
    actions.analyzeTerroismFlag({ ...data });
    actions.analyzeNsaFlag({ ...data });
  }),
  setPosts: action((state, payload) => {
    const { data, headers } = payload;
    console.log("PAYLOAD", payload);

    // let updatedState = {
    //   ...state,
    //   data,
    //   headers,
    //   count: data.length
    // };

    state.data = data;
    state.headers = headers;
    state.postAnaylzed = data.length;
    // state = { ...updatedState };
  }),

  analyzeThreadIds: action((state, payload) => {
    let threads = {};
    const { data } = payload;

    data.forEach(post => {
      const { thread_id } = post;
      threads[thread_id] = threads[thread_id] + 1 || 1;
    });

    state.threads = threads;
    state.threads.count = Object.keys(threads).length;
  }),
  analyzeBoards: action((state, payload) => {
    let boards = {};
    const { data } = payload;

    data.forEach(post => {
      const { board } = post;
      boards[board] = boards[board] + 1 || 1;
    });

    state.boards = boards;
    state.boards.count = Object.keys(boards).length;
  }),
  analyzeTerroismFlag: action((state, payload) => {
    const { data, headers } = payload;
    const index = headers.length - 1;
    const field = headers[index].replace("/r", "");
    let count = 0;

    data.forEach(post => {
      if (post[field].includes("True")) {
        count = count + 1 || 1;
      }
    });

    state.terroismFlagCount = count;
  }),
  analyzeNsaFlag: action((state, payload) => {
    const { data, headers } = payload;
    const index = headers.length - 2;
    const field = headers[index].replace("/r", "");
    let count = 0;

    data.forEach(post => {
      if (post[field].includes("True")) {
        count = count + 1 || 1;
      }
    });

    state.nsaFlagCount = count;
  })
};

const basketModel = {
  productIds: [1],
  logs: [],
  items: {
    1: { id: 1, name: "Peas", price: 10 }
  },

  // async
  updateProduct: thunk(async (actions, payload) => {
    // const updated = await productService.update(payload.id, payload);
    const updated = { id: 1, name: "jay" };

    actions.setProduct(updated); // 👈 dispatch local actions to update state
  }),
  // action
  setProduct: action((state, payload) => {
    state.items[payload.id] = payload;
  }),
  addProduct: action((state, payload) => {
    state.productIds.push(payload);
  }),
  // computed values
  count: computed(state => Object.values(state.items).length),

  // lisenterns
  onAddedToBasket: actionOn(
    // targetResolver function receives actions and resolves the targets:
    (actions, storeActions) => storeActions.basket.addProduct,
    // action handler that executes when target is executed:
    (state, target) => {
      state.logs.push(`Added product ${target.payload} to basket`);
    }
  )
};

export const storeModel = {
  basket: basketModel,
  posts: postsModel
};
