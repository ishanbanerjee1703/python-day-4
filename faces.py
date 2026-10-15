def main():
    response= input("Say something with a :) or a :( ")
    answer= response.replace(":)", "🙂").replace(":(", "🙁")
    print(answer)

main()
