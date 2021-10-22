#visits_management

Idea: In my company there are many external visitors: guests, auditors, external services, authorities, etc. It is difficult to manage them so that the visits do not coincide. Too many visitors at the same time create chaos and organization challenge. This app should help to coordinate visits in the site.

MAIN FUNCTIONS
Must have:
- register upcoming visits
- define person responsible for the visitor
- define visit time
- assign conference room (if needed)
- access: everybody can see registered visits, only defined employees can add new visits

Could have:
- sending email notification to the responsible person when the guest arrives
- send visits for approval to the site manager
- define special needs regarding accomodation, meals, transportation, etc

Views:
- main view, welcome to application, links to: visit registration, list of visits
- visit registration (access restricted to defined users-organizers)
- list of visits, possible to filter by day, visitor, organizer, etc. Links to delete visit and update visit.
- change, delete visit
- add, change, delete organizer (access - only superuser)
- add, change, delete visitor
- add, change, delete company
- add, change, delete conference room


Models:
- visit - organizer (OneToOne), visitor(many visitors to one visit), conference_room(ManyToMany, null=True), date (or start date, end date).
- organizer - first_name, surname, function, phone number
- visitor - first_name, surname, company(OneToOne), contact details, covid_cleared(boolean), last_training_date(default = date today).
- company - name, type(choices, np. customer, supplier, authorities, auditor, other)
- conference room - name, size
