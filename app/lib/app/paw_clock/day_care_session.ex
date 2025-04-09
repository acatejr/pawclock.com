defmodule App.PawClock.DayCareSession do
  use Ecto.Schema
  import Ecto.Changeset

  schema "daycare_sessions" do
    field :status, :string
    field :checkout, :utc_datetime
    field :checkin, :utc_datetime

    timestamps(type: :utc_datetime)
  end

  @doc false
  def changeset(day_care_session, attrs) do
    day_care_session
    |> cast(attrs, [:checkin, :checkout, :status])
    |> validate_required([:checkin, :checkout, :status])
  end
end
