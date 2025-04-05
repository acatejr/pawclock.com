defmodule App.PawClock.Owner do
  use Ecto.Schema
  import Ecto.Changeset
  alias App.PawClock.{Pet, OwnerPet}

  schema "owners" do
    field :first_name, :string
    field :last_name, :string
    field :email, :string
    many_to_many :pets, Pet, join_through: "owners_pets"
    timestamps(type: :utc_datetime)
  end

  @doc false
  def changeset(owner, attrs) do
    owner
    |> cast(attrs, [:first_name, :last_name, :email])
    |> validate_required([:first_name, :last_name, :email])
    |> unique_constraint(:email)
    # |> cast_assoc(:pets, required: false)
  end
end
