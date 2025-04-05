defmodule App.PawClock.OwnerPet do
  use Ecto.Schema

  @primary_key false
  schema "owners_pets" do
    belongs_to :owner, App.PawClock.Owner
    belongs_to :pet, App.PawClock.Pet
  end

end

# def module App.PawClock.OwnerPet do
#   use Ecto.Schema

#   @primary_key false
#   schema "owners_pets" do
#     belongs_to :owner, App.PawClock.Owner
#     belongs_to :pet, App.PawClock.Pet
#     # timestamps(type: :utc_datetime)
#   end

#   @doc false
#   def changeset(owner_pet, attrs) do
#     owner_pet
#     |> Ecto.Changeset.cast(attrs, [:owner_id, :pet_id])
#     |> Ecto.Changeset.validate_required([:owner_id, :pet_id])
#   end
# end
