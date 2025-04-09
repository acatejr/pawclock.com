defmodule App.Repo.Migrations.CreateDaycareSessions do
  use Ecto.Migration

  def change do
    create table(:daycare_sessions) do
      add :owner_id, references(:owners, on_delete: :delete_all), null: false
      add :pet_id, references(:pets, on_delete: :delete_all), null: false
      add :checkin, :utc_datetime, null: true
      add :checkout, :utc_datetime, null: true
      add :status, :string, null: true

      timestamps(type: :utc_datetime)
    end
  end
end
