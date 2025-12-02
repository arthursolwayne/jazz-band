
import pretty_midi

# Create a new MIDI file with tempo set to 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments
sax = pretty_midi.Instrument(program=66)       # Tenor sax
bass = pretty_midi.Instrument(program=33)      # Double bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Define drum notes: kick (36), snare (38), hihat (42)
kick = 36
snare = 38
hihat = 42

# Bar 1: Drums only (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar_length = 1.5  # 1.5 seconds per bar at 160 BPM

# Drums in bar 1
drum_notes = [
    (kick, 0.0), (hihat, 0.1875), (hihat, 0.375),
    (snare, 0.5625), (hihat, 0.75), (hihat, 0.9375),
    (kick, 1.125), (hihat, 1.3125), (hihat, 1.5)
]

for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 2: Full band enters (1.5 - 3.0s)
# SAX: Introduce the motif (D, F#, A, D)
# D = 62, F# = 66, A = 69, D = 62

sax_notes = [
    (62, 1.5), (66, 1.6875), (69, 1.875), (62, 2.0625),
    (62, 2.5), (66, 2.6875), (69, 2.875), (62, 3.0)
]

for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# BASS: Walking line in D minor (D, C, B, A, G, F#, E, D)
bass_notes = [
    (62, 1.5), (60, 1.6875), (59, 1.875), (67, 2.0625),
    (67, 2.5), (65, 2.6875), (64, 2.875), (62, 3.0)
]

for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.125))

# PIANO: 7th chords on 2 and 4
# D7 (D, F#, A, C), Bm7 (B, D, F#, A)
piano_notes = [
    (62, 1.6875), (66, 1.6875), (69, 1.6875), (60, 1.6875),
    (62, 2.6875), (66, 2.6875), (69, 2.6875), (64, 2.6875)
]

for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125))

# Drums continue in bar 2
drum_notes = [
    (kick, 1.5), (hihat, 1.6875), (hihat, 1.875),
    (snare, 2.0625), (hihat, 2.25), (hihat, 2.4375),
    (kick, 2.625), (hihat, 2.8125), (hihat, 3.0)
]

for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 3: Full band continues (3.0 - 4.5s)
# SAX: Repeat the motif, slightly transposed up a half step (E, G, B, E)
# D → E: half-step up

sax_notes = [
    (64, 3.0), (68, 3.1875), (71, 3.375), (64, 3.5625),
    (64, 4.0), (68, 4.1875), (71, 4.375), (64, 4.5)
]

for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# BASS: Walking line continues
bass_notes = [
    (64, 3.0), (62, 3.1875), (61, 3.375), (69, 3.5625),
    (69, 4.0), (67, 4.1875), (66, 4.375), (64, 4.5)
]

for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.125))

# PIANO: 7th chords on 2 and 4
# E7 (E, G#, B, D), Cm7 (C, Eb, G, Bb)
piano_notes = [
    (64, 3.1875), (68, 3.1875), (71, 3.1875), (62, 3.1875),
    (60, 4.1875), (63, 4.1875), (67, 4.1875), (62, 4.1875)
]

for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125))

# Drums continue in bar 3
drum_notes = [
    (kick, 3.0), (hihat, 3.1875), (hihat, 3.375),
    (snare, 3.5625), (hihat, 3.75), (hihat, 3.9375),
    (kick, 4.125), (hihat, 4.3125), (hihat, 4.5)
]

for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 4: Full band ends (4.5 - 6.0s)
# SAX: Return to original motif, leave it hanging on F#
sax_notes = [
    (62, 4.5), (66, 4.6875), (69, 4.875), (66, 5.0625)
]

for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# BASS: Walking line ends
bass_notes = [
    (62, 4.5), (60, 4.6875), (59, 4.875), (67, 5.0625)
]

for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.125))

# PIANO: 7th chord on 4 (D7)
piano_notes = [
    (62, 5.0625), (66, 5.0625), (69, 5.0625), (60, 5.0625)
]

for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125))

# Drums end with a snare on the "and" of 4
drum_notes = [
    (snare, 5.8125), (hihat, 5.8125)
]

for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Add instruments to MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI to a file
midi.write("dante_intro.mid")
