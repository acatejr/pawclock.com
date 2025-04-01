defmodule App.Repo.Migrations.AddTypeToPets do
  use Ecto.Migration

  def change do
    alter table(:pets) do
      add :type, :string, null: false, default: "dog"
    end
  end
end
