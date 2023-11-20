<script>
	import io from "socket.io-client";

	let connectedToServer = false;

	const denverDetails = {
		Key: "DEN",
		TeamID: 10,
		PlayerID: 49,
		City: "Denver",
		Name: "Broncos",
		Conference: "AFC",
		Division: "West",
		FullName: "Denver Broncos",
		StadiumID: 13,
		ByeWeek: 9,
		AverageDraftPosition: 343.9,
		AverageDraftPositionPPR: 342.3,
		HeadCoach: "Sean Payton",
		OffensiveCoordinator: "Joe Lombardi",
		DefensiveCoordinator: "Vance Joseph",
		SpecialTeamsCoach: "Ben Kotwica",
		OffensiveScheme: "3WR",
		DefensiveScheme: "3-4",
		UpcomingSalary: 5395,
		UpcomingOpponent: "Scrambled",
		UpcomingOpponentRank: 44,
		UpcomingOpponentPositionRank: 44,
		UpcomingFanDuelSalary: 6913,
		UpcomingDraftKingsSalary: 5395,
		UpcomingYahooSalary: null,
		PrimaryColor: "FC4C02",
		SecondaryColor: "0A2343",
		TertiaryColor: "FFFFFF",
		QuaternaryColor: null,
		WikipediaLogoUrl:
			"https://upload.wikimedia.org/wikipedia/en/4/44/Denver_Broncos_logo.svg",
		WikipediaWordMarkUrl:
			"https://upload.wikimedia.org/wikipedia/commons/c/c4/Denver_Broncos_wordmark_%28c._1997%29.png",
		GlobalTeamID: 10,
		DraftKingsName: "Broncos ",
		DraftKingsPlayerID: 332,
		FanDuelName: "Denver Broncos",
		FanDuelPlayerID: 12531,
		FantasyDraftName: "Denver Broncos",
		FantasyDraftPlayerID: 332,
		YahooName: "Denver Broncos",
		YahooPlayerID: 100007,
		AverageDraftPosition2QB: 257.3,
		AverageDraftPositionDynasty: 268.1,
		StadiumDetails: {
			StadiumID: 13,
			Name: "Empower Field at Mile High",
			City: "Denver",
			State: "CO",
			Country: "USA",
			Capacity: 76125,
			PlayingSurface: "Grass",
			GeoLat: 39.743889,
			GeoLong: -105.020097,
			Type: "Outdoor",
		},
	};

	const KansasCityDetails = {
		Key: "KC",
		TeamID: 16,
		PlayerID: 55,
		City: "Kansas City",
		Name: "Chiefs",
		Conference: "AFC",
		Division: "West",
		FullName: "Kansas City Chiefs",
		StadiumID: 15,
		ByeWeek: 10,
		AverageDraftPosition: 328.8,
		AverageDraftPositionPPR: 295.0,
		HeadCoach: "Andy Reid",
		OffensiveCoordinator: "Matt Nagy",
		DefensiveCoordinator: "Steve Spagnuolo",
		SpecialTeamsCoach: "Dave Toub",
		OffensiveScheme: "3WR",
		DefensiveScheme: "4-3",
		UpcomingSalary: 4384,
		UpcomingOpponent: "Scrambled",
		UpcomingOpponentRank: 10,
		UpcomingOpponentPositionRank: 10,
		UpcomingFanDuelSalary: 6238,
		UpcomingDraftKingsSalary: 4384,
		UpcomingYahooSalary: 27,
		PrimaryColor: "E31837",
		SecondaryColor: "FFB612",
		TertiaryColor: "FFFFFF",
		QuaternaryColor: null,
		WikipediaLogoUrl:
			"https://upload.wikimedia.org/wikipedia/en/e/e1/Kansas_City_Chiefs_logo.svg",
		WikipediaWordMarkUrl:
			"https://upload.wikimedia.org/wikipedia/commons/7/79/Kansas_City_Chiefs_wordmark.svg",
		GlobalTeamID: 16,
		DraftKingsName: "Chiefs ",
		DraftKingsPlayerID: 339,
		FanDuelName: "Kansas City Chiefs",
		FanDuelPlayerID: 12536,
		FantasyDraftName: "Kansas City Chiefs",
		FantasyDraftPlayerID: 339,
		YahooName: "Kansas City Chiefs",
		YahooPlayerID: 100012,
		AverageDraftPosition2QB: 272.3,
		AverageDraftPositionDynasty: 264.4,
		StadiumDetails: {
			StadiumID: 15,
			Name: "Arrowhead Stadium",
			City: "Kansas City",
			State: "MO",
			Country: "USA",
			Capacity: 76416,
			PlayingSurface: "Grass",
			GeoLat: 39.048889,
			GeoLong: -94.483889,
			Type: "Outdoor",
		},
	};

	let boxScore = {
		GameKey: "202310616",
		SeasonType: 1,
		Season: 2023,
		Week: 6,
		Date: "2023-10-12T20:15:00",
		AwayTeam: "DEN",
		HomeTeam: "KC",
		AwayScore: 0,
		HomeScore: 0,
		Channel: "AMAZON",
		PointSpread: -10.5,
		OverUnder: 47.5,
		Quarter: null,
		TimeRemaining: "15:00",
		Possession: null,
		Down: null,
		Distance: null,
		YardLine: null,
		YardLineTerritory: null,
		RedZone: null,
		AwayScoreQuarter1: null,
		AwayScoreQuarter2: null,
		AwayScoreQuarter3: null,
		AwayScoreQuarter4: null,
		AwayScoreOvertime: null,
		HomeScoreQuarter1: null,
		HomeScoreQuarter2: null,
		HomeScoreQuarter3: null,
		HomeScoreQuarter4: null,
		HomeScoreOvertime: null,
		HasStarted: true,
		IsInProgress: true,
		IsOver: false,
		Has1stQuarterStarted: true,
		Has2ndQuarterStarted: false,
		Has3rdQuarterStarted: false,
		Has4thQuarterStarted: false,
		IsOvertime: false,
		DownAndDistance: null,
		QuarterDescription: null,
		StadiumID: 15,
		LastUpdated: null,
		GeoLat: null,
		GeoLong: null,
		ForecastTempLow: 69,
		ForecastTempHigh: 69,
		ForecastDescription: "Overcast Clouds",
		ForecastWindChill: 69,
		ForecastWindSpeed: 19,
		AwayTeamMoneyLine: 454,
		HomeTeamMoneyLine: -633,
		Canceled: false,
		Closed: false,
		LastPlay: null,
		Day: "2023-10-12T00:00:00",
		DateTime: "2023-10-12T20:15:00",
		AwayTeamID: 10,
		HomeTeamID: 16,
		GlobalGameID: 18358,
		GlobalAwayTeamID: 10,
		GlobalHomeTeamID: 16,
		PointSpreadAwayTeamMoneyLine: -110,
		PointSpreadHomeTeamMoneyLine: -112,
		ScoreID: 18358,
		Status: "Not Started",
		GameEndDateTime: null,
		HomeRotationNumber: 112,
		AwayRotationNumber: 111,
		NeutralVenue: false,
		RefereeID: 51,
		OverPayout: -110,
		UnderPayout: -111,
		HomeTimeouts: 3,
		AwayTimeouts: 2,
		DateTimeUTC: "2023-10-13T00:15:00",
		Attendance: 0,
		IsClosed: false,
		StadiumDetails: {
			StadiumID: 15,
			Name: "Arrowhead Stadium",
			City: "Kansas City",
			State: "MO",
			Country: "USA",
			Capacity: 76416,
			PlayingSurface: "Grass",
			GeoLat: 39.048889,
			GeoLong: -94.483889,
			Type: "Outdoor",
		},
	};

	const socket = io("http://127.0.0.1:5000");

	socket.on("connect", () => {
		handleConnect();
	});

	socket.on("disconnect", () => {
		handleDisconnect();
	});

	socket.on("data_update", (game_data) => {
		boxScore = JSON.parse(game_data);
		console.log(boxScore);
	});

	function handleConnect() {
		connectedToServer = true;
	}
	function handleDisconnect() {
		connectedToServer = false;
	}
