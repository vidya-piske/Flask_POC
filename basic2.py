from basic import app

print(f"basic2.py: __name__ is {__name__}")

if __name__ == "__main__":
    print("Running basic2.py directly")
    app.run(debug=True)
else:
    print("Importing basic2.py as a module")
