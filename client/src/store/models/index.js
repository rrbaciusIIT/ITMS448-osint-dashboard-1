import { thunk, action, actionOn, thunkOn, computed } from "easy-peasy";

const productsModel = {
  items: {
    1: { id: 1, name: "Peas", price: 10 }
  }
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
  products: productsModel,
  basket: basketModel
};
