// ##############################
// // // General application
// #############################

const APPLICATION_NAME = "OSINT Dashboard";
// ##############################
// // // Tasks for TasksCard - see Dashboard view
// #############################

const bugs = [
  'Sign contract for "What are conference organizers afraid of?"',
  "Lines From Great Russian Literature? Or E-mails From My Boss?",
  "Flooded: One year later, assessing what was lost and what was found when a ravaging rain swept through metro Detroit",
  "Create 4 Invisible User Experiences you Never Knew About"
];
const website = [
  "Flooded: One year later, assessing what was lost and what was found when a ravaging rain swept through metro Detroit",
  'Sign contract for "What are conference organizers afraid of?"'
];
const server = [
  "Lines From Great Russian Literature? Or E-mails From My Boss?",
  "Flooded: One year later, assessing what was lost and what was found when a ravaging rain swept through metro Detroit",
  'Sign contract for "What are conference organizers afraid of?"'
];

const tableHeaderNames = {
  NoContent: "No content flagger tripped",
  ContentFlaggerNsaEchelon:
    "[content flagger] Contains keywords that may trigger NSA ECHELON filters",
  ContentFlaggerHateSpeech: "[content flagger] Contains hate speech",
  ContentFlaggerNsaPrism: "[content flagger] Contains keywords that may trigger NSA PRISM filters",
  ContentFlaggerRacism: "[content flagger] Contains racism",
  ContentFlaggerConspiracy: "[content flagger] Contains conspiracy theories",
  ContentFlaggerTerroism: "[content flagger] Contains terrorist language",
  Comment: "full_comment"
};

module.exports = {
  APPLICATION_NAME,
  // these 3 are used to create the tasks lists in TasksCard - Dashboard view
  bugs,
  website,
  server,
  tableHeaderNames
};
