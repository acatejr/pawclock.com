defmodule App.Repo.Migrations.CreateDayCareSessionTable do
  use Ecto.Migration

  def change do
    create table(:daycare_session, primary_key: false) do

      add :owner_id, references(:owners, on_delete: :delete_all), null: false
      add :pet_id, references(:pets, on_delete: :delete_all), null: false
      add :check_in_time, :utc_datetime, null: false
      add :check_out_time, :utc_datetime, null: true  # Allow null for check-out time if the pet hasn't checked out yet
      add :session_status, :string, null: false, default: "active", comment: "Status of the session: active, completed, cancelled"
      timestamps(type: :utc_datetime, default: fragment("now()"), null: false)
    end
  end
end
