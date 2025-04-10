defmodule App.PawClockFixtures do
  @moduledoc """
  This module defines test helpers for creating
  entities via the `App.PawClock` context.
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
      |> App.PawClock.create_pet()

    pet
  end

  @doc """
  Generate a unique owner email.
  """
  def unique_owner_email, do: "some email#{System.unique_integer([:positive])}"

  @doc """
  Generate a owner.
  """
  def owner_fixture(attrs \\ %{}) do
    {:ok, owner} =
      attrs
      |> Enum.into(%{
        email: unique_owner_email(),
        first_name: "some first_name",
        last_name: "some last_name"
      })
      |> App.PawClock.create_owner()

    owner
  end

  @doc """
  Generate a day_care_session.
  """
  def day_care_session_fixture(attrs \\ %{}) do
    {:ok, day_care_session} =
      attrs
      |> Enum.into(%{
        checkin: ~U[2025-04-08 17:35:00Z],
        checkout: ~U[2025-04-08 17:35:00Z],
        status: "some status"
      })
      |> App.PawClock.create_day_care_session()

    day_care_session
  end
end
