
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
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
]
drums.notes.extend(drum_notes)

# Bar 2: sax enters with motif, bass walks, piano comps, drums continue
# Sax motif: D (D4) -> F# (F#4) -> B (B4) -> D (D5) [staccato]
sax_notes = [
    pretty_midi.Note(velocity=105, pitch=62, start=1.5, end=1.625),
    pretty_midi.Note(velocity=105, pitch=66, start=1.625, end=1.75),
    pretty_midi.Note(velocity=105, pitch=67, start=1.75, end=1.875),
    pretty_midi.Note(velocity=105, pitch=70, start=1.875, end=2.0),
]
sax.notes.extend(sax_notes)

# Bass line: walking in D
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=45, start=1.5, end=1.625),  # D3
    pretty_midi.Note(velocity=90, pitch=46, start=1.625, end=1.75),  # Eb3
    pretty_midi.Note(velocity=90, pitch=47, start=1.75, end=1.875),  # E3
    pretty_midi.Note(velocity=90, pitch=49, start=1.875, end=2.0),  # G3
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2, beat 2: D7 chord (D, F#, A, C#)
    pretty_midi.Note(velocity=95, pitch=62, start=1.625, end=1.75),
    pretty_midi.Note(velocity=95, pitch=66, start=1.625, end=1.75),
    pretty_midi.Note(velocity=95, pitch=67, start=1.625, end=1.75),
    pretty_midi.Note(velocity=95, pitch=69, start=1.625, end=1.75),
    # Bar 2, beat 4: D7 chord again
    pretty_midi.Note(velocity=95, pitch=62, start=1.875, end=2.0),
    pretty_midi.Note(velocity=95, pitch=66, start=1.875, end=2.0),
    pretty_midi.Note(velocity=95, pitch=67, start=1.875, end=2.0),
    pretty_midi.Note(velocity=95, pitch=69, start=1.875, end=2.0),
]
piano.notes.extend(piano_notes)

# Bar 3: continuation of the motif, repeated and developed
# Sax plays the motif again, but with a slight variation
sax_notes = [
    pretty_midi.Note(velocity=105, pitch=62, start=2.0, end=2.125),
    pretty_midi.Note(velocity=105, pitch=66, start=2.125, end=2.25),
    pretty_midi.Note(velocity=105, pitch=67, start=2.25, end=2.375),
    pretty_midi.Note(velocity=105, pitch=70, start=2.375, end=2.5),
]
sax.notes.extend(sax_notes)

# Bass continues walking line
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=70, start=2.0, end=2.125),  # A3
    pretty_midi.Note(velocity=90, pitch=71, start=2.125, end=2.25),  # Bb3
    pretty_midi.Note(velocity=90, pitch=72, start=2.25, end=2.375),  # B3
    pretty_midi.Note(velocity=90, pitch=74, start=2.375, end=2.5),  # D4
]
bass.notes.extend(bass_notes)

# Piano: 7th chords again
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=62, start=2.125, end=2.25),
    pretty_midi.Note(velocity=95, pitch=66, start=2.125, end=2.25),
    pretty_midi.Note(velocity=95, pitch=67, start=2.125, end=2.25),
    pretty_midi.Note(velocity=95, pitch=69, start=2.125, end=2.25),
    pretty_midi.Note(velocity=95, pitch=62, start=2.375, end=2.5),
    pretty_midi.Note(velocity=95, pitch=66, start=2.375, end=2.5),
    pretty_midi.Note(velocity=95, pitch=67, start=2.375, end=2.5),
    pretty_midi.Note(velocity=95, pitch=69, start=2.375, end=2.5),
]
piano.notes.extend(piano_notes)

# Bar 4: sax finishes the motif with a resolution, bass walks, piano plays last chord
sax_notes = [
    pretty_midi.Note(velocity=105, pitch=62, start=2.5, end=2.625),
    pretty_midi.Note(velocity=105, pitch=66, start=2.625, end=2.75),
    pretty_midi.Note(velocity=105, pitch=67, start=2.75, end=2.875),
    pretty_midi.Note(velocity=105, pitch=70, start=2.875, end=3.0),
]
sax.notes.extend(sax_notes)

# Bass continues walking line
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=76, start=2.5, end=2.625),  # F4
    pretty_midi.Note(velocity=90, pitch=77, start=2.625, end=2.75),  # Gb4
    pretty_midi.Note(velocity=90, pitch=78, start=2.75, end=2.875),  # G4
    pretty_midi.Note(velocity=90, pitch=80, start=2.875, end=3.0),  # Bb4
]
bass.notes.extend(bass_notes)

# Piano: last 7th chord
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=62, start=2.625, end=2.75),
    pretty_midi.Note(velocity=95, pitch=66, start=2.625, end=2.75),
    pretty_midi.Note(velocity=95, pitch=67, start=2.625, end=2.75),
    pretty_midi.Note(velocity=95, pitch=69, start=2.625, end=2.75),
    pretty_midi.Note(velocity=95, pitch=62, start=2.875, end=3.0),
    pretty_midi.Note(velocity=95, pitch=66, start=2.875, end=3.0),
    pretty_midi.Note(velocity=95, pitch=67, start=2.875, end=3.0),
    pretty_midi.Note(velocity=95, pitch=69, start=2.875, end=3.0),
]
piano.notes.extend(piano_notes)

# Add drum notes for bar 3 and 4
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=2.0, end=2.375),
    pretty_midi.Note(velocity=100, pitch=36, start=2.875, end=3.25),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=2.375, end=2.5),
    pretty_midi.Note(velocity=110, pitch=38, start=3.25, end=3.5),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=2.0, end=2.375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.375, end=2.75),
    pretty_midi.Note(velocity=80, pitch=42, start=2.75, end=3.125),
    pretty_midi.Note(velocity=80, pitch=42, start=3.125, end=3.5),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
