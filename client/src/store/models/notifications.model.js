import fetchHelper from "helpers/fetchHelper";
import { thunk, action, actionOn, thunkOn, computed, debug } from "easy-peasy";
import { tableHeaderNames } from "variables/general";

const notificationsModel = {
  showNotification: false,
  notification: {},
  setNotification: thunk(async (actions, payload) => {
    const { message, type } = payload;
    await actions.openNotification({ message, type });
    setTimeout(function() {
      actions.closeNotification();
    }, 6000);
  }),
  openNotification: action((state, payload) => {
    const { message, type } = payload;

    state.notification = { message, type };
    state.showNotification = true;
  }),
  closeNotification: action((state, payload) => {
    state.showNotification = false;
    state.notifaction = {};
  })
};

export default notificationsModel;
