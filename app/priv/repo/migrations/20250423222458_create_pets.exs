defmodule App.Repo.Migrations.CreatePets do
  use Ecto.Migration

  def change do
    create table(:pets) do
      add :name, :string
      add :pet_type, :string

      timestamps(type: :utc_datetime)
    end
  end
end
