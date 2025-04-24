defmodule App.PawClock.Owner do
  use Ecto.Schema
  import Ecto.Changeset

  schema "owners" do
    field :first_name, :string
    field :last_name, :string
    field :phone, :string

    timestamps(type: :utc_datetime)
  end

  @doc false
  def changeset(owner, attrs) do
    owner
    |> cast(attrs, [:first_name, :last_name, :phone])
    |> validate_required([:first_name, :last_name, :phone])
  end
end
