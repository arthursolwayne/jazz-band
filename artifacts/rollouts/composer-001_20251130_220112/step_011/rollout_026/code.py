
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (0.0, 36), (0.375, 42), (0.75, 36), (1.125, 42),
    (1.5, 38), (1.875, 42), (2.25, 38), (2.625, 42)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches
bass_notes = [
    (1.5, 50), (1.75, 51), (2.0, 52), (2.25, 53),
    (2.5, 53), (2.75, 52), (3.0, 51), (3.25, 50),
    (3.5, 50), (3.75, 51), (4.0, 52), (4.25, 53),
    (4.5, 53), (4.75, 52), (5.0, 51), (5.25, 50)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (1.5, 70), (1.5, 72), (1.5, 74), (1.5, 76),  # Dm7
    (2.0, 70), (2.0, 72), (2.0, 74), (2.0, 76),  # Dm7
    (2.5, 70), (2.5, 72), (2.5, 74), (2.5, 76),  # Dm7
    (3.0, 70), (3.0, 72), (3.0, 74), (3.0, 76),  # Dm7
    (3.5, 70), (3.5, 72), (3.5, 74), (3.5, 76),  # Dm7
    (4.0, 70), (4.0, 72), (4.0, 74), (4.0, 76),  # Dm7
    (4.5, 70), (4.5, 72), (4.5, 74), (4.5, 76),  # Dm7
    (5.0, 70), (5.0, 72), (5.0, 74), (5.0, 76)   # Dm7
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    kick_time = start + 0.0
    snare_time = start + 0.375
    kick_time2 = start + 0.75
    snare_time2 = start + 1.125
    hihat_times = [start + i * 0.25 for i in range(6)]
    for time in hihat_times:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + 0.125))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.125))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=snare_time, end=snare_time + 0.125))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick_time2, end=kick_time2 + 0.125))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=snare_time2, end=snare_time2 + 0.125))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm scale: D, Eb, F, G, A, Bb, C
# Motif: D, F, Eb, G (1st bar), then D, C (2nd bar), then F, Eb, G, A (3rd bar), then repeat motif (4th bar)

# Bar 2: D, F, Eb, G
sax_notes = [
    (1.5, 62), (1.65, 64), (1.8, 63), (1.95, 66),  # D, F, Eb, G
    (2.1, 62), (2.25, 60),  # D, C
    (2.4, 64), (2.55, 63), (2.7, 66), (2.85, 67),  # F, Eb, G, A
    (3.0, 62), (3.15, 64), (3.3, 63), (3.45, 66)   # Repeat motif
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.15))

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
