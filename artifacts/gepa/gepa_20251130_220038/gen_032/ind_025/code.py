
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

# Bar 2: Full quartet (1.5 - 3.0s)

# Sax - motif: D (D4), F (F4), G (G4), Bb (Bb4)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.625, end=1.75),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=1.875),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.0),  # Bb4
]
sax.notes.extend(sax_notes)

# Bass - walking line in D
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=45, start=1.5, end=1.625),  # D3
    pretty_midi.Note(velocity=80, pitch=47, start=1.625, end=1.75),  # E3
    pretty_midi.Note(velocity=80, pitch=46, start=1.75, end=1.875),  # D#3
    pretty_midi.Note(velocity=80, pitch=48, start=1.875, end=2.0),  # F3
]
bass.notes.extend(bass_notes)

# Piano - 7th chords on 2 and 4
piano_notes = [
    # D7 on 2 (beat 2)
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.0),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.0),  # G4
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.0),  # Bb4
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.0),  # D5
    # F7 on 4 (beat 4)
    pretty_midi.Note(velocity=90, pitch=65, start=2.625, end=2.75),  # F4
    pretty_midi.Note(velocity=90, pitch=70, start=2.625, end=2.75),  # A4
    pretty_midi.Note(velocity=90, pitch=72, start=2.625, end=2.75),  # B4
    pretty_midi.Note(velocity=90, pitch=74, start=2.625, end=2.75),  # D5
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Sax - motif again
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.125),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=3.125, end=3.25),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.375),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.5),  # Bb4
]
sax.notes.extend(sax_notes)

# Bass - walking line in D
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=48, start=3.0, end=3.125),  # F3
    pretty_midi.Note(velocity=80, pitch=50, start=3.125, end=3.25),  # G3
    pretty_midi.Note(velocity=80, pitch=49, start=3.25, end=3.375),  # F#3
    pretty_midi.Note(velocity=80, pitch=51, start=3.375, end=3.5),  # A3
]
bass.notes.extend(bass_notes)

# Piano - 7th chords on 2 and 4
piano_notes = [
    # G7 on 2 (beat 2)
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.5),  # G4
    pretty_midi.Note(velocity=90, pitch=72, start=3.375, end=3.5),  # B4
    pretty_midi.Note(velocity=90, pitch=74, start=3.375, end=3.5),  # D5
    pretty_midi.Note(velocity=90, pitch=76, start=3.375, end=3.5),  # F5
    # A7 on 4 (beat 4)
    pretty_midi.Note(velocity=90, pitch=69, start=4.125, end=4.25),  # A4
    pretty_midi.Note(velocity=90, pitch=74, start=4.125, end=4.25),  # C5
    pretty_midi.Note(velocity=90, pitch=76, start=4.125, end=4.25),  # D5
    pretty_midi.Note(velocity=90, pitch=78, start=4.125, end=4.25),  # E5
]
piano.notes.extend(piano_notes)

# Drums - same pattern as bar 1
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),
]

drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Sax - finish the motif with a run up to Bb (Bb5)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.625),  # Bb4
    pretty_midi.Note(velocity=100, pitch=71, start=4.625, end=4.75),  # D5
    pretty_midi.Note(velocity=100, pitch=72, start=4.75, end=4.875),  # E5
    pretty_midi.Note(velocity=100, pitch=74, start=4.875, end=5.0),  # G5
    pretty_midi.Note(velocity=100, pitch=76, start=5.0, end=5.125),  # A5
    pretty_midi.Note(velocity=100, pitch=77, start=5.125, end=5.25),  # B5
    pretty_midi.Note(velocity=100, pitch=79, start=5.25, end=5.375),  # D6
    pretty_midi.Note(velocity=100, pitch=81, start=5.375, end=5.5),  # F6
]
sax.notes.extend(sax_notes)

# Bass - walking line in D
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=51, start=4.5, end=4.625),  # A3
    pretty_midi.Note(velocity=80, pitch=53, start=4.625, end=4.75),  # B3
    pretty_midi.Note(velocity=80, pitch=52, start=4.75, end=4.875),  # A#3
    pretty_midi.Note(velocity=80, pitch=54, start=4.875, end=5.0),  # C4
    pretty_midi.Note(velocity=80, pitch=55, start=5.0, end=5.125),  # C#4
    pretty_midi.Note(velocity=80, pitch=57, start=5.125, end=5.25),  # D4
    pretty_midi.Note(velocity=80, pitch=56, start=5.25, end=5.375),  # D#4
    pretty_midi.Note(velocity=80, pitch=58, start=5.375, end=5.5),  # E4
]
bass.notes.extend(bass_notes)

# Piano - 7th chords on 2 and 4
piano_notes = [
    # Bb7 on 2 (beat 2)
    pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=5.0),  # Bb4
    pretty_midi.Note(velocity=90, pitch=74, start=4.875, end=5.0),  # D5
    pretty_midi.Note(velocity=90, pitch=76, start=4.875, end=5.0),  # F5
    pretty_midi.Note(velocity=90, pitch=78, start=4.875, end=5.0),  # G5
    # D7 on 4 (beat 4)
    pretty_midi.Note(velocity=90, pitch=62, start=5.625, end=5.75),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=5.625, end=5.75),  # G4
    pretty_midi.Note(velocity=90, pitch=69, start=5.625, end=5.75),  # Bb4
    pretty_midi.Note(velocity=90, pitch=71, start=5.625, end=5.75),  # D5
]
piano.notes.extend(piano_notes)

# Finalize and save the MIDI file
midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
