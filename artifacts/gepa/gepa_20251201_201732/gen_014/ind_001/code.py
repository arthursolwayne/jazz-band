
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: All instruments come in
# Bass: D2 (MIDI 38) on beat 1, F2 (MIDI 41) on beat 2, A2 (MIDI 45) on beat 3, C3 (MIDI 48) on beat 4
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=45, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=48, start=2.625, end=3.0),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (F, A, C, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=3.0),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=3.0),  # C5
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=3.0),  # D4
]
piano.notes.extend(piano_notes)

# Sax: Short motif, start it, leave it hanging, then finish
# Motif: D4 (62), F4 (65), C4 (60), G4 (67)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),
    pretty_midi.Note(velocity=110, pitch=65, start=1.75, end=2.0),
    pretty_midi.Note(velocity=110, pitch=60, start=2.25, end=2.5),
    pretty_midi.Note(velocity=110, pitch=67, start=2.75, end=3.0),
]
sax.notes.extend(sax_notes)

# Bar 3: Same structure, but change chord and sax motif
# Bass: D2 (MIDI 38) on beat 1, A2 (MIDI 45) on beat 2, F2 (MIDI 41) on beat 3, Bb2 (MIDI 44) on beat 4
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=45, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=41, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=44, start=4.125, end=4.5),
]
bass.notes.extend(bass_notes)

# Piano: Dm7 -> Bbmaj7 (D, F, A, Bb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=4.5),  # D4
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=4.5),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # A4
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=4.5),  # Bb4
]
piano.notes.extend(piano_notes)

# Sax: Motif variation on D4 (62), F4 (65), Bb4 (66), D5 (67)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.25),
    pretty_midi.Note(velocity=110, pitch=65, start=3.25, end=3.5),
    pretty_midi.Note(velocity=110, pitch=66, start=3.75, end=4.0),
    pretty_midi.Note(velocity=110, pitch=67, start=4.25, end=4.5),
]
sax.notes.extend(sax_notes)

# Bar 4: Same structure, but final resolution
# Bass: D2 (MIDI 38) on beat 1, F2 (MIDI 41) on beat 2, A2 (MIDI 45) on beat 3, D3 (MIDI 50) on beat 4
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=41, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=45, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=50, start=5.625, end=6.0),
]
bass.notes.extend(bass_notes)

# Piano: Dm7 (D, F, A, C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=6.0),  # D4
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=6.0),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=6.0),  # C5
]
piano.notes.extend(piano_notes)

# Sax: Return to original motif, but finish it
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.75),
    pretty_midi.Note(velocity=110, pitch=65, start=4.75, end=5.0),
    pretty_midi.Note(velocity=110, pitch=60, start=5.25, end=5.5),
    pretty_midi.Note(velocity=110, pitch=67, start=5.75, end=6.0),
]
sax.notes.extend(sax_notes)

# Drums: Bar 3 and 4
# Same pattern as bar 1, repeated
for note in drum_notes:
    note.start += 3.0
    note.end += 3.0
drums.notes.extend(drum_notes)

# Add all instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
