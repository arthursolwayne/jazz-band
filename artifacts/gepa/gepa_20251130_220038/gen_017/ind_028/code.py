
import pretty_midi

# Create a MIDI file with tempo 160 BPM (4/4 time)
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments for the quartet
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum notes: kick=36, snare=38, hihat=42
drum_notes = {
    'kick': 36,
    'snare': 38,
    'hihat': 42
}

# Time per bar: 1.5 seconds (160 BPM, 4/4 time)
bar_length = 1.5
total_time = 6.0  # 4 bars

# Bar 1: Drums only (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(4):
    time = i * bar_length / 4  # 0.0, 0.375, 0.75, 1.125
    if i % 2 == 0:  # Kick on 1 and 3
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=drum_notes['kick'], start=time, end=time + 0.125))
    else:  # Snare on 2 and 4
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=drum_notes['snare'], start=time, end=time + 0.125))
    # Hihat on every eighth
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=drum_notes['hihat'], start=time, end=time + 0.125))

# Bar 2-4 (1.5 - 6.0s)
# Start with the bass line: walking line in D (D, C#, B, A, G, F#, E, D, etc.)
# D = 62, C# = 61, B = 60, A = 59, G = 58, F# = 57, E = 56, D = 62, etc.

# Bass line (walking in D, 4 bars)
bass_notes = [
    # Bar 2
    (62, 1.5), (61, 1.875), (60, 2.25), (59, 2.625),
    # Bar 3
    (58, 3.0), (57, 3.375), (56, 3.75), (62, 4.125),
    # Bar 4
    (61, 4.5), (60, 4.875), (59, 5.25), (58, 5.625)
]
for pitch, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=70, pitch=pitch, start=time, end=time + 0.25))

# Piano: 7th chords, comp on 2 and 4
# D7 = D, F#, A, C
# D7 chord at bar 2, 4
piano_notes = [
    # Bar 2 - D7 on 2 and 4
    (62, 1.875, 0.25), (66, 1.875, 0.25), (69, 1.875, 0.25), (64, 1.875, 0.25),
    (62, 3.0, 0.25), (66, 3.0, 0.25), (69, 3.0, 0.25), (64, 3.0, 0.25),
    # Bar 3 - G7 on 2 and 4
    (67, 3.375, 0.25), (71, 3.375, 0.25), (74, 3.375, 0.25), (69, 3.375, 0.25),
    (67, 4.5, 0.25), (71, 4.5, 0.25), (74, 4.5, 0.25), (69, 4.5, 0.25)
]
for pitch, time, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + duration))

# Drums for bars 2-4: same pattern as bar 1 (kick on 1 and 3, snare on 2 and 4, hihat every eighth)
for i in range(4):
    time = 1.5 + i * bar_length / 4
    if i % 2 == 0:
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=drum_notes['kick'], start=time, end=time + 0.125))
    else:
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=drum_notes['snare'], start=time, end=time + 0.125))
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=drum_notes['hihat'], start=time, end=time + 0.125))

# Sax melody: a short motif in D, with space and tension
# D (62), F# (66), A (69), C (64)
# Start at 1.5s, play D then F#, hold A, then drop to C with a little space

sax_notes = [
    (62, 1.5, 0.25),  # D at 1.5s
    (66, 1.75, 0.25),  # F# at 1.75s
    (69, 2.0, 0.5),    # A for 0.5s
    (64, 2.5, 0.5)     # C for 0.5s
]
for pitch, time, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + duration))

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
