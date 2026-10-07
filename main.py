from app.ui.cli import run


if __name__ == "__main__":
    try:
        run()

    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!")