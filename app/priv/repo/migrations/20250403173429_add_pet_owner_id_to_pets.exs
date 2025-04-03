defmodule App.Repo.Migrations.AddPetOwnerIdToPets do
  use Ecto.Migration

  def change do
    alter table(:pets) do
      add :pet_owner_id, references(:pet_owners, on_delete: :delete_all), null: true
    end
  end
end
