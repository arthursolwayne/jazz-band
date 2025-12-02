
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
]

drums.notes.extend(drum_notes)

# Bar 2: Everyone in. Sax starts motif.
# F7 - G7 - A7 - Bb7
# Play F7 on beat 1, G7 on beat 2, A7 on beat 3, Bb7 on beat 4

# Sax motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=87, start=1.5, end=1.875),  # F7
    pretty_midi.Note(velocity=100, pitch=88, start=1.875, end=2.25),  # G7
    pretty_midi.Note(velocity=100, pitch=89, start=2.25, end=2.625),  # A7
    pretty_midi.Note(velocity=100, pitch=85, start=2.625, end=3.0),  # Bb7
]

sax.notes.extend(sax_notes)

# Bass: Walking line with chromatic approaches
# F (D2), G (E2), A (F2), Bb (F#2)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # F (D2)
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25),  # G (E2)
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625),  # A (F2)
    pretty_midi.Note(velocity=100, pitch=44, start=2.625, end=3.0),  # Bb (F#2)
]

bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on last
# Bar 2: F7 (F A C E)
# Bar 3: G7 (G B D F)
# Bar 4: A7 (A C# E G)
# Bar 5: Bb7 (Bb D F Ab)

# Bar 2 (1.5-2.25s)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.25),  # F (F4)
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=2.25),  # A (A4)
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.25),  # C (C4)
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=2.25),  # E (E4)
]

# Bar 3 (2.25-3.0s)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=3.0),  # G (G4)
    pretty_midi.Note(velocity=100, pitch=77, start=2.25, end=3.0),  # B (B4)
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=3.0),  # D (D4)
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=3.0),  # F (F4)
])

piano.notes.extend(piano_notes)

# Bar 3: Drums - same pattern as bar 1
# Repeat kick, snare, hihat
for note in drum_notes:
    note.start += 1.5
    note.end += 1.5
drums.notes.extend([note.copy() for note in drum_notes])

# Bar 4: Drums again
for note in drum_notes:
    note.start += 3.0
    note.end += 3.0
drums.notes.extend([note.copy() for note in drum_notes])

# Bar 4: Bass continues with walking line
# F (D2), G (E2), A (F2), Bb (F#2)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),  # F (D2)
    pretty_midi.Note(velocity=100, pitch=40, start=3.375, end=3.75),  # G (E2)
    pretty_midi.Note(velocity=100, pitch=43, start=3.75, end=4.125),  # A (F2)
    pretty_midi.Note(velocity=100, pitch=44, start=4.125, end=4.5),  # Bb (F#2)
]

bass.notes.extend(bass_notes)

# Bar 4: Piano - Bb7 (Bb D F Ab)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.75),  # Bb (Bb4)
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.75),  # D (D4)
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.75),  # F (F4)
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.75),  # Ab (Ab4)
]

piano.notes.extend(piano_notes)

# Bar 4: Sax - repeat the motif on the last bar to finish it
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=87, start=3.0, end=3.375),  # F7
    pretty_midi.Note(velocity=100, pitch=88, start=3.375, end=3.75),  # G7
    pretty_midi.Note(velocity=100, pitch=89, start=3.75, end=4.125),  # A7
    pretty_midi.Note(velocity=100, pitch=85, start=4.125, end=4.5),  # Bb7
]

sax.notes.extend(sax_notes)

# Add all instruments
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
