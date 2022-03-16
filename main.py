import streamlit as st

RELEASE = ["MVP", "DEV", "STABLE", "TEST"]
PROJECT = "PROJECT NAME"
VERSION = 0.1


def main():
    st.title(f"Dashboard: {PROJECT}")
    st.write(f"Version: {RELEASE[0]} {VERSION}")


if __name__ == "__main__":
    main()
