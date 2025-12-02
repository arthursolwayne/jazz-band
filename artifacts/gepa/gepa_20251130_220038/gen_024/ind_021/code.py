
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    (36, 0.0, 1.0),  # Kick on 1
    (42, 0.0, 1.0),  # Hihat on 1
    (38, 0.5, 1.0),  # Snare on 2
    (42, 0.5, 1.0),  # Hihat on 2
    (36, 1.0, 1.0),  # Kick on 3
    (42, 1.0, 1.0),  # Hihat on 3
    (38, 1.5, 1.0),  # Snare on 4
    (42, 1.5, 1.0)   # Hihat on 4
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line with chromatic approaches
bass_notes = [
    (44, 1.5, 0.5),  # F
    (45, 2.0, 0.5),  # Gb
    (46, 2.5, 0.5),  # G
    (48, 3.0, 0.5),  # A
    (49, 3.5, 0.5),  # Bb
    (50, 4.0, 0.5),  # B
    (51, 4.5, 0.5),  # C
    (48, 5.0, 0.5),  # A
    (46, 5.5, 0.5),  # G
    (48, 6.0, 0.5)   # A
]

for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano (Diane): 7th chords on 2 and 4
piano_notes = [
    # Bar 2
    (50, 2.0, 0.5),  # Bb7 (Bb, D, F, Ab)
    (52, 2.0, 0.5),
    (53, 2.0, 0.5),
    (55, 2.0, 0.5),
    # Bar 3
    (50, 3.5, 0.5),  # Bb7
    (52, 3.5, 0.5),
    (53, 3.5, 0.5),
    (55, 3.5, 0.5),
    # Bar 4
    (50, 5.0, 0.5),  # Bb7
    (52, 5.0, 0.5),
    (53, 5.0, 0.5),
    (55, 5.0, 0.5)
]

for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax (Dante): The motif. Start it, leave it hanging, come back and finish it.
sax_notes = [
    # Bar 2
    (50, 1.5, 0.25),  # F
    (53, 1.75, 0.25),  # A
    (50, 2.0, 0.25),  # F
    (52, 2.25, 0.25),  # G
    # Bar 3
    (50, 3.0, 0.25),  # F
    (53, 3.25, 0.25),  # A
    (55, 3.5, 0.25),  # C
    (53, 3.75, 0.25),  # A
    # Bar 4
    (50, 4.5, 0.25),  # F
    (53, 4.75, 0.25),  # A
    (55, 5.0, 0.25),  # C
    (53, 5.25, 0.25)   # A
]

for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.5))
    # Snare on 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.5, end=start + 1.0))
    # Kick on 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 1.0, end=start + 1.5))
    # Snare on 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 2.0))
    # Hihat on every eighth
    for i in range(0, 4):
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.5, end=start + i * 0.5 + 0.5))

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Write MIDI file
midi.write("fm_intro.mid")
