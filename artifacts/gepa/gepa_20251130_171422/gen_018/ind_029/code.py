
import pretty_midi

# Initialize MIDI file with tempo
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments
sax = pretty_midi.Instrument(program=66)       # Tenor sax
bass = pretty_midi.Instrument(program=33)      # Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum notes: kick=36, snare=38, hihat=42
drum_notes = {
    'kick': 36,
    'snare': 38,
    'hihat': 42
}

# Time in seconds per bar
bar_length = 1.5  # 160 BPM => 60/160 = 0.375 sec per beat, 4 beats per bar = 1.5 sec

# Bar 1: Little Ray (drums) alone
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    start = bar * bar_length
    # Kick on 1 and 3 (beats 0 and 2)
    for beat in [0, 2]:
        time = start + beat * 0.375
        note = pretty_midi.Note(velocity=100, pitch=drum_notes['kick'], start=time, end=time + 0.1)
        drums.notes.append(note)
    # Snare on 2 and 4 (beats 1 and 3)
    for beat in [1, 3]:
        time = start + beat * 0.375
        note = pretty_midi.Note(velocity=110, pitch=drum_notes['snare'], start=time, end=time + 0.1)
        drums.notes.append(note)
    # Hihat on every eighth note
    for beat in range(8):
        time = start + (beat * 0.1875)
        note = pretty_midi.Note(velocity=90, pitch=drum_notes['hihat'], start=time, end=time + 0.1)
        drums.notes.append(note)

# Bar 2-4: Full quartet
# Start time for bars 2-4
start_time = 1.5

# Bass line: walking line in Fm, chromatic approaches
# Fm: F, Ab, Bb, D, E, G, Ab
# Walking bass line: F -> G -> Ab -> A -> Bb -> C -> B -> A -> Bb -> C -> D -> Eb -> E -> F
# Translating to MIDI notes: F=65, G=67, Ab=68, A=69, Bb=70, C=72, B=71, Eb=64, E=70
bass_notes = [
    65, 67, 68, 69, 70, 72, 71, 69, 70, 72, 74, 64, 70, 65
]
bass_durations = [0.375] * 14  # 1/4 note per beat (14 beats over 3 bars)

for i, pitch in enumerate(bass_notes):
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start_time + i * 0.375, end=start_time + i * 0.375 + 0.375)
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4, comping
# Fm7 = F, Ab, Bb, C
# Bbm7 = Bb, Db, Eb, F
# Fm7 on beat 2 of bar 2 (1.5 + 1*0.375 = 1.875)
# Bbm7 on beat 4 of bar 2 (1.5 + 3*0.375 = 2.625)
# Fm7 on beat 2 of bar 3 (1.5 + 5*0.375 = 3.375)
# Bbm7 on beat 4 of bar 3 (1.5 + 7*0.375 = 4.125)
# Fm7 on beat 2 of bar 4 (1.5 + 9*0.375 = 4.875)
# Bbm7 on beat 4 of bar 4 (1.5 + 11*0.375 = 5.625)

# Convert chord notes to MIDI pitches
# Fm7: F(65), Ab(68), Bb(70), C(72)
# Bbm7: Bb(70), Db(62), Eb(64), F(65)
chords = [
    (65, 68, 70, 72),  # Fm7
    (70, 62, 64, 65),  # Bbm7
    (65, 68, 70, 72),  # Fm7
    (70, 62, 64, 65),  # Bbm7
    (65, 68, 70, 72),  # Fm7
    (70, 62, 64, 65),  # Bbm7
]

# Time for each chord (beat 2 and 4)
times = [
    1.875, 2.625, 3.375, 4.125, 4.875, 5.625
]

for i, (pitch1, pitch2, pitch3, pitch4) in enumerate(chords):
    for pitch in [pitch1, pitch2, pitch3, pitch4]:
        note = pretty_midi.Note(velocity=100, pitch=pitch, start=times[i], end=times[i] + 0.375)
        piano.notes.append(note)

# Sax: The melody starts on bar 2, one short motif, make it sing
# Fm melody: F, G, Ab, A
# Time: 1.875 (beat 2 of bar 2) to 2.25 (beat 3 of bar 2)
# F -> G -> Ab -> A, then leave it hanging
# F (65) -> G (67) -> Ab (68) -> A (69)
sax_notes = [65, 67, 68, 69]
sax_durations = [0.375, 0.375, 0.375, 0.375]
# But we only play the first three notes (leaving the last one hanging)
for i, pitch in enumerate(sax_notes[:3]):
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=start_time + i * 0.375, end=start_time + i * 0.375 + 0.375)
    sax.notes.append(note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI
midi.write("dante_intro.mid")