</script>

{#if connectedToServer}
	<span style="color: darkgreen">Connected!</span>
{:else}
	<span style="color: darkred">Not Connected!</span>
{/if}

<main>
	<div class="box-score-container">
		<div class="header">
			<div class="title-container">
				<div class="title">Kansas City Chiefs vs. Denver Broncos</div>
				<div class="game-date">10/12</div>
			</div>
			<div class="game-status">
				{boxScore.Possession} Ball
				{boxScore.Down} &
				{boxScore.Distance} From
				{boxScore.YardLineTerritory}
				{boxScore.YardLine}
			</div>
			<div class="last-play">
				{boxScore.LastPlay}
			</div>
		</div>
		<div class="content">
			<div class="score-box">
				<img
					src={KansasCityDetails.WikipediaLogoUrl}
					alt=""
					class="team-logo"
				/>
				<div class="score">
					<div class="pos">
						{#if boxScore.Possession == "KC"}🏈{/if}
					</div>
					<div class="home-score">{boxScore.HomeScore}</div>
					<div class="dash">-</div>
					<div class="away-score">{boxScore.AwayScore}</div>
					<div class="pos">
						{#if boxScore.Possession == "DEN"}🏈{/if}
					</div>
				</div>
				<img
					src={denverDetails.WikipediaLogoUrl}
					alt=""
					class="team-logo"
				/>
			</div>
			<div class="time">
				{#if boxScore.Quarter === "1"}
					1st
				{/if}
				{#if boxScore.Quarter === "2"}
					2nd
				{/if}
				{#if boxScore.Quarter === "3"}
					3rd
				{/if}
				{#if boxScore.Quarter === "4"}
					4th
				{/if}

				{#if boxScore.Quarter == "HALF"}
					HALF
				{/if}

				<span
					class={boxScore.TimeRemaining !== "15:00" &&
						"time-remaining"}>{boxScore.TimeRemaining}</span
				>
			</div>
		</div>
	</div>
</main>

<style>
	@import url("https://fonts.googleapis.com/css2?family=Fira+Code:wght@300;400;500;700&family=Inter:wght@100;300;400;500;700&family=Poppins:wght@300;400;500;700&family=Roboto:wght@300;400;500;700;900&family=Ubuntu:wght@300;400;500;700&display=swap");

	main {
		display: flex;
		height: 100%;
		justify-content: center;
		align-items: center;
		font-family: "Poppins", sans-serif;
	}

	.box-score-container {
		height: 300px;
		width: 800px;
		box-shadow: rgba(100, 100, 111, 0.2) 0px 7px 29px 0px;
		padding: 20px;
	}

	.title {
		font-size: 25px;
		font-weight: bold;
		margin-right: auto;
	}

	.team-logo {
		height: 100px;
	}

	.score-box {
		display: flex;
		width: 100%;
		justify-content: space-between;
		align-items: center;
		font-size: 100px;
		margin-top: 2rem;
	}

	.content {
		height: 100%;
		width: 100%;
		display: flex;
		flex-direction: column;
		justify-content: start;
		align-items: center;
	}

	.score {
		display: flex;
		width: 50%;
		align-items: center;
		justify-content: space-between;
	}

	.pos {
		font-size: 35px;
	}

	.last-play {
		font-size: 15px;
		color: gray;
	}

	.time {
		display: flex;
		margin-bottom: 25px;
	}

	.title-container {
		display: flex;
		align-items: center;
	}

	.time-remaining {
		color: darkgreen;
		margin-left: 1rem;
	}

	.game-status {
		font-size: 20px;
	}
</style>
