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
# alias App.PawClock.OwnerPet

Repo.insert!(%Owner{
  # Add your schema fields here
  first_name: "Mike",
  last_name: "Smith",
  email: "msmith@email.com",
  pets: [
    # Note: pets will be initialized as an empty list in the Owner schema
    # If you want to add pets here, you can do it in the OwnerPet join table
    # or by using the many_to_many association later.
    # %OwnerPet{name: "Fluffy"}  # Uncomment this line if you want to add a pet directly
  ]  # Initialize with an empty list of pets
})

Repo.insert!(%Pet{
  # Add your schema fields here
  name: "Fluffy",
})

# Note: The above line assumes that the owner and pet have been created
# Repo.insert!(%OwnerPet{
#   owner_id: 1,  # Assuming the first owner has ID 1
#   pet_id: 1    # Assuming the first pet has ID 1
# })
