
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
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=110, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=110, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=110, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=110, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=110, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=110, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=110, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=110, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line in Fm (F, Ab, D, C)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=90, pitch=50, start=1.875, end=2.25), # Ab2
    pretty_midi.Note(velocity=90, pitch=57, start=2.25, end=2.625), # D2
    pretty_midi.Note(velocity=90, pitch=52, start=2.625, end=3.0),  # C2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.75),  # Ab
    pretty_midi.Note(velocity=100, pitch=52, start=1.5, end=1.75),  # C
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=1.75),  # D
]
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=58, start=2.25, end=2.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=55, start=2.25, end=2.5),  # D
    pretty_midi.Note(velocity=100, pitch=53, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=100, pitch=50, start=2.25, end=2.5),  # Ab
])
# Bar 4: Eb7 (Eb, G, Bb, D)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=59, start=3.0, end=3.25),  # G
    pretty_midi.Note(velocity=100, pitch=58, start=3.0, end=3.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=3.25),  # D
])
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F, Ab, G, F (Fm with a chromatic approach to G)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=53, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=110, pitch=50, start=1.625, end=1.75),  # Ab
    pretty_midi.Note(velocity=110, pitch=51, start=1.75, end=1.875),  # G
    pretty_midi.Note(velocity=110, pitch=53, start=1.875, end=2.0),   # F
    pretty_midi.Note(velocity=110, pitch=53, start=2.25, end=2.5),   # F
    pretty_midi.Note(velocity=110, pitch=50, start=2.5, end=2.625),  # Ab
    pretty_midi.Note(velocity=110, pitch=51, start=2.625, end=2.75), # G
    pretty_midi.Note(velocity=110, pitch=53, start=2.75, end=3.0),   # F
]
sax.notes.extend(sax_notes)

# Bar 3: Drums (3.0 - 4.5s)
# Same pattern as bar 1
for note in drum_notes:
    note.start += 1.5
    note.end += 1.5
drums.notes.extend([note.copy() for note in drum_notes])

# Bar 4: Drums (4.5 - 6.0s)
for note in drum_notes:
    note.start += 3.0
    note.end += 3.0
drums.notes.extend([note.copy() for note in drum_notes])

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
