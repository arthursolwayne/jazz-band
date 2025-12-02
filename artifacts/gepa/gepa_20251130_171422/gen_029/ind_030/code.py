
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Subtle dynamics, space, and tension
drum_notes = [
    # Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=60, pitch=42, start=0.0, end=0.375),  # Hihat on 1
    pretty_midi.Note(velocity=80, pitch=38, start=0.375, end=0.75), # Snare on 2
    pretty_midi.Note(velocity=60, pitch=42, start=0.375, end=0.75), # Hihat on 2
    pretty_midi.Note(velocity=80, pitch=36, start=0.75, end=1.125), # Kick on 3
    pretty_midi.Note(velocity=60, pitch=42, start=0.75, end=1.125), # Hihat on 3
    pretty_midi.Note(velocity=80, pitch=38, start=1.125, end=1.5),  # Snare on 4
    pretty_midi.Note(velocity=60, pitch=42, start=1.125, end=1.5),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Sax enters with the motif (1.5 - 3.0s)
# Motif: D (D4), F# (F#4), B (B4), D (D5) – concise and emotional
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),   # D4
    pretty_midi.Note(velocity=90, pitch=66, start=1.75, end=2.0),    # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.25),   # B4
    pretty_midi.Note(velocity=90, pitch=74, start=2.25, end=2.5),    # D5
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.75),   # D4 (repeat)
    pretty_midi.Note(velocity=90, pitch=66, start=2.75, end=3.0),    # F#4 (repeat)
]
sax.notes.extend(sax_notes)

# Bass line – chromatic and melodic (1.5 - 3.0s)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=55, start=1.5, end=1.75),   # D3
    pretty_midi.Note(velocity=80, pitch=57, start=1.75, end=2.0),   # E3
    pretty_midi.Note(velocity=80, pitch=59, start=2.0, end=2.25),   # F#3
    pretty_midi.Note(velocity=80, pitch=62, start=2.25, end=2.5),   # A3
    pretty_midi.Note(velocity=80, pitch=55, start=2.5, end=2.75),   # D3
    pretty_midi.Note(velocity=80, pitch=57, start=2.75, end=3.0),   # E3
]
bass.notes.extend(bass_notes)

# Piano (1.5 - 3.0s) – comping with 7th chords on 2 and 4
piano_notes = [
    # Bar 2: D7 (D4, F#4, A4, C#5)
    pretty_midi.Note(velocity=80, pitch=62, start=1.75, end=2.0),   # D4
    pretty_midi.Note(velocity=80, pitch=66, start=1.75, end=2.0),   # F#4
    pretty_midi.Note(velocity=80, pitch=69, start=1.75, end=2.0),   # A4
    pretty_midi.Note(velocity=80, pitch=72, start=1.75, end=2.0),   # C#5
    # Bar 3: D7 again
    pretty_midi.Note(velocity=80, pitch=62, start=2.25, end=2.5),   # D4
    pretty_midi.Note(velocity=80, pitch=66, start=2.25, end=2.5),   # F#4
    pretty_midi.Note(velocity=80, pitch=69, start=2.25, end=2.5),   # A4
    pretty_midi.Note(velocity=80, pitch=72, start=2.25, end=2.5),   # C#5
]
piano.notes.extend(piano_notes)

# Bar 3: Drums continue (1.5 - 3.0s)
drum_notes = [
    # Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=60, pitch=42, start=1.5, end=1.875),  # Hihat on 1
    pretty_midi.Note(velocity=80, pitch=38, start=1.875, end=2.25), # Snare on 2
    pretty_midi.Note(velocity=60, pitch=42, start=1.875, end=2.25), # Hihat on 2
    pretty_midi.Note(velocity=80, pitch=36, start=2.25, end=2.625), # Kick on 3
    pretty_midi.Note(velocity=60, pitch=42, start=2.25, end=2.625), # Hihat on 3
    pretty_midi.Note(velocity=80, pitch=38, start=2.625, end=3.0),  # Snare on 4
    pretty_midi.Note(velocity=60, pitch=42, start=2.625, end=3.0),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 4: Sax repeats motif with variation (3.0 - 4.5s)
# Motif: D (D4), F# (F#4), B (B4), D (D5) – same as before, but with a slight rubato
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),   # D4
    pretty_midi.Note(velocity=90, pitch=66, start=3.25, end=3.5),    # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=3.5, end=3.75),   # B4
    pretty_midi.Note(velocity=90, pitch=74, start=3.75, end=4.0),    # D5
    pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.25),   # D4 (repeat)
    pretty_midi.Note(velocity=90, pitch=66, start=4.25, end=4.5),    # F#4 (repeat)
]
sax.notes.extend(sax_notes)

# Bass line – chromatic and melodic (3.0 - 4.5s)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=55, start=3.0, end=3.25),   # D3
    pretty_midi.Note(velocity=80, pitch=57, start=3.25, end=3.5),   # E3
    pretty_midi.Note(velocity=80, pitch=59, start=3.5, end=3.75),   # F#3
    pretty_midi.Note(velocity=80, pitch=62, start=3.75, end=4.0),   # A3
    pretty_midi.Note(velocity=80, pitch=55, start=4.0, end=4.25),   # D3
    pretty_midi.Note(velocity=80, pitch=57, start=4.25, end=4.5),   # E3
]
bass.notes.extend(bass_notes)

# Piano (3.0 - 4.5s) – comping with 7th chords on 2 and 4
piano_notes = [
    # Bar 3: D7 (D4, F#4, A4, C#5)
    pretty_midi.Note(velocity=80, pitch=62, start=3.25, end=3.5),   # D4
    pretty_midi.Note(velocity=80, pitch=66, start=3.25, end=3.5),   # F#4
    pretty_midi.Note(velocity=80, pitch=69, start=3.25, end=3.5),   # A4
    pretty_midi.Note(velocity=80, pitch=72, start=3.25, end=3.5),   # C#5
    # Bar 4: D7 again
    pretty_midi.Note(velocity=80, pitch=62, start=3.75, end=4.0),   # D4
    pretty_midi.Note(velocity=80, pitch=66, start=3.75, end=4.0),   # F#4
    pretty_midi.Note(velocity=80, pitch=69, start=3.75, end=4.0),   # A4
    pretty_midi.Note(velocity=80, pitch=72, start=3.75, end=4.0),   # C#5
]
piano.notes.extend(piano_notes)

# Bar 4: Drums continue (3.0 - 4.5s)
drum_notes = [
    # Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=60, pitch=42, start=3.0, end=3.375),  # Hihat on 1
    pretty_midi.Note(velocity=80, pitch=38, start=3.375, end=3.75), # Snare on 2
    pretty_midi.Note(velocity=60, pitch=42, start=3.375, end=3.75), # Hihat on 2
    pretty_midi.Note(velocity=80, pitch=36, start=3.75, end=4.125), # Kick on 3
    pretty_midi.Note(velocity=60, pitch=42, start=3.75, end=4.125), # Hihat on 3
    pretty_midi.Note(velocity=80, pitch=38, start=4.125, end=4.5),  # Snare on 4
    pretty_midi.Note(velocity=60, pitch=42, start=4.125, end=4.5),  # Hihat on 4
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
