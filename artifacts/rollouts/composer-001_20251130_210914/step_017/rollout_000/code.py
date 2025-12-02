
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
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth note
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass (Marcus) - walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=63, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625),  # E
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=3.0),   # F
]
bass.notes.extend(bass_notes)

# Piano (Diane) - 7th chords on 2 and 4
piano_notes = [
    # Bar 2 - D7 (D, F#, A, C)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),
    # Bar 3 - G7 (G, B, D, F)
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=66, start=2.25, end=2.625),
    # Bar 4 - A7 (A, C#, E, G)
    pretty_midi.Note(velocity=100, pitch=70, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),
]
piano.notes.extend(piano_notes)

# Sax (Dante) - Motif in D, start on 1.5s
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=67, start=1.5, end=1.625),  # D (start of motif)
    pretty_midi.Note(velocity=110, pitch=71, start=1.625, end=1.75),  # F
    pretty_midi.Note(velocity=110, pitch=69, start=1.75, end=1.875),  # E
    pretty_midi.Note(velocity=110, pitch=71, start=1.875, end=2.0),   # F (end of first phrase)
    pretty_midi.Note(velocity=110, pitch=67, start=2.625, end=2.875), # D (return of motif)
    pretty_midi.Note(velocity=110, pitch=71, start=2.875, end=3.0),   # F
    pretty_midi.Note(velocity=110, pitch=69, start=3.0, end=3.125),   # E
    pretty_midi.Note(velocity=110, pitch=72, start=3.125, end=3.375), # F# (finish it)
]
sax.notes.extend(sax_notes)

# Bar 3: Drums continue with same pattern (3.0 - 4.5s)
for note in drum_notes:
    note.start += 3.0
    note.end += 3.0
    drums.notes.append(note)

# Bar 4: Drums continue with same pattern (4.5 - 6.0s)
for note in drum_notes:
    note.start += 6.0
    note.end += 6.0
    drums.notes.append(note)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save to a MIDI file
midi.write("dante_sax_intro.mid")
