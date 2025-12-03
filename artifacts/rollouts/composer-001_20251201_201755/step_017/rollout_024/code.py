
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Everyone in. Sax starts the melody (1.5 - 3.0s)
# Sax: motif - Fm7 (F, Ab, D, Eb)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25), # Ab
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=3.0),  # Eb
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line in Fm (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),   # F (D2)
    pretty_midi.Note(velocity=80, pitch=40, start=1.875, end=2.25),  # Ab (E2)
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625),  # D (F#2)
    pretty_midi.Note(velocity=80, pitch=41, start=2.625, end=3.0),   # Eb (G2)
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, D, Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=3.0),    # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0),    # Ab
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=3.0),    # D
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=3.0),    # Eb
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Fm7 -> Bbm7 (F, Ab, D, Eb -> Bb, Db, F, Ab)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=4.5),    # Bb
    pretty_midi.Note(velocity=100, pitch=70, start=3.0, end=4.5),    # Db
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=4.5),    # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),    # Ab
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Fm7 -> Gm7 (F, Ab, D, Eb -> G, Bb, D, F)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=6.0),    # G
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=6.0),    # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=6.0),    # D
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=6.0),    # F
]

for note in piano_notes:
    piano.notes.append(note)

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
    # Hihat on every eighth
    for i in range(4):
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.375))
    # Snare on 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125))
    # Kick on 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5))
    # Snare on 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.875))

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
