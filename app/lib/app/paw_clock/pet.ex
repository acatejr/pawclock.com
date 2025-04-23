defmodule App.PawClock.Pet do
  use Ecto.Schema
  import Ecto.Changeset

  schema "pets" do
    field :name, :string
    field :pet_type, Ecto.Enum, values: [:cat, :dog]

    timestamps(type: :utc_datetime)
  end

  @doc false
  def changeset(pet, attrs) do
    pet
    |> cast(attrs, [:name, :pet_type])
    |> validate_required([:name, :pet_type])
  end
end
