import { TextField, Checkbox, Select } from "@material-ui/core";
import * as yup from "yup";
const { REACT_APP_BOWSER_API_HOST, REACT_APP_BOWSER_API_PORT } = process.env;

const initialValues = {
  host: REACT_APP_BOWSER_API_HOST,
  port: REACT_APP_BOWSER_API_PORT,
  actionString: "/api/generate/4chan/csv",
  boards: [],
  flaggers: [],
  startPage: 1,
  stopPage: 2
};

const validationSchema = yup.object().shape({
  host: yup
    .string("Host must be a number")
    .max(40, "Host cannot exceed 21 characters")
    .required("Host is required"),
  port: yup
    .number("Port must be a number")
    .positive("Must be a postive number")
    .required("Port is required"),
  actionString: yup
    .string("Action Page must be a string")
    .max(24, "Action cannont be more than 14 characters")
    .required("Action is required"),
  boards: yup
    .array()
    .min(1, "At least one Board is required")
    .max(10, "Max boards allowed is 10")
    .required("Boards is required"),
  flaggers: yup
    .array()
    .min(1, "At least one Flagger is required")
    .max(6, "Max flaggers allowed is 6")
    .required("Flaggers is required"),
  startPage: yup
    .number("Start Page must be a number")
    .positive("Must be a postive number")
    .max(99, "Max start page is 99")
    .required("Start Page is required"),
  stopPage: yup
    .number("End Page must be a number")
    .positive("Must be a postive number")
    .max(100, "Max pages allowed to scrape is 100")
    .required("End Page is required")
});

const inputsModels = {
  hostSection: [
    {
      id: "host-disabled",
      name: "host",
      label: "Host",
      type: "input",
      columnSpan: { xs: 12, sm: 12, md: 5 },
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
        { value: "/api/generate/4chan/csv", text: "Generate CSV" },
        { value: "/api/generate/4chan/json", text: "Generate JSON" }
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
      id: "boards-adv",
      name: "boards",
      label: "Advice",
      type: "checkbox",
      value: "adv",
      columnSpan: { xs: 6, sm: 4, md: 3 },
      formControlProps: {
        fullWidth: false
      },
      component: "Checkbox"
    },
    {
      id: "boards-f",
      name: "boards",
      label: "Flash",
      type: "checkbox",
      value: "f",
      columnSpan: { xs: 6, sm: 4, md: 3 },
      formControlProps: {
        fullWidth: false
      },
      component: "Checkbox"
    },
    {
      id: "boards-hr",
      name: "boards",
      label: "High Resoulution",
      type: "checkbox",
      value: "hr",
      columnSpan: { xs: 6, sm: 4, md: 3 },
      formControlProps: {
        fullWidth: false
      },
      component: "Checkbox"
    },
    {
      id: "boards-o",
      name: "boards",
      label: "Auto",
      type: "checkbox",
      value: "o",
      columnSpan: { xs: 6, sm: 4, md: 3 },
      formControlProps: {
        fullWidth: false
      },
      component: "Checkbox"
    },
    {
      id: "boards-pol",
      name: "boards",
      label: "Politics",
      type: "checkbox",
      value: "pol",
      columnSpan: { xs: 6, sm: 4, md: 3 },
      formControlProps: {
        fullWidth: false
      },
      component: "Checkbox"
    },
    {
      id: "boards-s4s",
      name: "boards",
      label: "S*** 4Chan Says",
      type: "checkbox",
      value: "s4s",
      columnSpan: { xs: 6, sm: 4, md: 3 },
      formControlProps: {
        fullWidth: false
      },
      component: "Checkbox"
    },
    {
      id: "boards-sp",
      name: "boards",
      label: "Sports",
      type: "checkbox",
      value: "sp",
      columnSpan: { xs: 6, sm: 4, md: 3 },
      formControlProps: {
        fullWidth: false
      },
      component: "Checkbox"
    },
    {
      id: "boards-tg",
      name: "boards",
      label: "Traditional Games",
      type: "checkbox",
      value: "tg",
      columnSpan: { xs: 6, sm: 4, md: 3 },
      formControlProps: {
        fullWidth: false
      },
      component: "Checkbox"
    },
    {
      id: "boards-tv",
      name: "boards",
      label: "Television & Film",
      type: "checkbox",
      value: "tv",
      columnSpan: { xs: 6, sm: 4, md: 3 },
      formControlProps: {
        fullWidth: false
      },
      component: "Checkbox"
    },
    {
      id: "boards-x",
      name: "boards",
      label: "Paranormal",
      type: "checkbox",
      value: "x",
      columnSpan: { xs: 6, sm: 4, md: 3 },
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
      label: "NSA PRISM",
      type: "checkbox",
      value: "NSA_PRISM",
      columnSpan: { xs: 6, sm: 4, md: 3 },
      formControlProps: {
        fullWidth: false
      },
      component: "Checkbox"
    },
    {
      id: "flaggers-nsa-echelon",
      name: "flaggers",
      label: "NSA ECHELON",
      type: "checkbox",
      value: "NSA_ECHELON",
      columnSpan: { xs: 6, sm: 4, md: 3 },
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
      columnSpan: { xs: 6, sm: 4, md: 3 },
      formControlProps: {
        fullWidth: false
      },
      component: "Checkbox"
    },
    {
      id: "flaggers-conspiracy",
      name: "flaggers",
      label: "Conspiracy",
      type: "checkbox",
      value: "CONSPIRACY",
      columnSpan: { xs: 6, sm: 4, md: 3 },
      formControlProps: {
        fullWidth: false
      },
      component: "Checkbox"
    },
    {
      id: "flaggers-hate-speech",
      name: "flaggers",
      label: "Hate Speech",
      type: "checkbox",
      value: "HATE_SPEECH",
      columnSpan: { xs: 6, sm: 4, md: 3 },
      formControlProps: {
        fullWidth: false
      },
      component: "Checkbox"
    },
    {
      id: "flaggers-racism",
      name: "flaggers",
      label: "Racism",
      type: "checkbox",
      value: "RACISM",
      columnSpan: { xs: 6, sm: 4, md: 3 },
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
