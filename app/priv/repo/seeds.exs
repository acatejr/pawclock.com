# Script for populating the database. You can run it as:
#
#     mix run priv/repo/seeds.exs
#
# Inside the script, you can read and write to any of your
# repositories directly:
#
#     App.Repo.insert!(%App.SomeSchema{})
#
# We recommend using the bang functions (`insert!`, `update!`
# and so on) as they will fail if something goes wrong.

# App.PawClock.Repo.insert!(%App.PawClock.Pet{
#   # Add your schema fields here
#   name: "Fluffy"
# })
alias App.Repo
alias App.PawClock.Pet
alias App.PawClock.Owner

Repo.insert!(%Owner{
  # Add your schema fields here
  first_name: "Matt",
  last_name: "Smith",
  email: "msmith@email.com",
  pets: [
    Repo.insert!(%Pet{name: "Fluffy"})
  ]
})

Repo.insert!(%Owner{
  # Add your schema fields here
  first_name: "James",
  last_name: "Madison",
  email: "jmadison@email.com",
  pets: [
    Repo.insert!(%Pet{name: "Washington"})
  ]
})
