import { TextField, Checkbox, Select } from "@material-ui/core";
import * as yup from "yup";
const { REACT_APP_BOWSER_API_HOST, REACT_APP_BOWSER_API_PORT } = process.env;
// const { REACT_APP_JARRON_API_HOST, REACT_APP_JARRON_API_PORT } = process.env;

const initialValues = {
  host: REACT_APP_BOWSER_API_HOST,
  port: REACT_APP_BOWSER_API_PORT,
  actionString: "/generate/csv",
  boards: ["x", "pol"],
  flaggers: ["NSA_PRISM", "TERRORISM"],
  startPage: 1,
  stopPage: 2
};

const validationSchema = yup.object().shape({
  host: yup
    .string("Host must be a number")
    .max(50)
    .required("Host is required"),
  port: yup
    .number("Port must be a number")
    .positive("Must be a postive number")
    .required("Port is required"),
  actionString: yup
    .string("Action Page must be a string")
    .max(30)
    .required("Action is required"),
  boards: yup
    .array()
    .min(1, "At least one Board is required")
    .max(5)
    .required("Boards is required"),
  flaggers: yup
    .array()
    .min(1, "At least one Flagger is required")
    .max(5)
    .required("Flaggers is required"),
  startPage: yup
    .number("Start Page must be a number")
    .positive("Must be a postive number")
    .max(99)
    .required("Start Page is required"),
  stopPage: yup
    .number("End Page must be a number")
    .positive("Must be a postive number")
    .max(100)
    .required("End Page is required")
});

const inputsModels = {
  hostSection: [
    {
      id: "host-disabled",
      name: "host",
      label: "Host",
      type: "input",
      columnSpan: { xs: 12, sm: 12, md: 3 },
      formControlProps: {
        fullWidth: true
      },
      inputProps: {
        disabled: true
      },
      component: "TextField"
    },
    {
      id: "port-disabled",
      name: "port",
      label: "Port",
      type: "input",
      columnSpan: { xs: 12, sm: 12, md: 3 },
      formControlProps: {
        fullWidth: true
      },
      inputProps: {
        disabled: true
      },
      component: "TextField"
    },
    {
      id: "action-string",
      name: "actionString",
      menuItems: [
        { value: "/generate/csv", text: "Generate CSV" },
        { value: "/generate/json", text: "Generate JSON" }
      ],
      columnSpan: { xs: 12, sm: 12, md: 4 },
      formControlProps: {
        fullWidth: true
      },
      component: "Select"
    }
  ],
  boardSection: [
    {
      id: "boards-x",
      name: "boards",
      label: "X",
      type: "checkbox",
      value: "x",
      columnSpan: { xs: 4, sm: 4, md: 2 },
      formControlProps: {
        fullWidth: false
      },
      component: "Checkbox"
    },
    {
      id: "boards-pol",
      name: "boards",
      label: "Pol",
      type: "checkbox",
      value: "pol",
      columnSpan: { xs: 4, sm: 4, md: 2 },
      formControlProps: {
        fullWidth: false
      },
      component: "Checkbox"
    }
  ],
  flaggersSection: [
    {
      id: "flaggers-nsa-prism",
      name: "flaggers",
      label: "NSA Prism",
      type: "checkbox",
      value: "NSA_PRISM",
      columnSpan: { xs: 4, sm: 4, md: 2 },
      formControlProps: {
        fullWidth: false
      },
      component: "Checkbox"
    },
    {
      id: "flaggers-terroism",
      name: "flaggers",
      label: "Terrorism",
      type: "checkbox",
      value: "TERRORISM",
      columnSpan: { xs: 4, sm: 4, md: 2 },
      formControlProps: {
        fullWidth: false
      },
      component: "Checkbox"
    }
  ],
  pageFiltersSection: [
    {
      id: "startPage",
      name: "startPage",
      label: "Start Page",
      type: "input",
      columnSpan: { xs: 12, sm: 12, md: 4 },
      formControlProps: {
        fullWidth: true
      },
      component: "TextField"
    },
    {
      id: "stopPage",
      name: "stopPage",
      label: "End Page",
      type: "input",
      columnSpan: { xs: 12, sm: 12, md: 4 },
      formControlProps: {
        fullWidth: true
      },
      component: "TextField"
    }
  ],
  aboutMe: [
    {
      id: "about-me",
      name: "aboutMe",
      label: "About Me",
      type: "input",
      columnSpan: { xs: 12, sm: 12, md: 12 },
      formControlProps: {
        fullWidth: true
      },
      inputProps: {
        multiline: true,
        rows: 5
      },
      isTextArea: true,
      component: "TextField"
    }
  ]
};

export { inputsModels, initialValues, validationSchema };
