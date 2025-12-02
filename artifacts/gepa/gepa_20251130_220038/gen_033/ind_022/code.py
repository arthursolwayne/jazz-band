
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
    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=100, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Start of melody
# Sax - motif starts here
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),  # A
    pretty_midi.Note(velocity=100, pitch=60, start=2.0, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=2.5, end=2.75),  # A
    pretty_midi.Note(velocity=100, pitch=60, start=2.75, end=3.0),  # F
]

# Bass - walking line in F minor
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=45, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=80, pitch=46, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=80, pitch=43, start=2.0, end=2.25),  # D
    pretty_midi.Note(velocity=80, pitch=45, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=80, pitch=46, start=2.5, end=2.75),  # G
    pretty_midi.Note(velocity=80, pitch=43, start=2.75, end=3.0),  # D
]

# Piano - comping on 2 and 4
piano_notes = [
    # Bar 2, beat 2: C7 (F7)
    pretty_midi.Note(velocity=80, pitch=76, start=1.75, end=2.0),
    # Bar 2, beat 4: A7 (F7)
    pretty_midi.Note(velocity=80, pitch=81, start=2.75, end=3.0),
    # Bar 3, beat 2: C7 (F7)
    pretty_midi.Note(velocity=80, pitch=76, start=3.75, end=4.0),
    # Bar 3, beat 4: A7 (F7)
    pretty_midi.Note(velocity=80, pitch=81, start=4.75, end=5.0),
    # Bar 4, beat 2: C7 (F7)
    pretty_midi.Note(velocity=80, pitch=76, start=5.75, end=6.0),
    # Bar 4, beat 4: A7 (F7)
    pretty_midi.Note(velocity=80, pitch=81, start=5.75, end=6.0),
]

# Bar 3: Continue sax, bass, piano
# Sax - continuation of motif with slight variation
sax_notes.extend([
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=3.5, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),  # G
    pretty_midi.Note(velocity=100, pitch=60, start=4.0, end=4.25),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=4.25, end=4.5),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.75),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=5.0),  # G
])

# Bass - walking line
bass_notes.extend([
    pretty_midi.Note(velocity=80, pitch=45, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=80, pitch=46, start=3.25, end=3.5),  # G
    pretty_midi.Note(velocity=80, pitch=43, start=3.5, end=3.75),  # D
    pretty_midi.Note(velocity=80, pitch=45, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=80, pitch=46, start=4.0, end=4.25),  # G
    pretty_midi.Note(velocity=80, pitch=43, start=4.25, end=4.5),  # D
    pretty_midi.Note(velocity=80, pitch=45, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=80, pitch=46, start=4.75, end=5.0),  # G
    pretty_midi.Note(velocity=80, pitch=43, start=5.0, end=5.25),  # D
    pretty_midi.Note(velocity=80, pitch=45, start=5.25, end=5.5),  # F
])

# Piano - comping
piano_notes.extend([
    pretty_midi.Note(velocity=80, pitch=76, start=3.75, end=4.0),
    pretty_midi.Note(velocity=80, pitch=81, start=4.75, end=5.0),
    pretty_midi.Note(velocity=80, pitch=76, start=5.75, end=6.0),
    pretty_midi.Note(velocity=80, pitch=81, start=5.75, end=6.0),
])

# Bar 4: Sax finishes motif, bass resolves, piano resolves
# Sax - final note
sax_notes.append(pretty_midi.Note(velocity=100, pitch=60, start=5.5, end=6.0))  # F

# Bass - resolves to F
bass_notes.append(pretty_midi.Note(velocity=80, pitch=45, start=5.75, end=6.0))

# Drums in bar 4
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=3.875),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),  # Snare on 4
    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=100, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=100, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=100, pitch=42, start=4.3125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.0),
])

# Add all notes to instruments
sax.notes.extend(sax_notes)
bass.notes.extend(bass_notes)
piano.notes.extend(piano_notes)
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
