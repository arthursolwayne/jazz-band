
import pretty_midi

# Initialize the MIDI file with 160 BPM (4/4 time)
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments
sax = pretty_midi.Instrument(program=66)       # Tenor sax
bass = pretty_midi.Instrument(program=33)      # Double bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum notes: kick (36), snare (38), hihat (42)
drum_notes = {
    'kick': 36,
    'snare': 38,
    'hihat': 42
}

# Timing
bar_length = 1.5  # 4/4 time at 160 BPM = 1.5 seconds per bar
beat_length = bar_length / 4  # 0.375 seconds per beat

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Drums only: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for beat in range(4):
    time = beat * beat_length
    # Kick on 1 and 3 (beats 0 and 2)
    if beat in [0, 2]:
        note = pretty_midi.Note(velocity=100, pitch=drum_notes['kick'], start=time, end=time + 0.1)
        drums.notes.append(note)
    # Snare on 2 and 4 (beats 1 and 3)
    if beat in [1, 3]:
        note = pretty_midi.Note(velocity=100, pitch=drum_notes['snare'], start=time, end=time + 0.1)
        drums.notes.append(note)
    # Hihat on every eighth
    for eighth in [0, 0.5]:
        note = pretty_midi.Note(velocity=80, pitch=drum_notes['hihat'], start=time + eighth, end=time + eighth + 0.05)
        drums.notes.append(note)

# Bar 2-4 (1.5 - 6.0s): Full quartet

# Bass line: Marcus on walking bass (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (38, 1.5),     # D2 (beat 1)
    (40, 1.875),   # F2 (beat 2, chromatic approach)
    (43, 2.25),    # G2 (beat 3)
    (41, 2.625),   # F#2 (beat 4, chromatic approach)
    (38, 2.625),   # D2 (beat 1 of bar 2)
    (40, 2.625),   # F2 (beat 2)
    (43, 3.0),     # G2 (beat 3)
    (41, 3.375),   # F#2 (beat 4)
    (38, 3.375),   # D2 (beat 1 of bar 3)
    (40, 3.75),    # F2 (beat 2)
    (43, 4.125),   # G2 (beat 3)
    (41, 4.5),     # F#2 (beat 4)
    (38, 4.5),     # D2 (beat 1 of bar 4)
    (40, 4.875),   # F2 (beat 2)
    (43, 5.25),    # G2 (beat 3)
    (41, 5.625)    # F#2 (beat 4)
]

for pitch, time in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: Diane on open voicings, one chord per bar, resolve on the last
# Bar 2: Dmaj7 (D - F# - A - C#)
# Bar 3: G7 (G - B - D - F)
# Bar 4: Cmaj7 (C - E - G - B)
chords = [
    [(62, 1.5), (67, 1.5), (71, 1.5), (69, 1.5)],  # Dmaj7
    [(67, 2.625), (72, 2.625), (76, 2.625), (70, 2.625)],  # G7
    [(60, 3.75), (65, 3.75), (71, 3.75), (76, 3.75)]  # Cmaj7
]

for notes in chords:
    for pitch, time in notes:
        note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.75)
        piano.notes.append(note)

# Sax: Dante on tenor, one short motif, make it sing
# Motif: D (62) -> F (65) -> G (67) -> D (62), leave it hanging on the last note

sax_notes = [
    (62, 1.5),    # D (beat 1)
    (65, 1.75),   # F (beat 2)
    (67, 2.0),    # G (beat 3)
    (62, 2.25)    # D (beat 4), leave it hanging
]

for pitch, time in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=time, end=time + 0.25)
    sax.notes.append(note)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_russo_4_bar_intro.mid")
