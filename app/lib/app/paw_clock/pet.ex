defmodule App.PawClock.Pet do
  use Ecto.Schema
  import Ecto.Changeset
  alias App.PawClock.{Owner}

  schema "pets" do
    field :name, :string
    many_to_many :owners, Owner, join_through: "owners_pets"
    timestamps(type: :utc_datetime)
  end

  @doc false
  def changeset(pet, attrs) do
    pet
    |> cast(attrs, [:name])
    |> validate_required([:name])
    # |> validate_required([:owners])
    # |> cast_assoc(:owners, required: false)
    # |> unique_constraint(:name, name: :pets_name_index)
  end
end
