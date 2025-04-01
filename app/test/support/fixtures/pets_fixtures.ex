defmodule App.PetsFixtures do
  @moduledoc """
  This module defines test helpers for creating
  entities via the `App.Pets` context.
  """

  @doc """
  Generate a pet.
  """
  def pet_fixture(attrs \\ %{}) do
    {:ok, pet} =
      attrs
      |> Enum.into(%{
        name: "some name"
      })
      |> App.Pets.create_pet()

    pet
  end
end
